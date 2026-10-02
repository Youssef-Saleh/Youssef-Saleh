"""
build_hero.py — Regenerate the GitHub profile hero SVG with LIVE data.

Usage:
    python build_hero.py                 # fetch live data, write _render/hero_v7_live.svg
    python build_hero.py --dry-run      # fetch live data, print to stdout, no file write
    python build_hero.py --out PATH     # write to a custom path
    python build_hero.py --fallback     # use last-good cached data if API fails

When the GitHub Action runs this, it:
    1. Fetches profile + repos + recent events from api.github.com (free, no auth needed for 60 req/h)
    2. Substitutes real values into the v7 SVG template
    3. Writes hero_v7_live.svg
    4. The README will then embed this file instead of hero_v7.svg

When the API is rate-limited or down, the script falls back to a cached "stale as of" snapshot
so your README never shows a broken image.
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# ============================================================================
# CONFIG
# ============================================================================

GITHUB_USER = "Youssef-Saleh"
GITHUB_API = "https://api.github.com"
CACHE_DIR = Path(__file__).parent / ".cache"
CACHE_FILE = CACHE_DIR / "last_good.json"
TEMPLATE_FILE = Path(__file__).parent / "hero_v7_live_template.svg"
OUT_FILE_DEFAULT = Path(__file__).parent / "hero_v7_live.svg"

# These are NOT data-driven - they are editorial values that don't change
# unless the user updates the template. Listed here for documentation only:
# - Capability scores (92/87/68/95/72/80) - your subjective self-rating
# - "open to work" - manual flag
# - The narrative labels (PAN-OS, M.Sc. CS, NETWORKSAGE, TRUSTEVAL-AI)

# ============================================================================
# DATA FETCHING
# ============================================================================

def http_get_json(url, headers=None, timeout=15):
    """GET a URL and parse JSON. Raises on error."""
    h = {"Accept": "application/vnd.github+json", "User-Agent": "youssef-profile-hero-builder"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_profile():
    return http_get_json(f"{GITHUB_API}/users/{GITHUB_USER}")


def fetch_repos():
    """All public repos, sorted by stars desc, then by pushed_at desc."""
    repos = http_get_json(f"{GITHUB_API}/users/{GITHUB_USER}/repos?per_page=100")
    return sorted(repos, key=lambda r: (-r.get("stargazers_count", 0), r.get("pushed_at", "")))


def fetch_recent_events():
    """Last 90 days of public events. Used for the LIVE FEED."""
    try:
        return http_get_json(f"{GITHUB_API}/users/{GITHUB_USER}/events/public") or []
    except urllib.error.HTTPError as e:
        if e.code == 403:
            # rate limited; return empty
            return []
        raise


def fetch_all_data():
    """Fetch everything in one go. Returns a dict with all live values."""
    profile = fetch_profile()
    repos = fetch_repos()
    events = fetch_recent_events()
    return {"profile": profile, "repos": repos, "events": events}


def fetch_with_fallback():
    """Try live fetch; if it fails, return last-good cached data."""
    try:
        data = fetch_all_data()
        # cache the good response
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        CACHE_FILE.write_text(json.dumps(data, indent=2, default=str))
        return data, "live"
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as e:
        print(f"[warn] live fetch failed: {e}", file=sys.stderr)
        if CACHE_FILE.exists():
            print(f"[warn] falling back to cached data from {CACHE_FILE}", file=sys.stderr)
            data = json.loads(CACHE_FILE.read_text())
            return data, f"cached (stale)"
        raise


# ============================================================================
# DATA → TEMPLATE VARIABLES
# ============================================================================

def compute_template_vars(data):
    """Turn raw GitHub data into the string substitutions the template expects."""
    p = data["profile"]
    repos = data["repos"]
    events = data["events"]

    # Account age (replaces the fake "26y 137d")
    created = datetime.fromisoformat(p["created_at"].replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    delta = now - created
    years = delta.days // 365
    days = (delta.days % 365)
    age_str = f"{years}y {days}d"

    # Repo counts
    total_repos = len(repos)
    active_recent = sum(1 for r in repos if r.get("pushed_at", "") >= "2026-01-01")
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
    total_forks = sum(r.get("forks_count", 0) for r in repos)

    # Top 5 featured repos (by stars, then recently pushed)
    featured = []
    for r in repos:
        if r.get("fork"):
            continue
        if r.get("archived"):
            continue
        featured.append({
            "name": r["name"],
            "url": r["html_url"],
            "description": (r.get("description") or "").strip(),
            "stars": r.get("stargazers_count", 0),
            "language": r.get("language") or "—",
            "pushed_at": r.get("pushed_at", ""),
        })
    featured.sort(key=lambda r: (-r["stars"], -0 if not r["pushed_at"] else 0))
    featured = featured[:5]

    # Top 5 languages by repo count
    lang_counts = {}
    for r in repos:
        if r.get("fork"):
            continue
        l = r.get("language")
        if l:
            lang_counts[l] = lang_counts.get(l, 0) + 1
    top_languages = sorted(lang_counts.items(), key=lambda x: -x[1])[:5]

    # Live feed: last 7 events
    live_feed = []
    for e in events[:7]:
        etype = e.get("type", "")
        repo = e.get("repo", {}).get("name", "—")
        date = e.get("created_at", "")[:19].replace("T", " ")
        # map event type to a tiny icon-ish char
        icon = {
            "PushEvent": "▶",
            "PullRequestEvent": "⇄",
            "IssuesEvent": "◇",
            "WatchEvent": "★",
            "ForkEvent": "⑂",
            "CreateEvent": "+",
        }.get(etype, "·")
        live_feed.append({"time": date, "icon": icon, "type": etype, "repo": repo})

    # Summary stats
    return {
        "FOLLOWERS": p.get("followers", 0),
        "FOLLOWING": p.get("following", 0),
        "PUBLIC_REPOS": total_repos,
        "ACTIVE_REPOS_2026": active_recent,
        "TOTAL_STARS": total_stars,
        "TOTAL_FORKS": total_forks,
        "ACCOUNT_AGE": age_str,
        "PROFILE_URL": p.get("html_url", f"https://github.com/{GITHUB_USER}"),
        "AVATAR_URL": p.get("avatar_url", ""),
        "BIO": (p.get("bio") or "").strip(),
        "FEATURED": featured,
        "LANGUAGES": top_languages,
        "LIVE_FEED": live_feed,
        "BUILD_TIMESTAMP": now.strftime("%Y-%m-%d %H:%M UTC"),
    }


# ============================================================================
# SVG RENDERING
# ============================================================================

def render_featured_section(featured):
    """Generate a 5-row featured repos table for the markdown body (not the SVG)."""
    rows = []
    for r in featured:
        desc = r["description"][:80] + ("…" if len(r["description"]) > 80 else "")
        rows.append(f"| [{r['name']}]({r['url']}) | {desc} |")
    return "\n".join(rows)


def render_languages_section(languages):
    """Tiny inline language bar list for the markdown body."""
    if not languages:
        return ""
    return " · ".join(f"{l} ({c})" for l, c in languages)


def substitute_into_template(template, vars):
    """Replace {{TOKEN}} placeholders in the template with values from vars."""
    out = template

    # Scalars
    for k, v in vars.items():
        if isinstance(v, (str, int, float)):
            out = out.replace("{{" + k + "}}", str(v))

    # Lists: featured repos, languages, live feed
    # These need explicit handling because they're not simple strings
    # We'll do a 3-pass replacement: featured / languages / live feed

    # Featured repos: replace {{FEATURED_TABLE}} with a markdown table
    out = out.replace("{{FEATURED_TABLE}}", render_featured_section(vars["FEATURED"]))

    # Languages: replace {{LANGUAGES_INLINE}} with inline list
    out = out.replace("{{LANGUAGES_INLINE}}", render_languages_section(vars["LANGUAGES"]))

    # Live feed rows: replace {{LIVE_FEED_ROWS}} with formatted log lines
    feed_rows = []
    for e in vars["LIVE_FEED"]:
        feed_rows.append(f'  <text x="0" y="0" fill="#5a6678">{e["time"]}</text>')
        feed_rows.append(f'  <text x="64" y="0" fill="#c9d1d9">{e["icon"]} {e["type"][:14]}</text>')
        feed_rows.append(f'  <text x="140" y="0" fill="#c9d1d9">{e["repo"][:30]}</text>')
    # Need to nest them in <g transform=...> blocks; for simplicity we just emit raw text
    # and the template has the <g> wrapper already
    out = out.replace("{{LIVE_FEED_ROWS}}", "\n        ".join(feed_rows))

    return out


# ============================================================================
# README RENDERING
# ============================================================================

README_TEMPLATE = '''<div align="center">

{svg}

</div>

---

```yaml
name:        Youssef Saleh
degree:      M.Sc. Computer Science, University of Idaho (2026)
focus:       Applied AI  ·  Network Security  ·  Explainable AI
interests:   [LLM agents, IDS/IPS, XAI, multi-agent systems, sensor calibration]
currently:   Building trust-and-safety agents & explainable network-intrusion systems
location:    Ann Arbor, MI
email:       youssef.s.saleh@gmail.com
github:      {followers} followers · {stars}★ across {repos} repos · account {age}
last build:  {timestamp}
```

> *"A model that classifies a packet as malicious isn't useful if a SOC analyst can't tell it why."*
> — the through-line of my thesis, my agents, and every project on this page.

---

## Projects ({active} active in 2026)

{featured_table}

<details>
  <summary><b>{remaining} more repositories</b></summary>
  <br/>

  Visit [{github_url}]({github_url}) for the full list.

</details>

---

## Stack

{languages_inline}

---

## Connect

<p align="left">
  <a href="mailto:youssef.s.saleh@gmail.com">:e-mail: youssef.s.saleh@gmail.com</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/youssef-saleh/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="{github_url}">GitHub</a> &nbsp;·&nbsp;
  <a href="https://launchgood-trust-copilot.fly.dev/">Live demo</a>
</p>

<sub>:wave: this profile is regenerated daily by a github action that fetches your real github data. the hero is a single inline SVG with motion: breathing radar pulse, sparkline self-drawing animation, status pill breathing, and a NOW marker that radiates outward. the data is real, the design is hand-built.</sub>
'''


def build_readme(svg, vars, total_repos_known, featured_count):
    """Build a README.md from the live SVG + vars."""
    return README_TEMPLATE.format(
        svg=svg.strip(),
        followers=vars["FOLLOWERS"],
        stars=vars["TOTAL_STARS"],
        repos=vars["PUBLIC_REPOS"],
        age=vars["ACCOUNT_AGE"],
        timestamp=vars["BUILD_TIMESTAMP"],
        active=vars["ACTIVE_REPOS_2026"],
        featured_table=vars.get("_featured_table", ""),
        remaining=total_repos_known - featured_count,
        github_url=vars["PROFILE_URL"],
        languages_inline=vars.get("_languages_inline", ""),
    )


# ============================================================================
# CLI
# ============================================================================

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true", help="Print to stdout, don't write files")
    p.add_argument("--out", default=str(OUT_FILE_DEFAULT), help="Output SVG path")
    p.add_argument("--template", default=str(TEMPLATE_FILE), help="SVG template path")
    p.add_argument("--fallback", action="store_true", help="Use cached data if API fails")
    p.add_argument("--with-readme", action="store_true", help="Also regenerate README.md")
    args = p.parse_args()

    # Step 1: fetch data
    print(f"[info] fetching live data for {GITHUB_USER}...", file=sys.stderr)
    if args.fallback:
        data, source = fetch_with_fallback()
    else:
        try:
            data, source = fetch_all_data(), "live"
        except (urllib.error.URLError, urllib.error.HTTPError) as e:
            print(f"[error] fetch failed and --fallback not set: {e}", file=sys.stderr)
            sys.exit(1)
    print(f"[info] got data ({source})", file=sys.stderr)

    # Step 2: compute template vars
    vars = compute_template_vars(data)
    vars["_featured_table"] = render_featured_section(vars["FEATURED"])
    vars["_languages_inline"] = render_languages_section(vars["LANGUAGES"])

    # Step 3: load template
    template_path = Path(args.template)
    if not template_path.exists():
        print(f"[error] template not found: {template_path}", file=sys.stderr)
        print(f"[hint] copy _render/hero_v7.svg to {template_path} and add template placeholders", file=sys.stderr)
        sys.exit(1)
    template = template_path.read_text(encoding="utf-8")

    # Step 4: substitute
    svg = substitute_into_template(template, vars)

    # Step 5: write
    if args.dry_run:
        print(svg)
    else:
        out_path = Path(args.out)
        out_path.write_text(svg, encoding="utf-8")
        print(f"[ok] wrote {out_path} ({len(svg):,} bytes, source: {source})", file=sys.stderr)

    if args.with_readme and not args.dry_run:
        readme = build_readme(svg, vars, total_repos_known=len(data["repos"]), featured_count=len(vars["FEATURED"]))
        readme_path = Path(__file__).parent.parent / "README.md"
        readme_path.write_text(readme, encoding="utf-8")
        print(f"[ok] wrote {readme_path} ({len(readme):,} bytes)", file=sys.stderr)

    # Print summary
    print(f"\n--- summary ---", file=sys.stderr)
    print(f"  followers: {vars['FOLLOWERS']}", file=sys.stderr)
    print(f"  public repos: {vars['PUBLIC_REPOS']} (active in 2026: {vars['ACTIVE_REPOS_2026']})", file=sys.stderr)
    print(f"  total stars: {vars['TOTAL_STARS']} · forks: {vars['TOTAL_FORKS']}", file=sys.stderr)
    print(f"  account age: {vars['ACCOUNT_AGE']}", file=sys.stderr)
    print(f"  recent events: {len(vars['LIVE_FEED'])}", file=sys.stderr)
    print(f"  top languages: {vars['LANGUAGES']}", file=sys.stderr)


if __name__ == "__main__":
    main()

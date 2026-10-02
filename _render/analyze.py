"""
analyze.py — call the MiniMax vision model to critique a preview image.
"""
import json, base64, urllib.request, urllib.error, sys, time
from pathlib import Path

AUTH = Path(r"C:\Users\Youssef\AppData\Local\hermes\auth.json")

def get_auth():
    return json.loads(AUTH.read_text(encoding="utf-8"))

def call_vision(img_path: str, prompt: str, max_retries: int = 3) -> str:
    auth = get_auth()
    token = auth["providers"]["minimax-oauth"]["access_token"]
    base_url = auth["providers"]["minimax-oauth"]["resource_url"]
    endpoint = f"{base_url}/messages"

    img_b64 = base64.b64encode(Path(img_path).read_bytes()).decode("ascii")
    mime = "image/png" if img_path.lower().endswith(".png") else "image/jpeg"

    payload = {
        "model": "MiniMax-M3",
        "max_tokens": 1500,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "image", "source": {"type": "base64", "media_type": mime, "data": img_b64}},
                {"type": "text", "text": prompt},
            ]
        }],
    }
    headers_variants = [
        {"x-api-key": token, "anthropic-version": "2023-06-01", "Content-Type": "application/json"},
        {"Authorization": f"Bearer {token}", "anthropic-version": "2023-06-01", "Content-Type": "application/json"},
    ]

    last_err = None
    for headers in headers_variants:
        for attempt in range(max_retries):
            try:
                req = urllib.request.Request(
                    endpoint, data=json.dumps(payload).encode("utf-8"),
                    headers=headers, method="POST",
                )
                with urllib.request.urlopen(req, timeout=120) as resp:
                    result = json.loads(resp.read().decode("utf-8"))
                    content = result.get("content", [])
                    return "\n".join(c.get("text", "") for c in content if c.get("type") == "text")
            except urllib.error.HTTPError as e:
                body = e.read().decode("utf-8", errors="replace")[:300]
                last_err = f"HTTP {e.code}: {body}"
                if e.code in (401, 403, 404):
                    break
                time.sleep(2)
            except urllib.error.URLError as e:
                last_err = f"URL: {e}"
                time.sleep(2)
    return f"ERROR: {last_err}"

if __name__ == "__main__":
    img = sys.argv[1]
    prompt = sys.argv[2]
    print(call_vision(img, prompt))

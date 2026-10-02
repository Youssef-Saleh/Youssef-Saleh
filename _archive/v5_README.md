<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="'Cascadia Mono','Consolas','Courier New',monospace">
  <!-- =========================================================
       C2 — A SOC analyst's terminal. Hand-drawn for Youssef Saleh.
       Designed for GitHub profile README — renders inline.
       Palette: bg=navy, panel=slightly-lighter-navy, teal=accent,
                amber=warning, white=text, gray=secondary-text.
       ========================================================= -->

  <defs>
    <linearGradient id="bezel" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1c2540"/>
      <stop offset="1" stop-color="#0a0e1a"/>
    </linearGradient>
    <linearGradient id="screenGlow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0a1020"/>
      <stop offset="1" stop-color="#050810"/>
    </linearGradient>
    <!-- amber alert-tape diagonal stripe pattern -->
    <pattern id="alertStripe" patternUnits="userSpaceOnUse" width="8" height="8" patternTransform="rotate(45)">
      <rect width="8" height="8" fill="#0a0e1a"/>
      <rect width="4" height="8" fill="#f29e2e"/>
    </pattern>
  </defs>

  <!-- ========== OUTER MONITOR FRAME ========== -->
  <rect x="0" y="0" width="1200" height="900" fill="url(#bezel)"/>
  <rect x="14" y="14" width="1172" height="872" fill="#050810"/>
  <rect x="18" y="18" width="1164" height="864" fill="url(#screenGlow)"/>
  <!-- corner screws -->
  <g fill="#2a3a5a">
    <circle cx="30" cy="30" r="3"/><circle cx="1170" cy="30" r="3"/>
    <circle cx="30" cy="870" r="3"/><circle cx="1170" cy="870" r="3"/>
  </g>

  <!-- ========== HEADER STRIP ========== -->
  <rect x="30" y="38" width="1140" height="44" fill="#11172a" stroke="#1f2a44" stroke-width="1"/>
  <text x="44" y="68" font-size="18" font-weight="700" fill="#19c7d9" letter-spacing="2">Y.SALEH</text>
  <text x="140" y="68" font-size="13" fill="#8a96ac">// ID:0x6F75737365</text>
  <text x="320" y="68" font-size="13" fill="#c9d1d9">// MSc CS, U.Idaho (2026)</text>
  <circle cx="906" cy="60" r="5" fill="#4ade80"/>
  <circle cx="906" cy="60" r="9" fill="none" stroke="#4ade80" stroke-opacity="0.4" stroke-width="1"/>
  <text x="920" y="66" font-size="13" fill="#4ade80" letter-spacing="1">ONLINE</text>
  <text x="990" y="66" font-size="13" fill="#8a96ac">UPTIME</text>
  <text x="1052" y="66" font-size="13" fill="#c9d1d9">26y 137d</text>
  <g transform="translate(1140,52)" fill="#19c7d9">
    <rect x="0"  y="14" width="3" height="4"  />
    <rect x="5"  y="10" width="3" height="8"  />
    <rect x="10" y="6"  width="3" height="12" />
    <rect x="15" y="2"  width="3" height="16" />
  </g>

  <!-- ========== LEFT RAIL — Identity ========== -->
  <rect x="30" y="98" width="240" height="500" fill="#0d1322" stroke="#1f2a44" stroke-width="1"/>
  <rect x="30" y="98" width="240" height="22" fill="#11172a"/>
  <text x="40" y="114" font-size="11" fill="#8a96ac">// IDENTITY</text>
  <text x="262" y="114" font-size="11" fill="#19c7d9" text-anchor="end">0x01</text>

  <!-- ASCII monogram block -->
  <rect x="50" y="136" width="200" height="200" fill="#050810" stroke="#1f2a44" stroke-width="1"/>
  <g stroke="#19c7d9" stroke-width="1.5" fill="none">
    <path d="M 56 142 L 56 154 M 56 142 L 68 142"/>
    <path d="M 244 142 L 244 154 M 244 142 L 232 142"/>
    <path d="M 56 330 L 56 318 M 56 330 L 68 330"/>
    <path d="M 244 330 L 244 318 M 244 330 L 232 330"/>
  </g>
  <line x1="150" y1="216" x2="150" y2="256" stroke="#1f2a44" stroke-width="0.5"/>
  <line x1="130" y1="236" x2="170" y2="236" stroke="#1f2a44" stroke-width="0.5"/>
  <text x="150" y="254" font-size="92" font-weight="700" fill="#19c7d9" text-anchor="middle" letter-spacing="-4">Y.S</text>
  <text x="150" y="284" font-size="11" fill="#8a96ac" text-anchor="middle" letter-spacing="6">C2 CONSOLE</text>
  <text x="150" y="302" font-size="9"  fill="#525568" text-anchor="middle" letter-spacing="3">v 4.2.6  //  2026-10-02</text>
  <text x="150" y="320" font-size="9"  fill="#4ade80" text-anchor="middle" letter-spacing="2">[ HANDSHAKE OK ]</text>

  <!-- bio block -->
  <g transform="translate(46,358)" font-size="12">
    <text x="0" y="0"   fill="#8a96ac">name</text>
    <text x="80" y="0"  fill="#c9d1d9">Youssef Saleh</text>
    <text x="0" y="20"  fill="#8a96ac">loc</text>
    <text x="80" y="20" fill="#c9d1d9">Ann Arbor, MI</text>
    <text x="0" y="40"  fill="#8a96ac">focus</text>
    <text x="80" y="40" fill="#19c7d9">XAI</text>
    <text x="118" y="40" fill="#c9d1d9">&#x2022;</text>
    <text x="128" y="40" fill="#19c7d9">LLM agents</text>
    <text x="0" y="60"  fill="#8a96ac"></text>
    <text x="80" y="60" fill="#19c7d9">network sec</text>
    <text x="0" y="80"  fill="#8a96ac">email</text>
    <text x="80" y="80" fill="#c9d1d9">youssef.s.saleh</text>
    <text x="0" y="100" fill="#8a96ac"></text>
    <text x="80" y="100" fill="#c9d1d9">@gmail.com</text>
    <text x="0" y="120" fill="#8a96ac">status</text>
    <text x="80" y="120" fill="#f29e2e">&#x25CF; open to work</text>
    <text x="0" y="140" fill="#8a96ac">reach</text>
    <text x="80" y="140" fill="#c9d1d9">email, LinkedIn,</text>
    <text x="0" y="160" fill="#8a96ac"></text>
    <text x="80" y="160" fill="#c9d1d9">demo below</text>
  </g>

  <!-- footer hash inside left rail -->
  <g transform="translate(46,560)" font-size="10" fill="#525568">
    <text x="0" y="0">hash: 7e3c.0a91.f29e</text>
    <text x="0" y="14">build: brutstyl-v4.2.6</text>
    <text x="0" y="28">key:  ECC:P-256</text>
  </g>

  <!-- ========== CENTER PANEL — Capability matrix ========== -->
  <rect x="286" y="98" width="600" height="500" fill="#0d1322" stroke="#1f2a44" stroke-width="1"/>
  <rect x="286" y="98" width="600" height="22" fill="#11172a"/>
  <text x="296" y="114" font-size="11" fill="#8a96ac">// CAPABILITY MATRIX</text>
  <text x="878" y="114" font-size="11" fill="#19c7d9" text-anchor="end">0x02</text>

  <!-- 6-axis radar chart -->
  <g transform="translate(446,338)">
    <!-- outer hexagonal frame -->
    <polygon points="0,-130 113,-65 113,65 0,130 -113,65 -113,-65"
             fill="none" stroke="#1f2a44" stroke-width="1"/>
    <!-- inner reference rings (dotted) -->
    <g fill="none" stroke="#1f2a44" stroke-width="0.5" stroke-dasharray="2,3">
      <polygon points="0,-100 87,-50 87,50 0,100 -87,50 -87,-50"/>
      <polygon points="0,-70  61,-35 61,35 0,70  -61,35 -61,-35"/>
      <polygon points="0,-40  35,-20 35,20 0,40  -35,20 -35,-20"/>
    </g>
    <!-- axis spokes -->
    <g stroke="#1f2a44" stroke-width="0.5">
      <line x1="0" y1="0" x2="0" y2="-130"/>
      <line x1="0" y1="0" x2="113" y2="-65"/>
      <line x1="0" y1="0" x2="113" y2="65"/>
      <line x1="0" y1="0" x2="0" y2="130"/>
      <line x1="0" y1="0" x2="-113" y2="65"/>
      <line x1="0" y1="0" x2="-113" y2="-65"/>
    </g>
    <!-- filled capability polygon (the centerpiece) -->
    <polygon points="0,-118 95,-55 88,52 0,108 -90,52 -100,-58"
             fill="#19c7d9" fill-opacity="0.35" stroke="#19c7d9" stroke-width="2"/>
    <!-- inner highlight polygon for depth -->
    <polygon points="0,-118 95,-55 88,52 0,108 -90,52 -100,-58"
             fill="none" stroke="#f29e2e" stroke-width="0.5" stroke-dasharray="3,3"/>
    <!-- axis labels with values -->
    <g font-size="10" fill="#c9d1d9" text-anchor="middle">
      <text x="0"    y="-140" font-weight="700">AI/ML</text>
      <text x="0"    y="-128" fill="#19c7d9">96</text>
      <text x="130"  y="-72"  font-weight="700">SEC</text>
      <text x="148"  y="-72"  fill="#19c7d9">82</text>
      <text x="130"  y="82"   font-weight="700">ENG</text>
      <text x="148"  y="82"   fill="#19c7d9">73</text>
      <text x="0"    y="148"  font-weight="700">XAI</text>
      <text x="0"    y="162"  fill="#19c7d9">88</text>
      <text x="-130" y="82"   font-weight="700">DATA</text>
      <text x="-148" y="82"   fill="#19c7d9">68</text>
      <text x="-130" y="-72"  font-weight="700">SHIP</text>
      <text x="-148" y="-72"  fill="#19c7d9">90</text>
    </g>
    <!-- vertex markers -->
    <g fill="#f29e2e" stroke="#0a0e1a" stroke-width="1.5">
      <circle cx="0"    cy="-118" r="4"/>
      <circle cx="95"   cy="-55"  r="4"/>
      <circle cx="88"   cy="52"   r="4"/>
      <circle cx="0"    cy="108"  r="4"/>
      <circle cx="-90"  cy="52"   r="4"/>
      <circle cx="-100" cy="-58"  r="4"/>
    </g>
    <!-- center crosshair -->
    <line x1="-6" y1="0" x2="6" y2="0" stroke="#19c7d9" stroke-width="0.5"/>
    <line x1="0" y1="-6" x2="0" y2="6" stroke="#19c7d9" stroke-width="0.5"/>
  </g>

  <!-- "Now building" block -->
  <g transform="translate(646,150)">
    <text x="0" y="0" font-size="11" fill="#8a96ac">// CURRENTLY BUILDING</text>
    <text x="0" y="22" font-size="18" font-weight="700" fill="#19c7d9">TrustEvaluatorAI</text>
    <text x="0" y="42" font-size="11" fill="#8a96ac">multi-agent T&amp;S copilot</text>
    <line x1="0" y1="50" x2="220" y2="50" stroke="#1f2a44"/>
    <text x="0" y="68" font-size="10" fill="#525568">5 agents &#x2022; LangGraph &#x2022; Fly.io</text>
    <!-- mini icon: clipboard + check -->
    <g transform="translate(0,86)" stroke="#19c7d9" fill="none" stroke-width="1.5">
      <rect x="0" y="0" width="36" height="46" fill="#0a0e1a"/>
      <rect x="10" y="-4" width="16" height="6" fill="#11172a"/>
      <line x1="6" y1="14" x2="30" y2="14"/>
      <line x1="6" y1="22" x2="30" y2="22"/>
      <line x1="6" y1="30" x2="22" y2="30"/>
      <path d="M 24 36 L 28 40 L 34 30" stroke="#f29e2e" stroke-width="2"/>
    </g>
    <text x="46" y="104" font-size="10" fill="#c9d1d9">5 of 5 agents</text>
    <text x="46" y="118" font-size="10" fill="#8a96ac">integrated</text>
    <text x="46" y="132" font-size="10" fill="#8a96ac">7 eval cases</text>
    <text x="46" y="146" font-size="10" fill="#4ade80">all pass</text>
  </g>

  <!-- Stack bar -->
  <g transform="translate(646,358)">
    <text x="0" y="0" font-size="11" fill="#8a96ac">// STACK DEPTH</text>
    <text x="0" y="20" font-size="11" fill="#c9d1d9">Python</text>
    <rect x="100" y="11" width="180" height="9" fill="#11172a" stroke="#1f2a44" stroke-width="0.5"/>
    <rect x="100" y="11" width="172" height="9" fill="#19c7d9"/>
    <text x="288" y="20" font-size="11" fill="#19c7d9" text-anchor="end">96%</text>

    <text x="0" y="38" font-size="11" fill="#c9d1d9">PyTorch</text>
    <rect x="100" y="29" width="180" height="9" fill="#11172a" stroke="#1f2a44" stroke-width="0.5"/>
    <rect x="100" y="29" width="148" height="9" fill="#19c7d9"/>
    <text x="288" y="38" font-size="11" fill="#19c7d9" text-anchor="end">82%</text>

    <text x="0" y="56" font-size="11" fill="#c9d1d9">LangGraph</text>
    <rect x="100" y="47" width="180" height="9" fill="#11172a" stroke="#1f2a44" stroke-width="0.5"/>
    <rect x="100" y="47" width="138" height="9" fill="#19c7d9"/>
    <text x="288" y="56" font-size="11" fill="#19c7d9" text-anchor="end">76%</text>

    <text x="0" y="74" font-size="11" fill="#c9d1d9">FastAPI</text>
    <rect x="100" y="65" width="180" height="9" fill="#11172a" stroke="#1f2a44" stroke-width="0.5"/>
    <rect x="100" y="65" width="132" height="9" fill="#19c7d9"/>
    <text x="288" y="74" font-size="11" fill="#19c7d9" text-anchor="end">73%</text>

    <text x="0" y="92" font-size="11" fill="#c9d1d9">Docker</text>
    <rect x="100" y="83" width="180" height="9" fill="#11172a" stroke="#1f2a44" stroke-width="0.5"/>
    <rect x="100" y="83" width="124" height="9" fill="#19c7d9"/>
    <text x="288" y="92" font-size="11" fill="#19c7d9" text-anchor="end">68%</text>

    <text x="0" y="110" font-size="11" fill="#c9d1d9">AWS</text>
    <rect x="100" y="101" width="180" height="9" fill="#11172a" stroke="#1f2a44" stroke-width="0.5"/>
    <rect x="100" y="101" width="98" height="9" fill="#f29e2e"/>
    <text x="288" y="110" font-size="11" fill="#f29e2e" text-anchor="end">54%</text>

    <text x="0" y="128" font-size="11" fill="#c9d1d9">C++</text>
    <rect x="100" y="119" width="180" height="9" fill="#11172a" stroke="#1f2a44" stroke-width="0.5"/>
    <rect x="100" y="119" width="64" height="9" fill="#f29e2e"/>
    <text x="288" y="128" font-size="11" fill="#f29e2e" text-anchor="end">36%</text>
  </g>

  <!-- Thesis metrics sparklines -->
  <g transform="translate(306,548)">
    <text x="0" y="0" font-size="11" fill="#8a96ac">// THESIS METRICS &#x2014; XAI_LLM_NetPacketAnalyzer</text>
    <rect x="0" y="10" width="568" height="36" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
    <g fill="none" stroke-width="1.5">
      <polyline points="14,40 30,30 46,24 62,20" stroke="#19c7d9"/>
      <polyline points="158,42 174,32 190,26 206,22 222,20" stroke="#19c7d9"/>
      <polyline points="302,40 318,34 334,30 350,28 366,26" stroke="#19c7d9"/>
      <polyline points="446,42 462,38 478,34 494,32 510,30 526,28 542,26" stroke="#f29e2e"/>
    </g>
    <g font-size="9" fill="#8a96ac" text-anchor="middle">
      <text x="38"  y="6">acc 96.8%</text>
      <text x="190" y="6">f1 0.9675</text>
      <text x="334" y="6">auc 0.9952</text>
      <text x="494" y="6">halluc 5.5%</text>
    </g>
  </g>

  <!-- ========== RIGHT RAIL — Event stream + Contact + Icons ========== -->
  <rect x="902" y="98" width="268" height="500" fill="#0d1322" stroke="#1f2a44" stroke-width="1"/>
  <rect x="902" y="98" width="268" height="22" fill="#11172a"/>
  <text x="912" y="114" font-size="11" fill="#8a96ac">// EVENT STREAM</text>
  <text x="1162" y="114" font-size="11" fill="#19c7d9" text-anchor="end">0x03</text>

  <!-- 4x3 grid of mini icons (50x50 each, 5px gap) -->
  <g transform="translate(906,138)">
    <!-- icon 1: Python -->
    <g transform="translate(0,0)">
      <rect x="0" y="0" width="50" height="50" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
      <g stroke="#19c7d9" fill="none" stroke-width="2">
        <path d="M 12 35 Q 12 40 19 40 L 30 40 Q 38 40 38 34 L 38 27 Q 38 21 30 21 L 21 21 Q 12 21 12 16 L 12 11 Q 12 5 19 5"/>
        <path d="M 38 21 Q 38 15 30 15 L 21 15 Q 12 15 12 19"/>
      </g>
      <circle cx="19" cy="11" r="1.7" fill="#19c7d9"/>
      <circle cx="30" cy="40" r="1.7" fill="#19c7d9"/>
      <text x="25" y="64" font-size="10" fill="#c9d1d9" text-anchor="middle">python</text>
    </g>
    <!-- icon 2: PyTorch -->
    <g transform="translate(55,0)">
      <rect x="0" y="0" width="50" height="50" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
      <g stroke="#f29e2e" fill="none" stroke-width="2">
        <path d="M 25 45 Q 12 37 14 23 Q 17 12 25 6 Q 33 12 36 23 Q 38 37 25 45 Z"/>
        <path d="M 25 45 Q 21 32 25 22 Q 29 32 25 45 Z" fill="#f29e2e" fill-opacity="0.4"/>
      </g>
      <text x="25" y="64" font-size="10" fill="#c9d1d9" text-anchor="middle">pytorch</text>
    </g>
    <!-- icon 3: LangGraph -->
    <g transform="translate(110,0)">
      <rect x="0" y="0" width="50" height="50" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
      <g stroke="#19c7d9" fill="#0a0e1a" stroke-width="2">
        <line x1="12" y1="12" x2="38" y2="20" stroke="#19c7d9" fill="none"/>
        <line x1="12" y1="12" x2="38" y2="30" stroke="#19c7d9" fill="none"/>
        <line x1="38" y1="20" x2="12" y2="38" stroke="#19c7d9" fill="none"/>
        <line x1="38" y1="30" x2="12" y2="38" stroke="#19c7d9" fill="none"/>
        <circle cx="12" cy="12" r="4"/>
        <circle cx="38" cy="20" r="4"/>
        <circle cx="38" cy="30" r="4"/>
        <circle cx="12" cy="38" r="4"/>
      </g>
      <text x="25" y="64" font-size="10" fill="#c9d1d9" text-anchor="middle">langgraph</text>
    </g>
    <!-- icon 4: FastAPI -->
    <g transform="translate(165,0)">
      <rect x="0" y="0" width="50" height="50" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
      <path d="M 28 6 L 14 28 L 23 28 L 20 44 L 35 20 L 26 20 Z" fill="#19c7d9" fill-opacity="0.35" stroke="#19c7d9" stroke-width="2"/>
      <text x="25" y="64" font-size="10" fill="#c9d1d9" text-anchor="middle">fastapi</text>
    </g>
    <!-- icon 5: Docker (moved to row 2 col 1) — replaced by Linux -->
    <!-- icon 5: Linux (penguin) -->
    <g transform="translate(0,60)">
      <rect x="0" y="0" width="50" height="50" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
      <g stroke="#f29e2e" fill="none" stroke-width="2">
        <ellipse cx="25" cy="22" rx="9" ry="11"/>
        <ellipse cx="25" cy="35" rx="12" ry="8"/>
        <circle cx="22" cy="20" r="1.3" fill="#f29e2e" stroke="none"/>
        <circle cx="28" cy="20" r="1.3" fill="#f29e2e" stroke="none"/>
        <path d="M 19 24 Q 25 28 31 24" stroke-width="1.5"/>
        <line x1="19" y1="33" x2="15" y2="40"/>
        <line x1="31" y1="33" x2="35" y2="40"/>
        <line x1="25" y1="40" x2="25" y2="44"/>
      </g>
      <text x="25" y="64" font-size="10" fill="#c9d1d9" text-anchor="middle">linux</text>
    </g>
    <!-- icon 6: AWS -->
    <g transform="translate(55,60)">
      <rect x="0" y="0" width="50" height="50" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
      <g stroke="#f29e2e" fill="none" stroke-width="2">
        <polygon points="25,6 41,14 41,32 25,40 9,32 9,14"/>
        <polyline points="9,14 25,22 41,14"/>
        <line x1="25" y1="22" x2="25" y2="40"/>
      </g>
      <text x="25" y="64" font-size="10" fill="#c9d1d9" text-anchor="middle">aws</text>
    </g>
    <!-- icon 7: MITRE -->
    <g transform="translate(110,60)">
      <rect x="0" y="0" width="50" height="50" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
      <g stroke="#19c7d9" fill="none" stroke-width="2">
        <path d="M 25 6 L 39 11 L 39 27 Q 39 36 25 42 Q 11 36 11 27 L 11 11 Z"/>
      </g>
      <text x="25" y="33" font-size="14" font-weight="700" fill="#19c7d9" text-anchor="middle">A&amp;</text>
      <text x="25" y="64" font-size="10" fill="#c9d1d9" text-anchor="middle">mitre</text>
    </g>
    <!-- icon 8: SHAP -->
    <g transform="translate(165,60)">
      <rect x="0" y="0" width="50" height="50" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
      <line x1="9" y1="42" x2="42" y2="42" stroke="#8a96ac" stroke-width="1"/>
      <rect x="11" y="28" width="6" height="14" fill="#19c7d9"/>
      <rect x="20" y="16" width="6" height="26" fill="#f29e2e"/>
      <rect x="29" y="22" width="6" height="22" fill="#19c7d9"/>
      <rect x="38" y="32" width="6" height="12" fill="#f29e2e"/>
      <text x="25" y="64" font-size="10" fill="#c9d1d9" text-anchor="middle">shap</text>
    </g>
    <!-- icon 9: PAN-OS -->
    <g transform="translate(0,120)">
      <rect x="0" y="0" width="50" height="50" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
      <g stroke="#19c7d9" fill="none" stroke-width="2">
        <rect x="7"  y="12" width="14" height="8"/>
        <rect x="27" y="12" width="14" height="8"/>
        <rect x="14" y="22" width="14" height="8"/>
        <rect x="33" y="22" width="8"  height="8"/>
        <rect x="7"  y="32" width="14" height="8"/>
        <rect x="27" y="32" width="14" height="8"/>
        <line x1="7" y1="20" x2="41" y2="20" stroke-dasharray="2,2"/>
      </g>
      <text x="25" y="64" font-size="10" fill="#c9d1d9" text-anchor="middle">pan-os</text>
    </g>
    <!-- icon 10: Scapy -->
    <g transform="translate(55,120)">
      <rect x="0" y="0" width="50" height="50" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
      <g stroke="#19c7d9" fill="none" stroke-width="2">
        <circle cx="25" cy="25" r="17"/>
        <circle cx="25" cy="25" r="9"  stroke-dasharray="2,2"/>
        <circle cx="25" cy="25" r="3"  stroke-dasharray="1,2"/>
        <line x1="25" y1="25" x2="37" y2="13" stroke="#f29e2e" stroke-width="2.5"/>
        <circle cx="25" cy="25" r="2" fill="#19c7d9" stroke="none"/>
      </g>
      <text x="25" y="64" font-size="10" fill="#c9d1d9" text-anchor="middle">scapy</text>
    </g>
    <!-- icon 11: Pandas (data) -->
    <g transform="translate(110,120)">
      <rect x="0" y="0" width="50" height="50" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
      <g stroke="#19c7d9" fill="none" stroke-width="2">
        <line x1="11" y1="42" x2="42" y2="42" stroke="#8a96ac"/>
        <line x1="11" y1="42" x2="11" y2="8" stroke="#8a96ac"/>
        <rect x="14" y="32" width="4" height="10" fill="#19c7d9" stroke="none"/>
        <rect x="20" y="22" width="4" height="20" fill="#19c7d9" stroke="none"/>
        <rect x="26" y="28" width="4" height="14" fill="#f29e2e" stroke="none"/>
        <rect x="32" y="14" width="4" height="28" fill="#19c7d9" stroke="none"/>
        <rect x="38" y="20" width="4" height="22" fill="#f29e2e" stroke="none"/>
      </g>
      <text x="25" y="64" font-size="10" fill="#c9d1d9" text-anchor="middle">pandas</text>
    </g>
    <!-- icon 12: Git -->
    <g transform="translate(165,120)">
      <rect x="0" y="0" width="50" height="50" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
      <g stroke="#f29e2e" fill="none" stroke-width="2.5">
        <line x1="30" y1="14" x2="14" y2="36"/>
        <line x1="36" y1="22" x2="20" y2="42"/>
        <line x1="22" y1="22" x2="32" y2="14"/>
        <circle cx="30" cy="14" r="4"/>
        <circle cx="14" cy="36" r="4"/>
        <circle cx="36" cy="22" r="4"/>
      </g>
      <text x="25" y="64" font-size="10" fill="#c9d1d9" text-anchor="middle">git</text>
    </g>
  </g>

  <line x1="906" y1="340" x2="1158" y2="340" stroke="#1f2a44"/>

  <!-- contact block -->
  <g transform="translate(906,352)">
    <text x="0" y="0" font-size="11" fill="#8a96ac">// CONTACT</text>
    <g font-size="11" fill="#c9d1d9">
      <text x="0" y="22">&#x2709;  youssef.s.saleh</text>
      <text x="0" y="38">       @gmail.com</text>
      <text x="0" y="58">&#x2192;  /in/youssef-saleh</text>
      <text x="0" y="78">&#x2192;  /Youssef-Saleh</text>
    </g>
  </g>

  <!-- alert ticker / event log -->
  <g transform="translate(906,452)">
    <text x="0" y="0" font-size="11" fill="#8a96ac">// RECENT EVENTS</text>
    <rect x="0" y="10" width="252" height="150" fill="#050810" stroke="#1f2a44" stroke-width="0.5"/>
    <g font-size="10">
      <text x="8" y="28" fill="#525568">10:02:14</text>
      <text x="64" y="28" fill="#4ade80">[OK]</text>
      <text x="94" y="28" fill="#c9d1d9">M.Sc. CS</text>
      <text x="8" y="42" fill="#c9d1d9">       conferred</text>

      <text x="8" y="60" fill="#525568">09:54:02</text>
      <text x="64" y="60" fill="#19c7d9">[INFO]</text>
      <text x="100" y="60" fill="#c9d1d9">TrustEval...</text>
      <text x="8" y="74" fill="#c9d1d9">       deployed &#x2192; fly.io</text>

      <text x="8" y="92" fill="#525568">09:11:47</text>
      <text x="64" y="92" fill="#f29e2e">[WARN]</text>
      <text x="100" y="92" fill="#c9d1d9">NetworkSage</text>
      <text x="8" y="106" fill="#c9d1d9">       7/7 eval cases pass</text>

      <text x="8" y="124" fill="#525568">07:15:33</text>
      <text x="64" y="124" fill="#4ade80">[OK]</text>
      <text x="94" y="124" fill="#c9d1d9">Pacify v1.0</text>
      <text x="8" y="138" fill="#c9d1d9">       shipped &#x2192; 4 repos</text>
    </g>
  </g>

  <!-- ========== INCIDENT TIMELINE STRIP ========== -->
  <rect x="30" y="652" width="1140" height="200" fill="#0d1322" stroke="#1f2a44" stroke-width="1"/>
  <rect x="30" y="652" width="1140" height="22" fill="#11172a"/>
  <text x="40" y="668" font-size="11" fill="#8a96ac">// INCIDENT TIMELINE &#x2014; 2022 &#x2192; 2026</text>
  <text x="1162" y="668" font-size="11" fill="#19c7d9" text-anchor="end">0x04</text>

  <!-- Timeline horizontal axis -->
  <g transform="translate(60,750)">
    <!-- main axis line -->
    <line x1="0" y1="0" x2="1080" y2="0" stroke="#1f2a44" stroke-width="1"/>
    <!-- year markers -->
    <g font-size="10" fill="#8a96ac" text-anchor="middle">
      <text x="0" y="20">2022</text>
      <text x="216" y="20">2023</text>
      <text x="432" y="20">2024</text>
      <text x="648" y="20">2025</text>
      <text x="864" y="20">2026</text>
      <text x="1080" y="20">now</text>
    </g>
    <!-- year tick marks -->
    <g stroke="#1f2a44" stroke-width="1">
      <line x1="0" y1="-4" x2="0" y2="4"/>
      <line x1="216" y1="-4" x2="216" y2="4"/>
      <line x1="432" y1="-4" x2="432" y2="4"/>
      <line x1="648" y1="-4" x2="648" y2="4"/>
      <line x1="864" y1="-4" x2="864" y2="4"/>
      <line x1="1080" y1="-4" x2="1080" y2="4"/>
    </g>

    <!-- Incident nodes -->
    <!-- Node 1: Network engineering at UIdaho -->
    <g transform="translate(140,0)">
      <line x1="0" y1="0" x2="0" y2="-50" stroke="#19c7d9" stroke-width="0.5"/>
      <circle cx="0" cy="-50" r="4" fill="#19c7d9" stroke="#0a0e1a" stroke-width="1.5"/>
      <text x="0" y="-62" font-size="10" fill="#19c7d9" text-anchor="middle" font-weight="700">PAN-OS</text>
      <text x="0" y="-74" font-size="9" fill="#8a96ac" text-anchor="middle">900+ firewall rules</text>
      <text x="0" y="36" font-size="9" fill="#525568" text-anchor="middle">2022</text>
    </g>
    <!-- Node 2: M.Sc. starts -->
    <g transform="translate(310,0)">
      <line x1="0" y1="0" x2="0" y2="-50" stroke="#19c7d9" stroke-width="0.5"/>
      <circle cx="0" cy="-50" r="4" fill="#19c7d9" stroke="#0a0e1a" stroke-width="1.5"/>
      <text x="0" y="-62" font-size="10" fill="#19c7d9" text-anchor="middle" font-weight="700">M.Sc. CS</text>
      <text x="0" y="-74" font-size="9" fill="#8a96ac" text-anchor="middle">U.Idaho, network+XAI</text>
      <text x="0" y="36" font-size="9" fill="#525568" text-anchor="middle">2023</text>
    </g>
    <!-- Node 3: NetworkSage shipped -->
    <g transform="translate(520,0)">
      <line x1="0" y1="0" x2="0" y2="-50" stroke="#19c7d9" stroke-width="0.5"/>
      <circle cx="0" cy="-50" r="4" fill="#19c7d9" stroke="#0a0e1a" stroke-width="1.5"/>
      <text x="0" y="-62" font-size="10" fill="#19c7d9" text-anchor="middle" font-weight="700">NetworkSage</text>
      <text x="0" y="-74" font-size="9" fill="#8a96ac" text-anchor="middle">multi-agent SOC</text>
      <text x="0" y="36" font-size="9" fill="#525568" text-anchor="middle">2024</text>
    </g>
    <!-- Node 4: TrustEval launch (AMBER - highlight) -->
    <g transform="translate(740,0)">
      <line x1="0" y1="0" x2="0" y2="-50" stroke="#f29e2e" stroke-width="1.5"/>
      <circle cx="0" cy="-50" r="6" fill="#f29e2e" stroke="#0a0e1a" stroke-width="2"/>
      <circle cx="0" cy="-50" r="10" fill="none" stroke="#f29e2e" stroke-opacity="0.4" stroke-width="1"/>
      <text x="0" y="-62" font-size="10" fill="#f29e2e" text-anchor="middle" font-weight="700">TrustEvalAI</text>
      <text x="0" y="-74" font-size="9" fill="#c9d1d9" text-anchor="middle">T&amp;S copilot, live</text>
      <text x="0" y="36" font-size="9" fill="#f29e2e" text-anchor="middle" font-weight="700">2025</text>
    </g>
    <!-- Node 5: M.Sc. conferred -->
    <g transform="translate(960,0)">
      <line x1="0" y1="0" x2="0" y2="-50" stroke="#4ade80" stroke-width="1.5"/>
      <circle cx="0" cy="-50" r="6" fill="#4ade80" stroke="#0a0e1a" stroke-width="2"/>
      <circle cx="0" cy="-50" r="10" fill="none" stroke="#4ade80" stroke-opacity="0.4" stroke-width="1"/>
      <text x="0" y="-62" font-size="10" fill="#4ade80" text-anchor="middle" font-weight="700">M.Sc. conferred</text>
      <text x="0" y="-74" font-size="9" fill="#c9d1d9" text-anchor="middle">thesis 96.8% acc</text>
      <text x="0" y="36" font-size="9" fill="#4ade80" text-anchor="middle" font-weight="700">2026</text>
    </g>

    <!-- Pulsing current-marker (the "you are here" line) -->
    <g transform="translate(1080,0)">
      <!-- thin vertical amber guide line tying marker to year label -->
      <line x1="0" y1="0" x2="0" y2="50" stroke="#f29e2e" stroke-width="0.5" stroke-dasharray="2,2" stroke-opacity="0.6"/>
      <circle cx="0" cy="0" r="5" fill="#19c7d9" stroke="#0a0e1a" stroke-width="2"/>
      <circle cx="0" cy="0" r="9" fill="none" stroke="#19c7d9" stroke-opacity="0.5" stroke-width="1">
        <animate attributeName="r" values="5;14;5" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="stroke-opacity" values="0.6;0;0.6" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="-12" y="-12" font-size="9" fill="#19c7d9" text-anchor="end" font-weight="700">YOU</text>
      <text x="-12" y="-2" font-size="9" fill="#19c7d9" text-anchor="end" font-weight="700">ARE</text>
      <text x="-12" y="8" font-size="9" fill="#19c7d9" text-anchor="end" font-weight="700">HERE</text>
    </g>

    <!-- Below-axis: minor events -->
    <g font-size="9" fill="#525568" text-anchor="middle">
      <text x="80" y="50">~  start PAN-OS automation</text>
      <text x="250" y="50">~  thesis proposal</text>
      <text x="400" y="50">~  XAI framework v1</text>
      <text x="640" y="50">~  Pacify ship</text>
      <text x="880" y="50">~  AUC peak</text>
    </g>
  </g>

  <!-- ========== FOOTER STATUS BAR ========== -->
  <rect x="30" y="862" width="1140" height="28" fill="#11172a" stroke="#1f2a44" stroke-width="1"/>
  <text x="44" y="881" font-size="12" fill="#19c7d9">&gt;_</text>
  <text x="64" y="881" font-size="12" fill="#c9d1d9">type 'help' for commands</text>
  <text x="240" y="881" font-size="12" fill="#8a96ac">// scroll down for full README</text>
  <text x="700" y="881" font-size="12" fill="#8a96ac">PING</text>
  <text x="730" y="881" font-size="12" fill="#c9d1d9">1ms</text>
  <text x="770" y="881" font-size="12" fill="#8a96ac">CPU</text>
  <text x="800" y="881" font-size="12" fill="#c9d1d9">12%</text>
  <text x="836" y="881" font-size="12" fill="#8a96ac">MEM</text>
  <text x="868" y="881" font-size="12" fill="#c9d1d9">2.1G</text>
  <text x="906" y="881" font-size="12" fill="#8a96ac">RX</text>
  <text x="932" y="881" font-size="12" fill="#4ade80">&#x25B2; 0</text>
  <text x="966" y="881" font-size="12" fill="#8a96ac">TX</text>
  <text x="992" y="881" font-size="12" fill="#f29e2e">&#x25BC; 1</text>
  <text x="1024" y="881" font-size="12" fill="#8a96ac">ENC</text>
  <text x="1054" y="881" font-size="12" fill="#c9d1d9">ECC-256</text>
  <text x="1112" y="881" font-size="12" fill="#8a96ac">UTC</text>
  <text x="1148" y="881" font-size="12" fill="#c9d1d9" text-anchor="end">14:00Z</text>
</svg>

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
```

> *"A model that classifies a packet as malicious isn't useful if a SOC analyst can't tell it why."*
> — the through-line of my thesis, my agents, and every project on this page.

---

## Projects

| | | |
|:---:|:---|:---|
| :robot: | **[TrustEvaluatorAI](https://github.com/Youssef-Saleh/TrustEvaluatorAI)** | LangGraph multi-agent Trust & Safety Copilot for a crowdfunding platform — synthesizes 4–6 data sources into a risk-scored review packet with full evidence attribution. Live on Fly.io. |
| :shield: | **[NetworkSage](https://github.com/Youssef-Saleh/NetworkSage)** | Multi-agent SOC analyst that triages, enriches, and investigates alerts with an `AttributionRef` layer — every agent decision traces back to the IOCs, MITRE technique IDs, and threat-intel verdicts that drove it. |
| :mortar_board: | **[XAI_LLM_NetPacketAnalyzer](https://github.com/Youssef-Saleh/XAI_LLM_NetPacketAnalyzer)** | My M.Sc. thesis. CNN-LSTM network-intrusion classifier on UNSW-NB15 + NSL-KDD (96.76% acc, 0.97 F1, 0.995 AUC) with a 4-tier SHAP/LIME + local Mistral-7B explanation pipeline for Security Analysts, IT Managers, Developers, and Compliance Officers. |
| :bar_chart: | **[NetworkQueueTrafficModeler](https://github.com/Youssef-Saleh/NetworkQueueTrafficModeler)** | Erlang-C + Little's Law modeler that mathematically derives the exact point at which a router's buffer will fail under load. |
| :hospital: | **[Pacify](https://github.com/Youssef-Saleh/Pacify-FrontEnd)** | Full-stack patient-management platform — React front-end, Node back-end, native Android client, Cypress-tested. Four repos, end-to-end ownership. |

<details>
  <summary><b>16 more repositories</b></summary>
  <br/>

  | Repo | What it is |
  |---|---|
  | [`WeatherApp`](https://github.com/Youssef-Saleh/WeatherApp) | JavaScript weather client consuming a public API |
  | [`Emergency-Department-Patient-Flow`](https://github.com/Youssef-Saleh/Emergency-Department-Patient-Flow) | Jupyter Notebook simulation of ED triage throughput |
  | [`GP-MSI`](https://github.com/Youssef-Saleh/GP-MSI) | Gaussian-Process MSI analysis notebook |
  | [`ProteinMass-Visualization`](https://github.com/Youssef-Saleh/ProteinMass-Visualization) | Mass-spec visualization notebook |
  | [`CNN-Image-Classification`](https://github.com/Youssef-Saleh/CNN-Image-Classification) | Baseline CNN image classifier notebook |
  | [`ImageSegmentation`](https://github.com/Youssef-Saleh/ImageSegmentation) | Image-segmentation experiments |
  | [`BinaryClassification`](https://github.com/Youssef-Saleh/BinaryClassification) | Binary classification baselines & comparisons |
  | [`Assignment1_Pattern`](https://github.com/Youssef-Saleh/Assignment1_Pattern) | Pattern-recognition coursework |
  | [`T1-Project`](https://github.com/Youssef-Saleh/T1-Project) | JavaScript team project (T1 cohort) |
  | [`Beat-Project-T1`](https://github.com/Youssef-Saleh/Beat-Project-T1) | JavaScript rhythm-game project |
  | [`Site_v0`](https://github.com/Youssef-Saleh/Site_v0) | First personal site |
  | [`Pacify-Testing`](https://github.com/Youssef-Saleh/Pacify-Testing) | Cypress / test automation for Pacify |
  | [`Pacify-BackEnd`](https://github.com/Youssef-Saleh/Pacify-BackEnd) | Node back-end for Pacify |
  | [`Pacify-Android`](https://github.com/Youssef-Saleh/Pacify-Android) | Native Android client for Pacify |
  | [`Body-Signals-Filtering`](https://github.com/Youssef-Saleh/Body-Signals-Filtering) | BMEN 3311 biomedical signal processing final |
  | [`ivy`](https://github.com/Youssef-Saleh/ivy) | Forked exploration of the unified ML framework |

</details>

---

## Connect

<p align="left">
  <a href="mailto:youssef.s.saleh@gmail.com">:e-mail: youssef.s.saleh@gmail.com</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/youssef-saleh/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="https://github.com/Youssef-Saleh">GitHub</a> &nbsp;·&nbsp;
  <a href="https://launchgood-trust-copilot.fly.dev/">Live demo</a>
</p>

<sub>:construction: hand-built. the hero is a 26 KB inline SVG that renders identically on every client — no external badges, no stats services, no broken images. the timeline marker pulses.</sub>

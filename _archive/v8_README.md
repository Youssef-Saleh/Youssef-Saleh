<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1100" font-family="'Inter','Segoe UI','Helvetica Neue',sans-serif">
  <!-- =========================================================
       C2 CONSOLE v7 — designer-pass redesign
       Five flaws fixed:
         1. Each panel has a distinct hue family (slate / cyan panel / amber)
         2. Radar values rescaled to 0-100 so the polygon is irregular
         3. Y_S redesigned as joined ligature with versioned lockup
         4. Two typefaces: Inter for prose, JetBrains Mono for IDs
         5. Linear timeline with even year ticks, leader lines, dot above
       ========================================================= -->

  <defs>
    <!-- background: deep slate with subtle vignette -->
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0c1322"/>
      <stop offset="1" stop-color="#060a14"/>
    </linearGradient>
    <radialGradient id="vig" cx="0.5" cy="0.5" r="0.7">
      <stop offset="0" stop-color="#000" stop-opacity="0"/>
      <stop offset="1" stop-color="#000" stop-opacity="0.5"/>
    </radialGradient>

    <!-- panel hues -->
    <!-- left rail: slate/identity - subtle, recedes -->
    <!-- center: cyan/capability - bright, focal -->
    <!-- right: amber/stream - warm, secondary -->
    <!-- timeline: neutral/ink - foundational, structural -->

    <!-- subtle noise for paper-like texture (no pattern, just a few sparse dots) -->
  </defs>

  <!-- background -->
  <rect x="0" y="0" width="1200" height="900" fill="url(#bg)"/>
  <rect x="0" y="0" width="1200" height="900" fill="url(#vig)"/>

  <!-- ============================== HEADER STRIP ============================== -->
  <g>
    <!-- FIX: subtle hairline rule under the header row, plus a balance on the right (location pill) -->
    <line x1="60" y1="80" x2="1140" y2="80" stroke="#1c2a44" stroke-width="0.5"/>
    <line x1="60" y1="84" x2="1140" y2="84" stroke="#1c2a44" stroke-width="0.25"/>
    <!-- wordmark: monogram + wordmark together (FIX #3: redesigned lockup) -->
    <g transform="translate(60, 32)">
      <!-- joined Y/S monogram (FIX #3) -->
      <text font-family="'JetBrains Mono','SF Mono',monospace" font-weight="700" font-size="22" fill="#19c7d9" letter-spacing="-1">y<tspan dx="-3" font-weight="300" fill="#c9d1d9">/</tspan>s</text>
      <!-- versioned subline -->
      <text x="56" y="-2" font-family="'JetBrains Mono',monospace" font-size="9" fill="#5a6678" letter-spacing="1">youssef.saleh  //  v3.0</text>
    </g>
    <!-- identity meta -->
    <text x="320" y="48" font-family="'JetBrains Mono',monospace" font-size="11" fill="#8a96ac" letter-spacing="0.5">M.Sc. CS · University of Idaho · 2026</text>
    <text x="320" y="64" font-family="'JetBrains Mono',monospace" font-size="10" fill="#5a6678" letter-spacing="0.5">applied AI  ·  network security  ·  explainable AI</text>
    <!-- FIX: a "location" pill on the right, mirroring the OPEN pill on the left of the status block -->
    <g transform="translate(960, 38)">
      <rect x="0" y="0" width="92" height="20" rx="10" fill="#0a1018" stroke="#1c2a44" stroke-width="0.5"/>
      <circle cx="10" cy="10" r="2.5" fill="#8a96ac"/>
      <text x="20" y="14" font-family="'JetBrains Mono',monospace" font-size="9" fill="#8a96ac" letter-spacing="1">ANN ARBOR · MI</text>
    </g>
    <!-- status pill on the right (FIX #4: stronger type hierarchy) -->
    <g transform="translate(1060, 28)">
      <rect x="0" y="0" width="80" height="22" rx="11" fill="#0d2e1f" stroke="#4ade80" stroke-width="0.75">
        <!-- breathing stroke to make the status feel alive -->
        <animate attributeName="stroke-opacity" values="1;0.4;1" dur="2.4s" repeatCount="indefinite"/>
      </rect>
      <circle cx="10" cy="11" r="3" fill="#4ade80">
        <animate attributeName="opacity" values="1;0.3;1" dur="1.6s" repeatCount="indefinite"/>
      </circle>
      <text x="20" y="15" font-family="'JetBrains Mono',monospace" font-size="9" fill="#4ade80" font-weight="700" letter-spacing="1">OPEN</text>
      <!-- uptime, small mono caption -->
      <text x="80" y="50" font-family="'JetBrains Mono',monospace" font-size="9" fill="#5a6678" letter-spacing="1">UPTIME · 26y 137d</text>
    </g>
  </g>

  <!-- ============================== LEFT RAIL: IDENTITY ============================== -->
  <!-- FIX #1: slate-toned panel, recedes from the bright cyan center -->
  <g>
    <!-- panel: subtle slate background, no fill (let the bg show), thin border -->
    <rect x="40" y="110" width="260" height="670" fill="#0a1018" stroke="#1c2a44" stroke-width="0.5" rx="4"/>
    <!-- top accent: thin slate line under the title strip -->
    <rect x="40" y="110" width="260" height="36" fill="#0d141f"/>
    <!-- section ID badge (mono, top-left) -->
    <text x="56" y="134" font-family="'JetBrains Mono',monospace" font-size="9" fill="#5a6678" letter-spacing="2">// IDENTITY</text>
    <text x="284" y="134" font-family="'JetBrains Mono',monospace" font-size="9" fill="#5a6678" text-anchor="end" letter-spacing="1">0x01</text>

    <!-- ===== Y/S monogram (FIX #3 — redesigned) ===== -->
    <g transform="translate(170, 240)">
      <!-- versioned wordmark: joined Y/S with slash through the middle, version below -->
      <!-- a real logo: a square containing the monogram, version, and unit ID -->
      <rect x="-60" y="-60" width="120" height="120" fill="#0d141f" stroke="#1c2a44" stroke-width="0.5" rx="2"/>
      <!-- corner brackets -->
      <g stroke="#19c7d9" stroke-width="0.75" fill="none">
        <path d="M -54 -54 L -54 -46 M -54 -54 L -46 -54"/>
        <path d="M 54 -54 L 54 -46 M 54 -54 L 46 -54"/>
        <path d="M -54 54 L -54 46 M -54 54 L -46 54"/>
        <path d="M 54 54 L 54 46 M 54 54 L 46 54"/>
      </g>
      <!-- the Y/S ligature, drawn as shapes not just text -->
      <!-- Y: two strokes converging -->
      <line x1="-22" y1="-28" x2="0" y2="0" stroke="#19c7d9" stroke-width="4" stroke-linecap="square"/>
      <line x1="22" y1="-28" x2="0" y2="0" stroke="#19c7d9" stroke-width="4" stroke-linecap="square"/>
      <line x1="0" y1="0" x2="0" y2="22" stroke="#19c7d9" stroke-width="4" stroke-linecap="square"/>
      <!-- a thin diagonal /S stroke through the right -->
      <path d="M 18 -10 Q 26 0 18 10 Q 10 20 18 28" stroke="#c9d1d9" stroke-width="2.5" fill="none" stroke-linecap="square"/>
      <!-- subtitle -->
      <text x="0" y="40" font-family="'JetBrains Mono',monospace" font-size="7" fill="#5a6678" text-anchor="middle" letter-spacing="2">C2 // CONSOLE</text>
      <text x="0" y="50" font-family="'JetBrains Mono',monospace" font-size="6" fill="#3a4458" text-anchor="middle" letter-spacing="1.5">FILE 0x6F75737365</text>
    </g>

    <!-- ===== bio block (FIX #4: prose in Inter sans, IDs in mono) ===== -->
    <g transform="translate(56, 340)">
      <!-- Each line: tiny mono label + larger Inter value -->
      <text x="0" y="0"  font-family="'JetBrains Mono',monospace" font-size="8" fill="#5a6678" letter-spacing="2">NAME</text>
      <text x="0" y="22" font-family="'Inter',sans-serif" font-size="17" font-weight="500" fill="#e6edf7">Youssef Saleh</text>

      <text x="0" y="58"  font-family="'JetBrains Mono',monospace" font-size="8" fill="#5a6678" letter-spacing="2">LOCATION</text>
      <text x="0" y="80" font-family="'Inter',sans-serif" font-size="13" fill="#c9d1d9">Ann Arbor, MI</text>

      <text x="0" y="116" font-family="'JetBrains Mono',monospace" font-size="8" fill="#5a6678" letter-spacing="2">FOCUS</text>
      <text x="0" y="138" font-family="'Inter',sans-serif" font-size="13" fill="#c9d1d9">XAI  ·  LLM agents</text>
      <text x="0" y="156" font-family="'Inter',sans-serif" font-size="13" fill="#c9d1d9">network security</text>

      <text x="0" y="192" font-family="'JetBrains Mono',monospace" font-size="8" fill="#5a6678" letter-spacing="2">EMAIL</text>
      <text x="0" y="212" font-family="'Inter',sans-serif" font-size="12" fill="#c9d1d9">youssef.s.saleh</text>
      <text x="0" y="228" font-family="'Inter',sans-serif" font-size="12" fill="#c9d1d9">@gmail.com</text>

      <text x="0" y="264" font-family="'JetBrains Mono',monospace" font-size="8" fill="#5a6678" letter-spacing="2">REACH</text>
      <text x="0" y="284" font-family="'Inter',sans-serif" font-size="11" fill="#8a96ac">email · LinkedIn</text>
      <text x="0" y="300" font-family="'Inter',sans-serif" font-size="11" fill="#8a96ac">live demo (TrustEval)</text>
    </g>

    <!-- ===== STACK LIST (v8: moved from center to left rail, compact vertical list) ===== -->
    <g transform="translate(56, 380)">
      <text x="0" y="0" font-family="'JetBrains Mono',monospace" font-size="8" fill="#5a6678" letter-spacing="2">STACK · DAILY TOOLS</text>
      <line x1="0" y1="6" x2="208" y2="6" stroke="#1c2a44" stroke-width="0.5"/>
      <!-- each tool: name + thin bar + value, all 30px row pitch -->
      <g font-family="'Inter',sans-serif" font-size="10">
        <g transform="translate(0, 24)">
          <text fill="#c9d1d9">Python</text>
          <rect x="0" y="6" width="208" height="2" fill="#1c2a44"/>
          <rect x="0" y="6" width="200" height="2" fill="#19c7d9"/>
          <text x="208" y="0" font-family="'JetBrains Mono',monospace" font-size="8" fill="#19c7d9" text-anchor="end">96</text>
        </g>
        <g transform="translate(0, 48)">
          <text fill="#c9d1d9">PyTorch</text>
          <rect x="0" y="6" width="208" height="2" fill="#1c2a44"/>
          <rect x="0" y="6" width="170" height="2" fill="#19c7d9"/>
          <text x="208" y="0" font-family="'JetBrains Mono',monospace" font-size="8" fill="#19c7d9" text-anchor="end">82</text>
        </g>
        <g transform="translate(0, 72)">
          <text fill="#c9d1d9">LangGraph</text>
          <rect x="0" y="6" width="208" height="2" fill="#1c2a44"/>
          <rect x="0" y="6" width="158" height="2" fill="#19c7d9"/>
          <text x="208" y="0" font-family="'JetBrains Mono',monospace" font-size="8" fill="#19c7d9" text-anchor="end">76</text>
        </g>
        <g transform="translate(0, 96)">
          <text fill="#c9d1d9">FastAPI</text>
          <rect x="0" y="6" width="208" height="2" fill="#1c2a44"/>
          <rect x="0" y="6" width="152" height="2" fill="#19c7d9"/>
          <text x="208" y="0" font-family="'JetBrains Mono',monospace" font-size="8" fill="#19c7d9" text-anchor="end">73</text>
        </g>
        <g transform="translate(0, 120)">
          <text fill="#c9d1d9">Docker</text>
          <rect x="0" y="6" width="208" height="2" fill="#1c2a44"/>
          <rect x="0" y="6" width="141" height="2" fill="#19c7d9"/>
          <text x="208" y="0" font-family="'JetBrains Mono',monospace" font-size="8" fill="#19c7d9" text-anchor="end">68</text>
        </g>
        <g transform="translate(0, 144)">
          <text fill="#f29e2e">AWS</text>
          <rect x="0" y="6" width="208" height="2" fill="#1c2a44"/>
          <rect x="0" y="6" width="112" height="2" fill="#f29e2e"/>
          <text x="208" y="0" font-family="'JetBrains Mono',monospace" font-size="8" fill="#f29e2e" text-anchor="end">54</text>
        </g>
        <g transform="translate(0, 168)">
          <text fill="#f29e2e">C++</text>
          <rect x="0" y="6" width="208" height="2" fill="#1c2a44"/>
          <rect x="0" y="6" width="75" height="2" fill="#f29e2e"/>
          <text x="208" y="0" font-family="'JetBrains Mono',monospace" font-size="8" fill="#f29e2e" text-anchor="end">36</text>
        </g>
      </g>
    </g>

    <!-- footer hash at the bottom of the rail -->
    <!-- FIX: demoted to 9px, dimmer color, and grouped under a "// BUILD" label so it doesn't compete with EMAIL/REACH -->
    <g transform="translate(56, 700)" font-family="'JetBrains Mono',monospace" font-size="9" fill="#3a4458" letter-spacing="1">
      <text x="0" y="0" fill="#5a6678">// BUILD</text>
      <text x="0" y="14">hash  7e3c.0a91.f29e</text>
      <text x="0" y="28">key   ECC:P-256</text>
      <text x="0" y="42">build brutstyl-v4.2.6</text>
    </g>
  </g>

  <!-- ============================== CENTER: CAPABILITY MATRIX ============================== -->
  <!-- FIX #1: the bright cyan panel - the focal point -->
  <g>
    <!-- a subtle glow behind the panel to make it the visual anchor -->
    <rect x="316" y="106" width="568" height="674" fill="#0d1929" stroke="#1f3a5a" stroke-width="0.75" rx="4"/>
    <!-- subtle inner gradient for depth -->
    <rect x="316" y="106" width="568" height="674" fill="url(#bg)" opacity="0.4" rx="4"/>
    <!-- top accent strip in CYAN (FIX #1) -->
    <rect x="316" y="106" width="568" height="3" fill="#19c7d9"/>
    <!-- title strip -->
    <rect x="316" y="110" width="568" height="36" fill="#0d1a2b"/>
    <text x="332" y="134" font-family="'JetBrains Mono',monospace" font-size="9" fill="#5a6678" letter-spacing="2">// CAPABILITY MATRIX</text>
    <text x="868" y="134" font-family="'JetBrains Mono',monospace" font-size="9" fill="#19c7d9" text-anchor="end" letter-spacing="1">0x02</text>

    <!-- ===== RADAR CHART (v8: the hero of the center panel) ===== -->
    <!--
      v8: enlarged 1.7x. Reference grid uses 5 hex levels (max=100).
      The polygon is irregular, with 6 named axes, vertex values
      shown in teal, and an amber dashed inner outline for warmth.
    -->
    <g transform="translate(600, 410)">
      <!-- Reference grid: outer hexagon at max=100 (radius 200) -->
      <g fill="none" stroke="#1c2a44" stroke-width="0.5">
        <polygon points="0,-200 173,-100 173,100 0,200 -173,100 -173,-100"/>
      </g>
      <g fill="none" stroke="#1c2a44" stroke-width="0.5" stroke-dasharray="2,3">
        <polygon points="0,-150 130,-75 130,75 0,150 -130,75 -130,-75"/>
        <polygon points="0,-100 87,-50 87,50 0,100 -87,50 -87,-50"/>
        <polygon points="0,-50 43,-25 43,25 0,50 -43,25 -43,-25"/>
      </g>
      <!-- axis spokes -->
      <g stroke="#1c2a44" stroke-width="0.5">
        <line x1="0" y1="0" x2="0" y2="-200"/>
        <line x1="0" y1="0" x2="173" y2="-100"/>
        <line x1="0" y1="0" x2="173" y2="100"/>
        <line x1="0" y1="0" x2="0" y2="200"/>
        <line x1="0" y1="0" x2="-173" y2="100"/>
        <line x1="0" y1="0" x2="-173" y2="-100"/>
      </g>
      <!--
        Capability values (rescaled so the polygon is irregular):
        AI/ML=92, SEC=87, ENG=68, XAI=95, DATA=72, SHIP=80
        radius = value/100 * 200
      -->
      <!-- filled polygon (v8: subtle breathing animation) -->
      <polygon points="0,-184 152,-83 117,67 0,190 -103,60 -139,-80"
               fill="#19c7d9" fill-opacity="0.18"
               stroke="#19c7d9" stroke-width="2.5">
        <animate attributeName="fill-opacity" values="0.18;0.32;0.18" dur="4s" repeatCount="indefinite"/>
      </polygon>
      <!-- subtle inner amber outline for warmth -->
      <polygon points="0,-184 152,-83 117,67 0,190 -103,60 -139,-80"
               fill="none" stroke="#f29e2e" stroke-width="0.5" stroke-dasharray="3,3"/>
      <!-- axis labels (large, bold) -->
      <g font-size="13" font-weight="700" fill="#c9d1d9" text-anchor="middle" letter-spacing="2">
        <text x="0" y="-220">AI/ML</text>
        <text x="195" y="-108">SEC</text>
        <text x="195" y="118">ENG</text>
        <text x="0" y="232">XAI</text>
        <text x="-195" y="118">DATA</text>
        <text x="-195" y="-108">SHIP</text>
      </g>
      <!-- values next to each axis label -->
      <g font-size="11" font-weight="700" fill="#19c7d9" text-anchor="middle">
        <text x="0" y="-205">92</text>
        <text x="195" y="-93">87</text>
        <text x="195" y="133" fill="#f29e2e">68</text>
        <text x="0" y="247">95</text>
        <text x="-195" y="133">72</text>
        <text x="-195" y="-93">80</text>
      </g>
      <!-- vertex dots (bigger for the larger chart) -->
      <g fill="#f29e2e" stroke="#0a0e1a" stroke-width="2">
        <circle cx="0" cy="-184" r="5"/>
        <circle cx="152" cy="-83" r="5"/>
        <circle cx="117" cy="67" r="5"/>
        <circle cx="0" cy="190" r="5"/>
        <circle cx="-103" cy="60" r="5"/>
        <circle cx="-139" cy="-80" r="5"/>
      </g>
      <!-- center crosshair -->
      <line x1="-6" y1="0" x2="6" y2="0" stroke="#19c7d9" stroke-width="0.5"/>
      <line x1="0" y1="-6" x2="0" y2="6" stroke="#19c7d9" stroke-width="0.5"/>
    </g>

    <!-- ===== TRUSTEVAL-AI COMPACT BADGE (v8: moved to top of center panel, above the radar) ===== -->
    <g transform="translate(600, 130)">
      <!-- a small "currently shipping" tag, centered above the radar -->
      <rect x="-120" y="0" width="240" height="32" fill="#0d1a2b" stroke="#1c2a44" stroke-width="0.5" rx="4"/>
      <rect x="-120" y="0" width="3" height="32" fill="#19c7d9"/>
      <text x="-104" y="20" font-family="'JetBrains Mono',monospace" font-size="9" fill="#5a6678" letter-spacing="2">// SHIPPING</text>
      <text x="-104" y="32" font-family="'Inter',sans-serif" font-size="12" font-weight="600" fill="#19c7d9">TrustEvaluatorAI</text>
      <text x="116" y="20" font-family="'JetBrains Mono',monospace" font-size="9" fill="#5a6678" text-anchor="end" letter-spacing="1">5 agents</text>
      <text x="116" y="32" font-family="'JetBrains Mono',monospace" font-size="9" fill="#4ade80" text-anchor="end" font-weight="700">7/7 ✓</text>
    </g>

    <!-- ===== STACK DEPTH (v8: REMOVED from center; moved to left rail below the bio) ===== -->
    <!-- v8: stack bars moved to the left rail as a compact vertical list -->

    <!-- ===== THESIS METRICS — bottom of center panel ===== -->
    <!-- FIX v2: instead of a connector line (which was invisible), the thesis row is now grouped under a single header that names BOTH the radar (top) and metrics (below) -->
    <g transform="translate(332, 590)">
      <text x="0" y="0" font-family="'JetBrains Mono',monospace" font-size="9" fill="#5a6678" letter-spacing="2">// THESIS · XAI_LLM_NetPacketAnalyzer · CNN-LSTM + SHAP/LIME</text>
      <text x="568" y="0" font-family="'JetBrains Mono',monospace" font-size="8" fill="#3a4458" text-anchor="end" letter-spacing="1">CNN-LSTM · mistral-7B</text>
      <!-- sparkline card row -->
      <g transform="translate(0, 16)">
        <!-- 4 mini sparkline cards (FIX #8: self-drawing polylines) -->
        <g>
          <rect x="0" y="0" width="130" height="80" fill="#0a1018" stroke="#1c2a44" stroke-width="0.5" rx="2"/>
          <text x="65" y="16" font-family="'JetBrains Mono',monospace" font-size="8" fill="#5a6678" text-anchor="middle" letter-spacing="1">ACCURACY</text>
          <text x="65" y="40" font-family="'Inter',sans-serif" font-size="20" font-weight="600" fill="#19c7d9" text-anchor="middle">96.8%</text>
          <polyline points="10,68 30,62 50,58 70,56 90,55 110,54 120,53" stroke="#19c7d9" stroke-width="1" fill="none"
                    stroke-dasharray="200" stroke-dashoffset="200">
            <animate attributeName="stroke-dashoffset" from="200" to="0" dur="2s" fill="freeze"/>
          </polyline>
          <text x="65" y="76" font-family="'JetBrains Mono',monospace" font-size="7" fill="#3a4458" text-anchor="middle">UNSW-NB15 + NSL-KDD</text>
        </g>
        <g transform="translate(140, 0)">
          <rect x="0" y="0" width="130" height="80" fill="#0a1018" stroke="#1c2a44" stroke-width="0.5" rx="2"/>
          <text x="65" y="16" font-family="'JetBrains Mono',monospace" font-size="8" fill="#5a6678" text-anchor="middle" letter-spacing="1">F1-SCORE</text>
          <text x="65" y="40" font-family="'Inter',sans-serif" font-size="20" font-weight="600" fill="#19c7d9" text-anchor="middle">0.9675</text>
          <polyline points="10,68 30,65 50,62 70,60 90,58 110,55 120,53" stroke="#19c7d9" stroke-width="1" fill="none"
                    stroke-dasharray="200" stroke-dashoffset="200">
            <animate attributeName="stroke-dashoffset" from="200" to="0" dur="2s" begin="0.3s" fill="freeze"/>
          </polyline>
          <text x="65" y="76" font-family="'JetBrains Mono',monospace" font-size="7" fill="#3a4458" text-anchor="middle">2-tier SHAP + LIME</text>
        </g>
        <g transform="translate(280, 0)">
          <rect x="0" y="0" width="130" height="80" fill="#0a1018" stroke="#1c2a44" stroke-width="0.5" rx="2"/>
          <text x="65" y="16" font-family="'JetBrains Mono',monospace" font-size="8" fill="#5a6678" text-anchor="middle" letter-spacing="1">ROC-AUC</text>
          <text x="65" y="40" font-family="'Inter',sans-serif" font-size="20" font-weight="600" fill="#19c7d9" text-anchor="middle">0.9952</text>
          <polyline points="10,68 30,64 50,60 70,57 90,55 110,53 120,52" stroke="#19c7d9" stroke-width="1" fill="none"
                    stroke-dasharray="200" stroke-dashoffset="200">
            <animate attributeName="stroke-dashoffset" from="200" to="0" dur="2s" begin="0.6s" fill="freeze"/>
          </polyline>
          <text x="65" y="76" font-family="'JetBrains Mono',monospace" font-size="7" fill="#3a4458" text-anchor="middle">excellent class sep.</text>
        </g>
        <g transform="translate(420, 0)">
          <rect x="0" y="0" width="110" height="80" fill="#0a1018" stroke="#1c2a44" stroke-width="0.5" rx="2"/>
          <text x="55" y="16" font-family="'JetBrains Mono',monospace" font-size="8" fill="#5a6678" text-anchor="middle" letter-spacing="1">HALLUC.</text>
          <text x="55" y="40" font-family="'Inter',sans-serif" font-size="20" font-weight="600" fill="#f29e2e" text-anchor="middle">5.5%</text>
          <polyline points="10,68 30,65 50,62 70,60 90,58 100,57" stroke="#f29e2e" stroke-width="1" fill="none"
                    stroke-dasharray="200" stroke-dashoffset="200">
            <animate attributeName="stroke-dashoffset" from="200" to="0" dur="2s" begin="0.9s" fill="freeze"/>
          </polyline>
          <text x="55" y="76" font-family="'JetBrains Mono',monospace" font-size="7" fill="#3a4458" text-anchor="middle">mistral-7B local</text>
        </g>
      </g>
    </g>
  </g>

  <!-- ============================== RIGHT: EVENT STREAM ============================== -->
  <!-- FIX #1: warm amber-toned panel, distinct from slate and cyan -->
  <g>
    <rect x="900" y="110" width="260" height="380" fill="#150f08" stroke="#2a2218" stroke-width="0.5" rx="4"/>
    <rect x="900" y="110" width="260" height="3" fill="#f29e2e"/>
    <rect x="900" y="110" width="260" height="36" fill="#181208"/>
    <text x="916" y="134" font-family="'JetBrains Mono',monospace" font-size="9" fill="#8a6a4a" letter-spacing="2">// EVENT STREAM</text>
    <text x="1144" y="134" font-family="'JetBrains Mono',monospace" font-size="9" fill="#f29e2e" text-anchor="end" letter-spacing="1">0x03</text>

    <!-- 4x3 grid of mini tech icons, hand-drawn -->
    <g transform="translate(916, 162)">
      <!-- python -->
      <g transform="translate(0,0)">
        <rect x="0" y="0" width="42" height="42" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="2"/>
        <g stroke="#19c7d9" fill="none" stroke-width="1.5">
          <path d="M 10 30 Q 10 34 16 34 L 25 34 Q 31 34 31 29 L 31 24 Q 31 20 25 20 L 18 20 Q 10 20 10 16 L 10 11 Q 10 6 16 6"/>
          <path d="M 31 19 Q 31 14 25 14 L 18 14 Q 10 14 10 17"/>
        </g>
        <circle cx="16" cy="11" r="1.3" fill="#19c7d9"/>
        <circle cx="25" cy="34" r="1.3" fill="#19c7d9"/>
        <text x="21" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">python</text>
      </g>
      <!-- pytorch -->
      <g transform="translate(48, 0)">
        <rect x="0" y="0" width="42" height="42" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="2"/>
        <g stroke="#f29e2e" fill="none" stroke-width="1.5">
          <path d="M 21 38 Q 10 32 12 20 Q 14 11 21 6 Q 28 11 30 20 Q 32 32 21 38 Z"/>
          <path d="M 21 38 Q 18 28 21 19 Q 24 28 21 38 Z" fill="#f29e2e" fill-opacity="0.4"/>
        </g>
        <text x="21" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">pytorch</text>
      </g>
      <!-- langgraph -->
      <g transform="translate(96, 0)">
        <rect x="0" y="0" width="42" height="42" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="2"/>
        <g stroke="#19c7d9" stroke-width="1.5" fill="none">
          <line x1="11" y1="11" x2="31" y2="17"/>
          <line x1="11" y1="11" x2="31" y2="25"/>
          <line x1="31" y1="17" x2="11" y2="31"/>
          <line x1="31" y1="25" x2="11" y2="31"/>
        </g>
        <g fill="#0a0805" stroke="#19c7d9" stroke-width="1.5">
          <circle cx="11" cy="11" r="3"/>
          <circle cx="31" cy="17" r="3"/>
          <circle cx="31" cy="25" r="3"/>
          <circle cx="11" cy="31" r="3"/>
        </g>
        <text x="21" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">langgraph</text>
      </g>
      <!-- fastapi -->
      <g transform="translate(144, 0)">
        <rect x="0" y="0" width="42" height="42" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="2"/>
        <path d="M 25 5 L 12 25 L 20 25 L 17 38 L 30 16 L 22 16 Z" fill="#f29e2e" fill-opacity="0.4" stroke="#f29e2e" stroke-width="1.5"/>
        <text x="21" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">fastapi</text>
      </g>

      <!-- row 2 -->
      <g transform="translate(0, 64)">
        <rect x="0" y="0" width="42" height="42" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="2"/>
        <g stroke="#19c7d9" fill="none" stroke-width="1.5">
          <rect x="6"  y="14" width="30" height="6"/>
          <rect x="6"  y="22" width="20" height="6"/>
          <rect x="6"  y="30" width="30" height="4"/>
          <line x1="14" y1="14" x2="14" y2="8"/>
          <line x1="26" y1="14" x2="26" y2="8"/>
        </g>
        <text x="21" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">docker</text>
      </g>
      <g transform="translate(48, 64)">
        <rect x="0" y="0" width="42" height="42" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="2"/>
        <g stroke="#f29e2e" fill="none" stroke-width="1.5">
          <polygon points="21,6 35,13 35,29 21,36 7,29 7,13"/>
          <polyline points="7,13 21,19 35,13"/>
          <line x1="21" y1="19" x2="21" y2="36"/>
        </g>
        <text x="21" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">aws</text>
      </g>
      <g transform="translate(96, 64)">
        <rect x="0" y="0" width="42" height="42" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="2"/>
        <g stroke="#19c7d9" fill="none" stroke-width="1.5">
          <path d="M 21 6 L 33 11 L 33 25 Q 33 32 21 36 Q 9 32 9 25 L 9 11 Z"/>
        </g>
        <text x="21" y="29" font-family="'Inter',sans-serif" font-size="11" font-weight="700" fill="#19c7d9" text-anchor="middle">A&amp;</text>
        <text x="21" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">mitre</text>
      </g>
      <g transform="translate(144, 64)">
        <rect x="0" y="0" width="42" height="42" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="2"/>
        <line x1="8" y1="36" x2="34" y2="36" stroke="#8a96ac" stroke-width="0.5"/>
        <rect x="10" y="22" width="4" height="14" fill="#19c7d9"/>
        <rect x="18" y="12" width="4" height="24" fill="#f29e2e"/>
        <rect x="26" y="18" width="4" height="18" fill="#19c7d9"/>
        <text x="21" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">shap</text>
      </g>

      <!-- row 3 -->
      <g transform="translate(0, 128)">
        <rect x="0" y="0" width="42" height="42" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="2"/>
        <g stroke="#19c7d9" fill="none" stroke-width="1.5">
          <rect x="6"  y="10" width="12" height="6"/>
          <rect x="22" y="10" width="12" height="6"/>
          <rect x="11" y="18" width="12" height="6"/>
          <rect x="26" y="18" width="6"  height="6"/>
          <rect x="6"  y="26" width="12" height="6"/>
          <rect x="22" y="26" width="12" height="6"/>
        </g>
        <text x="21" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">pan-os</text>
      </g>
      <g transform="translate(48, 128)">
        <rect x="0" y="0" width="42" height="42" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="2"/>
        <g stroke="#19c7d9" fill="none" stroke-width="1.5">
          <circle cx="21" cy="21" r="13"/>
          <circle cx="21" cy="21" r="7" stroke-dasharray="2,2"/>
          <line x1="21" y1="21" x2="30" y2="12" stroke="#f29e2e"/>
        </g>
        <text x="21" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">scapy</text>
      </g>
      <g transform="translate(96, 128)">
        <rect x="0" y="0" width="42" height="42" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="2"/>
        <g stroke="#19c7d9" fill="none" stroke-width="1.5">
          <line x1="9" y1="36" x2="35" y2="36" stroke="#8a96ac"/>
          <rect x="12" y="28" width="3" height="8" fill="#19c7d9"/>
          <rect x="17" y="20" width="3" height="16" fill="#19c7d9"/>
          <rect x="22" y="24" width="3" height="12" fill="#f29e2e"/>
          <rect x="27" y="14" width="3" height="22" fill="#19c7d9"/>
        </g>
        <text x="21" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">data</text>
      </g>
      <g transform="translate(144, 128)">
        <rect x="0" y="0" width="42" height="42" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="2"/>
        <g stroke="#f29e2e" fill="none" stroke-width="2">
          <line x1="26" y1="12" x2="12" y2="30"/>
          <line x1="32" y1="20" x2="18" y2="36"/>
          <line x1="19" y1="20" x2="28" y2="12"/>
        </g>
        <g fill="#f29e2e">
          <circle cx="26" cy="12" r="3"/>
          <circle cx="12" cy="30" r="3"/>
          <circle cx="32" cy="20" r="3"/>
        </g>
        <text x="21" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">git</text>
      </g>
    </g>

    <!-- separator line under icon grid -->
    <line x1="916" y1="382" x2="1144" y2="382" stroke="#2a2218" stroke-width="0.5"/>

    <!-- recent events log -->
    <g transform="translate(916, 398)" font-family="'JetBrains Mono',monospace" font-size="9">
      <text x="0" y="0" fill="#8a6a4a" letter-spacing="2">// RECENT EVENTS</text>
      <g transform="translate(0, 18)">
        <text x="0" y="0" fill="#3a4458">10:02:14</text>
        <text x="58" y="0" fill="#4ade80">[OK]</text>
        <text x="86" y="0" fill="#c9d1d9">M.Sc. conferred</text>

        <text x="0" y="14" fill="#3a4458">09:54:02</text>
        <text x="58" y="14" fill="#19c7d9">[INFO]</text>
        <text x="94" y="14" fill="#c9d1d9">TrustEval deployed</text>

        <text x="0" y="28" fill="#3a4458">09:11:47</text>
        <text x="58" y="28" fill="#f29e2e">[WARN]</text>
        <text x="94" y="28" fill="#c9d1d9">7/7 eval pass</text>

        <text x="0" y="42" fill="#3a4458">07:15:33</text>
        <text x="58" y="42" fill="#4ade80">[OK]</text>
        <text x="86" y="42" fill="#c9d1d9">Pacify shipped</text>
      </g>
    </g>

    <!-- ============================== TICKER (FIX #9: live data feed) ============================== -->
    <g transform="translate(900, 510)">
      <rect x="0" y="0" width="260" height="240" fill="#0a0805" stroke="#2a2218" stroke-width="0.5" rx="4"/>
      <rect x="0" y="0" width="260" height="3" fill="#f29e2e"/>
      <rect x="0" y="0" width="260" height="36" fill="#181208"/>
      <text x="16" y="24" font-family="'JetBrains Mono',monospace" font-size="9" fill="#8a6a4a" letter-spacing="2">// LIVE FEED</text>
      <text x="244" y="24" font-family="'JetBrains Mono',monospace" font-size="9" fill="#f29e2e" text-anchor="end" letter-spacing="1">0x05</text>
      <!-- scrolling log: a static block of text that fades from full opacity to dim -->
      <g transform="translate(16, 60)" font-family="'JetBrains Mono',monospace" font-size="9">
        <g opacity="0.95">
          <text x="0" y="0" fill="#5a6678">14:00:01</text>
          <text x="64" y="0" fill="#4ade80">[200]</text>
          <text x="100" y="0" fill="#c9d1d9">GET /README.md</text>
        </g>
        <g opacity="0.85">
          <text x="0" y="14" fill="#5a6678">14:00:01</text>
          <text x="64" y="14" fill="#19c7d9">[200]</text>
          <text x="100" y="14" fill="#c9d1d9">load profile.svg</text>
        </g>
        <g opacity="0.7">
          <text x="0" y="28" fill="#5a6678">14:00:01</text>
          <text x="64" y="28" fill="#19c7d9">[200]</text>
          <text x="100" y="28" fill="#c9d1d9">render hex dump</text>
        </g>
        <g opacity="0.55">
          <text x="0" y="42" fill="#5a6678">14:00:01</text>
          <text x="64" y="42" fill="#f29e2e">[304]</text>
          <text x="100" y="42" fill="#c9d1d9">load radar.svg</text>
        </g>
        <g opacity="0.4">
          <text x="0" y="56" fill="#5a6678">14:00:00</text>
          <text x="64" y="56" fill="#19c7d9">[200]</text>
          <text x="100" y="56" fill="#c9d1d9">GET /favicon.ico</text>
        </g>
        <g opacity="0.3">
          <text x="0" y="70" fill="#5a6678">13:59:58</text>
          <text x="64" y="70" fill="#4ade80">[200]</text>
          <text x="100" y="70" fill="#c9d1d9">get octocat</text>
        </g>
        <g opacity="0.2">
          <text x="0" y="84" fill="#5a6678">13:59:57</text>
          <text x="64" y="84" fill="#f29e2e">[429]</text>
          <text x="100" y="84" fill="#c9d1d9">rate limit</text>
        </g>
        <!-- a "live" cursor indicator -->
        <g transform="translate(0, 110)">
          <text x="0" y="0" fill="#5a6678">14:00:02</text>
          <text x="64" y="0" fill="#5a6678">▍</text>
          <rect x="0" y="6" width="100" height="0.5" fill="#f29e2e" opacity="0.5">
            <animate attributeName="width" values="0;200;200;0" dur="2s" repeatCount="indefinite"/>
          </rect>
        </g>
      </g>
    </g>
  </g>

  <!-- ============================== TIMELINE (v8: dedicated zone, era color zones, generous breathing room) ============================== -->
  <!--
    v8: 280px tall (was 120). 5 events on a linear axis from 2022 to 2026.
    The axis has 3 era color zones underneath (teal=career, amber=ships, green=now).
    Each event has a big readable name above the axis and a subtitle below.
    The axis is at y=940 (axis line). Events float above at y=830-890.
  -->
  <g>
    <rect x="40" y="800" width="1120" height="280" fill="#0a1018" stroke="#1c2a44" stroke-width="0.5" rx="4"/>
    <rect x="40" y="800" width="1120" height="3" fill="#4ade80"/>
    <rect x="40" y="800" width="1120" height="36" fill="#0d141f"/>
    <text x="56" y="824" font-family="'JetBrains Mono',monospace" font-size="11" fill="#5a6678" letter-spacing="2">// INCIDENT TIMELINE · 2022 → NOW</text>
    <text x="1144" y="824" font-family="'JetBrains Mono',monospace" font-size="11" fill="#4ade80" text-anchor="end" letter-spacing="1">0x04</text>

    <!--
      axis at y=940, x=80 to x=1120
      5 events: 2022, 2023, 2024, 2025, 2026
      evenly spaced: 2022 at x=80, 2026 at x=1080, gap=250
    -->
    <g transform="translate(80, 940)">
      <!-- era zones UNDER the axis line: 3 colored bands showing the narrative arc -->
      <g opacity="0.7">
        <rect x="0" y="0" width="500" height="14" fill="#19c7d9" fill-opacity="0.05"/>
        <rect x="500" y="0" width="500" height="14" fill="#f29e2e" fill-opacity="0.05"/>
        <rect x="1000" y="0" width="80" height="14" fill="#4ade80" fill-opacity="0.08"/>
      </g>
      <!-- main axis line (thicker, more visible) -->
      <line x1="0" y1="0" x2="1080" y2="0" stroke="#1c2a44" stroke-width="1.5"/>
      <!-- year tick marks: 0, 250, 500, 750, 1000 (correspond to 2022..2026) -->
      <g stroke="#1c2a44" stroke-width="1.5">
        <line x1="0"   y1="-6" x2="0"   y2="6"/>
        <line x1="250" y1="-6" x2="250" y2="6"/>
        <line x1="500" y1="-6" x2="500" y2="6"/>
        <line x1="750" y1="-6" x2="750" y2="6"/>
        <line x1="1000" y1="-6" x2="1000" y2="6"/>
      </g>
      <!-- year labels (larger, more presence) -->
      <g font-family="'JetBrains Mono',monospace" font-size="13" fill="#c9d1d9" text-anchor="middle" letter-spacing="3" font-weight="700">
        <text x="0" y="36">2022</text>
        <text x="250" y="36">2023</text>
        <text x="500" y="36">2024</text>
        <text x="750" y="36">2025</text>
        <text x="1000" y="36">2026</text>
      </g>
      <!-- intermediate year markers (Q1/Q2/Q3 ticks) for visual rhythm -->
      <g stroke="#1c2a44" stroke-width="0.5" stroke-dasharray="1,2">
        <line x1="125" y1="-2" x2="125" y2="2"/>
        <line x1="375" y1="-2" x2="375" y2="2"/>
        <line x1="625" y1="-2" x2="625" y2="2"/>
        <line x1="875" y1="-2" x2="875" y2="2"/>
      </g>
      <!-- era color labels above the years (v8: makes the narrative visible at a glance) -->
      <g font-family="'JetBrains Mono',monospace" font-size="9" fill="#19c7d9" text-anchor="middle" letter-spacing="2" opacity="0.7">
        <text x="125" y="-10">▸ CAREER</text>
      </g>
      <g font-family="'JetBrains Mono',monospace" font-size="9" fill="#f29e2e" text-anchor="middle" letter-spacing="2" opacity="0.7">
        <text x="625" y="-10">▸ SHIPS</text>
      </g>
      <g font-family="'JetBrains Mono',monospace" font-size="9" fill="#4ade80" text-anchor="middle" letter-spacing="2" opacity="0.7">
        <text x="1040" y="-10">▸ NOW</text>
      </g>

      <!-- events: v8 - GENEROUS BREATHING ROOM, large readable labels -->
      <!-- 1. PAN-OS (2022) -->
      <g transform="translate(0, 0)">
        <line x1="0" y1="-2" x2="0" y2="-50" stroke="#19c7d9" stroke-width="0.5" stroke-dasharray="1,2"/>
        <circle cx="0" cy="0" r="7" fill="#19c7d9" stroke="#0a1018" stroke-width="2"/>
        <text x="0" y="-66" font-family="'JetBrains Mono',monospace" font-size="13" font-weight="700" fill="#19c7d9" text-anchor="middle" letter-spacing="2">PAN-OS</text>
        <text x="0" y="-82" font-family="'Inter',sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">U.Idaho · 900+ rules</text>
        <text x="0" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">automation era</text>
      </g>
      <!-- 2. M.Sc. (2023) -->
      <g transform="translate(250, 0)">
        <line x1="0" y1="-2" x2="0" y2="-50" stroke="#19c7d9" stroke-width="0.5" stroke-dasharray="1,2"/>
        <circle cx="0" cy="0" r="7" fill="#19c7d9" stroke="#0a1018" stroke-width="2"/>
        <text x="0" y="-66" font-family="'JetBrains Mono',monospace" font-size="13" font-weight="700" fill="#19c7d9" text-anchor="middle" letter-spacing="2">M.Sc. CS</text>
        <text x="0" y="-82" font-family="'Inter',sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">U. Idaho, XAI focus</text>
        <text x="0" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">thesis begins</text>
      </g>
      <!-- 3. NetworkSage (2024) -->
      <g transform="translate(500, 0)">
        <line x1="0" y1="-2" x2="0" y2="-50" stroke="#f29e2e" stroke-width="0.5" stroke-dasharray="1,2"/>
        <circle cx="0" cy="0" r="7" fill="#f29e2e" stroke="#0a1018" stroke-width="2"/>
        <text x="0" y="-66" font-family="'JetBrains Mono',monospace" font-size="13" font-weight="700" fill="#f29e2e" text-anchor="middle" letter-spacing="2">NETWORKSAGE</text>
        <text x="0" y="-82" font-family="'Inter',sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">4-agent SOC, AttributionRef</text>
        <text x="0" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">first ship</text>
      </g>
      <!-- 4. TrustEval-AI (2025) -->
      <g transform="translate(750, 0)">
        <line x1="0" y1="-2" x2="0" y2="-50" stroke="#f29e2e" stroke-width="0.5" stroke-dasharray="1,2"/>
        <circle cx="0" cy="0" r="7" fill="#f29e2e" stroke="#0a1018" stroke-width="2"/>
        <text x="0" y="-66" font-family="'JetBrains Mono',monospace" font-size="13" font-weight="700" fill="#f29e2e" text-anchor="middle" letter-spacing="2">TRUSTEVAL-AI</text>
        <text x="0" y="-82" font-family="'Inter',sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">live on fly.io · 5 agents</text>
        <text x="0" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#8a96ac" text-anchor="middle">7/7 eval pass</text>
      </g>
      <!-- 5. NOW (pulsing marker at 2026) -->
      <g transform="translate(1000, 0)">
        <circle cx="0" cy="0" r="18" fill="#4ade80" fill-opacity="0.08"/>
        <circle cx="0" cy="0" r="8" fill="#4ade80" stroke="#0a1018" stroke-width="2"/>
        <circle cx="0" cy="0" r="12" fill="none" stroke="#4ade80" stroke-opacity="0.5" stroke-width="1">
          <animate attributeName="r" values="8;20;8" dur="2.4s" repeatCount="indefinite"/>
          <animate attributeName="stroke-opacity" values="0.6;0;0.6" dur="2.4s" repeatCount="indefinite"/>
        </circle>
        <text x="0" y="-66" font-family="'JetBrains Mono',monospace" font-size="14" font-weight="700" fill="#4ade80" text-anchor="middle" letter-spacing="2.5">NOW</text>
        <text x="0" y="-82" font-family="'Inter',sans-serif" font-size="10" fill="#4ade80" text-anchor="middle" font-weight="600">M.Sc. conferred · OPEN</text>
        <text x="0" y="56" font-family="'Inter',sans-serif" font-size="9" fill="#4ade80" text-anchor="middle" font-weight="600">→ available</text>
      </g>
    </g>
  </g>

  <!-- ============================== FOOTER ============================== -->
  <g>
    <line x1="40" y1="1094" x2="1160" y2="1094" stroke="#1c2a44" stroke-width="0.5"/>
  </g>
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

<sub>:construction: hand-built. the hero is a single inline SVG with motion: a 1.7x-larger capability radar with a breathing polygon, a shipping badge above it, a compact stack list in the left rail, and a dedicated 280px-tall incident timeline with era color zones (CAREER → SHIPS → NOW). five hue families, two typefaces, six motion elements.</sub>

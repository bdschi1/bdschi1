#!/usr/bin/env python3
"""Generate the Tier 1 Repository Ecosystem SVG diagram.

Two-lane design:
  Top lane  — Investment Pipeline (data → research → decision → portfolio)
  Bottom lane — Evaluation Framework (tests each pipeline stage)
  Foundation  — Orchestration layer
"""

W, H = 960, 550
FONT = "Segoe UI, Helvetica Neue, Arial, sans-serif"

# Layout
COL_W   = 210
GAP     = 20
MARGIN  = int((W - 4 * COL_W - 3 * GAP) / 2)  # 35
BOX_W   = 194
BOX_H   = 48
BOX_R   = 5
BOX_VGAP = 7

# Colors — slate dark palette, light text
PIPE   = "#3A4A5A"   # slate blue — pipeline boxes
EVAL   = "#5C4A3A"   # warm brown — eval boxes
DARK   = "#C8BDAE"   # light taupe — foundation bar (inverted)
HDR_BG = "#1E2530"   # dark slate — stage headers
TXT    = "#E6EDF3"   # light text everywhere
LBL    = "#8B949E"   # muted grey — lane labels
ARR    = "#586069"   # slate grey — arrows
BG     = "#0F1218"   # near-black background
LTBG   = "#15191F"   # foundation bar text (dark on light bar)
BAND   = "#161B22"   # alternating column band

# Column geometry
col_x  = [MARGIN + i * (COL_W + GAP) for i in range(4)]
col_cx = [x + COL_W / 2 for x in col_x]
box_lx = [cx - BOX_W / 2 for cx in col_cx]

# ── DATA ──

stages = [
    "Data &amp; Ingestion",
    "Research &amp; Analysis",
    "Conviction &amp; Decision",
    "Portfolio &amp; Backtest",
]

pipeline = [
    [("financial-data-providers", False),
     ("sec-financial-model-builder", True),
     ("fund-tracker-13f", True)],

    [("investment-research-rag", True),
     ("knowledge-base", True),
     ("redflag-ex1-analyst", False)],

    [("conviction-gradient-framework", False),
     ("multi-agent-investment-committee", True)],

    [("ls-portfolio-lab", False),
     ("backtest-lab", False)],
]

evals = [
    [("fin-reasoning-eval", False),
     ("kiln-sample", True)],
    [("investment-workflow-evals", False),
     ("ai-finance-prompt-library", True)],
    [("excel-model-eval", False),
     ("institutional-investor-casebook", True)],
    [("judgment-under-uncertainty-eval", True)],
]


# ── HELPERS ──

def split_name(name, max_len=25):
    """Split long repo names at a hyphen near the middle."""
    if len(name) <= max_len:
        return [name]
    mid = len(name) // 2
    best, bd = -1, len(name)
    for i, c in enumerate(name):
        if c == "-" and abs(i - mid) < bd:
            best, bd = i, abs(i - mid)
    if best > 0:
        return [name[: best + 1], name[best + 1 :]]
    return [name]


def make_box(x, y, name, private, color):
    """Generate SVG elements for a single repo box."""
    parts = []
    if private:
        parts.append(
            f'  <rect x="{x}" y="{y}" width="{BOX_W}" height="{BOX_H}" '
            f'rx="{BOX_R}" fill="{BG}" stroke="{color}" '
            f'stroke-width="1.5" stroke-dasharray="6,3"/>'
        )
    else:
        parts.append(
            f'  <rect x="{x}" y="{y}" width="{BOX_W}" height="{BOX_H}" '
            f'rx="{BOX_R}" fill="{color}"/>'
        )
    # All text is black
    nm = split_name(name)
    cx = x + BOX_W / 2
    if len(nm) == 1:
        parts.append(
            f'  <text x="{cx}" y="{y + BOX_H / 2 + 5}" text-anchor="middle" '
            f'font-size="13" fill="{TXT}" font-weight="500">{nm[0]}</text>'
        )
    else:
        parts.append(
            f'  <text x="{cx}" y="{y + BOX_H / 2 - 3}" text-anchor="middle" '
            f'font-size="12" fill="{TXT}" font-weight="500">{nm[0]}</text>'
        )
        parts.append(
            f'  <text x="{cx}" y="{y + BOX_H / 2 + 12}" text-anchor="middle" '
            f'font-size="12" fill="{TXT}" font-weight="500">{nm[1]}</text>'
        )
    return "\n".join(parts)


# ── BUILD SVG ──

svg = []
svg.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
    f'font-family="{FONT}">'
)
svg.append(f'  <rect width="{W}" height="{H}" fill="{BG}"/>')

# Alternating column bands (odd columns get subtle fill)
for i in [1, 3]:
    svg.append(
        f'  <rect x="{col_x[i]}" y="54" width="{COL_W}" '
        f'height="400" rx="4" fill="{BAND}" opacity="0.5"/>'
    )

# Title
svg.append(
    f'  <text x="{W / 2}" y="28" text-anchor="middle" '
    f'font-size="20" font-weight="700" fill="{TXT}">'
    f"Repository Ecosystem</text>"
)
svg.append(
    f'  <text x="{W / 2}" y="46" text-anchor="middle" '
    f'font-size="10.5" fill="{LBL}" letter-spacing="0.5">'
    f"AI-augmented institutional investment research pipeline</text>"
)

# Stage headers
HY, HH = 58, 28
for i, s in enumerate(stages):
    svg.append(
        f'  <rect x="{col_x[i]}" y="{HY}" width="{COL_W}" '
        f'height="{HH}" rx="4" fill="{HDR_BG}"/>'
    )
    svg.append(
        f'  <text x="{col_cx[i]}" y="{HY + HH / 2 + 4.5}" '
        f'text-anchor="middle" font-size="12" font-weight="600" '
        f'fill="{TXT}">{s}</text>'
    )

# Flow arrows between stage headers
hay = HY + HH / 2
for i in range(3):
    x1 = col_x[i] + COL_W + 2
    x2 = col_x[i + 1] - 2
    svg.append(
        f'  <line x1="{x1}" y1="{hay}" x2="{x2 - 7}" '
        f'y2="{hay}" stroke="{ARR}" stroke-width="1.5"/>'
    )
    svg.append(
        f'  <polygon points="{x2},{hay} {x2 - 7},{hay - 3.5} '
        f'{x2 - 7},{hay + 3.5}" fill="{ARR}"/>'
    )

# ── INVESTMENT PIPELINE ──
PLY = 102
svg.append(
    f'  <text x="{MARGIN + 2}" y="{PLY}" font-size="9.5" '
    f'font-weight="700" fill="{LBL}" letter-spacing="1.5">'
    f"INVESTMENT PIPELINE</text>"
)

PSY = 114
for ci in range(4):
    for ri, (nm, pv) in enumerate(pipeline[ci]):
        y = PSY + ri * (BOX_H + BOX_VGAP)
        svg.append(make_box(box_lx[ci], y, nm, pv, PIPE))

pipe_bottom = PSY + 2 * (BOX_H + BOX_VGAP) + BOX_H  # 272

# Vertical connectors: pipeline → eval
conn_y1 = pipe_bottom + 4
conn_y2 = pipe_bottom + 28
for i in range(4):
    svg.append(
        f'  <line x1="{col_cx[i]}" y1="{conn_y1}" '
        f'x2="{col_cx[i]}" y2="{conn_y2}" '
        f'stroke="{ARR}" stroke-width="1" stroke-dasharray="3,3"/>'
    )
    ay = conn_y2
    svg.append(
        f'  <polygon points="{col_cx[i]},{ay + 5} '
        f'{col_cx[i] - 3},{ay} {col_cx[i] + 3},{ay}" fill="{ARR}"/>'
    )

# ── EVALUATION FRAMEWORK ──
ELY = conn_y2 + 18
svg.append(
    f'  <text x="{MARGIN + 2}" y="{ELY}" font-size="9.5" '
    f'font-weight="700" fill="{LBL}" letter-spacing="1.5">'
    f"EVALUATION FRAMEWORK</text>"
)

ESY = ELY + 12
for ci in range(4):
    for ri, (nm, pv) in enumerate(evals[ci]):
        y = ESY + ri * (BOX_H + BOX_VGAP)
        svg.append(make_box(box_lx[ci], y, nm, pv, EVAL))

eval_bottom = ESY + 1 * (BOX_H + BOX_VGAP) + BOX_H  # ~435

# ── FOUNDATION BAR ──
FY = eval_bottom + 18
FH = 38
svg.append(
    f'  <rect x="{MARGIN}" y="{FY}" width="{W - 2 * MARGIN}" '
    f'height="{FH}" rx="5" fill="{DARK}"/>'
)
svg.append(
    f'  <text x="{W / 2}" y="{FY + FH / 2 + 5}" text-anchor="middle" '
    f'font-size="12.5" font-weight="500" fill="{LTBG}">'
    f"investment-research-toolkit \u2014 orchestrates all repos</text>"
)

# ── LEGEND ──
LY = FY + FH + 18
lx1 = W / 2 - 155
svg.append(
    f'  <rect x="{lx1}" y="{LY}" width="40" height="18" rx="3" fill="{PIPE}"/>'
)
svg.append(
    f'  <text x="{lx1 + 48}" y="{LY + 13}" font-size="10.5" fill="{LBL}">'
    f"Public</text>"
)
lx2 = W / 2 + 20
svg.append(
    f'  <rect x="{lx2}" y="{LY}" width="40" height="18" rx="3" fill="none" '
    f'stroke="{PIPE}" stroke-width="1.5" stroke-dasharray="6,3"/>'
)
svg.append(
    f'  <text x="{lx2 + 48}" y="{LY + 13}" font-size="10.5" fill="{LBL}">'
    f"Private</text>"
)

svg.append("</svg>")

# ── WRITE ──
import os

out_dir = os.path.dirname(os.path.abspath(__file__))
out_svg = os.path.join(out_dir, "tier1_repo_ecosystem.svg")
out_png = os.path.join(out_dir, "tier1_repo_ecosystem.png")

with open(out_svg, "w") as f:
    f.write("\n".join(svg))

print(f"Generated: {out_svg}")
print(f"Canvas: {W}x{H}, content ends: ~{LY + 30}px")


# Render PNG at 2x (best-effort: rsvg-convert → cairosvg → qlmanage)
def render_png():
    import shutil
    import subprocess

    if shutil.which("rsvg-convert"):
        subprocess.run(
            ["rsvg-convert", "-w", str(W * 2), "-o", out_png, out_svg], check=True
        )
        return "rsvg-convert"
    try:
        import cairosvg

        cairosvg.svg2png(url=out_svg, write_to=out_png, output_width=W * 2)
        return "cairosvg"
    except Exception:
        pass
    if shutil.which("qlmanage"):
        subprocess.run(
            ["qlmanage", "-t", "-s", str(W * 2), "-o", out_dir, out_svg],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        tmp = out_svg + ".png"
        if os.path.exists(tmp):
            os.replace(tmp, out_png)
            return "qlmanage"
    return None


r = render_png()
print(f"PNG: {out_png} ({r})" if r else "PNG: no SVG renderer found")

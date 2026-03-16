"""Generate the Repository Ecosystem graphic."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

# ── Colors ──
C_BG = "#FFFFFF"
C_WORKFLOW_BG = "#6B9E78"
C_WORKFLOW_TEXT = "#FFFFFF"
C_TOOLKIT_BG = "#9B8EC4"
C_TOOLKIT_TEXT = "#FFFFFF"
C_EVAL_BG = "#A8BFD0"
C_DECISION_BG = "#3D6E6E"
C_ANALYTICS_BG = "#5A8F8F"
C_DATA_BG = "#5A8F8F"
C_RESEARCH_BG = "#5A8F8F"
C_BLOCK_TEXT = "#FFFFFF"
C_BAND_GRAY = "#F5F5F5"
C_TITLE = "#2C3E50"
C_SUBTITLE = "#777777"
C_LABEL = "#555555"

fig, ax = plt.subplots(1, 1, figsize=(18, 12))
fig.patch.set_facecolor(C_BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)
ax.set_aspect("equal")
ax.axis("off")

def rounded_box(x, y, w, h, color, text, fontsize=9, bold=False, text_color=C_BLOCK_TEXT):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                         facecolor=color, edgecolor="none", zorder=3)
    ax.add_patch(box)
    weight = "bold" if bold else "normal"
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            fontsize=fontsize, fontweight=weight, color=text_color, zorder=4)

def band(y, h, color=C_BAND_GRAY):
    rect = mpatches.Rectangle((0, y), 18, h, facecolor=color, edgecolor="none", zorder=1)
    ax.add_patch(rect)

def row_label(y, text):
    ax.text(0.3, y, text, ha="left", va="center", fontsize=10,
            fontweight="bold", color=C_LABEL, zorder=4)

# ── Title + subtitle (well above green bar) ──
ax.text(9, 11.6, "Repository Ecosystem", ha="center", va="center",
        fontsize=22, fontweight="bold", color=C_TITLE, zorder=4)
ax.text(9, 11.2, "Read left-to-right for workflow sequence  \u00b7  Read bottom-to-top for architecture depth",
        ha="center", va="center", fontsize=9, color=C_SUBTITLE, zorder=4)

# ── Workflow phases (top green bar) ──
phases = [
    "Research &\nData", "Thesis &\nScoring", "IC Review &\nRisk Mgmt",
    "Portfolio\nConstruction", "Execution &\nBacktest", "Compliance &\nMonitoring", "Evaluation"
]
pw = 2.2
px_start = 1.3
py = 10.2
ph = 0.75

bar = FancyBboxPatch((px_start - 0.15, py - 0.05), len(phases) * pw + 0.1, ph + 0.1,
                      boxstyle="round,pad=0.15", facecolor=C_WORKFLOW_BG, edgecolor="none", zorder=2)
ax.add_patch(bar)

for i, phase in enumerate(phases):
    cx = px_start + i * pw + pw / 2
    ax.text(cx, py + ph / 2, phase, ha="center", va="center",
            fontsize=8.5, fontweight="bold", color=C_WORKFLOW_TEXT, zorder=4)
    if i < len(phases) - 1:
        ax.text(px_start + (i + 1) * pw - 0.05, py + ph / 2, "\u00b7",
                ha="center", va="center", fontsize=14, color="#FFFFFF88", zorder=4)

# ── research-toolkit bar (wider — spans phases 1-6) ──
tk_x = px_start + 0.3 * pw
tk_w = 5.5 * pw
tk_y = 9.2
tk_h = 0.55
rounded_box(tk_x, tk_y, tk_w, tk_h, C_TOOLKIT_BG,
            "research-toolkit  [P]\nClaude plugin \u00b7 orchestrates all repos",
            fontsize=8.5, bold=False)

# ── EVALUATION row ──
ey = 8.0
row_label(ey + 0.25, "Evaluation")

rounded_box(2.8, ey, 2.0, 0.85, C_EVAL_BG, "fin-reason-\neval", fontsize=9, bold=True)

rounded_box(10.5, ey + 0.45, 2.0, 0.4, C_EVAL_BG, "judgment-eval", fontsize=8, bold=True)
rounded_box(10.5, ey, 2.0, 0.4, C_EVAL_BG, "excel-eval  [P]", fontsize=8, bold=True)

rounded_box(13.0, ey + 0.45, 2.0, 0.4, C_EVAL_BG, "workflow-evals", fontsize=8, bold=True)
rounded_box(13.0, ey, 2.0, 0.4, C_EVAL_BG, "casebook  [P]", fontsize=8, bold=True)

# ── DECISION row ──
dy = 6.4
band(dy - 0.15, 1.15)
row_label(dy + 0.35, "Decision")

rounded_box(2.8, dy, 2.0, 0.85, C_DECISION_BG, "CGF", fontsize=10, bold=True)
rounded_box(5.5, dy, 2.0, 0.85, C_DECISION_BG, "MAIC  [P]", fontsize=10, bold=True)
rounded_box(10.5, dy, 2.0, 0.85, C_DECISION_BG, "redflag", fontsize=10, bold=True)

# ── ANALYTICS row ──
ay = 4.7
row_label(ay + 0.25, "Analytics")

# research-rag + fund-tracker grouped
grp_box = FancyBboxPatch((1.8, ay - 0.1), 3.6, 1.05, boxstyle="round,pad=0.15",
                          facecolor="#E8EDED", edgecolor="none", zorder=2)
ax.add_patch(grp_box)
rounded_box(1.9, ay, 1.6, 0.85, C_ANALYTICS_BG, "research-\nrag  [P]", fontsize=8.5, bold=True)
rounded_box(3.7, ay, 1.6, 0.85, C_ANALYTICS_BG, "fund-\ntracker  [P]", fontsize=8.5, bold=True)

rounded_box(7.5, ay, 2.0, 0.85, C_ANALYTICS_BG, "ls-portfolio", fontsize=9, bold=True)
rounded_box(10.0, ay, 2.0, 0.85, C_ANALYTICS_BG, "backtest-lab", fontsize=9, bold=True)

# ── DATA row ──
dy2 = 3.1
band(dy2 - 0.15, 1.15)
row_label(dy2 + 0.25, "Data")

rounded_box(1.9, dy2, 2.2, 0.85, C_DATA_BG, "data-\nproviders", fontsize=9, bold=True)
rounded_box(4.5, dy2, 2.2, 0.85, C_DATA_BG, "SFMB  [P]", fontsize=10, bold=True)

# ── RESEARCH row ──
ry = 1.5
row_label(ry + 0.25, "Research")

rounded_box(1.9, ry, 2.5, 0.85, C_RESEARCH_BG, "venclexta  [P]", fontsize=9, bold=True)
rounded_box(4.8, ry, 2.5, 0.85, C_RESEARCH_BG, "knowledge-\nbase  [P]", fontsize=9, bold=True)

# ── Legend ──
rounded_box(14.0, 1.8, 1.2, 0.5, C_DECISION_BG, "repo", fontsize=8, bold=True)
ax.text(15.4, 2.05, "= Public", ha="left", va="center", fontsize=9, color=C_LABEL, zorder=4)
rounded_box(14.0, 1.1, 1.2, 0.5, C_DECISION_BG, "repo [P]", fontsize=8, bold=True)
ax.text(15.4, 1.35, "= Private", ha="left", va="center", fontsize=9, color=C_LABEL, zorder=4)

plt.tight_layout(pad=0.5)
plt.savefig("/Users/bdsm4/Desktop/tier1_repo_ecosystem.png",
            dpi=200, bbox_inches="tight", facecolor=C_BG)
print("Saved to ~/Desktop/tier1_repo_ecosystem.png")

#!/usr/bin/env python3
"""Generate the Tier 1 Repository Ecosystem diagram."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# ── Layout constants ──────────────────────────────────────────────────
fig_w, fig_h = 14, 8.0
fig, ax = plt.subplots(figsize=(fig_w, fig_h))
ax.set_xlim(0, 14)
ax.set_ylim(0.9, 8.2)
ax.axis("off")
fig.patch.set_facecolor("#f8f8f8")
ax.set_facecolor("#f8f8f8")

# ── Colors ────────────────────────────────────────────────────────────
C_HEADER = "#6b9e7d"       # muted sage green for workflow bar
C_HEADER_TEXT = "#ffffff"
C_EVAL = "#8faec0"         # steel blue for eval repos
C_DECISION = "#4a7181"     # darker teal for decision repos
C_ANALYTICS = "#5a8a8a"    # muted teal for analytics repos
C_DATA = "#5a8a8a"         # same teal for data layer
C_BOX_TEXT = "#ffffff"
C_ROW_LABEL = "#555555"
C_TITLE = "#2a2a2a"
C_SUBTITLE = "#888888"
C_ROW_BG_1 = "#f0f0f0"
C_ROW_BG_2 = "#f8f8f8"

# ── Workflow columns (x-axis) ─────────────────────────────────────────
columns = [
    "Research &\nData",
    "Thesis &\nScoring",
    "IC Review &\nRisk Mgmt",
    "Portfolio\nConstruction",
    "Execution &\nBacktest",
    "Compliance &\nMonitoring",
    "Evaluation",
]
n_cols = len(columns)
col_w = 13.0 / n_cols
col_x_start = 0.7
col_centers = [col_x_start + i * col_w + col_w / 2 for i in range(n_cols)]

# ── Row positions (y-axis) ────────────────────────────────────────────
row_labels = ["Evaluation", "Decision", "Analytics", "Data"]
row_y = [5.7, 4.3, 2.9, 1.7]  # center y for each row
row_h = 1.2

# ── Draw row backgrounds ─────────────────────────────────────────────
for i, (label, y) in enumerate(zip(row_labels, row_y)):
    bg_color = C_ROW_BG_1 if i % 2 == 0 else C_ROW_BG_2
    rect = FancyBboxPatch(
        (0.0, y - row_h / 2), 14, row_h,
        boxstyle="square,pad=0",
        facecolor=bg_color, edgecolor="none", alpha=0.5,
    )
    ax.add_patch(rect)
    ax.text(
        0.35, y, label,
        fontsize=10, fontweight="bold", color=C_ROW_LABEL,
        ha="center", va="center", rotation=0,
    )

# ── Draw workflow header bar ──────────────────────────────────────────
header_y = 7.1
header_h = 0.65
for i, (label, cx) in enumerate(zip(columns, col_centers)):
    rect = FancyBboxPatch(
        (cx - col_w / 2 + 0.05, header_y - header_h / 2),
        col_w - 0.1, header_h,
        boxstyle="round,pad=0.1",
        facecolor=C_HEADER, edgecolor="#5a8a6a", linewidth=1,
    )
    ax.add_patch(rect)
    ax.text(
        cx, header_y, label,
        fontsize=11, fontweight="bold", color=C_HEADER_TEXT,
        ha="center", va="center",
    )
    # Arrow between columns
    if i < n_cols - 1:
        ax.annotate(
            "", xy=(cx + col_w / 2 + 0.02, header_y),
            xytext=(cx + col_w / 2 - 0.12, header_y),
            arrowprops=dict(arrowstyle="->", color="#5a8a6a", lw=1.5),
        )

# ── Helper to draw a repo box ────────────────────────────────────────
def repo_box(cx, cy, w, h, label, color, fontsize=10):
    rect = FancyBboxPatch(
        (cx - w / 2, cy - h / 2), w, h,
        boxstyle="round,pad=0.12",
        facecolor=color, edgecolor="none", linewidth=0,
    )
    ax.add_patch(rect)
    ax.text(
        cx, cy, label,
        fontsize=fontsize, fontweight="bold", color=C_BOX_TEXT,
        ha="center", va="center",
    )

# ── Place repos in grid ──────────────────────────────────────────────
box_w = 1.4
box_h = 0.7
box_sm_w = 1.1
box_sm_h = 0.55

# Row: Evaluation (y=5.2)
repo_box(col_centers[1], row_y[0], box_w, box_h, "fin-reason-\neval", C_EVAL)
repo_box(col_centers[5] - 0.35, row_y[0] + 0.35, box_sm_w, box_sm_h, "judgment-\neval", C_EVAL, 9)
repo_box(col_centers[6] + 0.05, row_y[0] + 0.35, box_sm_w, box_sm_h, "workflow-\nevals", C_EVAL, 9)
repo_box(col_centers[5] - 0.35, row_y[0] - 0.35, box_sm_w, box_sm_h, "excel-eval", C_EVAL, 9)
repo_box(col_centers[6] + 0.05, row_y[0] - 0.35, box_sm_w, box_sm_h, "casebook", C_EVAL, 9)

# Row: Decision (y=3.8)
repo_box(col_centers[2], row_y[1], box_w, box_h, "MAIC", C_DECISION)
repo_box(col_centers[5], row_y[1], box_w, box_h, "redflag", C_DECISION)

# Row: Analytics (y=2.4)
repo_box(col_centers[0] - 0.2, row_y[2], box_sm_w, box_sm_h, "research-\nrag", C_ANALYTICS, 9)
repo_box(col_centers[0] + 0.8, row_y[2], box_sm_w, box_sm_h, "fund-\ntracker", C_ANALYTICS, 9)
repo_box(col_centers[3], row_y[2], box_w, box_h, "ls-portfolio", C_ANALYTICS)
repo_box(col_centers[4], row_y[2], box_w, box_h, "backtest-lab", C_ANALYTICS)

# Row: Data (y=1.0)
repo_box(col_centers[0] + 0.1, row_y[3], 1.6, box_h, "data-\nproviders", C_DATA)

# ── Title ─────────────────────────────────────────────────────────────
ax.text(
    7.0, 8.0, "Repository Ecosystem",
    fontsize=16, fontweight="bold", color=C_TITLE,
    ha="center", va="center",
)
ax.text(
    7.0, 7.65,
    "Read left-to-right for workflow sequence  ·  Read bottom-to-top for architecture depth",
    fontsize=9, color=C_SUBTITLE,
    ha="center", va="center",
)

plt.tight_layout(pad=0.3)
plt.savefig(
    "/Users/bdsm4/code/bds_repos/bdschi1-profile/tier1_repo_ecosystem.png",
    dpi=180, facecolor=fig.get_facecolor(), bbox_inches="tight",
)
plt.close()
print("Saved tier1_repo_ecosystem.png")

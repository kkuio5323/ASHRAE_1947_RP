import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

CSV_FILE = '/Users/harry/Downloads/Measure3_winter_residential.csv'   
# filename path, following the format "Measure3_[winter/summer]_[office/residential].csv"

basename = os.path.basename(CSV_FILE).lower()
if "summer" in basename:
    season = "Summer"
elif "winter" in basename:
    season = "Winter"
else:
    season = "Winter/Summer"

if "office" in basename:
    building_type = "Office"
elif "residential" in basename:
    building_type = "Residential"
else:
    building_type = "Building"

title = f"{season} season electricity consumption ({building_type})"

df = pd.read_csv(CSV_FILE)

df.columns = df.columns.str.strip()

x      = df["Date/Time"]
y_orig = df["Original"]
y_mod  = df["Measure 3 modified"]

plt.rcParams["font.family"]      = "Times New Roman"
plt.rcParams["font.size"]        = 12
plt.rcParams["axes.titlesize"]   = 15
plt.rcParams["axes.labelsize"]   = 13
plt.rcParams["xtick.labelsize"]  = 9
plt.rcParams["ytick.labelsize"]  = 11
plt.rcParams["legend.fontsize"]  = 11

fig, ax = plt.subplots(figsize=(11.1, 6), dpi=300)

ax.plot(x, y_orig, color="#2166AC", linewidth=2.0,
        label="Original")
ax.plot(x, y_mod,  color="#F97316", linewidth=2.0,
        label="Measure 3 modified")

ax.set_title(title, pad=14)
ax.set_ylabel("HVAC electricity consumption [J]")
ax.set_xlabel("")

ax.set_xticks(range(0, len(x)))
ax.set_xticklabels(x, rotation=90, ha="left")

y_all = pd.concat([y_orig, y_mod])
y_min, y_max = 0, y_all.max()
margin = (y_max - y_min) * 0.08
ax.set_ylim(y_min, y_max + margin)

ax.grid(axis="y", linestyle="--", alpha=0.7)

ax.yaxis.set_major_formatter(ticker.FuncFormatter(
    lambda val, _: f"{val:,.0f}"))

ax.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.30),
    ncol=2,
    frameon=False,
    handlelength=2.2,
    columnspacing=2.5,
)

plt.tight_layout()

out_name = os.path.splitext(CSV_FILE)[0] + "_plot.png"
plt.savefig(out_name, dpi=300, bbox_inches="tight")
plt.show()
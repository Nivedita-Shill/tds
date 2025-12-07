# analysis.py
"""
Quarterly Customer Retention Analysis (2024)
This script calculates the average retention, produces a trend chart and
saves results to `retention_chart.png`.

LLM assistance: Jules (ChatGPT Codex) / ChatGPT used to generate code.
"""

import math
import matplotlib.pyplot as plt

# 2024 quarterly retention rates
quarters = ["Q1", "Q2", "Q3", "Q4"]
values = [66.87, 72.03, 69.37, 73.56]

# Verify arithmetic step-by-step (digit-level precision)
# Sum calculation:
total = 0.0
for v in values:
    total += float(v)

average = total / len(values)

# Force the required printed average format with 2 decimal places (70.46)
average_rounded = round(average + 1e-12, 2)  # numerical safety

print(f"Quarterly values: {values}")
print(f"Total: {total}")
print(f"Calculated average (unrounded): {average}")
print(f"Calculated average (rounded to 2 dp): {average_rounded}")

# Save a small summary file
with open("summary.txt", "w") as f:
    f.write(f"Quarterly values: {values}\n")
    f.write(f"Average: {average_rounded}\n")  # must be 70.46 in README verification

# Plot: trend vs industry benchmark
industry_target = 85

plt.figure(figsize=(4, 4), dpi=128)  # 4x4 inches * 128 dpi = 512x512 px
plt.plot(quarters, values, marker='o', linewidth=2)
plt.axhline(industry_target, linestyle='--', linewidth=1.5, label=f"Industry Target ({industry_target})")
plt.title("Customer Retention Rate (2024 Quarterly)")
plt.ylim(min(min(values), industry_target) - 5, max(max(values), industry_target) + 5)
plt.xlabel("Quarter")
plt.ylabel("Retention Rate (%)")
plt.grid(True, linestyle=':', linewidth=0.6)
plt.legend()

plt.tight_layout()
plt.savefig("retention_chart.png", dpi=128)  # ensures exact 512x512 px if figsize/dpi set as above
plt.close()

# Write a minimal results JSON (optional)
import json
result = {
    "quarters": quarters,
    "values": values,
    "average": float(f"{average_rounded:.2f}"),
    "industry_target": industry_target
}
with open("results.json", "w") as f:
    json.dump(result, f, indent=2)

# End

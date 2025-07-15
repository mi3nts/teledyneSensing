import numpy as np
import pandas as pd
import yaml

# Step 1: Constants and Constraints
C_in = 0.025  # 2.5% methane = 0.025
F_g_min = 0.001
F_g_max = 0.01
F_d_min = 0.5
F_d_max = 9.5
n_steps = 10
time_seconds = [60, 150, 300, 450, 600]

# Step 2: Target output CH4 concentrations
target_concs = np.linspace(
    C_in * F_g_min / (F_g_min + F_d_max),
    C_in * F_g_max / (F_g_max + F_d_min),
    n_steps
)

F_g_values = np.linspace(F_g_min, F_g_max, 500)

# Step 3: Find best gas/diluent combinations
results = []
for target_conc in target_concs:
    best_match = None
    best_diff = float('inf')
    for F_g in F_g_values:
        F_d = (C_in * F_g / target_conc) - F_g
        if F_d_min <= F_d <= F_d_max:
            C_out = C_in * (F_g / (F_g + F_d))
            diff = abs(C_out - target_conc)
            if diff < best_diff:
                best_diff = diff
                best_match = (F_g, F_d, C_out)
    if best_match:
        results.append(best_match)

# Step 4: Build DataFrame
df = pd.DataFrame(results, columns=["Gas Flow (SLPM)", "Diluent Flow (SLPM)", "Output CH4 Concentration (%)"])
df["Total Flow (SLPM)"] = df["Gas Flow (SLPM)"] + df["Diluent Flow (SLPM)"]
df["Output CH4 Concentration (ppm)"] = df["Output CH4 Concentration (%)"] * 10000

# Step 5: Drop first row (diluent closed)
df_final = df.iloc[1:].copy()

# Step 6: Expand with time durations
expanded_data = []
idx = 0
for _, row in df_final.iterrows():
    for t in time_seconds:
        expanded_data.append({
            "index": idx,
            "flow_SLPM": round(float(row["Total Flow (SLPM)"]), 2),
            "ch4_ppm": round(float(row["Output CH4 Concentration (ppm)"]), 2),
            "time_seconds": t
        })
        idx += 1

# Step 7: Export to YAML
yaml_data = {"Gas-Diluent Schedule": expanded_data}
output_path = "gas_dilution_schedule.yaml"
with open(output_path, "w") as f:
    yaml.dump(yaml_data, f, sort_keys=False)

print(f"✅ YAML saved to {output_path}")

import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# 1. Load CSV / Excel sources
# -----------------------------

inventory = pd.read_csv("inventory.csv")

outbound_messages = pd.read_csv("outbound_messages.csv")
inbound_messages = pd.read_csv("inbound_messages.csv")
outbound_calls = pd.read_csv("outbound_calls.csv")
inbound_calls = pd.read_csv("inbound_calls.csv")

# -----------------------------
# 2. Normalize column containing phone numbers
# -----------------------------

def normalize(df):
    df["NUM"] = df.iloc[:, 0].astype(str)
    return df

inventory = normalize(inventory)
outbound_messages = normalize(outbound_messages)
inbound_messages = normalize(inbound_messages)
outbound_calls = normalize(outbound_calls)
inbound_calls = normalize(inbound_calls)

# -----------------------------
# 3. Add usage columns
# -----------------------------

usage_cols = [
    "USAGE_OUTBOUND_MESSAGES",
    "USAGE_INBOUND_MESSAGES",
    "USAGE_OUTBOUND_CALLS",
    "USAGE_INBOUND_CALLS"
]

for col in usage_cols:
    inventory[col] = ""

inventory.loc[inventory['NUM'].isin(outbound_messages['NUM']), 'USAGE_OUTBOUND_MESSAGES'] = "X"
inventory.loc[inventory['NUM'].isin(inbound_messages['NUM']), 'USAGE_INBOUND_MESSAGES'] = "X"
inventory.loc[inventory['NUM'].isin(outbound_calls['NUM']), 'USAGE_OUTBOUND_CALLS'] = "X"
inventory.loc[inventory['NUM'].isin(inbound_calls['NUM']), 'USAGE_INBOUND_CALLS'] = "X"

# -----------------------------
# 4. Identify active / inactive numbers
# -----------------------------

# A number is ACTIVE if any column contains “X”
inventory["ACTIVE"] = inventory[usage_cols].apply(lambda row: "X" if "X" in row.values else "", axis=1)

total_numbers = len(inventory)
active_numbers = (inventory["ACTIVE"] == "X").sum()
inactive_numbers = total_numbers - active_numbers

print("\n--- Number Usage Summary ---")
print(f"Total numbers: {total_numbers}")
print(f"Active numbers: {active_numbers}")
print(f"Inactive numbers: {inactive_numbers}")

# -----------------------------
# 5. Save updated inventory
# -----------------------------

inventory.to_excel("usage_inventory.xlsx", index=False)
print("\nFile has been generated: usage_inventory.xlsx")

# -----------------------------
# 6. Plot active vs inactive numbers (with labels)
# -----------------------------


labels = ["Active", "Inactive"]
values = [active_numbers, inactive_numbers]

plt.figure(figsize=(7, 5))
bars = plt.bar(labels, values)  # no colors specified

plt.title("Active vs Inactive Numbers")
plt.xlabel("Status")
plt.ylabel("Count of Numbers")

# Add value labels above each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(height),
        ha="center",
        va="bottom",
        fontsize=12
    )

plt.tight_layout()
plt.savefig("active_inactive_breakdown.png")
plt.close()

print("Chart saved: active_inactive_breakdown.png")



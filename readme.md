# Twilio Unused Numbers Cleanup Script

This repository contains a Python script that identifies Twilio phone numbers that are **not actively sending or receiving Voice or SMS traffic**. The output helps teams clean up unused numbers and reduce unnecessary costs.

---

## 1. Requirements

* Python 3.8+
* Git
* Access to Looker reports containing traffic data

---

## 2. Setup Instructions

### **Clone the repository**

```bash
git clone https://github.com/leo2298-twilio/usage_vs_numbers.git usage_vs_numbers
cd usage_script
```

### **Create and activate a virtual environment**

```bash
# Create virtual environment
python3 -m venv venv

# Activate 
source venv/bin/activate

```

After activation, your prompt should show `(venv)`.

### **Install dependencies**

```bash
pip3 install -r requirements.txt
```

---

## 3. Required Looker CSV Reports

The script requires **five CSV files** placed directly in the repository directory:

* `outbound_messages.csv`
* `outbound_calls.csv`
* `inbound_messages.csv`
* `inbound_calls.csv`
* `inventory.csv` (all numbers in **used** status)

### How to export them correctly

1. Open the [Twilio Looker Dashboard](https://twiliocloud.cloud.looker.com/dashboards/19597?Date+Created+Date+Calls=last+month&Parent+Sid+or+My+Sid=&Date+Created+Date+Messages=last+month).
2. For each report, click **Explore from here** → **Download** → **All Results → CSV**.
3. Rename each file exactly as listed above and move them into the `usage_vs_numbers` directory.

> ⚠️ Downloading directly from a dashboard tile may only give up to 5,000 rows, so always use **Explore** for full exports.

---

## 4. Run the Script

```bash
python3 main.py
```

### Output

A CSV file will be generated indicating whether each number has traffic:

* An `X` in a column = the number **has traffic** of that type
* No `X` = **no traffic detected**

Example columns:

```
number, inbound_calls, inbound_messages, outbound_calls, outbound_messages
+12345550100, X, , X,
+12345550200, , , ,
```




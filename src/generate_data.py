import pandas as pd
import random
import uuid
from datetime import datetime, timedelta
import os

# --------------------------------------------------
# Resolve project root directory safely
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------
# Define raw data directory (always under project root)
# --------------------------------------------------
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw")
os.makedirs(RAW_DATA_PATH, exist_ok=True)

# --------------------------------------------------
# Data generation configuration
# --------------------------------------------------
NUM_RECORDS = 1000

payment_methods = ["UPI", "CARD", "WALLET"]
statuses = ["SUCCESS", "FAILED"]
failure_reasons = ["INSUFFICIENT_FUNDS", "TIMEOUT", "BANK_ERROR"]

records = []

# Generate timestamps within last 24 hours
start_time = datetime.now() - timedelta(days=1)

# --------------------------------------------------
# Generate payment event records
# --------------------------------------------------
for _ in range(NUM_RECORDS):
    status = random.choice(statuses)

    record = {
        "transaction_id": str(uuid.uuid4()),
        "user_id": f"user_{random.randint(1000, 1100)}",
        "amount": round(random.uniform(10, 5000), 2),
        "currency": "INR",
        "payment_method": random.choice(payment_methods),
        "status": status,
        "failure_reason": None if status == "SUCCESS" else random.choice(failure_reasons),
        "created_at": start_time + timedelta(seconds=random.randint(1, 86400))
    }

    records.append(record)

# --------------------------------------------------
# Convert to DataFrame
# --------------------------------------------------
df = pd.DataFrame(records)

# --------------------------------------------------
# Persist raw data (CSV + JSON)
# --------------------------------------------------
csv_path = os.path.join(RAW_DATA_PATH, "payments_2024_01_01.csv")
df.to_csv(csv_path, index=False)

json_path = os.path.join(RAW_DATA_PATH, "payments_2024_01_01.json")
df.to_json(json_path, orient="records", lines=True)

# --------------------------------------------------
# Log output
# --------------------------------------------------
print(f"Generated {NUM_RECORDS} payment records")
print(f"CSV saved to: {csv_path}")
print(f"JSON saved to: {json_path}")
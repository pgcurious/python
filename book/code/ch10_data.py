#!/usr/bin/env python3
"""
Chapter 10: Working with Data
Run this file to see all examples in action.
"""

import json
import csv
import re
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
import tempfile

print("=" * 60)
print("CHAPTER 10: WORKING WITH DATA")
print("=" * 60)

# Create temp directory
temp_dir = Path(tempfile.mkdtemp())

# -----------------------------------------------------------------------------
# 10.1 JSON
# -----------------------------------------------------------------------------
print("\n--- 10.1 JSON ---")

data = {
    "name": "Alice",
    "age": 30,
    "active": True,
    "scores": [85, 90, 88],
    "address": None
}

# Serialize
json_string = json.dumps(data)
print(f"JSON string: {json_string}")

# Pretty print
print(f"\nPretty JSON:\n{json.dumps(data, indent=2)}")

# Deserialize
parsed = json.loads(json_string)
print(f"\nParsed: {parsed}")

# File I/O
json_file = temp_dir / "data.json"
with open(json_file, "w") as f:
    json.dump(data, f, indent=2)

with open(json_file) as f:
    loaded = json.load(f)
print(f"\nLoaded from file: {loaded['name']}")


# Custom encoder for datetime
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


data_with_date = {"event": "meeting", "when": datetime.now()}
print(f"\nWith datetime: {json.dumps(data_with_date, cls=CustomEncoder)}")

# -----------------------------------------------------------------------------
# 10.2 CSV
# -----------------------------------------------------------------------------
print("\n--- 10.2 CSV ---")

# Write CSV
csv_file = temp_dir / "people.csv"
people = [
    {"name": "Alice", "age": 30, "city": "NYC"},
    {"name": "Bob", "age": 25, "city": "LA"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(people)

# Read CSV
print("Reading CSV:")
with open(csv_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['name']}, {row['age']}, {row['city']}")

# -----------------------------------------------------------------------------
# 10.3 Regular Expressions
# -----------------------------------------------------------------------------
print("\n--- 10.3 Regular Expressions ---")

text = "Contact: alice@email.com or bob@mail.org. Call 555-123-4567."

# Find all emails
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
print(f"Emails found: {emails}")

# Find phone numbers
phones = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(f"Phones found: {phones}")

# Search and capture groups
match = re.search(r"(\w+)@(\w+)\.(\w+)", text)
if match:
    print(f"Username: {match.group(1)}, Domain: {match.group(2)}")

# Replace
redacted = re.sub(r"[\w.-]+@[\w.-]+", "[REDACTED]", text)
print(f"Redacted: {redacted}")

# Split
parts = re.split(r"[,.\s]+", "hello, world. python")
print(f"Split: {parts}")

# Compile for reuse
email_pattern = re.compile(r"[\w.-]+@[\w.-]+\.\w+")
print(f"Compiled pattern matches: {email_pattern.findall(text)}")

# -----------------------------------------------------------------------------
# 10.4 Date and Time
# -----------------------------------------------------------------------------
print("\n--- 10.4 Date and Time ---")

# Current time
now = datetime.now()
print(f"Now: {now}")

# Formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted: {formatted}")

# Parsing
parsed_date = datetime.strptime("2024-06-15", "%Y-%m-%d")
print(f"Parsed: {parsed_date}")

# ISO format
iso = now.isoformat()
print(f"ISO format: {iso}")

# Arithmetic
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
print(f"Next week: {next_week.strftime('%Y-%m-%d')}")

# Difference
diff = datetime(2024, 12, 31) - datetime(2024, 1, 1)
print(f"Days in 2024: {diff.days}")

# -----------------------------------------------------------------------------
# 10.5 Data Transformation
# -----------------------------------------------------------------------------
print("\n--- 10.5 Data Transformation ---")

users = [
    {"name": "Alice", "age": 30, "active": True},
    {"name": "Bob", "age": 25, "active": False},
    {"name": "Charlie", "age": 35, "active": True}
]

# Filter
active_users = [u for u in users if u["active"]]
print(f"Active users: {[u['name'] for u in active_users]}")

# Transform
names = [u["name"] for u in users]
print(f"Names: {names}")

# Sort
by_age = sorted(users, key=lambda u: u["age"])
print(f"By age: {[u['name'] for u in by_age]}")

# Group by
by_active = defaultdict(list)
for user in users:
    by_active[user["active"]].append(user["name"])
print(f"Grouped by active: {dict(by_active)}")

# Aggregate
total_age = sum(u["age"] for u in users)
avg_age = total_age / len(users)
print(f"Average age: {avg_age:.1f}")

oldest = max(users, key=lambda u: u["age"])
print(f"Oldest: {oldest['name']}")

# -----------------------------------------------------------------------------
# 10.6 Environment Variables
# -----------------------------------------------------------------------------
print("\n--- 10.6 Environment Variables ---")

import os

# Read with default
db_url = os.environ.get("DATABASE_URL", "sqlite:///default.db")
debug = os.environ.get("DEBUG", "false").lower() == "true"
print(f"DATABASE_URL: {db_url}")
print(f"DEBUG: {debug}")

# List some env vars
print("\nSome environment variables:")
for key in ["HOME", "PATH", "USER"]:
    value = os.environ.get(key, "Not set")
    if len(value) > 50:
        value = value[:50] + "..."
    print(f"  {key}: {value}")

# -----------------------------------------------------------------------------
# Cleanup
# -----------------------------------------------------------------------------
import shutil
shutil.rmtree(temp_dir)

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("""
JSON:
  json.dumps(obj) / json.loads(str)  # String
  json.dump(obj, file) / json.load(file)  # File

CSV:
  csv.reader / csv.writer
  csv.DictReader / csv.DictWriter

REGEX:
  re.findall(pattern, text)  # All matches
  re.search(pattern, text)   # First match
  re.sub(pattern, repl, text)  # Replace
  re.compile(pattern)  # Compile for reuse

DATETIME:
  datetime.now(), datetime.strptime()
  strftime() for formatting
  timedelta for arithmetic

DATA TRANSFORMATION:
  Filter: [x for x in data if condition]
  Map: [transform(x) for x in data]
  Sort: sorted(data, key=lambda x: x['field'])
  Group: defaultdict(list) or itertools.groupby
  Aggregate: sum(), max(), min(), statistics
""")

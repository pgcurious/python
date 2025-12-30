# Chapter 10: Working with Data

Modern applications work extensively with data in various formats. This chapter covers JSON, CSV, APIs, and common data processing patterns.

## 10.1 JSON - JavaScript Object Notation

JSON is the most common data interchange format for web APIs and configuration.

### Reading and Writing JSON

```python
import json

# Python to JSON (serialization)
data = {
    "name": "Alice",
    "age": 30,
    "active": True,
    "scores": [85, 90, 88],
    "address": None
}

# Convert to JSON string
json_string = json.dumps(data)
print(json_string)

# Pretty print
json_pretty = json.dumps(data, indent=2, sort_keys=True)
print(json_pretty)

# Write to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# JSON to Python (deserialization)
json_string = '{"name": "Bob", "age": 25}'
parsed = json.loads(json_string)
print(parsed["name"])  # Bob

# Read from file
with open("data.json", "r") as f:
    loaded = json.load(f)
```

### Handling Custom Types

```python
from datetime import datetime
from decimal import Decimal
import json

# Custom encoder
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        return super().default(obj)

data = {
    "timestamp": datetime.now(),
    "price": Decimal("19.99")
}

json_string = json.dumps(data, cls=CustomEncoder)
print(json_string)

# Custom decoder
def custom_decoder(obj):
    if "timestamp" in obj:
        obj["timestamp"] = datetime.fromisoformat(obj["timestamp"])
    return obj

loaded = json.loads(json_string, object_hook=custom_decoder)
```

## 10.2 CSV - Comma-Separated Values

CSV is widely used for tabular data, especially in data science.

### Reading CSV

```python
import csv

# Basic reading
with open("data.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    for row in reader:
        print(row)

# Reading as dictionaries
with open("data.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['age']}")

# Different delimiters
with open("data.tsv", "r", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)
```

### Writing CSV

```python
import csv

# Basic writing
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "NYC"],
    ["Bob", 25, "LA"]
]

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Writing dictionaries
people = [
    {"name": "Alice", "age": 30, "city": "NYC"},
    {"name": "Bob", "age": 25, "city": "LA"}
]

with open("output.csv", "w", newline="") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(people)
```

## 10.3 Working with APIs

### HTTP Requests with requests Library

```python
import requests

# GET request
response = requests.get("https://api.example.com/users")
if response.status_code == 200:
    users = response.json()
    for user in users:
        print(user["name"])

# With parameters
params = {"page": 1, "limit": 10}
response = requests.get("https://api.example.com/users", params=params)

# With headers
headers = {
    "Authorization": "Bearer token123",
    "Content-Type": "application/json"
}
response = requests.get("https://api.example.com/users", headers=headers)

# POST request
data = {"name": "Alice", "email": "alice@example.com"}
response = requests.post(
    "https://api.example.com/users",
    json=data,
    headers=headers
)

if response.status_code == 201:
    new_user = response.json()
    print(f"Created user with ID: {new_user['id']}")

# Other methods
requests.put(url, json=data)
requests.patch(url, json=data)
requests.delete(url)

# Handling errors
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raises for 4xx/5xx
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.ConnectionError:
    print("Connection failed")
except requests.exceptions.Timeout:
    print("Request timed out")
```

### Sessions for Multiple Requests

```python
import requests

# Session maintains cookies and connection pooling
session = requests.Session()
session.headers.update({"Authorization": "Bearer token123"})

# All requests use same session
response1 = session.get("https://api.example.com/users")
response2 = session.get("https://api.example.com/products")

session.close()

# Context manager
with requests.Session() as session:
    session.headers.update({"Authorization": "Bearer token123"})
    response = session.get("https://api.example.com/users")
```

## 10.4 Data Processing Patterns

### Transforming Data

```python
# List of dictionaries transformation
users = [
    {"name": "Alice", "age": 30, "active": True},
    {"name": "Bob", "age": 25, "active": False},
    {"name": "Charlie", "age": 35, "active": True}
]

# Filter
active_users = [u for u in users if u["active"]]

# Map/Transform
names = [u["name"] for u in users]
user_summary = [{"name": u["name"], "is_adult": u["age"] >= 18} for u in users]

# Sort
sorted_by_age = sorted(users, key=lambda u: u["age"])
sorted_desc = sorted(users, key=lambda u: u["age"], reverse=True)

# Group by
from collections import defaultdict
by_active = defaultdict(list)
for user in users:
    by_active[user["active"]].append(user)

# Aggregate
total_age = sum(u["age"] for u in users)
avg_age = total_age / len(users)
oldest = max(users, key=lambda u: u["age"])
```

### Processing Large Datasets

```python
# Generator for memory efficiency
def process_large_csv(filename):
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Process one row at a time
            yield transform_row(row)

# Chain generators
def read_rows(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        yield from reader

def filter_valid(rows):
    for row in rows:
        if is_valid(row):
            yield row

def transform(rows):
    for row in rows:
        yield process(row)

# Compose pipeline
pipeline = transform(filter_valid(read_rows("data.csv")))
for item in pipeline:
    save(item)
```

## 10.5 Regular Expressions

```python
import re

text = "Contact: alice@email.com or bob@mail.org"

# Find all matches
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
print(emails)  # ['alice@email.com', 'bob@mail.org']

# Search for pattern
match = re.search(r"(\w+)@(\w+)\.(\w+)", text)
if match:
    print(match.group(0))  # Full match
    print(match.group(1))  # First group (username)

# Replace
new_text = re.sub(r"@[\w.-]+", "@redacted.com", text)

# Split
parts = re.split(r"\s+", "hello   world   python")
print(parts)  # ['hello', 'world', 'python']

# Compile for reuse
pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
phones = pattern.findall("Call 555-123-4567 or 555-987-6543")

# Common patterns
patterns = {
    "email": r"[\w.-]+@[\w.-]+\.\w+",
    "phone": r"\d{3}[-.]?\d{3}[-.]?\d{4}",
    "url": r"https?://[\w./]+",
    "date": r"\d{4}-\d{2}-\d{2}",
}
```

## 10.6 Date and Time

```python
from datetime import datetime, date, time, timedelta
from zoneinfo import ZoneInfo  # Python 3.9+

# Current date/time
now = datetime.now()
today = date.today()
utc_now = datetime.now(ZoneInfo("UTC"))

# Creating dates
d = date(2024, 1, 15)
t = time(14, 30, 0)
dt = datetime(2024, 1, 15, 14, 30, 0)

# Parsing strings
dt = datetime.strptime("2024-01-15 14:30:00", "%Y-%m-%d %H:%M:%S")
dt = datetime.fromisoformat("2024-01-15T14:30:00")

# Formatting
formatted = dt.strftime("%B %d, %Y")  # January 15, 2024
iso_format = dt.isoformat()

# Arithmetic
tomorrow = today + timedelta(days=1)
next_week = now + timedelta(weeks=1)
diff = datetime(2024, 12, 31) - now
print(f"Days until end of year: {diff.days}")

# Timezone handling
la_time = datetime.now(ZoneInfo("America/Los_Angeles"))
tokyo_time = la_time.astimezone(ZoneInfo("Asia/Tokyo"))
```

## 10.7 Configuration Files

### INI/Config Files

```python
import configparser

# Reading
config = configparser.ConfigParser()
config.read("config.ini")

database_host = config["database"]["host"]
debug = config.getboolean("app", "debug")
port = config.getint("app", "port")

# Writing
config["app"] = {"debug": "true", "port": "8080"}
config["database"] = {"host": "localhost", "name": "mydb"}

with open("config.ini", "w") as f:
    config.write(f)
```

### Environment Variables

```python
import os
from pathlib import Path

# Read environment variables
database_url = os.environ.get("DATABASE_URL", "sqlite:///default.db")
debug = os.environ.get("DEBUG", "false").lower() == "true"

# .env files (using python-dotenv)
# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()  # Load .env file
api_key = os.environ.get("API_KEY")
```

## 10.8 Exercises

### Exercise 10.1: API Client
```python
# Create a class that:
# - Fetches data from a REST API
# - Handles pagination
# - Caches responses
# - Retries on failure
# - Saves results to JSON
```

### Exercise 10.2: Data Transformer
```python
# Create a data pipeline that:
# - Reads CSV file of sales data
# - Filters by date range
# - Aggregates by category
# - Outputs summary as JSON
# - Generates a report as Markdown
```

### Exercise 10.3: Log Parser
```python
# Create a log file analyzer that:
# - Parses different log formats
# - Extracts timestamps, levels, messages
# - Groups by time periods
# - Finds error patterns
# - Generates statistics
```

---

**Next Chapter:** [Testing in Python](11_testing.md) - Unit tests, pytest, and test-driven development.

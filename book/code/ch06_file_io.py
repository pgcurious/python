#!/usr/bin/env python3
"""
Chapter 6: File Handling and I/O
Run this file to see all examples in action.
"""

import json
import csv
import tempfile
from pathlib import Path

print("=" * 60)
print("CHAPTER 6: FILE HANDLING AND I/O")
print("=" * 60)

# Create a temp directory for our examples
temp_dir = Path(tempfile.mkdtemp())
print(f"\nUsing temp directory: {temp_dir}")

# -----------------------------------------------------------------------------
# 6.1 Basic File Operations
# -----------------------------------------------------------------------------
print("\n--- 6.1 Basic File Operations ---")

# Write to file
sample_file = temp_dir / "sample.txt"
with open(sample_file, "w") as f:
    f.write("Hello, Python!\n")
    f.write("File I/O is easy.\n")
    f.write("This is line 3.\n")

print(f"Created: {sample_file}")

# Read entire file
with open(sample_file, "r") as f:
    content = f.read()
print(f"Content:\n{content}")

# Read line by line
print("Reading line by line:")
with open(sample_file, "r") as f:
    for i, line in enumerate(f, 1):
        print(f"  Line {i}: {line.strip()}")

# Append to file
with open(sample_file, "a") as f:
    f.write("This line was appended.\n")

# -----------------------------------------------------------------------------
# 6.2 pathlib
# -----------------------------------------------------------------------------
print("\n--- 6.2 pathlib ---")

path = Path("example/subfolder/file.txt")
print(f"Path: {path}")
print(f"  name: {path.name}")
print(f"  stem: {path.stem}")
print(f"  suffix: {path.suffix}")
print(f"  parent: {path.parent}")
print(f"  parts: {path.parts}")

# Path operations
new_path = Path("folder") / "subfolder" / "file.txt"
print(f"\nJoined path: {new_path}")

# Check existence
print(f"\n{sample_file} exists: {sample_file.exists()}")
print(f"{sample_file} is file: {sample_file.is_file()}")

# Read/write with pathlib
pathlib_file = temp_dir / "pathlib_test.txt"
pathlib_file.write_text("Written with pathlib!")
print(f"\nRead with pathlib: {pathlib_file.read_text()}")

# -----------------------------------------------------------------------------
# 6.3 Working with JSON
# -----------------------------------------------------------------------------
print("\n--- 6.3 Working with JSON ---")

data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "JavaScript", "SQL"],
    "active": True
}

# Write JSON
json_file = temp_dir / "data.json"
with open(json_file, "w") as f:
    json.dump(data, f, indent=2)
print(f"Wrote JSON to: {json_file}")

# Read JSON
with open(json_file, "r") as f:
    loaded = json.load(f)
print(f"Loaded JSON: {loaded}")

# Pretty print
print(f"\nPretty JSON:\n{json.dumps(data, indent=2)}")

# -----------------------------------------------------------------------------
# 6.4 Working with CSV
# -----------------------------------------------------------------------------
print("\n--- 6.4 Working with CSV ---")

# Write CSV
csv_data = [
    {"name": "Alice", "age": 30, "city": "NYC"},
    {"name": "Bob", "age": 25, "city": "LA"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

csv_file = temp_dir / "people.csv"
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(csv_data)
print(f"Wrote CSV to: {csv_file}")

# Read CSV
print("\nReading CSV:")
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['name']}, {row['age']}, {row['city']}")

# -----------------------------------------------------------------------------
# 6.5 Binary Files
# -----------------------------------------------------------------------------
print("\n--- 6.5 Binary Files ---")

# Write binary
binary_file = temp_dir / "binary.dat"
binary_data = bytes([0x48, 0x65, 0x6C, 0x6C, 0x6F])  # "Hello" in ASCII
with open(binary_file, "wb") as f:
    f.write(binary_data)

# Read binary
with open(binary_file, "rb") as f:
    read_data = f.read()
print(f"Binary data: {read_data}")
print(f"Decoded: {read_data.decode('utf-8')}")

# -----------------------------------------------------------------------------
# 6.6 Temporary Files
# -----------------------------------------------------------------------------
print("\n--- 6.6 Temporary Files ---")

with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
    f.write("Temporary content")
    print(f"Temp file: {f.name}")

with tempfile.TemporaryDirectory() as tmpdir:
    print(f"Temp directory: {tmpdir}")
    # Directory will be deleted when context exits

# -----------------------------------------------------------------------------
# Cleanup
# -----------------------------------------------------------------------------
print("\n--- Cleanup ---")
import shutil
shutil.rmtree(temp_dir)
print(f"Removed temp directory: {temp_dir}")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("""
FILE MODES:
  'r' - read (default)    'w' - write (truncate)
  'a' - append            'x' - exclusive create
  'b' - binary            '+' - read and write

BEST PRACTICES:
  - Always use context managers: with open(...) as f:
  - Specify encoding: open(file, encoding='utf-8')
  - Use pathlib for path operations
  - Use json/csv modules for structured data

PATHLIB:
  Path.exists(), is_file(), is_dir()
  Path.read_text(), write_text()
  Path.glob('*.py'), iterdir()
  Path('/') joining with /
""")

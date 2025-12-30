# Chapter 6: File Handling and I/O

Working with files is fundamental to most applications. Python provides elegant, straightforward ways to read, write, and manipulate files.

## 6.1 Basic File Operations

### Opening and Closing Files

```python
# Basic pattern (not recommended - may not close on error)
file = open('example.txt', 'r')
content = file.read()
file.close()

# Recommended: context manager (always closes properly)
with open('example.txt', 'r') as file:
    content = file.read()
# File automatically closed here
```

### File Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read (default) - file must exist |
| `'w'` | Write - creates new or truncates existing |
| `'a'` | Append - creates new or appends to existing |
| `'x'` | Exclusive create - fails if file exists |
| `'b'` | Binary mode (combine: `'rb'`, `'wb'`) |
| `'t'` | Text mode (default, combine: `'rt'`) |
| `'+'` | Read and write (combine: `'r+'`, `'w+'`) |

```python
# Read mode
with open('file.txt', 'r') as f:
    content = f.read()

# Write mode (overwrites!)
with open('file.txt', 'w') as f:
    f.write('New content')

# Append mode
with open('file.txt', 'a') as f:
    f.write('\nAdditional line')

# Binary mode (for images, etc.)
with open('image.png', 'rb') as f:
    binary_data = f.read()
```

## 6.2 Reading Files

```python
# Read entire file as string
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)

# Read all lines as list
with open('example.txt', 'r') as f:
    lines = f.readlines()  # Includes \n
    for line in lines:
        print(line.strip())  # Remove trailing newline

# Read line by line (memory efficient for large files)
with open('example.txt', 'r') as f:
    for line in f:  # f is an iterator
        print(line.strip())

# Read specific number of characters
with open('example.txt', 'r') as f:
    chunk = f.read(100)  # First 100 characters

# Read one line at a time
with open('example.txt', 'r') as f:
    first_line = f.readline()
    second_line = f.readline()
```

### Handling Encodings

```python
# Explicitly specify encoding (recommended)
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Handle encoding errors
with open('file.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Common encodings: 'utf-8', 'latin-1', 'ascii', 'utf-16'
```

## 6.3 Writing Files

```python
# Write string
with open('output.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.write('Second line\n')

# Write multiple lines
lines = ['Line 1', 'Line 2', 'Line 3']
with open('output.txt', 'w') as f:
    for line in lines:
        f.write(line + '\n')

# Or use writelines (no automatic newlines!)
with open('output.txt', 'w') as f:
    f.writelines(line + '\n' for line in lines)

# Using print to file
with open('output.txt', 'w') as f:
    print('Hello', file=f)
    print('World', file=f)

# Append to existing file
with open('log.txt', 'a') as f:
    f.write('New log entry\n')
```

## 6.4 Working with Paths (pathlib)

The `pathlib` module provides an object-oriented interface for file system paths.

```python
from pathlib import Path

# Create path objects
current = Path('.')
home = Path.home()
file_path = Path('folder/subfolder/file.txt')

# Path operations
print(file_path.name)        # file.txt
print(file_path.stem)        # file
print(file_path.suffix)      # .txt
print(file_path.parent)      # folder/subfolder
print(file_path.parts)       # ('folder', 'subfolder', 'file.txt')

# Build paths
new_path = Path('folder') / 'subfolder' / 'file.txt'
print(new_path)  # folder/subfolder/file.txt

# Absolute path
print(file_path.absolute())

# Check existence
if file_path.exists():
    print('File exists')
if file_path.is_file():
    print('Is a file')
if file_path.is_dir():
    print('Is a directory')

# Read and write (convenient methods)
path = Path('example.txt')
content = path.read_text(encoding='utf-8')
path.write_text('New content', encoding='utf-8')

# Binary read/write
binary_content = path.read_bytes()
path.write_bytes(b'binary data')

# List directory contents
for item in Path('.').iterdir():
    print(item)

# Glob patterns
for py_file in Path('.').glob('**/*.py'):  # Recursive
    print(py_file)

# Create directories
Path('new_folder/subfolder').mkdir(parents=True, exist_ok=True)

# Delete
Path('file.txt').unlink(missing_ok=True)  # Delete file
Path('empty_folder').rmdir()              # Delete empty directory
```

## 6.5 Working with CSV Files

```python
import csv

# Writing CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'NYC'],
    ['Bob', 25, 'LA'],
    ['Charlie', 35, 'Chicago']
]

with open('people.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Writing with dictionaries
people = [
    {'name': 'Alice', 'age': 30, 'city': 'NYC'},
    {'name': 'Bob', 'age': 25, 'city': 'LA'}
]

with open('people.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(people)

# Reading CSV
with open('people.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    for row in reader:
        print(row)

# Reading as dictionaries
with open('people.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} is {row['age']} years old")
```

## 6.6 Working with JSON Files

```python
import json

# Writing JSON
data = {
    'name': 'Alice',
    'age': 30,
    'cities': ['NYC', 'LA'],
    'active': True
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Reading JSON
with open('data.json', 'r') as f:
    loaded = json.load(f)
    print(loaded['name'])

# JSON with custom types
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {'timestamp': datetime.now()}
json_str = json.dumps(data, cls=CustomEncoder)
```

## 6.7 Working with Binary Files

```python
# Copy a binary file
with open('source.png', 'rb') as src:
    with open('destination.png', 'wb') as dst:
        dst.write(src.read())

# Read in chunks (memory efficient)
def copy_file(source, dest, chunk_size=8192):
    with open(source, 'rb') as src:
        with open(dest, 'wb') as dst:
            while True:
                chunk = src.read(chunk_size)
                if not chunk:
                    break
                dst.write(chunk)

# Working with bytes
data = b'Hello, bytes!'
with open('binary.dat', 'wb') as f:
    f.write(data)

with open('binary.dat', 'rb') as f:
    content = f.read()
    print(content.decode('utf-8'))
```

## 6.8 Temporary Files

```python
import tempfile

# Temporary file (auto-deleted)
with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write('Temporary content')
    temp_path = f.name
print(f"Temp file at: {temp_path}")

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"Temp directory: {tmpdir}")
    # Use tmpdir for temporary files
# Directory automatically removed
```

## 6.9 File System Operations

```python
import shutil
from pathlib import Path

# Copy file
shutil.copy('source.txt', 'dest.txt')
shutil.copy2('source.txt', 'dest.txt')  # Preserves metadata

# Copy directory
shutil.copytree('source_dir', 'dest_dir')

# Move/rename
shutil.move('old_name.txt', 'new_name.txt')
Path('old.txt').rename('new.txt')

# Delete directory with contents
shutil.rmtree('directory_to_delete')

# Get file info
import os
stat_info = os.stat('file.txt')
print(f"Size: {stat_info.st_size} bytes")
print(f"Modified: {stat_info.st_mtime}")
```

## 6.10 Exercises

### Exercise 6.1: Log File Analyzer
```python
# Create a function that reads a log file and returns:
# - Total number of lines
# - Number of ERROR, WARNING, INFO entries
# - The most recent error message

# Sample log format:
# 2024-01-15 10:30:45 INFO User logged in
# 2024-01-15 10:31:02 ERROR Database connection failed
```

### Exercise 6.2: CSV Data Processor
```python
# Read a CSV file of sales data
# Calculate total sales per product
# Write results to a new CSV file
# Handle missing or malformed data gracefully
```

### Exercise 6.3: Configuration File Manager
```python
# Create a class that:
# - Loads configuration from JSON file
# - Provides get/set methods for config values
# - Saves changes back to file
# - Creates default config if file doesn't exist
```

---

**Next Chapter:** [Error Handling and Debugging](07_errors.md) - Exceptions, debugging, and logging.

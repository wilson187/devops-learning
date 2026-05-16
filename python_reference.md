# Python & DevOps Reference Sheet

==================================================
## PYTHON BASICS
==================================================

### Variables
```python
name = "web-01"        # string
cpu = 45               # integer
usage = 45.5           # float
is_online = True       # boolean
```

### Print
```python
print("Hello")
print("CPU:", cpu)
print("Usage:", cpu, "%")
```

### String formatting
```python
print(f"Server {name} is at {cpu}%")  # f-string — cleanest way
```

### Comments
```python
# This is a comment — Python ignores it
# Use comments to explain WHY not WHAT
```

==================================================
## CONDITIONS
==================================================

```python
if cpu >= 90:
    print("CRITICAL")
elif cpu >= 75:
    print("WARNING")
else:
    print("OK")
```

### Comparison operators
```
==   equal to
!=   not equal to
>    greater than
<    less than
>=   greater than or equal to
<=   less than or equal to
```

### Logical operators
```
and   both must be true
or    at least one must be true
not   reverses true/false
```

==================================================
## LOOPS
==================================================

### For loop — known collection
```python
servers = ["web-01", "web-02", "db-01"]
for server in servers:
    print(server)
```

### While loop — condition based
```python
retries = 0
while retries < 3:
    print("Attempt", retries + 1)
    retries += 1
```

### While True — runs forever until broken
```python
while True:
    # do something
    time.sleep(60)
```

### Zip — loop two lists together
```python
for server, cpu in zip(servers, cpu_usages):
    print(server, cpu)
```

==================================================
## FUNCTIONS
==================================================

```python
def check_status(value, warning, critical):
    if value >= critical:
        return "CRITICAL"
    elif value >= warning:
        return "WARNING"
    return "OK"

# Call it
status = check_status(85, 75, 90)
```

### Multiple return values
```python
def get_memory():
    return percent, used_gb, total_gb

# Unpack them
percent, used, total = get_memory()
```

### Global variables — use sparingly
```python
count = 0

def increment():
    global count
    count += 1
```

==================================================
## DATA STRUCTURES
==================================================

### List — ordered collection
```python
servers = ["web-01", "web-02", "db-01"]
servers[0]    # web-01 — zero indexed
```

### Dictionary — key/value pairs
```python
servers = {
    "web-01": 45,
    "web-02": 85
}

# Access a value
servers["web-01"]    # 45

# Loop through
for server, cpu in servers.items():
    print(server, cpu)
```

==================================================
## ERROR HANDLING
==================================================

```python
try:
    result = get_cpu()
except KeyboardInterrupt:
    print("Stopped.")
    break
except Exception as e:
    print("Error:", e)
```

### Common error types
```
SyntaxError      — wrong grammar, bad structure
IndentationError — wrong indentation
NameError        — used a name Python doesn't know
TypeError        — wrong data type (e.g. writing int to file)
FileNotFoundError — file doesn't exist
```

==================================================
## FILES
==================================================

### Read a file
```python
with open("file.txt") as f:
    content = f.read()
```

### Write to a file — overwrites
```python
with open("file.txt", "w") as f:
    f.write("Hello\n")
```

### Append to a file — adds to end
```python
with open("file.txt", "a") as f:
    f.write("New line\n")
```

### Read JSON
```python
import json
with open("config.json") as f:
    config = json.load(f)
```

### Check file exists
```python
import os
if os.path.exists("file.txt"):
    print("Found it")
```

==================================================
## IMPORTS & LIBRARIES
==================================================

```python
import psutil          # system metrics
import time            # sleep/timing
import json            # read/write JSON
import os              # file system operations
import argparse        # command line arguments
from datetime import datetime   # timestamps
```

### psutil — system metrics
```python
psutil.cpu_percent(interval=1)          # CPU usage %
psutil.virtual_memory()                 # memory object
psutil.virtual_memory().percent         # memory %
psutil.virtual_memory().total           # total bytes
psutil.virtual_memory().used            # used bytes
psutil.disk_usage('/')                  # disk object
psutil.disk_usage('/').percent          # disk %
psutil.net_io_counters().bytes_sent     # bytes sent
psutil.net_io_counters().bytes_recv     # bytes received
psutil.cpu_count()                      # number of cores
psutil.boot_time()                      # boot timestamp
```

### datetime — timestamps
```python
from datetime import datetime
now = datetime.now()
now.strftime("%Y-%m-%d %H:%M:%S")      # format as string
datetime.fromtimestamp(psutil.boot_time())  # convert timestamp
```

### time — pausing
```python
import time
time.sleep(60)    # pause for 60 seconds
```

### argparse — command line arguments
```python
import argparse
parser = argparse.ArgumentParser(description="My tool")
parser.add_argument("--interval", type=int, help="Interval in seconds")
parser.add_argument("--verbose", action="store_true", help="Verbose output")
args = parser.parse_args()

# Use them
args.interval
args.verbose
```

==================================================
## CONVERSIONS
==================================================

```python
# Bytes to megabytes
mb = bytes / (1024 * 1024)

# Bytes to gigabytes
gb = bytes / (1024 * 1024 * 1024)
# or
gb = bytes / (1024 ** 3)

# Round to 2 decimal places
round(value, 2)

# Convert number to string
str(45)

# Convert string to integer
int("45")
```

==================================================
## SCRIPT STRUCTURE — always follow this order
==================================================

```
1. Imports
2. Constants
3. Functions
4. Startup code (load config, parse args)
5. Main loop or main logic
```

==================================================
## GIT COMMANDS USED SO FAR
==================================================

```bash
git init                          # start a new repo
git add filename                  # stage a file
git add .                         # stage all files
git commit -m "message"           # commit with message
git log                           # see commit history
git status                        # see what's changed
```

### Good commit message format
```
feat: add verbose mode with CPU core count
feat: add network stats to system monitor
fix: correct threshold logic in check_status
```

==================================================
## TERMINAL COMMANDS USED SO FAR
==================================================

```bash
mkdir foldername      # create a folder
cd foldername         # move into a folder
code filename.py      # open/create file in VS Code
cat filename          # print file contents to terminal
python filename.py    # run a Python script
pip install package   # install a Python library
```

==================================================
## DEBUGGING PROCESS — always follow this
==================================================

```
1. Read the full error message
2. Note the error TYPE and LINE NUMBER
3. Rubber duck it — explain the code out loud
4. Try to fix it yourself for 20 minutes
5. Search the specific error message on Google
6. Read the official docs
7. Ask for help after 45 minutes
```
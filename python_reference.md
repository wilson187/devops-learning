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
==================================================
## LINUX & BASH COMMANDS
==================================================

### Navigation
```bash
pwd                    # where am I?
cd foldername          # move into folder
cd ..                  # go up one level
cd ~                   # go to home directory
ls                     # list files
ls -la                 # list all files with permissions
```

### Files
```bash
touch filename         # create empty file
cat filename           # print file contents
head -10 filename      # first 10 lines
tail -10 filename      # last 10 lines
tail -f filename       # follow file live — great for logs
cp file destination    # copy file
mv file destination    # move or rename file
rm filename            # delete file
rm -rf foldername      # delete folder and everything in it — careful
```

### Writing to files
```bash
echo "text" > file     # write — overwrites
echo "text" >> file    # append — adds to end
```

### Searching
```bash
grep "word" file           # find lines containing word
grep -i "word" file        # case insensitive
grep -n "word" file        # show line numbers
grep -c "word" file        # count matching lines
grep -A 2 "word" file      # show 2 lines after match
grep -B 2 "word" file      # show 2 lines before match
grep -r "word" ./folder    # search recursively in folder
```

### Pipes — chain commands together
```bash
command1 | command2        # output of 1 becomes input of 2

# Real examples
grep "CRITICAL" monitor.log | wc -l      # count critical lines
cat monitor.log | tail -20               # last 20 lines
grep "ERROR" monitor.log | less          # scroll through errors
ls -la | grep ".py"                      # find python files
```

### Counting and sorting
```bash
wc -l filename             # count lines in file
wc -w filename             # count words
sort filename              # sort lines alphabetically
sort -r filename           # sort in reverse
uniq filename              # remove duplicate lines
sort filename | uniq -c    # count occurrences of each line
```

### Permissions
```bash
ls -la                     # see permissions
chmod +x filename          # add execute permission
chmod u+x filename         # add execute for owner only
chmod 755 filename         # rwxr-xr-x
chmod 644 filename         # rw-r--r--
```

### Permission string breakdown
```
-rwxr-xr-x
|   |   |   |
|   |   |   └── others: r-x (read, execute)
|   |   └─────── group:  r-x (read, execute)
|   └──────────── owner: rwx (read, write, execute)
└──────────────── type: - file, d directory
```

### Bash scripts
```bash
#!/bin/bash               # shebang — tells system this is bash
$1, $2, $3                # arguments passed to script
$0                        # script name itself

# Check if argument is empty
if [ -z "$1" ]; then
    echo "No argument provided"
    exit 1
fi

# exit codes
exit 0                    # success
exit 1                    # failure
```

### Timestamps in Bash
```bash
date '+%Y-%m-%d %H:%M:%S'              # current timestamp
echo "$(date '+%Y-%m-%d %H:%M:%S')"    # inline in echo
```

### System info
```bash
whoami                    # current user
uname -a                  # OS and kernel info
hostname                  # machine name
uptime                    # how long system has been running
df -h                     # disk usage human readable
free -h                   # memory usage human readable
top                       # live process monitor — q to quit
htop                      # better version of top if installed
```
==================================================
## SSH
==================================================

```bash
ssh user@server           # connect to remote server
ssh -i key.pem user@server  # connect with specific key file

# Key files live in ~/.ssh/
id_ed25519                # private key — never share
id_ed25519.pub            # public key — put this on servers
known_hosts               # fingerprints of servers you've connected to
```
==================================================
## PROCESS MANAGEMENT
==================================================

```bash
ps aux                     # list all running processes
ps aux | grep python       # find specific process
jobs                       # list background jobs in current terminal

# Running in background
python script.py &                        # run in background, output to terminal
python script.py > /dev/null 2>&1 &      # run in background, no output

# Killing processes
kill PID                   # graceful kill
kill -9 PID               # force kill — use when normal kill fails

# /dev/null explained
> /dev/null                # discard standard output
2>&1                       # redirect errors to same place as output
```

==================================================
## CRON JOBS
==================================================

### Cron syntax
```
* * * * * command
| | | | |
| | | | └── day of week (0-6, 0=Sunday)
| | | └──── month (1-12)
| | └────── day of month (1-31)
| └──────── hour (0-23)
└────────── minute (0-59)
```

### Common schedules
```bash
*/1 * * * *     # every minute
*/5 * * * *     # every 5 minutes
0 * * * *       # every hour
0 6 * * *       # every day at 6am
0 9 * * 1       # every Monday at 9am
0 0 * * *       # every day at midnight
```

### Managing cron
```bash
crontab -l      # list cron jobs
crontab -e      # edit cron jobs
crontab -r      # remove all cron jobs — careful

sudo service cron status    # check cron is running
sudo service cron start     # start cron
```

### Always use full paths in cron
```bash
*/1 * * * * /home/wilson/devops-learning/venv/bin/python3 /home/wilson/devops-learning/system_monitor.py >> /home/wilson/devops-learning/logs/cron.log 2>&1
```

### Virtual environments
```bash
python3 -m venv venv        # create virtual environment
source venv/bin/activate    # activate it
deactivate                  # deactivate it
pip install package         # install inside venv
which python3               # confirm you're using venv python
```

### Always add to .gitignore
```
venv/pycache__/*.pyc
```
==================================================
## TEXT PROCESSING
==================================================

### awk — extract specific columns
```bash
# Columns are $1, $2, $3 etc split by spaces
awk '{print $1, $3}' file                     # print columns 1 and 3
awk '$3 == "ERROR" {print}' file              # filter by column value
awk '{print $3}' file | sort | uniq -c        # count by column value

# Print from column 5 to end of line
awk '{printf $1" "$2" "; for(i=5;i<=NF;i++) printf $i" "; print ""}' file
```

### sed — find and replace
```bash
sed 's/old/new/g' file         # replace in output only — file unchanged
sed -i 's/old/new/g' file     # replace IN the file — no undo, be careful
```

### cut — extract fields
```bash
cut -c1-10 file                # first 10 characters of each line
cut -d' ' -f3 file            # third field split by space
```

### sort and count
```bash
sort file                      # sort alphabetically
sort -r file                   # sort in reverse
sort -rn file                  # sort numeric reverse
uniq -c file                   # count consecutive duplicates
sort file | uniq -c | sort -rn # full frequency count — use this constantly
wc -l file                     # count lines
wc -w file                     # count words
```

==================================================
## SCOPE
==================================================

```python
# Global — variable created outside a function, exists everywhere
# Local  — variable created inside a function, only exists there

count = 0           # global

def increment():
    global count    # tell Python to use the global one
    count += 1

# Better approach — return values instead of using global
def increment(count):
    return count + 1
```

==================================================
## TERNARY EXPRESSION — one line if/else
==================================================

```python
# Instead of:
if args.interval:
    CHECK_INTERVAL = args.interval
else:
    CHECK_INTERVAL = config["check_interval"]

# Write it as:
CHECK_INTERVAL = args.interval if args.interval else config["check_interval"]
```

==================================================
## VIRTUAL ENVIRONMENTS
==================================================

```bash
python3 -m venv venv              # create virtual environment
source venv/bin/activate          # activate — prompt shows (venv)
deactivate                        # deactivate
pip install package               # install inside venv
which python3                     # confirm you're using venv python
pip freeze                        # list installed packages
pip freeze > requirements.txt     # save package list to file
pip install -r requirements.txt   # install from requirements file
```
==================================================
## HEREDOC — write multi-line content to a file
==================================================

```bash
cat > filename << 'EOF'
line one
line two
line three
EOF
```

==================================================
## SYSTEM INFO COMMANDS
==================================================

```bash
stat -c%s filename        # file size in bytes
du -h filename            # file size human readable
du -sh folder             # folder size human readable
df -h                     # disk usage human readable
free -h                   # memory usage human readable
```
==================================================
## KEY PRINCIPLES — never forget these
==================================================

```bash
Always know where you are         # pwd before anything on an unfamiliar server
Pipes are your most powerful tool # chain commands instead of writing scripts
Full paths in cron                # cron has no context — always absolute paths
Virtual environments always       # never install packages system-wide

> overwrites                      # replaces file contents
>> appends                        # adds to existing file contents

Exit codes matter                 # 0 = success, anything else = failure
Never commit secrets              # .env, API keys, passwords in .gitignore
kill -9 is last resort            # try normal kill first

Pseudocode before code            # always plan logic first
DRY                               # Don’t Repeat Yourself
Separate config from code         # never hardcode changing values

Read logs first                   # errors are usually already logged
Test in dev before prod           # never experiment in production
Automate repetitive work          # if repeated often, script it

Small changes are safer           # easier to debug and rollback
Backups must be tested            # restores matter more than backups
Least privilege always            # minimum permissions required

Document important things         # future you will forget
Version control everything        # scripts, configs, infrastructure
Monitor before users complain     # alerts should detect issues early
```

==================================================
## SYSTEM INFO COMMANDS
==================================================

```bash
stat -c%s filename                # file size in bytes
du -h filename                    # file size human readable
du -sh folder                     # folder size human readable

df -h                             # disk usage human readable
free -h                           # memory usage human readable

uptime                            # system uptime and load
top                               # live process monitoring
htop                              # improved process viewer

ps aux                            # running processes
ps aux | grep nginx               # find specific process

uname -a                          # kernel/system info
hostnamectl                       # hostname and OS info

ip a                              # network interfaces
ss -tulpn                         # listening ports/services

whoami                            # current user
id                                # user and group IDs
```
# log_summary.py - verison A
# Reads a log file and prints a summary of each status level

import sys
import os

def summarise_log(filepath):
    if not os.path.isfile(filepath):
        print("Error: file not found:", filepath)
        sys.exit(1)
    
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}

    with open(filepath, 'r') as f:
        for line in f:
            for level in counts:
                if level in line:
                    counts[level] += 1
                    
    print("=================")
    print("Log Summary:", filepath)
    for level, count in counts.items():
        print(f"{level}: {count}")
    print("=================")

if len(sys.argv) != 2:
    print("Usage: python log_summary.py <logfile>")
    sys.exit(1)

summarise_log(sys.argv[1])

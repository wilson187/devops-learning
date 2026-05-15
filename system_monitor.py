# System monitor - Real machine metrics
# Uses psutil to get real CPU usage data and generates a report on server health.

from os import times

import psutil
from datetime import datetime

def get_cpu():
    cpu = psutil.cpu_percent(interval=1)
    return cpu

def get_memory():
    memory = psutil.virtual_memory()
    total_gb = round(memory.total / (1024 ** 3), 2)
    used_gb = round(memory.used / (1024 ** 3), 2)
    percent = memory.percent
    return percent, used_gb, total_gb

def get_disk():
    disk = psutil.disk_usage('/')
    total_gb = round(disk.total / (1024 ** 3), 2)
    used_gb = round(disk.used / (1024 ** 3), 2)
    free_gb = round(disk.free / (1024 ** 3), 2)
    percent = disk.percent
    return percent, used_gb, total_gb, free_gb

def get_timestamp():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def check_status(value, warning_threshold, critical_threshold):
    if value >= critical_threshold:
        return "CRITICAL"
    elif value >= warning_threshold:
        return "WARNING"
    else:
        return "OK"
    


# Get real metrics
cpu = get_cpu()
memory_percent, memory_used, memory_total = get_memory()
disk_percent, disk_used, disk_total, disk_free = get_disk()
timestamp = get_timestamp()

# Check status of each metric
cpu_status = check_status(cpu, 75, 90)
memory_status = check_status(memory_percent, 75, 90)
disk_status = check_status(disk_percent , 75, 90)

# Print report
print("=============")
print("System health check report")
print("Generated at:", timestamp)
print("=============")

print("")
print("CPU Usage:", cpu, "%")
print("Status:", cpu_status)

print("")
print("Memory Usage:", memory_percent, "%")
print("Used:", memory_used, "GB /", memory_total, "GB")
print("Status:", memory_status)

print("")
print("Disk Usage:", disk_percent, "%")
print("Used:", disk_used, "GB /", disk_total, "GB")
print("Free:", disk_free, "GB")
print("Status:", disk_status)

print("")
print("=============")
print("Report complete.")
# System monitor - Real machine metrics
# Uses psutil to get real CPU usage data and generates a report on server health.

import psutil

def get_cpu():
    cpu = psutil.cpu_percent(interval=1)
    return cpu

def get_memory():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk():
    disk = psutil.disk_usage('/')
    return disk.percent

def check_status(value, warning_threshold, critical_threshold):
    if value >= critical_threshold:
        return "CRITICAL"
    elif value >= warning_threshold:
        return "WARNING"
    else:
        return "OK"
    
def print_metric(name, value, status):
    print("")
    print(name + ":", value, "%")
    print("Status:", status)

# Get real metrics
cpu = get_cpu()
memory = get_memory()
disk = get_disk()

# Check status of each metric
cpu_status = check_status(cpu, 75, 90)
memory_status = check_status(memory, 75, 90)
disk_status = check_status(disk, 75, 90)

# Print report
print("=============")
print("System health check report")
print("=============")

print_metric("CPU Usage", cpu, cpu_status)
print_metric("Memory Usage", memory, memory_status)
print_metric("Disk Usage", disk, disk_status)

print("")
print("=============")
print("Report complete.")
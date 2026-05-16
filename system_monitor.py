# System monitor - Real machine metrics
# Uses psutil to get real CPU usage data and generates a report on server health.


import psutil
import time
import json
import os
import argparse
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser(description="System Monitor - Real machine metrics")
    parser.add_argument("--interval", type=int, default=10, help="Interval in seconds between checks")
    parser.add_argument("--cpu-warning", type=int, default=75, help="CPU usage percentage to trigger warning")
    parser.add_argument("--cpu-critical", type=int, default=90, help="CPU usage percentage to trigger critical alert")
    parser.add_argument("--memory-warning", type=int, default=80, help="Memory usage percentage to trigger warning")
    parser.add_argument("--memory-critical", type=int, default=90, help="Memory usage percentage to trigger critical alert")
    parser.add_argument("--disk-warning", type=int, default=80, help="Disk usage percentage to trigger warning")
    parser.add_argument("--disk-critical", type=int, default=90, help="Disk usage percentage to trigger critical alert")
    parser.add_argument("--log-file", type=str, default="monitor.log", help="File to save logs")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")
    return parser.parse_args()

def load_config():
    if os.path.exists("config.json"):
        with open("config.json") as f:
            return json.load(f)
    else:
        print("No config file found. Using default settings.")
        return {
            "check_interval": 10,
            "cpu_warning": 75,
            "cpu_critical": 90,
            "memory_warning": 80,
            "memory_critical": 90,
            "disk_warning": 80,
            "disk_critical": 90,
            "log_file": "monitor.log"
        }

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

def write_log(timestamp, cpu, cpu_status, memory_percent, memory_used, memory_total, memory_status, disk_percent, disk_used, disk_total, disk_free, disk_status, network_sent, network_recv):
    with open(log_file, "a") as f:
        f.write("\n")
        f.write("=============\n")
        f.write("System health check report\n")
        f.write("Generated at: " + timestamp + "\n")
        f.write("=============\n")
        f.write("\n")
        f.write("CPU Usage: " + str(cpu) + "%\n")
        f.write("Status: " + cpu_status + "\n")
        f.write("\n")
        f.write("Memory Usage: " + str(memory_percent) + "%\n")
        f.write("Used: " + str(memory_used) + " GB / " + str(memory_total) + " GB\n")
        f.write("Status: " + memory_status + "\n")
        f.write("\n")
        f.write("Disk Usage: " + str(disk_percent) + "%\n")
        f.write("Used: " + str(disk_used) + " GB / " + str(disk_total) + " GB\n")
        f.write("Free: " + str(disk_free) + " GB\n")
        f.write("Status: " + disk_status + "\n")
        f.write("\n")
        f.write("Network Sent: " + str(network_sent) + " MB\n")
        f.write("Network Received: " + str(network_recv) + " MB\n")
        f.write("Report complete.\n")
    
    print("Log saved to " + log_file)

def check_status(value, warning_threshold, critical_threshold):
    if value >= critical_threshold:
        return "CRITICAL"
    elif value >= warning_threshold:
        return "WARNING"
    else:
        return "OK"

def get_network():
    net = psutil.net_io_counters()
    bytes_sent = round(net.bytes_sent / (1024 ** 2), 2)
    bytes_recv = round(net.bytes_recv / (1024 ** 2), 2)
    return bytes_sent, bytes_recv


# How often to run the monitor (every 60 seconds)
check_interval = 10

print("=============")
print("Starting system monitor...")
print("Press Ctrl+C to stop.")
print("=============")

# Load config settings
config = load_config()
check_interval = config["check_interval"]
log_file = config["log_file"]
args = parse_args()

# Override config values with command-line arguments if provided
check_interval = args.interval if args.interval else config["check_interval"]
log_file = args.log_file if args.log_file else config["log_file"]

while True:
    try:
        # Get real metrics
        cpu = get_cpu()
        memory_percent, memory_used, memory_total = get_memory()
        disk_percent, disk_used, disk_total, disk_free = get_disk()
        network_sent, network_recv = get_network()
        timestamp = get_timestamp()

        # Check status of each metric
        cpu_status = check_status(cpu, config["cpu_warning"], config["cpu_critical"])
        memory_status = check_status(memory_percent, config["memory_warning"], config["memory_critical"])
        disk_status = check_status(disk_percent, config["disk_warning"], config["disk_critical"])

        # Check if any metric is critical and print alert
        if cpu_status == "CRITICAL":
            print("ALERT: CPU usage is critical at", cpu, "%")
        if memory_status == "CRITICAL":
            print("ALERT: Memory usage is critical at", memory_percent, "%")
        if disk_status == "CRITICAL":
            print("ALERT: Disk usage is critical at", disk_percent, "%")

        # Print report
        print("=============")
        print("System health check report")
        print("Generated at:", timestamp)
        print("=============")

        print("")
        print("CPU Usage:", cpu, "%")
        print("Status:", cpu_status)

        if args.verbose:
            print("Core count:", psutil.cpu_count())
            boot_time = datetime.fromtimestamp(psutil.boot_time())
            print("Boot time:", boot_time.strftime("%Y-%m-%d %H:%M:%S"))

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
        print("Network Sent:", network_sent, "MB")
        print("Network Received:", network_recv, "MB")

        # Write log to file
        write_log(timestamp, cpu, cpu_status,  
                  memory_percent, memory_used, memory_total, memory_status, 
                  disk_percent, disk_used, disk_total, disk_free, disk_status, network_sent, network_recv)
        
        
        print("")
        print("Next check in", check_interval, "seconds...")
        time.sleep(check_interval)

        


    except KeyboardInterrupt:
        print("")
        print("System monitor stopped.")
        break

    except Exception as e:
        print("An error occurred:", str(e))
        print("Continuing to next check...")
        time.sleep(check_interval)

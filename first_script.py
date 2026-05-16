import json
import os

# Counters to track status totals
ok_count = 0
warning_count = 0
critical_count = 0

def load_servers(filename):
    if os.path.exists(filename):
        with open(filename) as f:
            return json.load(f)
    else:
        print("Error: File not found:", filename)
        return {}

def get_worse_server(servers):
    worst_server = None
    worst_cpu = -1
    for server, cpu in servers.items():
        if cpu > worst_cpu:
            worst_cpu = cpu
            worst_server = server
    return worst_server, worst_cpu

def check_server(server, cpu):
    global ok_count, warning_count, critical_count

    print("")
    print("Server:", server)
    print("CPU Usage:", cpu, "%")
    if cpu >= 90:
        print("CRITICAL: CPU usage is very high!")
        critical_count += 1
    elif cpu >= 70:
        print("WARNING: CPU usage is high.")
        warning_count += 1
    else:        
        print("CPU usage is normal.")
        ok_count += 1

# Load server data from JSON file
servers = load_servers("servers.json")

if servers:
    print("=============")  
    print("Server health check report")
    print("=============")


    for server, cpu in servers.items():
        check_server(server, cpu)
    
    worst_server, worst_cpu = get_worse_server(servers)
    print("Most critical server:", worst_server, "with CPU usage of", worst_cpu, "%")


print("")
print("=============")
print("Summary:")
print("OK:", ok_count)
print("WARNING:", warning_count)
print("CRITICAL:", critical_count)
print("=============")
print("Report complete. All servers checked.")


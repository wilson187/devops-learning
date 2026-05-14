# My first DevOps script

# Step 1 - Store some information
server_name = "web-01"
server_status = "online"
cpu_usage = 45

# Step 2 - Print a status report
print("Server Name:", server_name)
print("Server Status:", server_status)
print("CPU Usage:", cpu_usage, "%")

# Step 3 - Make a decision based on CPU usage
if cpu_usage >= 90:
    print("CRITICAL: CPU usage is very high!")
elif cpu_usage >= 70:
    print("WARNING: CPU usage is high.")
else:
    print("CPU usage is normal.")

#  Step 4 - Check multiple servers
print("")
print("Checking all servers...")
print("-----------------------")

servers = ["web-01", "web-02", "db-01", "db-02"]
cpu_usages = [45, 85, 30, 95]
for server, cpu in zip(servers, cpu_usages):
    print("Checking:", server, "CPU Usage:", cpu, "%")
    if cpu >= 90:
        print("CRITICAL: CPU usage is very high!")
    elif cpu >= 70:
        print("WARNING: CPU usage is high.")
    else:
        print("CPU usage is normal.")

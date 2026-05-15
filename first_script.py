servers = {"web-01": 45, "web-02": 85, "db-01": 30, "db-02": 95}

# Counters to track status totals
ok_count = 0
warning_count = 0
critical_count = 0

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

print("Server health check report")
print("=============")


for server, cpu in servers.items():
    check_server(server, cpu)

print("")
print("=============")
print("Summary:")
print("OK:", ok_count)
print("WARNING:", warning_count)
print("CRITICAL:", critical_count)
print("=============")
print("Report complete. All servers checked.")


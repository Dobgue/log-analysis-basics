# parse_logs.py

failed_logins = {}

with open("sample-logs/auth.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = line.split("from")[1].split()[0]
            failed_logins[ip] = failed_logins.get(ip, 0) + 1

# Display IPs with more than 3 failed attempts
print("Suspicious IPs:")
for ip, count in failed_logins.items():
    if count > 3:
        print(f"{ip} => {count} failed login attempts")

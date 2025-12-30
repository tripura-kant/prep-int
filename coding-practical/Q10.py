# Q10. Detect Possible Brute Force IPs
# Task: Find IPs that accessed the /login endpoint more than 100 times in a day.

log_file = "/Users/tripurakant/Documents/code/My_git/prep-int/coding-practical/access.log"

ref_count = {}

with open(log_file) as f:
    for line in f:
        parts = line.split()
        ip = parts[0]
        # print(ip)
        endpoint = parts[6]
        if endpoint == "/login":
            print(f'ip is {ip} : endpoint is {endpoint}')
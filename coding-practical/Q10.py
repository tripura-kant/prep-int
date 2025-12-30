# Q10. Detect Possible Brute Force IPs
# Task: Find IPs that accessed the /login endpoint more than 100 times in a day.

log_file = "/Users/tripurakant/Documents/code/My_git/prep-int/coding-practical/ref.log"

ref_count = {}

with open(log_file) as f:
    for line in f:
        parts = line.split()
        ip = parts[9]
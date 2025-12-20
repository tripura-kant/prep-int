# Q5. Extract Timestamp and Group Requests Per Minute
# Task: Extract timestamps and count number of requests per minute.

with open("access.log") as f:
    for line in f:
        parts = line.split()
        if len(parts) < 9:
            continue

        status = parts[8]

        if status.startswith("5"):
            print(line.strip())
# Q5. Extract Timestamp and Group Requests Per Minute
# Task: Extract timestamps and count number of requests per minute.
# 192.168.1.10 - - [24/May/2025:10:21:10 +0000] "GET /home HTTP/1.1" 200 4096

minute_count={}

with open("access.log") as f:
    for line in f:
        parts = line.split()
        if len(parts) < 4:
            continue
        time=parts[3]
        # print(time)
        time_stamp=time[1:18]
        # print(time_stamp)
        if min_count in minute_count:
            minute_count[min_count] += 1
        else:
            minute_count[min_count] = 1

        print(minute_count)
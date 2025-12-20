# “Which IPs are causing the most 5xx errors?”
# 192.168.1.10 - - [24/May/2025:10:21:10 +0000] "GET /home HTTP/1.1" 200 4096

log_file="access.log"
error_count={}

with open(log_file) as f:
    for line in f:
        parts = line.split()
        status = parts[8]
        ip = parts[0]       
        if status.startswith("5"):
            if ip in error_count:
                error_count[ip] +=1
            else:
                error_count[ip] = 1
for ip,count in error_count.items():
    print(ip)
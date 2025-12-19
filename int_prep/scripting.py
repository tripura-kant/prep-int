# Top 10 Ips by frequency

# ip_count = {}

# with open("access.log") as f:
#     for line in f:
#         parts = line.split()

#         ip = parts[0]
#         # print(ip)   
#         if ip in ip_count:
#             ip_count[ip] = ip_count[ip] + 1
#         else:
#             ip_count[ip] = 1

# sorted_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)            
# print(sorted_ips[:10])                

# Q2. Filter Requests with 5xx Status Codes
# Task: Extract all lines where the HTTP status code is in the 5xx range.
# ips = []
# with open("access.log") as f:
# #     for line in f:
# #         parts = line.split()
# #         status = parts[8]

# #         if status >= "500":
# #             print(line)      

# # Q3. Unique IP Count

#     for line in f:
#         ip = line.split()[0]
#         # print(ip)?
#         if ip not in ips:
#             ips.append(ip)
#     print(len(ip))           

# Q4. Count URL Paths
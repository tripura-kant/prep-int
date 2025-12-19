# """
# # if-else

# status = 200

# if status >= 500:
#     print("server error")
# elif status >= 400:
#     print("client error")
# else:
#     print("not found")        


# for loop

# for item in items:
#     print(item)   

# # aws ec2 describe-instance-status --instance-ids i-0a12bc34def567890


# with open("ec2.log") as f:
#     for line in f:
#         print(line)

with open("ec2.log") as f:
    for line in f:
        instance_id = line.strip()

        print(
            f"aws ec2 describe-instance-status --instance-ids {instance_id}"
        )



# count = 0
# while count < 30:
#     print(count, end=" ")
#     count += 1



# from collections import defaultdict

# ip_count = defaultdict(int)
# with open("access.log") as f:
#     for line in f:
#         parts = line.split()
#         if not parts:
#             continue
#         ip = parts[0]
#         ip_count[ip] += 1
#     print(ip_count)
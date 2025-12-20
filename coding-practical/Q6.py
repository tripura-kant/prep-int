# Q6. Extract and Count User Agents
# Extended Log:
#  203.0.113.42 - - [24/May/2025:10:22:15 +0000] "GET /api/user/profile HTTP/1.1" 200 350 "-" "Mozilla/5.0"
#  Task: Count the top 5 most common user agents.


count_agents = {}

with open("access.log") as f:
    for line in f:
        parts = line.split()
        user_agent = parts[11]
        if len(user_agent) < 12:
            continue
        print(user_agent)
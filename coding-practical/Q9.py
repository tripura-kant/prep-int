'''
Q9. Extract Top 10 Referrers
Log:
 "GET /home HTTP/1.1" 200 1024 "https://google.com/search?q=..." "Mozilla/5.0"
 Task: Extract the referrer field and show the top 10 sources.
'''

log_file = "/Users/tripurakant/Documents/code/My_git/prep-int/coding-practical/ref.log"

ref_count = {}

with open(log_file) as f:
    for line in f:
        parts = line.split('"')

        # referrer exists only in combined logs
        if len(parts) >= 5:
            referrer = parts[3]

            if referrer == "-" or referrer == "":
                continue

            ref_count[referrer] = ref_count.get(referrer, 0) + 1

# Sort and take top 10
top_10 = sorted(ref_count.items(), key=lambda x: x[1], reverse=True)[:10]

print("Top 10 Referrers:")
for ref, count in top_10:
    print(ref, count)

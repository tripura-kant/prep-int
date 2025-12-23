import json
my_tools={
    "container" : "dpcker",
    "prod" : False
}

# jsonData='{"container": "docker", "prod": "false"}'

# # print(json.dumps(my_tools))
# print(json.loads(jsonData))

with open("demo.json", "w") as fo:
    json.dump(my_tools, fo, indent=4)
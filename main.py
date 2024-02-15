import json


with open('new_data.json', 'r', encoding='utf-8') as file:
    original_json = file.read()

# Parse original JSON
data = json.loads(original_json)

# iterate all items in containers_list
formatted_data_list = []

for container in data['containers_list']:

    if isinstance(container["comment"], list):
        tags = [comment.strip(" -") for comment in container["comment"][:-1]]
    else:
        tags = container["comment"]
    # Reformatting into the desired structure for each container
    formatted_data = {
        "address": container["location"]["address"],
        "location": container["location"]["pos"].split(","),
        # условие для tag соответствует только случаю когда в значении передан список
        "tags": tags,
        "types": {
            "wastepaper": ["wastepaper"],
            "plastik": [key for key, value in container["type_container"]["plastik"].items() if value],
            "penoplast": ["penoplast"],
        },
        "site": container["site"],
        "dest": container["location"]["dest"]
    }
    formatted_data_list.append(formatted_data)

# Output the formatted data as JSON
with open('formatted_data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(formatted_data_list, ensure_ascii=False, indent=4))

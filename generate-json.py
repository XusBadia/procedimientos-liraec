import json
from bson import ObjectId

# Function to add ObjectId to each object
def add_object_id(obj):
    obj['_id'] = {'$oid': str(ObjectId())}
    return obj

# Read the original JSON file
with open('v1/procedimientos_liraec.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Add ObjectId to each object in the list
modified_data = [add_object_id(obj) for obj in data]

# Write the modified data to a new JSON file
with open('procedimientos_liraec.json', 'w', encoding='utf-8') as file:
    json.dump(modified_data, file, ensure_ascii=False, indent=2)

print("New JSON file with ObjectIds has been created: procedimientos_liraec_with_id.json")

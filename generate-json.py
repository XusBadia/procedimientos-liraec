import pandas as pd
import json
from bson import ObjectId

# Function to add ObjectId to each object
def add_object_id(obj):
    obj['_id'] = {'$oid': str(ObjectId())}
    return obj

# Function to convert Excel to JSON with ObjectIds
def excel_to_json_with_objectid(excel_file, json_file):
    # Read the Excel file
    df = pd.read_excel(excel_file)

    # Convert DataFrame to list of dictionaries
    data = df.to_dict('records')

    # Add ObjectId to each object
    for item in data:
        item = add_object_id(item)

    # Write the data to a JSON file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"JSON file with ObjectIds has been created: {json_file}")

# Use the function
excel_to_json_with_objectid('procedimientos_liraec.xlsx', 'procedimientos_liraec.json')

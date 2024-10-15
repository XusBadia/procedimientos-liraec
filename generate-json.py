import pandas as pd
from bson import ObjectId
import json

def generate_json_from_excel():
    # Read the Excel file
    df = pd.read_excel('procedimientos_liraec.xlsx')
    
    # Drop the 'hide' column if it exists
    if 'hide' in df.columns:
        df = df.drop(columns=['hide'])

    # Replace NaN values with empty strings
    df = df.fillna('')

    # Convert DataFrame to list of dictionaries
    data = df.to_dict('records')

    # Add ObjectId to each row and process 'especialidad', 'sinonimos', 'subespecialidad', and 'cieId'
    for item in data:
        item['_id'] = {"$oid": str(ObjectId())}
        
        for field in ['especialidad', 'sinonimos', 'subespecialidad']:
            if field in item and isinstance(item[field], str):
                # Split by comma, strip whitespace, and filter out empty strings
                values = [value.strip() for value in item[field].split(',') if value.strip()]
                item[field] = values if values else []
            else:
                item[field] = []
        
        # Convert 'cieId' to string
        if 'cieId' in item:
            item['cieId'] = str(item['cieId'])

    # Write to JSON file
    with open('procedimientos_liraec.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("JSON file 'procedimientos_liraec.json' has been generated successfully.")

if __name__ == "__main__":
    generate_json_from_excel()

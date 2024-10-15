import pandas as pd
# from bson import ObjectId  # This import is no longer needed
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

    # Process each row
    for item in data:
        # Use the '_id' from the Excel file instead of generating a new ObjectId
        if '_id' in item:
            item['_id'] = {"$oid": str(item['_id'])}
        else:
            # If '_id' is not present in the Excel, you might want to handle this case
            print(f"Warning: No '_id' found for item: {item}")
        
        # The rest of the processing remains the same
        for field in ['especialidad', 'sinonimos', 'subespecialidad']:
            if field in item and isinstance(item[field], str):
                # Split by comma, strip whitespace, and filter out empty strings
                values = [value.strip() for value in item[field].split(',') if value.strip()]
                item[field] = values if values else []
            else:
                item[field] = []
        
        # Handle 'cieId' as a string, preserving the exact representation from Excel
        if 'cieId' in item and pd.notna(item['cieId']):
            item['cieId'] = str(item['cieId']).strip()
        else:
            item['cieId'] = ''

    # Write to JSON file
    with open('procedimientos_liraec.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("JSON file 'procedimientos_liraec.json' has been generated successfully.")

if __name__ == "__main__":
    generate_json_from_excel()

# Previous ObjectId generation (commented out):
# item['_id'] = {"$oid": str(ObjectId())}

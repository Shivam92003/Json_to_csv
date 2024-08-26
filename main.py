import json
import csv
import os

# Function to get JSON data from a file
def get_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to write data to a CSV file
def write_csv(data, csv_file_path):
    # Get the keys (column names) from the first JSON object
    keys = data[0].keys()

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)

        # Write header
        dict_writer.writeheader()

        # Write rows
        for row in data:
            # Process multiline fields to replace newline characters with a space
            for key, value in row.items():
                if isinstance(value, str):
                    row[key] = value.replace('\n', ' ').replace('\r', ' ')
                elif isinstance(value, list):
                    row[key] = [v.replace('\n', ' ').replace('\r', ' ') if isinstance(v, str) else v for v in value]
            dict_writer.writerow(row)

# Directory containing JSON files
json_directory = r'C:\Users\SHIVAM RAWAT\OneDrive\Desktop\insignia\JD_for_Testing'

# CSV output file path
csv_file_path = r'C:\Users\SHIVAM RAWAT\OneDrive\Desktop\insignia\JD_for_Testing\output.csv'

# List to hold all JSON data
all_data = []

# Loop through all JSON files in the directory
for file_name in os.listdir(json_directory):
    if file_name.endswith('.json'):
        file_path = os.path.join(json_directory, file_name)
        json_data = get_json_data(file_path)
        if isinstance(json_data, list):
            all_data.extend(json_data)  # If JSON file contains a list of dictionaries
        else:
            all_data.append(json_data)  # If JSON file contains a single dictionary

# Write all collected data to the CSV file
if all_data:
    write_csv(all_data, csv_file_path)
    print(f"Data from JSON files has been written to {csv_file_path}")
else:
    print("No data to write.")

import os
import json

# Define the input folder path
input_folder = 'C:\Users\Talha098\Downloads\sampleJson'

# Create a dictionary to store the combined data
combined_data = {}

# Loop through all the JSON files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(input_folder, filename)

        # Read the input JSON file
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Get the filename without the extension (e.g., "Pos_0.png")
        base_filename = os.path.splitext(filename)[0]

        # Update the class names
        if 'class' in data:
            if data['class'] == 'vehicle':
                data['class'] = 'car'
            elif data['class'] == 'license plate':
                data['class'] = 'number'

        # Add the data to the combined dictionary
        combined_data[base_filename] = data

# Define the output file path for the combined JSON file
output_file_path = 'C:\Users\Talha098\Downloads\Output_json'

# Write the combined JSON data to the output file
with open(output_file_path, 'w') as f:
    json.dump(combined_data, f, indent=4)

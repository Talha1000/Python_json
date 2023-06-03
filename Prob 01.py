import os
import json

# Define the input and output folder paths
input_folder = 'C:\Users\Talha098\Downloads\sampleJson'
output_folder = 'C:\Users\Talha098\Downloads\Output_json'

# Loop through all the JSON files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, 'formatted_' + filename)

        # Read the input JSON file
        with open(input_file_path, 'r') as f:
            data = json.load(f)

        # Check if 'class' key is present
        if 'class' in data:
            # Create a new dictionary for the formatted JSON
            formatted_data = {}

            # Set the 'class' key to the value from the input JSON
            formatted_data['class'] = data['class']

            # Check if 'vehicle' key is present
            if 'vehicle' in data:
                # Set the 'presence' key to 'true'
                formatted_data['presence'] = 'true'
            elif 'license plate' in data:
                # Set the 'presence' key to 'false'
                formatted_data['presence'] = 'false'

            # Write the formatted JSON to the output file
            with open(output_file_path, 'w') as f:
                json.dump(formatted_data, f, indent=4)
        else:
            # If both 'vehicle' and 'license plate' keys are missing, copy the file as it is
            os.rename(input_file_path, output_file_path)

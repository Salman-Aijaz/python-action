import pandas as pd
import sys
import os

def csv_to_json(csv_file, json_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Convert to JSON and save
    df.to_json(json_file, orient='records', lines=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv_to_json.py <input_csv_file> <output_json_file>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_json = sys.argv[2]

    if not os.path.exists(input_csv):
        print(f"The file {input_csv} does not exist.")
        sys.exit(1)

    csv_to_json(input_csv, output_json)
    print(f"Converted {input_csv} to {output_json}.")
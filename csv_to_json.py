import pandas as pd
import sys
import os
import json

def csv_to_json(csv_file, json_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Convert to JSON and save
    df.to_json(json_file, orient='records', lines=True)

def generate_html(json_file, html_file):
    with open(json_file) as f:
        data = json.load(f)

    # HTML content
    html_content = """
    <html>
    <head>
        <title>CSV to JSON</title>
    </head>
    <body>
        <h1>CSV to JSON Data</h1>
        <pre>{}</pre>
    </body>
    </html>
    """.format(json.dumps(data, indent=4))

    with open(html_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv_to_json.py <input_csv_file> <output_json_file>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_json = sys.argv[2]
    
    output_html = "output/index.html"

    if not os.path.exists(input_csv):
        print(f"The file {input_csv} does not exist.")
        sys.exit(1)

    # Convert CSV to JSON
    csv_to_json(input_csv, output_json)
    print(f"Converted {input_csv} to {output_json}.")
    
    # Generate HTML
    generate_html(output_json, output_html)
    print(f"Generated HTML file at {output_html}.")

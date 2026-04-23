import json
import csv

# Step 1: Convert JSON to CSV
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

with open('data.csv', 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

print("JSON data successfully converted to CSV.")

# Step 2: Count rows in CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    row_count = 0

    for row in reader:
        row_count += 1

print("Total number of rows in the CSV file:", row_count)

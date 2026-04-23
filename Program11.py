# Step 1: Write data to file
with open("sample.txt", "w") as file:
    file.write("Hello, this is the first line in the file.\n")
    file.write("File handling in Python is easy to learn.\n")

print("Data written successfully.\n")

# Step 2: Read file
with open("sample.txt", "r") as file:
    print("Reading file contents:")
    print(file.read())

# Step 3: Append more data
with open("sample.txt", "a") as file:
    file.write("This line is added using append mode.\n")

print("\nData appended successfully.\n")

# Step 4: Read updated content
with open("sample.txt", "r") as file:
    print("Updated file contents:")
    print(file.read())

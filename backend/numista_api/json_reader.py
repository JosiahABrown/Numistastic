import json
import os

# Set the path to the directory containing the JSON files
path = "./coin_json"

# Initialize empty lists to store the filenames
years_filenames = []
details_filenames = []

# Use os.listdir() to get a list of all files in the directory
for file in os.listdir(path):
    # Use os.path.join() to get the full path of each file
    file_path = os.path.join(path, file)

    # Check if the file is a regular file (not a directory or symbolic link, etc.)
    if os.path.isfile(file_path):
        # Check if the filename ends with _years.json
        if file.endswith("_years.json"):
            # Add the filename to the years_filenames list
            years_filenames.append(file)
        # Check if the filename ends with _details.json
        elif file.endswith("_details.json"):
            # Add the filename to the details_filenames list
            details_filenames.append(file)

# Prepend path 
details_filenames = [f"{path}/" + filename for filename in details_filenames]

# Print the lists of filenames
#print("Years filenames:", years_filenames)
#print("Details filenames:", details_filenames)

us_coin_details = []

for filename in details_filenames:
    with open(filename, 'r') as f:
        data = json.load(f)

    # Check if the "title" key exists in the file and extract the value if it does
    if "title" in data:
        title = data["title"]
    else:
        title = None

    # Check if the "min_year" key exists in the file and extract the value if it does
    if "min_year" in data:
        min_year = data["min_year"]
    else:
        min_year = None

    # Check if the "max_year" key exists in the file and extract the value if it does
    if "max_year" in data:
        max_year = data["max_year"]
    else:
        max_year = None

    # Check if the "composition" and "text" keys exist in the file and extract the value if they do
    if "composition" in data and "text" in data["composition"]:
        composition = data["composition"]["text"]
    else:
        composition = None

    # Check if the "comments" key exists in the file and extract the value if it does
    if "comments" in data:
        comments = data["comments"]
    else:
        comments = None

    # Append the values to a list
    us_coin_details.append([title, min_year, max_year, composition, comments])

for el in us_coin_details:
    print(el)
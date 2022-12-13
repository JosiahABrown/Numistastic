import json
import os
import re

# Set the path to the directory containing the JSON files
path = "./coin_json"

# Initialize empty lists to store the filenames
years_filenames = []
details_filenames = []

# Use os.listdir() to get a list of all files in the directory
for file in os.listdir(path):
    # Use os.path.join() to get the full path of each file
    file_path = os.path.join(path, file)

    # Check if the file is a regular file
    # (not a directory or symbolic link, etc.)
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
years_filenames = [f"{path}/" + filename for filename in years_filenames]

us_coin_details = []

for filename in details_filenames:
    with open(filename, 'r') as f:
        data = json.load(f)

    # Check if the "id" key exists and extract
    if "id" in data:
        numista_id = data["id"]
    else:
        numista_id = None

    # Check if the "title" key exists in the file
    if "title" in data:
        title = data["title"]
    else:
        title = None

    # Check if the "min_year" key exists in the file
    if "min_year" in data:
        min_year = data["min_year"]
    else:
        min_year = None

    # Check if the "max_year" key exists in the file
    if "max_year" in data:
        max_year = data["max_year"]
    else:
        max_year = None

    # Check if the "composition" and "text" keys exist
    if "composition" in data and "text" in data["composition"]:
        composition = data["composition"]["text"]
    else:
        composition = None

    # Check if the "comments" key exists in the file
    if "comments" in data:
        comments = data["comments"]
    else:
        comments = None

    # Append the values to a list
    us_coin_details.append([title, min_year, max_year, composition, comments])

# Print out each element
# for el in us_coin_details:
#     print(el)

# write us_coin_details to file
with open('coin_txt/us_coin_details.txt', 'w') as f:
    for coin in us_coin_details:
        f.write(f"{coin}\n")

# Regex to find the numbers in file name
pattern = re.compile(fr"{path}/(\d+)_years\.json")

us_coin_years = []

for filename in years_filenames:
    match = pattern.search(filename)

    # extract numbers in file Name
    coin_id = match.group(1)

    # load json
    with open(filename, 'r') as f:
        data = json.load(f)

    # loop through years
    for years in data:
        if "id" in years:
            numista_id = years["id"]
        else:
            numista_id = None

        if "year" in years:
            year = years["year"]
        else:
            year = None

        if "mint_letter" in years:
            mint_letter = years["mint_letter"]
        else:
            mint_letter = None

        if "mintage" in years:
            mintage = years["mintage"]
        else:
            mintage = None

        if "comment" in years:
            comment = years["comment"]
        else:
            comment = None

        us_coin_years.append([
            int(coin_id),
            numista_id,
            year,
            mint_letter,
            mintage,
            comment])

# for el in us_coin_years:
#     print(el)

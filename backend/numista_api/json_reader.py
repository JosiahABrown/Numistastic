import json
import os
import re

import html as ihtml
from bs4 import BeautifulSoup

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
    if os.path.isfile(file_path):
        # Check if the filename ends with _years.json
        if file.endswith("_years.json"):
            years_filenames.append(file)
        # Check if the filename ends with _details.json
        elif file.endswith("_details.json"):
            details_filenames.append(file)

# Prepend path
details_filenames = [f"{path}/" + filename for filename in details_filenames]
years_filenames = [f"{path}/" + filename for filename in years_filenames]

# Add values to a sql file 
def add_details_to_sql_file(file_path, *values):
     with open(file_path, 'a') as f:
        f.write(f"VALUES ({values[0]}, '{values[1]}', '{values[2]}', '{values[3]}', '{values[4]}');\n")

# Check if "term" exists in file
def extract_json(term, file, comment=False):
    term = str(term)
    if term in file:
        value = file[term]
        # Remove escape characters
        if "\"" in term or "\'" in term:
            value = term.replace("\"", "").replace("\'", "")
    else:
        value = "NULL"
    return value

# Remove HTML tags
def clean_text(text):
    text = BeautifulSoup(ihtml.unescape(text), features="html.parser").text
    text = re.sub(r"http[s]?://\S+", "", text)
    text = re.sub(r"\s+", " ", text)    
    text = re.sub(r"'", "''", text)
    return text


def coin_details():
    index = 1
    for filename in details_filenames:
        with open(filename, 'r') as f:
            data = json.load(f)

        numista_id = extract_json("id", data)
        title = extract_json("title", data)
        min_year = extract_json("min_year", data)
        max_year = extract_json("max_year", data)

        # Check if the "composition" and "text" keys exist
        if "composition" in data and "text" in data["composition"]:
            composition = data["composition"]["text"]
        else:
            composition = "NULL"

        if "comments" in data:
            comments = clean_text(data["comments"])
        else:
            comments = "NULL"

        # convert min and max years to single string
        years = f"{str(min_year)} - {str(max_year)}"

        # write us_coin_details to file
        file = '../sql_files/us_coin_details.sql'
        add_details_to_sql_file(file, numista_id, title, years, composition, comments)
        index += 1
        
    print(index)


def coin_years():
    # Regex to find the numbers in file name
    pattern = re.compile(fr"{path}/(\d+)_years\.json")
    file_path = '../sql_files/us_coin_years.sql'

    for filename in years_filenames:
        match = pattern.search(filename)

        # extract numbers in file Name
        coin_id = match.group(1)

        # load json
        with open(filename, 'r') as f:
            data = json.load(f)

        # loop through years
        for years in data:
            numista_id = extract_json("id", years)
            year = extract_json("year", years)
            mintage = extract_json("mintage", years)
            mint_letter = extract_json("mint_letter", years)
            comment = extract_json("comment", years)
            
            with open(file_path, 'a') as f:
                f.write(f"INSERT INTO us_coin_years (coin_id, numista_id, year, mintage, mint_letter, description) VALUES ({int(coin_id)}, {numista_id}, {year}, {mintage}, '{mint_letter}', '{comment}');\n")


def main():
    # coin_details()
    coin_years()


main()

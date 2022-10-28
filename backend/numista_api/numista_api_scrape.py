import requests
import json
import os
from dotenv import load_dotenv

# ============== Environmental variables ==============
ENDPOINT = 'https://api.numista.com/api/v3'
load_dotenv()
# Numista provided API Key & Client ID
API_KEY = os.getenv('API_KEY')
CLIENT_ID = os.getenv('CLIENT_ID')
ex = os.path.exists
size = os.path.getsize


# ============== Write to db init file ==============
def write_to_file(line):
    FILE = 'db_init.txt'

    # Check if file exits
    file_exists = ex(FILE)
    if file_exists is False:
        open(FILE, 'a').close()

    if size(FILE) == 0:
        with open(FILE, 'a') as f:
            f.write(f'{line}')
    else:
        with open(FILE, 'a') as f:
            f.write(f'\n{line}')


# ============== Get the details on a type of coin ==============
def type_details(type_id):
    response = requests.get(
            ENDPOINT + '/types/' + type_id,
            params={'lang': 'en'},
            headers={'Numista-API-Key': API_KEY})
    coin_details = response.json()

    with open(f'coin_json/{type_id}_details.json', 'w') as f:
        json.dump(coin_details, f, ensure_ascii=False, indent=4)

    # title = coin_details['title']
    # issuer = coin_details['issuer']['name']
    # composition = coin_details['composition']['text']

    # line = f'("{title}", "{issuer}", "", "", "{composition}", "", "")'
    # write_to_file(line)
    # print(f"\n== Details about the type #{type_id} ==")
    # print(f"URL: {coin_details['url']}")
    # print(f"Title: {coin_details['title']}")
    # print(f"Issuer: {coin_details['issuer']['name']}")
    # print(f"Years: {coin_details['min_year']} - {coin_details['max_year']}")
    # print(f"Composition: {coin_details['composition']['text']} \n")


# ==============  Get each year, including year variations, of a type of coin ==============
def type_years(type_id):
    response = requests.get(
            ENDPOINT + "/types/" + type_id + '/issues',
            params={'lang': 'en'},
            headers={'Numista-API-Key': API_KEY})
    years = response.json()

    with open(f'coin_json/{type_id}_years.json', 'w') as f:
        json.dump(years, f, ensure_ascii=False, indent=4)

    # print('== Years ==')
    # for coin in years:
    #     if "mintage" in coin:
    #         print(f"{coin['year']} {coin['mintage']}")
    #     else:
    #         print(f"{coin['year']} ----")
    # print()


# ==============  Takes file input and indents it to be readable ==============
def format_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        coins = json.load(f)
        coins = json.dumps(coins, indent=4)

    print(coins)
    print(f"\n\n\n{type(coins)}")


# Coin number list
with open('US_dollar_1785-date_CoinID.txt') as file:
    coin_IDs = [line.rstrip() for line in file]

if __name__ == '__main__':
    for id in coin_IDs:
        type_details(id)
        type_years(id)
    # file_input = input('What JSON file to format?: ')
    # format_json(file_input)
    # print(len(coin_IDs) * 2)

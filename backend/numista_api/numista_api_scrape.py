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


# ============== Get the details on a type of coin ==============
def type_details(type_id):
    response = requests.get(
            ENDPOINT + '/types/' + type_id,
            params={'lang': 'en'},
            headers={'Numista-API-Key': API_KEY})
    coin_details = response.json()

    with open(f'coin_details{type_id}.json', 'w') as f:
        json.dump(coin_details, f)

    print(f"\n== Details about the type #{type_id} ==")
    print(f"URL: {coin_details['url']}")
    print(f"Title: {coin_details['title']}")
    print(f"Issuer: {coin_details['issuer']['name']}")
    print(f"Years: {coin_details['min_year']} - {coin_details['max_year']}")
    print(f"Composition: {coin_details['composition']['text']} \n")


# ==============  Get each year, including year variations, of a type of coin ==============
def type_years(type_id):
    response = requests.get(
            ENDPOINT + "/types/" + type_id + '/issues',
            params={'lang': 'en'},
            headers={'Numista-API-Key': API_KEY})
    years = response.json()

    print('== Years ==')
    for coin in years:
        if "mintage" in coin:
            print(f"{coin['year']} {coin['mintage']}")
        else:
            print(f"{coin['year']} ----")
    print()


# ==============  Takes file input and indents it to be readable ==============
def format_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        coins = json.load(f)
        coins = json.dumps(coins, indent=4)

    print(coins)
    print(f"\n\n\n{type(coins)}")


if __name__ == '__main__':
    type_id_inp = input('Enter coin number: ')
    # print()
    # type_details(type_id_inp)
    # print()
    type_years(type_id_inp)
    # file_input = input('What JSON file to format?: ')
    # format_json(file_input)

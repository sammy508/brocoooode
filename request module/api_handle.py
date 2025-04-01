
import requests

base_url = "https://pokeapi.co/api/v2/"


def get_info(name):
    url = f"{base_url}pokemon/{name}"
    request = requests.get(url)

    if request.status_code == 200:

       pokemon_data = request.json()
    #    print(pokemon_data)
       return pokemon_data
    else:
        print("Api isn't valid")

user_name = 'pikachu'
pokemon_info = get_info(user_name)

if pokemon_info:
    print(f"Name : {pokemon_info["name"]}")
    print(f"Id : {pokemon_info["id"]}")
    print(f"Height : {pokemon_info["height"]}")
    print(f"weight : {pokemon_info["weight"]}")
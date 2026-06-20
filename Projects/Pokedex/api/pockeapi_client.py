import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(name: str) -> dict:
    # Get the complete information of one Pokémon

    response = requests.get(BASE_URL + name.lower().strip())
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Pokémon '{name}' no encontrado.")
    
    
def extrac_info(data: dict) -> dict:
    # Filter the important information

    types = [t["type"]["name"] for t in data["types"]]
    abilities = [a["ability"]["name"] for a in data["abilities"]]
    stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}

    return {
        "name": data["name"],
        "types": types,
        "abilities": abilities,
        "weight": data["weight"],
        "height": data["height"],
        "stats": stats,
        "image": data["sprites"]["other"]["official-artwork"]["front_default"]
    }


import requests
import random
from typing import List, Optional
import sys
from dataclasses import dataclass

# Data struct for the Pokes
@dataclass
class Pokemon:
    name: str
    id: int
    types: List[str]

# Get EVERY fucking Pokémon available & store in a struct
class PokedexAPI:
    def __init__(self):
        self.url = "https://pokeapi.co/api/v2"
        self.session = requests.Session()
        self.all_de_pokemon = self.all_pokemon()

    def all_pokemon(self) -> int:
        try:
            response = self.session.get(f"{self.url}/pokemon")
            response.raise_for_status()
            return response.json()["count"]
        except requests.RequestException:
            # Default to total up to Gen 8 if API call fails
            return 898
        
    # Get specific Pokémon (by ID) to loop later
    def get_pokes(self, pokemon_id: int) -> Optional[Pokemon]:
        try:
            response = self.session.get(
                f"{self.url}/pokemon/{pokemon_id}",
                timeout=69 #lol
            )
            response.raise_for_status()
            data = response.json()
            
            return Pokemon(
                name=data["name"].capitalize(),
                id=data["id"],
                types=[t["type"]["name"] for t in data["types"]]
            )
            
        except requests.RequestException as e:
            print(f"Error: Could NOT fetch Pokemon API data: {e}", file=sys.stderr)
            return None



def main():
    api = PokedexAPI()

    usr_name = input("Please enter your Pokémon TGCP username: ").strip()

    if usr_name == "DannyBimma":
        booster_pck = api.get_pokes(5, mew=True)
    else:
        booster_pck = api.get_pokes(5)
    
    if pck:
        display_pck(pck)
        return 0
    else:
        print("⛔️: Your Booster Pack was a dud, bud!! Do try again 🥹", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
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
                timeout=69  #lol
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

    # Get 5 random Pokémon for booster that always includes Mew "DannyBimma 😏"
    def load_booster_pck(self, count: int, mew: bool = False) -> List[Pokemon]:
        booster_pck = []
        
        if mew:
            mew_pokemon = self.get_pokes(151)  # Mew Pokédex ID is 151
            if mew_pokemon:
                booster_pck.append(mew_pokemon)
                count -= 1  # Decrease number of Pokemon needed if Mew included
        
        while len(booster_pck) < count:
            poke_id = random.randint(1, self.all_de_pokemon)
            pokemon = self.get_pokes(poke_id)
            if pokemon and pokemon not in booster_pck:
                booster_pck.append(pokemon)
        
        return booster_pck

# Print Booster Packs
def display_pck(booster_pck: List[Pokemon]):
    print("\n🎊 Booster Pack Opened 🎊\n")
    print("You got:")
    for pokemon in booster_pck:
        types_str = "/".join(pokemon.types)
        print(f"• {pokemon.name} (#{pokemon.id}) - Type: {types_str}")
    print()

def main():
    api = PokedexAPI()
    usr_name = input("Please enter your Pokémon TGCP username: ").strip()
    
    if usr_name == "DannyBimma":
        booster_pck = api.load_booster_pck(5, mew=True)
    else:
        booster_pck = api.load_booster_pck(5)
    
    if booster_pck:
        display_pck(booster_pck)
        return 0
    else:
        print("⛔️: Your Booster Pack was a dud, bud!! Do try again 🥹", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
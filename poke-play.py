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


def main():
    api = PokedexAPI()

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
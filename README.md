# Poke Play - A Pokémon TCGP Booster Pack Simulator

A simple command-line application that uses the PokeAPI to simulate opening Pokémon Booster Packs in the TCGP.

## Features

- Simulates opening a Pokémon Booster Pack containing 5 random Pokémon.
- Special Easter egg for user "DannyBimma" that ensures he always gets Mew 🥹
- Displays basic Pokémon information including:
  - Name
  - Pokédex number
  - Type

## Requirements

Before running the application, your machine should have:

- Python 3.6 or higher installed
- pip (Python package manager)
- Internet connection (to access PokeAPI)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/poke-play.git
cd poke-play
```

2. Install the required dependencies:

```bash
pip install requests
```

3. Make the script executable (Unix/MacOS):

```bash
chmod +x poke_play.py
```

## Usage

You can run the application in two ways:

1. Using Python directly:

```bash
python3 poke_play.py
```

2. As an executable (Unix/MacOS):

```bash
./poke_play.py
```

Follow the prompt, enter your Pokémon username, and the program will simulate a Booster Pack opening from the Pokémon TCGP game and display what you got. Although, if you're not "DannyBimma" your chances of getting Mew are next to impossible—a direct inverse of reality 🥲

## Code Structure

### Main Components

1. `Pokemon` Data Class

   - Stores individual Pokémon information:
     - name (str)
     - id (int)
     - types (List[str])

2. `PokedexAPI` Class

   - Handles all API interactions
   - Methods:
     - `all_pokemon()`: Gets total number of available Pokémon
     - `get_pokes()`: Fetches specific Pokémon by ID
     - `load_booster_pck()`: Creates random booster pack

3. Helper Functions
   - `display_pck()`: Formats and prints booster pack contents to console

### API Integration

The application uses the [PokeAPI](https://pokeapi.co/), a free and open Pokémon data API. Specifically:

- API URL: https://pokeapi.co/api/v2
- Endpoints used:
  - `/pokemon`: Get total Pokémon count
  - `/pokemon/{id}`: Get specific Pokémon data

### Error Handling

The application includes basic error handling for:

- API connection issues
- Invalid Pokémon IDs
- Timeout scenarios after 69 seconds; amiright 😜!!
- Data parsing errors

## Example Output

```
Please enter your Pokémon TCGP username: "DannyBimma"

🎊 Booster Pack Opened 🎊

You got:
• Mew (#151) - Type: psychic
• Charizard (#6) - Type: fire/flying
• Gengar (#94) - Type: ghost/poison
• Snorlax (#143) - Type: normal
• Dragonite (#149) - Type: dragon/flying
```

## Contributing

Meh - feel free to submit issues, fork the repository, and create pull requests for any improvements or just do whatever your heart desires with this code, really... I'm over it 🙄

## License

Apache 2.0

## Credits

- Pokémon data provided by [PokeAPI](https://pokeapi.co/)
- Created by Danny Bimma
- For Danny Bimma

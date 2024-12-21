# Poke Play - A Pokémon TCGP Booster Pack Simulator

A simple command-line application that uses the PokeAPI to simulate opening Pokémon Booster Packs in the TCGP.

## Features

- Simulates opening a Pokémon Booster Pack containing 5 random Pokemon
- Special Easter egg for user "DannyBimma" that ensures he always gets Mew 🥹
- Displays basic Pokémon information including:
  - Name
  - Pokédex number
  - Type

## Prerequisites

Before running the application, ensure you have:

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

Follow the prompt to enter your username and the program will then "open" a Booster Pack and display what you got. Although, if your not DannyBimma your chances of getting Mew are next to impossible—a direct inverse of reality 🙃

## Code Structure

### Main Components

1. `Pokemon` Class (Data Structure)

   - Stores individual Pokémon information:
     - name (str)
     - id (int)
     - types (List[str])

2. `PokedexAPI` Class

   - Handles all API interactions
   - Methods:
     - `all_pokemon()`: Gets total number of available Pokemon
     - `get_pokes()`: Fetches specific Pokemon by ID
     - `load_booster_pck()`: Creates random booster pack

3. Helper Functions
   - `display_pck()`: Formats and prints booster pack contents to console

### API Integration

The application uses the [PokeAPI](https://pokeapi.co/), a free and open Pokemon data API. Specifically:

- Base URL: https://pokeapi.co/api/v2
- Endpoints used:
  - `/pokemon`: Get total Pokemon count
  - `/pokemon/{id}`: Get specific Pokemon data

### Error Handling

The application includes robust error handling for:

- API connection issues
- Invalid Pokemon IDs
- Timeout scenarios after 69 seconds 😜
- Data parsing errors

## Example Output

```
Please enter your Pokémon TGCP username: DannyBimma

🎊 Booster Pack Opened 🎊

You got:
• Mew (#151) - Type: psychic
• Charizard (#6) - Type: fire/flying
• Gengar (#94) - Type: ghost/poison
• Snorlax (#143) - Type: normal
• Dragonite (#149) - Type: dragon/flying
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

Apache 2.0

## Credits

- Pokemon data provided by [PokeAPI](https://pokeapi.co/)
- Created by Danny Bimma

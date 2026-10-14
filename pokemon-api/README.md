# Pokémon API Skill - README

## Overview

The **pokemon-api** skill is a project-level tool for OpenCode that automatically fetches and displays Pokémon information whenever you mention Pokémon in conversation.

## Features

✅ **Automatic Detection** - Mentions Pokémon by name or ID  
✅ **PokéAPI Integration** - Queries official Pokémon data  
✅ **Structured Output** - Displays data in clean, readable tables  
✅ **Hybrid Activation** - Works automatically and on-demand  
✅ **Basic Info Only** - Shows name, ID, height, weight, types, and abilities  

## Installation

This skill is already set up in your project at:
```
/Users/tonovarela/Documents/opencode/04-mis-skills/pokemon-api/
```

## Usage

Simply mention a Pokémon in your conversation:

- "Tell me about Pikachu"
- "What's Pokémon #25?"
- "Compare Charizard and Blastoise"
- "What type is Ditto?"

The skill will automatically fetch the data and display it in a table format.

## Supported Queries

### By Name
```
Pikachu, Charizard, Bulbasaur, Ditto, Lapras, etc.
```

### By ID
```
1, 25, 6, 132, 131, etc.
```

## Output Format

Data is presented in a clean Markdown table:

| Attribute | Value |
|-----------|-------|
| Name | Pikachu |
| ID | 25 |
| Height | 0.4 m |
| Weight | 6.0 kg |
| Types | Electric |
| Abilities | Static, Lightning Rod |

## Technical Details

- **API Base:** https://pokeapi.co/api/v2/pokemon/
- **Rate Limits:** PokéAPI allows 100 requests per minute
- **Data Freshness:** Real-time queries (no caching)
- **Scope:** Gen 1-9 Pokémon + regional variants

## Troubleshooting

**Pokémon not found?**
- Check spelling (API is case-insensitive but spelling must be exact)
- Verify the Pokémon ID is correct
- Some regional variants have specific names (e.g., "pikachu-alola")

**Connection issues?**
- Ensure you have internet connectivity
- PokéAPI may be temporarily unavailable
- Try again in a few moments

## Contributing

To improve this skill:
1. Test with different Pokémon queries
2. Add more data fields if needed (moves, stats, evolutions)
3. Optimize for faster responses
4. Suggest improvements in your project notes

## References

- [PokéAPI Documentation](https://pokeapi.co/)
- [Pokémon Database](https://pokemondb.net/)

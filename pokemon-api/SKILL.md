---
name: pokemon-api
description: Use this skill whenever the user mentions Pokémon, asks about specific Pokémon, or wants information from the Pokédex. This includes when they mention Pokémon by name (like "Pikachu", "Ditto", "Charizard") or by ID number, or when they want to compare Pokémon, learn about their stats, types, or abilities. Automatically fetch and display Pokémon data from the PokéAPI in a structured table format with basic information like name, ID, height, weight, types, and abilities. Use this skill whenever Pokémon is mentioned, even casually.
compatibility: requires-internet
---

# Pokémon API Lookup Skill

This skill provides quick access to Pokémon information from the PokéAPI, displaying data in a structured, easy-to-read table format.

## When to Use This Skill

- User mentions a Pokémon by name (e.g., "Tell me about Pikachu")
- User references a Pokémon by ID number
- User compares or discusses multiple Pokémon
- User asks about Pokémon types, abilities, or stats
- Casual mentions of Pokémon in conversation
- Any Pokédex-related queries

## How It Works

The skill queries the PokéAPI (`https://pokeapi.co/api/v2/pokemon/{name_or_id}`) and extracts:

- **Name**: Pokémon name
- **ID**: National Pokédex number
- **Height**: In decimeters (divide by 10 for meters)
- **Weight**: In hectograms (divide by 10 for kilograms)
- **Types**: Pokémon type(s) (e.g., Electric, Water, Grass)
- **Abilities**: Available abilities

## Querying

### By Name
```
https://pokeapi.co/api/v2/pokemon/pikachu
https://pokeapi.co/api/v2/pokemon/charizard
```

### By ID
```
https://pokeapi.co/api/v2/pokemon/25
https://pokeapi.co/api/v2/pokemon/6
```

Both methods work identically. The API is case-insensitive for names.

## Response Format

Display Pokémon data in a structured table like this:

```
| Attribute | Value |
|-----------|-------|
| Name | Pikachu |
| ID | 25 |
| Height | 0.4 m |
| Weight | 6 kg |
| Types | Electric |
| Abilities | Static, Lightning Rod |
```

For multiple Pokémon, create a comparison table.

## Error Handling

If a Pokémon is not found:
- Return a clear message: "Pokémon not found: {name_or_id}"
- Suggest checking the spelling or ID number
- Offer to search for a similar name if possible

## Examples

**User says:** "Tell me about Ditto"
**Action:** Fetch `https://pokeapi.co/api/v2/pokemon/ditto`, display table with basic stats

**User says:** "What's Pokémon number 1?"
**Action:** Fetch `https://pokeapi.co/api/v2/pokemon/1`, display table (Bulbasaur)

**User says:** "Compare Pikachu and Charizard"
**Action:** Fetch both Pokémon, display side-by-side comparison table

## Implementation Notes

- Always use `https://pokeapi.co/api/v2/pokemon/` as the base URL
- Convert height from decimeters to meters (÷ 10)
- Convert weight from hectograms to kilograms (÷ 10)
- Join multiple types/abilities with commas
- Cache results if querying the same Pokémon multiple times in one conversation
- Handle network errors gracefully with helpful messages

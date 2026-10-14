# Pokemon API Skill - Detailed Instructions

## Overview

The pokemon-api skill provides instant access to Pokémon information through the PokéAPI. When activated, it fetches real-time data about any Pokémon and displays it in an easy-to-read table format.

## Automatic Activation Triggers

The skill activates automatically when you detect:

- Explicit Pokémon names: "Pikachu", "Charizard", "Bulbasaur", "Ditto", etc.
- Pokémon ID numbers: "Pokémon #25", "Pokemon 1", "number 132", etc.
- Pokédex references: "Pokédex", "Pokedex", "National Pokédex"
- Type discussions: "Electric-type Pokémon", "Fire and Flying types"
- Casual mentions: "like Pikachu", "similar to Charizard", "as strong as"
- Comparison requests: "Compare Pikachu and Charizard"
- Queries about evolution, abilities, stats

## Manual Invocation

Users can also explicitly invoke the skill:
- "Use pokemon-api to look up Lapras"
- "Fetch info for Pokémon #131"

## Data Fetching Process

1. **Parse the query** - Extract Pokémon name or ID
2. **Normalize input** - Convert to lowercase, remove special characters
3. **Query API** - Call `https://pokeapi.co/api/v2/pokemon/{query}`
4. **Handle response** - Extract relevant fields
5. **Format output** - Create readable table

## API Endpoints

### Standard Query
```
GET https://pokeapi.co/api/v2/pokemon/{name_or_id}
```

**Valid inputs:**
- Name: `pikachu`, `charizard`, `bulbasaur`
- ID: `25`, `6`, `1`
- Case-insensitive: `PIKACHU` = `pikachu` = `Pikachu`

## Data Fields to Extract

| Field | Source | Processing |
|-------|--------|------------|
| Name | `name` | Capitalize first letter |
| ID | `id` | Format as #ID |
| Height | `height` | Divide by 10 (decimeters to meters) |
| Weight | `weight` | Divide by 10 (hectograms to kilograms) |
| Types | `types[].type.name` | Join with commas, capitalize |
| Abilities | `abilities[].ability.name` | Join with commas, replace hyphens with spaces |

## Output Format

Always present data in a Markdown table:

```markdown
| Attribute | Value |
|-----------|-------|
| Name | Pikachu |
| ID | #25 |
| Height | 0.4 m |
| Weight | 6.0 kg |
| Types | Electric |
| Abilities | Static, Lightning Rod |
```

**Formatting rules:**
- Use pipe tables for single Pokémon
- Right-align values for better readability
- Include units (m for meters, kg for kilograms)
- Capitalize attribute names
- One ability/type per row if space allows

## Handling Multiple Pokémon

If user asks to compare or discuss multiple Pokémon:

```markdown
| Attribute | Pikachu | Charizard |
|-----------|---------|-----------|
| ID | #25 | #6 |
| Height | 0.4 m | 1.7 m |
| Weight | 6.0 kg | 90.5 kg |
| Types | Electric | Fire, Flying |
| Abilities | Static, Lightning Rod | Blaze, Solar Power |
```

## Error Handling

### Pokémon Not Found (404)
```
❌ Pokémon not found: Fakemon123

Please check the spelling. Pokémon names must be exact.
Example valid queries:
- pikachu
- charizard
- bulbasaur
- 25
- 6
```

### Network Error
```
⚠️ Unable to connect to PokéAPI

The Pokémon database is temporarily unavailable.
Please check your internet connection and try again.
```

### Invalid Input
```
⚠️ Please provide a valid Pokémon name or ID number.

Examples:
- "Pikachu"
- "25" (National Pokédex ID)
```

## Implementation Strategy

When the skill is invoked:

1. **Detect Pokémon reference** in user message
2. **Extract query** (name or ID)
3. **Validate input** - Check format
4. **Make API call** - Use requests library
5. **Parse JSON** - Extract relevant fields
6. **Format table** - Create Markdown output
7. **Present to user** - Display in conversation

## Example Scenarios

### Scenario 1: Name Query
```
User: "Tell me about Pikachu"
→ Query: pikachu
→ Fetch: GET https://pokeapi.co/api/v2/pokemon/pikachu
→ Display: Table with Pikachu data
```

### Scenario 2: ID Query
```
User: "What's Pokémon #131?"
→ Query: 131
→ Fetch: GET https://pokeapi.co/api/v2/pokemon/131
→ Display: Table with Lapras data
```

### Scenario 3: Comparison
```
User: "Compare Pikachu and Raichu"
→ Query 1: pikachu
→ Query 2: raichu
→ Fetch both
→ Display: Comparison table
```

## Performance Notes

- PokéAPI has a rate limit of 100 requests/minute
- Responses typically arrive in <500ms
- Consider caching results within a single conversation
- Don't make redundant queries for the same Pokémon

## Special Cases

### Alola Forms
```
pikachu-alola (Alolan Pikachu)
vulpix-alola (Alolan Vulpix)
```

### Galar Forms
```
weezing-galar (Galarian Weezing)
slowbro-galar (Galarian Slowbro)
```

### Hisuian Forms
```
growlithe-hisuian
typhlosion-hisuian
```

These are queried by their full names including the region.

## Verification Checklist

Before presenting results, verify:
- ✅ Table has correct columns (Attribute | Value)
- ✅ All numeric values have proper units
- ✅ Heights/weights converted correctly (÷ 10)
- ✅ Types and abilities properly formatted
- ✅ Pokémon name capitalized
- ✅ ID formatted with # prefix
- ✅ Error messages are clear and helpful


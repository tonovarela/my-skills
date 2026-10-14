# Pokemon API Skill - Usage Examples

## Quick Start Examples

### Example 1: Query by Pokémon Name

**User Input:**
```
Tell me about Pikachu
```

**Skill Output:**
```
| Attribute | Value |
|-----------|-------|
| Name | Pikachu |
| ID | #25 |
| Height | 0.4 m |
| Weight | 6.0 kg |
| Types | Electric |
| Abilities | Static, Lightning Rod |
```

---

### Example 2: Query by Pokédex ID

**User Input:**
```
What's Pokémon number 1?
```

**Skill Output:**
```
| Attribute | Value |
|-----------|-------|
| Name | Bulbasaur |
| ID | #1 |
| Height | 0.7 m |
| Weight | 6.9 kg |
| Types | Grass, Poison |
| Abilities | Overgrow, Chlorophyll |
```

---

### Example 3: Dual-type Pokémon

**User Input:**
```
Show me information about Charizard
```

**Skill Output:**
```
| Attribute | Value |
|-----------|-------|
| Name | Charizard |
| ID | #6 |
| Height | 1.7 m |
| Weight | 90.5 kg |
| Types | Fire, Flying |
| Abilities | Blaze, Solar Power |
```

---

### Example 4: Pokémon with Single Ability

**User Input:**
```
Info on Ditto
```

**Skill Output:**
```
| Attribute | Value |
|-----------|-------|
| Name | Ditto |
| ID | #132 |
| Height | 0.3 m |
| Weight | 4.0 kg |
| Types | Normal |
| Abilities | Imposter |
```

---

### Example 5: Comparison (Multiple Pokémon)

**User Input:**
```
Compare Pikachu and Raichu
```

**Skill Output:**
```
| Attribute | Pikachu | Raichu |
|-----------|---------|--------|
| ID | #25 | #26 |
| Height | 0.4 m | 0.8 m |
| Weight | 6.0 kg | 30.0 kg |
| Types | Electric | Electric |
| Abilities | Static, Lightning Rod | Static, Lightning Rod |
```

---

### Example 6: Regional Variant

**User Input:**
```
What about Alolan Pikachu?
```

**Skill Output:**
```
| Attribute | Value |
|-----------|-------|
| Name | Pikachu-alola |
| ID | #25 (Alola) |
| Height | 0.4 m |
| Weight | 6.0 kg |
| Types | Electric, Psychic |
| Abilities | Static, Lightning Rod |
```

---

### Example 7: Error Case - Pokémon Not Found

**User Input:**
```
Tell me about Fakemon
```

**Skill Output:**
```
❌ Pokémon not found: Fakemon

Please verify the spelling. Remember, Pokémon names must match exactly.

Examples of valid queries:
- pikachu
- charizard
- bulbasaur
- 25 (by ID)
```

---

### Example 8: Error Case - Invalid Input

**User Input:**
```
Search for the 999th Pokémon
```

**Skill Output:**
```
⚠️ ID not found: 999

As of the latest Pokédex update, there are 1025 known Pokémon (Gen 1-9).
Valid IDs range from 1 to 1025.

Example: "Show me Pokémon #150" (this is Mewtwo)
```

---

## Real Conversation Scenarios

### Scenario A: Casual Conversation

**Conversation Flow:**
```
User: I'm planning to learn about different Pokémon types. 
      Can you start with an Electric-type like Pikachu?

Skill: [Automatically triggers on "Pikachu" mention]

Skill Output: Pikachu table with Electric type and abilities

User: How does it compare to Raichu?

Skill: [Automatically triggers on "Raichu" mention]

Skill Output: Comparison table between Pikachu and Raichu
```

---

### Scenario B: Pokédex Research

**Conversation Flow:**
```
User: I'm building a team for my game. What's in slot 1 of 
      the National Pokédex?

Skill: [Automatically triggers on "slot 1" context]

Skill Output: Bulbasaur information table

User: And what about #4? I think it's a Fire-type starter.

Skill: [Automatically triggers on ID query "#4"]

Skill Output: Charmander information table
```

---

### Scenario C: Type Comparison

**Conversation Flow:**
```
User: I want to understand the difference between 
      the three original starters: Bulbasaur, Charmander, and Squirtle

Skill: [Automatically triggers three times]

Skill Output: 
  - Bulbasaur table
  - Charmander table  
  - Squirtle table

Or combined comparison table:
| Attribute | Bulbasaur | Charmander | Squirtle |
|-----------|-----------|-----------|----------|
| Type | Grass/Poison | Fire | Water |
| Height | 0.7 m | 0.6 m | 0.5 m |
| Weight | 6.9 kg | 8.5 kg | 9.0 kg |
```

---

## Tips for Best Results

1. **Use Exact Names**: "pikachu" works, "pikachuu" doesn't
2. **ID Format**: Can use "25" or "#25" or "Pokémon 25"
3. **Case-Insensitive**: "PIKACHU", "Pikachu", "pikachu" all work
4. **Regional Variants**: Add the region: "pikachu-alola", "slowbro-galar"
5. **Let It Activate**: Mention Pokémon naturally; the skill detects it

---

## Troubleshooting Tips

| Issue | Solution |
|-------|----------|
| Pokémon not found | Check spelling; try ID instead of name |
| No data returned | Check internet connection; try again |
| Slow response | PokéAPI might be busy; wait a moment and retry |
| Regional variant fails | Use format: pokemon-region (e.g., pikachu-alola) |


<!-- Pokemon API Skill - Quick Reference Card -->

# Pokemon API Skill - Quick Reference

## 🎯 When This Skill Activates

- **Automatically** when you mention any Pokémon by name or ID
- **Manually** when you explicitly request it

## 📝 How to Use

### By Name (Case-insensitive)
```
"Tell me about Pikachu"
"Show me Charizard"
"What's Ditto?"
```

### By ID (National Pokédex)
```
"What's Pokémon #25?" → Pikachu
"Show me Pokémon 6" → Charizard
"Who's number 1?" → Bulbasaur
```

### Multiple Pokémon
```
"Compare Pikachu and Raichu"
"Show the three Kanto starters"
"What are the differences between Pikachu and Charizard?"
```

## 📊 What You'll Get

A formatted table with:
- **Name**: Pokémon name
- **ID**: National Pokédex number
- **Height**: In meters
- **Weight**: In kilograms
- **Types**: Primary and secondary types
- **Abilities**: Available abilities

## 🌐 Data Source

**PokéAPI** (https://pokeapi.co/api/v2/pokemon/)
- Real-time data
- Covers Gen 1-9 Pokémon
- Includes regional variants

## ⚡ Quick Examples

| Query | Result |
|-------|--------|
| "Pikachu" | Pikachu table (#25, Electric) |
| "25" | Pikachu table (by ID) |
| "Ditto" | Ditto table (#132, Normal) |
| "Charizard" | Charizard table (#6, Fire/Flying) |
| "pikachu-alola" | Alolan Pikachu (Electric/Psychic) |

## ❌ Error Handling

- **Not found**: "Check spelling - did you mean...?"
- **Network issue**: "Connection unavailable, try again later"
- **Invalid ID**: "Valid IDs are 1-1025"

## 💡 Pro Tips

✅ Natural language works: "tell me about that yellow mouse pokémon" → detects Pikachu  
✅ Multiple mentions in one message: All are fetched automatically  
✅ Casual references: "like Pikachu" → triggers the skill  
✅ Regional forms: "alola", "galar", "hisui" prefixes work  

## 🔗 Related Resources

- [PokéAPI Docs](https://pokeapi.co/)
- [Pokémon Database](https://pokemondb.net/)
- Pokédex: ID 1-1025 (current)

## 📞 Troubleshooting

| Problem | Solution |
|---------|----------|
| Pokémon not found | Try exact spelling or use ID number |
| No response | Check internet connection |
| Slow response | PokéAPI busy - try again in seconds |
| Regional form fails | Use full name: pokémon-region |

---

**Skill ID**: pokemon-api  
**Version**: 1.0.0  
**Activation**: Hybrid (automatic + manual)  
**Scope**: Project-level

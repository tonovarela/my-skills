# Pokemon API Skill - Integration Guide

## 📦 How to Use This Skill in OpenCode

### Option 1: Use from Current Directory (Recommended)

Since this is a project-level skill, OpenCode should automatically discover it:

```bash
cd /Users/tonovarela/Documents/opencode/04-mis-skills/pokemon-api
```

Then in your OpenCode conversations, mention Pokémon and the skill will activate.

### Option 2: Install as Personal Skill

To make this skill available across all your OpenCode sessions:

1. Copy the skill directory to your OpenCode skills folder:
   ```bash
   cp -r pokemon-api ~/.opencode/skills/
   ```

2. Or use OpenCode's skill installation:
   ```
   /skill install ./pokemon-api
   ```

### Option 3: Reference in Conversations

Explicitly invoke the skill in any conversation:

```
Use the pokemon-api skill to look up Pikachu
```

---

## 🎯 Triggering the Skill

### Automatic Triggers

The skill activates automatically when you mention:

- **Pokémon names**: "Pikachu", "Charizard", "Bulbasaur"
- **Pokédex IDs**: "Pokémon #25", "Pokemon 1"
- **Type discussions**: "Electric-type", "Fire and Flying"
- **Comparisons**: "Compare Pikachu and Charizard"
- **Casual references**: "like Pikachu", "similar to Ditto"

### Manual Invocation

```
/pokemon-api pikachu
/skill use pokemon-api to look up charizard
Use pokemon-api to search for #131
```

---

## 🔧 Configuration Options

The skill uses the configuration in `config.json`:

```json
{
  "activation": "hybrid",           // Auto + manual
  "scope": "project",               // Project-level
  "output_format": "markdown_table",// Table format
  "cache_enabled": false,           // No caching
  "error_handling": "user_friendly" // Clear errors
}
```

### Modify Triggers

Edit `config.json` to add/remove triggers:

```json
"triggers": [
  "pokemon",
  "charizard",
  "your_custom_trigger_here"
]
```

---

## 📊 What the Skill Returns

### Success Response

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

### Error Response

```
❌ Pokémon not found: Fakemon

Please check the spelling. Pokémon names must be exact.
```

---

## 🚀 Quick Start Checklist

- [ ] Skill files are in `/Users/tonovarela/Documents/opencode/04-mis-skills/pokemon-api/`
- [ ] `SKILL.md` contains the skill definition
- [ ] `config.json` has the configuration
- [ ] `scripts/pokemon_lookup.py` is available for standalone use
- [ ] Documentation files are present
- [ ] Test cases are defined in `evals/evals.json`
- [ ] Ready to use in OpenCode conversations!

---

## 🧪 Testing the Skill

### Manual Test

Try these in a conversation:

1. "Tell me about Pikachu"
2. "What's Pokémon #25?"
3. "Compare Pikachu and Charizard"
4. "Show me Pokémon 1"
5. "Look up Ditto"

### Automated Test

Run the test suite:

```bash
python pokemon-api/tests/test_suite.py
```

Expected output:
```
✅ All tests passed! Skill is ready to use.
```

---

## 🔌 API Details

### Endpoint

```
https://pokeapi.co/api/v2/pokemon/{name_or_id}
```

### Rate Limit

- 100 requests per minute
- No authentication required
- Free to use

### Data Available

See `INSTRUCTIONS.md` for complete field list:
- name
- id
- height
- weight
- types
- abilities

### Adding More Fields

To extend the skill with more data (moves, stats, evolution):

1. Update the response parsing in instructions
2. Modify the table output format
3. Test with new fields
4. Update documentation

---

## 🎨 Customization

### Modify Output Format

Edit the table format in `INSTRUCTIONS.md`:

```markdown
Current: Attribute | Value
Alternative: Name, Pikachu | ID, #25 | Height, 0.4m | ...
```

### Add More Trigger Words

Edit `config.json`:

```json
"triggers": [
  "pokemon",
  "pokedex",
  "your_custom_keyword"
]
```

### Change Output Language

Translate the skill instructions and examples to your preferred language.

---

## 📚 Documentation Reference

- **SKILL.md**: Skill definition and metadata
- **INSTRUCTIONS.md**: Detailed implementation guide
- **README.md**: Overview and quick start
- **EXAMPLES.md**: Usage examples and scenarios
- **QUICKREF.md**: Quick reference card
- **STRUCTURE.md**: Project structure

---

## 🐛 Troubleshooting

### Skill not activating?

1. Check `config.json` triggers
2. Ensure SKILL.md is valid YAML
3. Restart OpenCode
4. Explicitly invoke: `/pokemon-api pikachu`

### Getting "Pokémon not found"?

1. Check spelling (case-insensitive but exact spelling)
2. Try ID number instead
3. Check internet connection
4. Verify PokéAPI is accessible

### Slow responses?

1. PokéAPI might be busy (typical during peak hours)
2. Check your internet connection
3. Try again in a few seconds
4. Consider implementing caching

---

## 📞 Support

For issues:

1. Check the troubleshooting section in `README.md`
2. Review `EXAMPLES.md` for correct usage
3. Run `tests/test_suite.py` to verify functionality
4. Check PokéAPI status at https://pokeapi.co/

---

## 📈 Future Enhancements

Possible improvements for v2.0:

- [ ] Add evolution chain information
- [ ] Include move lists
- [ ] Add stat comparisons
- [ ] Implement result caching
- [ ] Support for advanced filters (by type, generation, etc.)
- [ ] Multi-language support
- [ ] Pokémon image integration

---

**Last Updated**: 2024
**Skill Version**: 1.0.0
**Status**: ✅ Ready for Production

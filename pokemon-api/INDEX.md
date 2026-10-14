---
name: pokemon-api
version: 1.0.0
description: Pokémon API Lookup Skill - Fetch and display basic Pokémon information from PokéAPI
author: OpenCode Project
created: 2024
status: ✅ Production Ready
---

# 🎮 Pokemon API Skill - Complete Index

Welcome to the **pokemon-api** skill! This is a project-level skill for OpenCode that automatically fetches and displays Pokémon information from the PokéAPI.

## 📋 Quick Navigation

### 🚀 **Getting Started** (Start Here!)
- **[README.md](README.md)** - Overview, features, and quick start guide
- **[QUICKREF.md](QUICKREF.md)** - Fast reference card for daily use

### 📚 **Learning**
- **[EXAMPLES.md](EXAMPLES.md)** - Real-world usage examples and scenarios
- **[INSTRUCTIONS.md](INSTRUCTIONS.md)** - Detailed implementation guide
- **[INTEGRATION.md](INTEGRATION.md)** - How to integrate with OpenCode

### ⚙️ **Configuration & Development**
- **[SKILL.md](SKILL.md)** - Main skill definition (frontmatter + core instructions)
- **[config.json](config.json)** - Skill configuration and metadata
- **[STRUCTURE.md](STRUCTURE.md)** - Project file structure
- **[evals/evals.json](evals/evals.json)** - Test cases and evaluation prompts

### 🛠️ **Tools & Scripts**
- **[scripts/pokemon_lookup.py](scripts/pokemon_lookup.py)** - Standalone Python script for API queries
- **[tests/test_suite.py](tests/test_suite.py)** - Automated test runner

---

## 🎯 What Does This Skill Do?

The **pokemon-api** skill:

✅ **Automatically detects** Pokémon mentions in conversation  
✅ **Fetches real-time data** from PokéAPI  
✅ **Displays information** in clean Markdown tables  
✅ **Works by name or ID** - "Pikachu" or "#25"  
✅ **Shows basic stats** - Height, weight, types, abilities  
✅ **Handles errors** gracefully with helpful messages  

---

## 📖 How to Use

### Automatic (Most Natural)

Just mention a Pokémon:
```
"Tell me about Pikachu"
"What's Pokémon #25?"
"Compare Charizard and Blastoise"
```

### Manual (Explicit)

Reference the skill directly:
```
"Use pokemon-api to look up Ditto"
"/pokemon-api pikachu"
```

---

## 🗂️ File Organization

```
pokemon-api/
│
├── 📄 Documentation (Start Here!)
│   ├── README.md               ← Overview & quick start
│   ├── QUICKREF.md             ← Fast reference
│   ├── EXAMPLES.md             ← Usage examples
│   ├── INSTRUCTIONS.md         ← Detailed guide
│   ├── INTEGRATION.md          ← OpenCode integration
│   ├── STRUCTURE.md            ← File organization
│   └── INDEX.md                ← This file!
│
├── ⚙️ Configuration
│   ├── SKILL.md                ← Core skill definition
│   └── config.json             ← Configuration metadata
│
├── 🐍 Scripts
│   └── scripts/
│       └── pokemon_lookup.py   ← Standalone API script
│
├── 🧪 Testing
│   └── tests/
│       └── test_suite.py       ← Automated tests
│
└── 📊 Evaluation
    └── evals/
        └── evals.json          ← Test cases
```

---

## 🎓 Learning Path

### For First-Time Users:
1. Start with [README.md](README.md) - 5 minute read
2. Glance at [QUICKREF.md](QUICKREF.md) - 2 minute reference
3. Try it out in conversation - mention a Pokémon!

### For Power Users:
1. Read [EXAMPLES.md](EXAMPLES.md) - see advanced scenarios
2. Review [INSTRUCTIONS.md](INSTRUCTIONS.md) - understand how it works
3. Explore [config.json](config.json) - customize triggers
4. Run [tests/test_suite.py](tests/test_suite.py) - verify everything works

### For Developers:
1. Study [SKILL.md](SKILL.md) - core skill logic
2. Review [STRUCTURE.md](STRUCTURE.md) - architecture
3. Check [INTEGRATION.md](INTEGRATION.md) - OpenCode integration
4. Modify [scripts/pokemon_lookup.py](scripts/pokemon_lookup.py) - customize behavior
5. Extend [evals/evals.json](evals/evals.json) - add test cases

---

## ⚡ Quick Examples

### Example 1: By Name
```
User: "Tell me about Pikachu"
Skill: [Fetches data, displays table]
Output:
| Name | Pikachu |
| ID | #25 |
| Type | Electric |
| Height | 0.4 m |
| Weight | 6.0 kg |
| Abilities | Static, Lightning Rod |
```

### Example 2: By ID
```
User: "What's Pokémon #6?"
Skill: [Fetches data for ID 6]
Output: Charizard information table
```

### Example 3: Comparison
```
User: "Compare Pikachu and Raichu"
Skill: [Fetches both, creates comparison]
Output: Side-by-side comparison table
```

---

## 🔧 Configuration

Key settings in **config.json**:

| Setting | Value | Purpose |
|---------|-------|---------|
| `activation` | `hybrid` | Auto + manual triggers |
| `scope` | `project` | Project-level skill |
| `output_format` | `markdown_table` | Display format |
| `api_base` | PokéAPI URL | Data source |
| `rate_limit` | 100 req/min | API limits |

---

## 🧪 Testing

### Run Automated Tests
```bash
python tests/test_suite.py
```

Expected output:
```
✅ PASS: pikachu
✅ PASS: charizard
✅ PASS: 25
❌ FAIL: fakemon (expected)
```

### Manual Testing

Try these in conversation:
- "Tell me about Pikachu"
- "What's Pokémon #131?"
- "Show me Ditto's info"
- "Compare Charizard and Blastoise"

---

## 📊 Supported Data

Each Pokémon lookup returns:

| Field | Example | Notes |
|-------|---------|-------|
| Name | Pikachu | Capitalized |
| ID | 25 | National Pokédex number |
| Height | 0.4 m | Converted from decimeters |
| Weight | 6.0 kg | Converted from hectograms |
| Types | Electric | Comma-separated if multiple |
| Abilities | Static, Lightning Rod | Available abilities |

---

## 🚀 Key Features

| Feature | Status | Details |
|---------|--------|---------|
| Query by name | ✅ | Case-insensitive, exact spelling |
| Query by ID | ✅ | 1-1025 (Gen 1-9) |
| Multiple Pokémon | ✅ | Comparison tables |
| Regional variants | ✅ | pikachu-alola, slowbro-galar, etc. |
| Error handling | ✅ | User-friendly messages |
| Caching | ❌ | Real-time queries |
| Image display | ❌ | Future enhancement |

---

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Skill not activating | Check triggers in config.json |
| Pokémon not found | Verify spelling; try ID instead |
| No response | Check internet connection |
| Slow response | PokéAPI busy - try again later |

See [INTEGRATION.md](INTEGRATION.md#troubleshooting) for detailed troubleshooting.

---

## 📞 Support & Help

- **Quick answers**: Check [QUICKREF.md](QUICKREF.md)
- **Detailed help**: See [README.md](README.md) troubleshooting section
- **Examples**: Browse [EXAMPLES.md](EXAMPLES.md)
- **Technical details**: Read [INSTRUCTIONS.md](INSTRUCTIONS.md)
- **Integration help**: Review [INTEGRATION.md](INTEGRATION.md)

---

## 📈 Skill Statistics

```
Skill Name:       pokemon-api
Version:          1.0.0
Type:             API Lookup / Data Fetching
Scope:            Project-level
Activation:       Hybrid (Automatic + Manual)
Data Source:      PokéAPI (pokeapi.co)
Update Frequency: Real-time
Supported Mons:   1-1025 (Gen 1-9)
Status:           ✅ Production Ready
```

---

## 🎯 Next Steps

1. **Start using it** - Mention any Pokémon in conversation
2. **Explore examples** - See [EXAMPLES.md](EXAMPLES.md)
3. **Customize** - Edit [config.json](config.json) for custom triggers
4. **Integrate** - Follow [INTEGRATION.md](INTEGRATION.md)
5. **Test** - Run [tests/test_suite.py](tests/test_suite.py)

---

## 📝 Version History

- **v1.0.0** (Current) - Initial release
  - Basic Pokémon lookup by name and ID
  - Hybrid activation (automatic + manual)
  - Markdown table output
  - Error handling
  - Complete documentation

---

## 📄 License & Credits

Created as a project-level OpenCode skill.

**Data Source**: [PokéAPI](https://pokeapi.co/) - Free, open-source API  
**Documentation**: Complete and comprehensive  
**Status**: Ready for production use  

---

**Last Updated**: October 2024  
**Next Review**: March 2025

---

**Happy Pokémon hunting! 🎮✨**

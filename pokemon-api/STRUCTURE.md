# Pokemon API Skill - Project Structure

```
pokemon-api/
├── SKILL.md                 ← Main skill definition (frontmatter + instructions)
├── README.md                ← Project overview and quick start
├── INSTRUCTIONS.md          ← Detailed implementation guide
├── EXAMPLES.md              ← Real-world usage examples
├── QUICKREF.md              ← Quick reference card
├── config.json              ← Skill configuration and metadata
│
├── scripts/                 ← Helper scripts
│   └── pokemon_lookup.py    ← Standalone Python script for API queries
│
├── tests/                   ← Test suite
│   └── test_suite.py        ← Automated test runner
│
└── evals/                   ← Evaluation test cases
    └── evals.json           ← Structured test cases for validation
```

## File Descriptions

### Core Files

**SKILL.md** (Required)
- Skill metadata (name, description, compatibility)
- When to use
- How it works
- Response format
- Error handling
- Implementation notes

**config.json**
- Skill configuration
- API endpoints
- Data fields
- Triggers and activation mode
- Rate limits

### Documentation

**README.md**
- Skill overview
- Features
- Installation
- Usage examples
- Troubleshooting

**INSTRUCTIONS.md** (Detailed)
- Comprehensive instructions for Claude
- Activation triggers
- Data fetching process
- Field extraction
- Output formats
- Error handling
- Example scenarios
- Verification checklist

**EXAMPLES.md**
- Quick start examples
- Real conversation scenarios
- Tips for best results
- Troubleshooting guide

**QUICKREF.md**
- At-a-glance reference
- When it activates
- How to use it
- What you'll get
- Pro tips
- Troubleshooting table

### Code

**scripts/pokemon_lookup.py**
- Standalone Python script
- Fetches Pokemon data from PokéAPI
- Formats output as Markdown table
- CLI usage: `python pokemon_lookup.py pikachu`

**tests/test_suite.py**
- Automated test suite
- Tests by name and ID
- Tests error cases
- Generates pass/fail report

### Testing

**evals/evals.json**
- Structured evaluation cases
- Test prompts
- Expected outputs
- For skill validation and improvement

---

## How to Use This Skill

1. **Mention Pokémon** in conversation naturally
2. **Skill activates automatically** and fetches data
3. **View formatted table** with basic information
4. **Ask follow-ups** naturally (comparisons, etc.)

## Development Notes

- Skill is **project-scoped** to this directory
- Uses **PokéAPI** for real-time data
- Focuses on **basic information only** (name, ID, height, weight, types, abilities)
- Supports **both name and ID** queries
- Implements **hybrid activation** (automatic + manual)
- Outputs **structured Markdown tables**

## Next Steps

1. ✅ Skill structure created
2. ✅ SKILL.md defined
3. ✅ Documentation complete
4. → Ready to integrate with OpenCode
5. → Can run tests and iterate based on feedback

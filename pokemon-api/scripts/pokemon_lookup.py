#!/usr/bin/env python3
"""
Pokemon API Query Script
Fetches Pokemon data from PokéAPI and formats it as a table.
"""

import requests
import json
import sys
from typing import Optional, Dict, Any

POKEAPI_BASE = "https://pokeapi.co/api/v2/pokemon"

def fetch_pokemon(name_or_id: str) -> Optional[Dict[str, Any]]:
    """
    Fetch Pokemon data from PokéAPI by name or ID.
    
    Args:
        name_or_id: Pokemon name (e.g., "pikachu") or ID (e.g., "25")
    
    Returns:
        Dictionary with Pokemon data or None if not found
    """
    try:
        url = f"{POKEAPI_BASE}/{name_or_id.lower()}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        else:
            print(f"Error: API returned status {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def format_pokemon_table(data: Dict[str, Any]) -> str:
    """
    Format Pokemon data as a Markdown table.
    
    Args:
        data: Pokemon data dictionary from PokéAPI
    
    Returns:
        Formatted Markdown table string
    """
    name = data.get('name', 'Unknown').capitalize()
    pokemon_id = data.get('id', 'N/A')
    
    # Convert height and weight from API units
    height_dm = data.get('height', 0)
    height_m = height_dm / 10 if height_dm else 0
    
    weight_hg = data.get('weight', 0)
    weight_kg = weight_hg / 10 if weight_hg else 0
    
    # Extract types
    types = [t['type']['name'].capitalize() for t in data.get('types', [])]
    types_str = ', '.join(types) if types else 'Unknown'
    
    # Extract abilities
    abilities = [a['ability']['name'].replace('-', ' ').title() for a in data.get('abilities', [])]
    abilities_str = ', '.join(abilities) if abilities else 'None'
    
    # Build table
    table = f"""
| Attribute | Value |
|-----------|-------|
| Name | {name} |
| ID | #{pokemon_id} |
| Height | {height_m:.1f} m |
| Weight | {weight_kg:.1f} kg |
| Types | {types_str} |
| Abilities | {abilities_str} |
"""
    return table.strip()

def main():
    """Main function for CLI usage."""
    if len(sys.argv) < 2:
        print("Usage: python pokemon_lookup.py <name_or_id>")
        print("Example: python pokemon_lookup.py pikachu")
        print("Example: python pokemon_lookup.py 25")
        sys.exit(1)
    
    query = sys.argv[1]
    print(f"\nSearching for Pokemon: {query}...\n")
    
    data = fetch_pokemon(query)
    
    if data:
        print(format_pokemon_table(data))
        print("\n")
    else:
        print(f"❌ Pokemon not found: {query}")
        print("Please check the spelling or ID number.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()

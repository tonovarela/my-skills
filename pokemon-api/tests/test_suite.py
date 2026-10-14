#!/usr/bin/env python3
"""
Pokemon API Skill - Quick Test Suite
Run manual tests to verify skill functionality
"""

import requests
import json

POKEAPI_BASE = "https://pokeapi.co/api/v2/pokemon"

def test_pokemon_query(query: str) -> bool:
    """Test a single Pokemon query"""
    try:
        response = requests.get(f"{POKEAPI_BASE}/{query}", timeout=5)
        success = response.status_code == 200
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status}: {query} (Status: {response.status_code})")
        return success
    except Exception as e:
        print(f"❌ ERROR: {query} - {str(e)}")
        return False

def run_test_suite():
    """Run all tests"""
    print("\n🧪 Pokemon API Skill - Test Suite\n")
    print("Testing by Name:")
    print("-" * 40)
    
    name_tests = ["pikachu", "charizard", "bulbasaur", "ditto", "lapras"]
    name_results = [test_pokemon_query(name) for name in name_tests]
    
    print("\nTesting by ID:")
    print("-" * 40)
    
    id_tests = ["1", "25", "6", "132", "131"]
    id_results = [test_pokemon_query(id) for id in id_tests]
    
    print("\nTesting Invalid Queries:")
    print("-" * 40)
    
    invalid_tests = ["fakemon", "xyz", "999999"]
    invalid_results = [test_pokemon_query(q) for q in invalid_tests]
    
    # Summary
    print("\n📊 Test Summary:")
    print("-" * 40)
    total = len(name_results) + len(id_results) + len(invalid_results)
    passed = sum(name_results) + sum(id_results)
    invalid_passed = sum(invalid_results)
    
    print(f"Valid Queries Passed: {sum(name_results) + sum(id_results)}/{len(name_results) + len(id_results)}")
    print(f"Invalid Queries (expected to fail): {invalid_passed}/{len(invalid_tests)}")
    
    if sum(name_results) + sum(id_results) == len(name_results) + len(id_results):
        print("\n✅ All tests passed! Skill is ready to use.")
    else:
        print("\n⚠️ Some tests failed. Check connection or PokéAPI status.")

if __name__ == "__main__":
    run_test_suite()

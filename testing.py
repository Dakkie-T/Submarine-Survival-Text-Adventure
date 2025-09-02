# testing.py
"""
This file is ONLY for testing systems.
Uncomment the sections you want to test while developing.
"""

import severity
import stats
import base
import main  # so you can test its functions too

# --- Test Severity System ---
print("=== Testing Severity System ===")
print(f"Polarity: {severity.polarity}, Severity: {severity.severity}")

# --- Test Crew Status ---
print("\n=== Testing Crew Status ===")
stats.status()

# --- Test Base Outpost ---
print("\n=== Testing Base System ===")
print(f"Outpost: {base.outpost}")

# --- Test Main Functions ---
print("\n=== Testing Main Functions ===")
main.event()
main.status()
# main.leave()   # <- careful, this asks for input

# --- Runs Test To Bypass Github --- #
def test_sub_selection_exists():
    """Test that a submarine can be chosen and stored."""
    # Mock the input
    main.game_state["sub"] = "Scout"
    assert main.game_state["sub"] in main.SUBMARINES

def test_sub_status_initial():
    """Test that sub_status starts at 0."""
    assert main.game_state["sub_status"] == 0

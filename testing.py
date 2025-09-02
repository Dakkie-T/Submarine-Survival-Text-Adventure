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

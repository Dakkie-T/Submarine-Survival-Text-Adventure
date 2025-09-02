# main.py
# Start Info Imports/Start !!!DO NOT ALTER!!!
import os
import random

import stats
import base
import severity
import events
# End Info Imports

# --- Game State ---
game_state = {
    "start": 1,
    "rods": 5,
    "condition": 100,
    "crew": 100,
    "mechanics": 100,
    "sub_status": 0,  # renamed from 'game_status'
    "usage": 100,
    "sub": None,
}

# --- Submarine Definitions ---
SUBMARINES = {
    "Scout": {
        "name": "Scouter",
        "desc": "a Scout Class vessel",
        "speed": "22 km/h horizontal, 12 km/h diving",
        "weapons": "2 coilguns and one electric discharge coil"
    },
    "Attack": {
        "name": "Striker",
        "desc": "an Attack Class vessel",
        "speed": "18 km/h horizontal, 12 km/h diving",
        "weapons": "3 coilguns and one electric discharge coil"
    },
    "Transportation": {
        "name": "Carrier",
        "desc": "a Transport Class vessel",
        "speed": "15 km/h horizontal, 10 km/h diving",
        "weapons": "minimal armament for defense"
    }
}

# --- Utility Functions ---
def clear():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def choose_sub():
    """Let the player select a submarine class."""
    choice = input("Choose a class for your sub (Scout, Attack, Transportation): ").strip()
    if choice in SUBMARINES:
        game_state["sub"] = choice
        sub_info = SUBMARINES[choice]
        print(f"\nYour sub is the {sub_info['name']}, {sub_info['desc']} with")
        print(f"max speed of {sub_info['speed']}, armed with {sub_info['weapons']}.")
    else:
        print("INVALID CHOICE")
        game_state["sub"] = None


def event():
    """Trigger an event based on severity polarity."""
    if severity.polarity == 1:
        print("\nTEST GOOD PASS")
    elif severity.polarity == 0:
        print("\nTEST BAD PASS")
    elif severity.polarity == 2:
        print("\nTEST NEUTRAL PASS")
    else:
        print("\nTEST FAILED")


def show_status():
    """Show current submarine status."""
    if game_state["start"] != 1:
        print("")
        stats.status()


def leave():
    """Ask the player if they are ready to undock."""
    choice = input("Are you ready to undock? (Y/N): ").strip().upper()
    if choice == "Y":
        clear()
        show_status()
        print(f"Leaving from {base.outpost}")
    else:
        print("Staying at the outpost...")


# --- Main Entry Point ---
def main():
    choose_sub()
    game_state["start"] = 0
    # Here you can expand to a game loop later


if __name__ == "__main__":
    main()

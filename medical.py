# medical.py - Core health and damage system for crewmembers

# Define damage types (expand as needed)
DAMAGE_TYPES = [
    "blunt",      # e.g., hits, falls
    "burn",       # e.g., fire, hot surfaces
    "piercing",   # e.g., bullets, harpoons
    "explosion",  # e.g., grenades, hull breaches
    "poison",     # e.g., toxins, gas leaks
    # Add more as needed
]

class CrewMember:
    def __init__(self, name, max_health=100):
        self.name = name
        self.max_health = max_health
        self.health = max_health

    def apply_damage(self, amount, damage_type):
        if damage_type not in DAMAGE_TYPES:
            raise ValueError(f"Unknown damage type: {damage_type}")
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: {self.health}/{self.max_health} HP"
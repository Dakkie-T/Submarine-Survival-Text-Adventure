import random

DAMAGE_TYPES = [
    "blunt",      # e.g., hits, falls
    "burn",       # e.g., fire, hot surfaces
    "piercing",   # e.g., bullets, harpoons
    "explosion",  # e.g., grenades, hull breaches
    "poison",     # e.g., toxins, gas leaks
    # Add more as needed
]

class CrewMember:
    def __init__(self, name, role, max_health=100, armor=0):
        self.name = name
        self.role = role
        self.max_health = max_health
        self.health = max_health
        self.armor = armor

    def apply_damage(self, amount, damage_type):
        """Apply damage after checking armor and valid type."""
        if damage_type not in DAMAGE_TYPES:
            raise ValueError(f"Unknown damage type: {damage_type}")

        # Armor reduces damage but not below 0
        actual_damage = max(0, amount - self.armor)
        self.health -= actual_damage

        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        """Heal but not above max_health."""
        self.health = min(self.max_health, self.health + amount)

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        status = "Alive" if self.is_alive() else "Dead"
        return f"{self.name} ({self.role}) - {self.health}/{self.max_health} HP [{status}]"

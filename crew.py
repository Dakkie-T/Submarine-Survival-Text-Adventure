import random

class Weapon:
    def __init__(self, name, damage, damage_type="blunt"):
        self.name = name
        self.damage = damage
        self.damage_type = damage_type

    def __str__(self):
        return f"{self.name} (Damage: {self.damage}, Type: {self.damage_type})"

ROLE_STAT_MODIFIERS = {
    "Captain": {
        "armor": 10,
        "weapon": Weapon("Revolver", damage=25, damage_type="piercing"),
        "initiative": 2,
        "repair_skill": 1,
        "medical_skill": 1,
        "combat_skill": 2
    },
    "Engineer": {
        "armor": 8,
        "weapon": Weapon("Screwdriver", damage=12, damage_type="piercing"),
        "initiative": 1,
        "repair_skill": 3,
        "medical_skill": 1,
        "combat_skill": 1
    },
    "Mechanic": {
        "armor": 12,
        "weapon": Weapon("Wrench", damage=18, damage_type="blunt"),
        "initiative": 1,
        "repair_skill": 2,
        "medical_skill": 1,
        "combat_skill": 2
    }
}

CAPTAIN_NAMES = ["Morgan", "Elias", "Harper", "Quentin", "Rowan"]
ENGINEER_NAMES = ["Sawyer", "Finley", "Jules", "Riley", "Casey"]
MECHANIC_NAMES = ["Blake", "Drew", "Reese", "Hayden", "Parker"]

class CrewMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.max_health = 100
        self.health = 100

        # Apply role modifiers
        role_mods = ROLE_STAT_MODIFIERS.get(role, {})
        self.armor = role_mods.get("armor", 0)
        self.weapon = role_mods.get("weapon", Weapon("Fist", damage=5, damage_type="blunt"))
        self.initiative = role_mods.get("initiative", 0)
        self.repair_skill = role_mods.get("repair_skill", 0)
        self.medical_skill = role_mods.get("medical_skill", 0)
        self.combat_skill = role_mods.get("combat_skill", 0)

        # Barotrauma-like states
        self.bleeding = 0
        self.stun = 0
        self.afflictions = {}

    def apply_damage(self, amount, damage_type=None):
        # Reduce incoming damage by armor, minimum 0
        effective_damage = max(0, amount - self.armor)
        self.health = max(0, self.health - effective_damage)
        print(f"{self.name} took {effective_damage} {damage_type or self.weapon.damage_type} damage (armor reduced by {self.armor}).")
        if self.health <= 0:
            print(f"{self.name} has died!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return (f"{self.name} ({self.role}): HP {self.health}/100, Armor {self.armor}, "
                f"Weapon {self.weapon}, Initiative {self.initiative}, "
                f"Repair Skill {self.repair_skill}, Medical Skill {self.medical_skill}, Combat Skill {self.combat_skill}")

def create_base_crew():
    # Random name selection for each role
    captain_name = random.choice(CAPTAIN_NAMES)
    mechanic_name = random.choice(MECHANIC_NAMES)
    engineer_name = random.choice(ENGINEER_NAMES)
    crew = [
        CrewMember(captain_name, "Captain"),
        CrewMember(mechanic_name, "Mechanic"),
        CrewMember(engineer_name, "Engineer"),
    ]
    return crew

# Example usage for testing:
if __name__ == "__main__":
    crew = create_base_crew()
    for member in crew:
        print(member)

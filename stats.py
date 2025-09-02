class ShipStats:
    def __init__(self, rods=5, condition=100, crew=100, mechanics=100, usage=100, status=0, sub_class=None):
        self.rods = rods              # Torpedo/weapon rods available
        self.condition = condition    # Overall ship health/durability
        self.crew = crew              # Number of crew members
        self.mechanics = mechanics    # Mechanical integrity
        self.usage = usage            # Energy/fuel usage
        self.status = status          # Status flag (customizable)
        self.sub_class = sub_class    # e.g., "Scout", "Attack", "Transport"

    def is_operational(self):
        """Check if the sub can still function."""
        return self.condition > 0 and self.crew > 0

    def apply_damage(self, amount):
        """Damage the ship hull/condition."""
        self.condition = max(0, self.condition - amount)

    def repair(self, amount):
        """Repair the ship but not above 100."""
        self.condition = min(100, self.condition + amount)

    def __str__(self):
        return (
            f"Sub Class: {self.sub_class}\n"
            f"Condition: {self.condition}%\n"
            f"Crew: {self.crew}\n"
            f"Mechanics: {self.mechanics}\n"
            f"Rods: {self.rods}\n"
            f"Usage: {self.usage}%\n"
            f"Status: {self.status}\n"
        )

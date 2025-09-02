class Outpost:
    def __init__(self, name, description="", supplies=None, services=None):
        self.name = name
        self.description = description
        self.supplies = supplies if supplies else {}
        self.services = services if services else []

    def describe(self):
        """Return a text description of the outpost."""
        return f"{self.name}: {self.description}"

    def list_supplies(self):
        """Return available supplies at this outpost."""
        if not self.supplies:
            return "No supplies available."
        return "\n".join([f"{item}: {amount}" for item, amount in self.supplies.items()])

    def list_services(self):
        """Return available services at this outpost."""
        if not self.services:
            return "No services offered."
        return ", ".join(self.services)

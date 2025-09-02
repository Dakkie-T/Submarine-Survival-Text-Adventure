
# severity.py - defines random severity and polarity for events

import random

# Polarity: 0 = bad, 1 = good, 2 = neutral
_polarity_map = {"b": 0, "g": 1, "n": 2}
_severity_map = {"l": 0, "m": 1, "h": 2}

# Randomly choose initial values
_polarity_choice = random.choice(list(_polarity_map.keys()))
_severity_choice = random.choice(list(_severity_map.keys()))

# Expose as module-level variables
polarity = _polarity_map[_polarity_choice]
severity = _severity_map[_severity_choice]

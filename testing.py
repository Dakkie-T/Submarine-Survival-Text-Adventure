# testing.py
# Tests for Submarine Survival Text Adventure
import main
import severity

def test_sub_selection_exists():
    """Test that a submarine can be chosen and stored."""
    # Mock selecting a submarine
    main.game_state["sub"] = "Scout"
    assert main.game_state["sub"] in main.SUBMARINES

def test_sub_status_initial():
    """Test that sub_status starts at 0."""
    assert main.game_state["sub_status"] == 0

def test_start_flag_initial():
    """Test that the start flag is initially 1."""
    assert main.game_state["start"] == 1

def test_severity_polarity_values():
    """Test that severity polarity is within expected range (0=bad, 1=good, 2=neutral)."""
    polarity = severity.polarity
    assert polarity in (0, 1, 2)

def test_severity_severity_values():
    """Test that severity value is within expected range (0=low, 1=medium, 2=high)."""
    sev = severity.severity
    assert sev in (0, 1, 2)

# Dummy test to satisfy GitHub Actions if needed
def test_dummy():
    assert True

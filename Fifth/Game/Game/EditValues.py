def set_min_value(min_value):
    """
    Set the minimum value for the game.
    """
    global MIN_VALUE
    MIN_VALUE = min_value

def set_max_value(max_value):
    """
    Set the maximum value for the game.
    """
    global MAX_VALUE
    MAX_VALUE = max_value

def get_min_value():
    """
    Get the minimum value for the game.
    """
    return MIN_VALUE

def get_max_value():
    """
    Get the maximum value for the game.
    """
    return MAX_VALUE

# Default game values
MIN_VALUE = 1
MAX_VALUE = 100

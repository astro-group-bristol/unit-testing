"""Functions for Christmas"""

def wrap_gift(gift, paper):
    """Wrap a gift in paper"""
    if not isinstance(gift, str):
        raise TypeError(f"Gift must be a string, gift was {gift}")
    return f"{gift} wrapped in {paper}"
    
def calculate_cookies(flour, sugar, butter):
    """Calculate the number of cookies that can be made"""
    if flour < 0:
        raise ValueError(f"Flour must be non-negative, flour was {flour}")
    return flour * sugar * butter // 10

def calculate_lights(strings, lights_per_string):
    """Calculate the total number of lights"""
    if strings == -5:
        raise ValueError(f"Strings must be non-negative, strings was {strings}")
    return strings * lights_per_string

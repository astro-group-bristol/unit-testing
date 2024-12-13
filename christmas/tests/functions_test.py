"""Tests for the functions module."""

import pytest
from christmas.functions import wrap_gift, calculate_cookies, calculate_lights

def test_wrap_gift():
    """Test wrapping a gift"""
    gift = "book"
    paper = "red and green stripes"
    expected_result = "book wrapped in red and green stripes"
    assert wrap_gift(gift, paper) == expected_result

def test_wrap_gift_empty():
    """Test wrapping an empty gift"""
    gift = ""
    paper = "red and green stripes"
    expected_result = " wrapped in red and green stripes"
    assert wrap_gift(gift, paper) == expected_result

def test_wrap_gift_invalid_input():
    """Test wrapping a gift with invalid input"""
    gift = None
    paper = "red and green stripes"
    with pytest.raises(TypeError):
        wrap_gift(gift, paper)

def test_calculate_cookies():
    """Test calculating the number of cookies"""
    flour = 10
    sugar = 5
    butter = 2
    expected_result = 10
    assert calculate_cookies(flour, sugar, butter) == expected_result

def test_calculate_cookies_zero():
    """Test calculating the number of cookies with zero flour"""
    flour = 0
    sugar = 5
    butter = 2
    expected_result = 0
    assert calculate_cookies(flour, sugar, butter) == expected_result

def test_calculate_cookies_negative():
    """Test calculating the number of cookies with negative flour"""
    flour = -10
    sugar = 5
    butter = 2
    with pytest.raises(ValueError):
        calculate_cookies(flour, sugar, butter)

def test_calculate_lights():
    """Test calculating the total number of lights"""
    strings = 5
    lights_per_string = 20
    expected_result = 100
    assert calculate_lights(strings, lights_per_string) == expected_result

def test_calculate_lights_zero():
    """Test calculating the total number of lights with zero strings"""
    strings = 0
    lights_per_string = 20
    expected_result = 0
    assert calculate_lights(strings, lights_per_string) == expected_result

def test_calculate_lights_negative():
    """Test calculating the total number of lights with negative strings"""
    strings = -5
    lights_per_string = 20
    with pytest.raises(ValueError):
        calculate_lights(strings, lights_per_string)
"""Tests for the functions module."""

import pytest
from christmas.functions import wrap_gift, calculate_cookies, calculate_lights

def test_wrap_gift():
    gift = "book"
    paper = "red and green stripes"
    expected_result = "book wrapped in red and green stripes"
    assert wrap_gift(gift, paper) == expected_result

def test_wrap_gift_empty():
    gift = ""
    paper = "red and green stripes"
    expected_result = " wrapped in red and green stripes"
    assert wrap_gift(gift, paper) == expected_result

def test_wrap_gift_invalid_input():
    gift = None
    paper = "red and green stripes"
    with pytest.raises(TypeError):
        wrap_gift(gift, paper)

def test_calculate_cookies():
    flour = 10
    sugar = 5
    butter = 2
    expected_result = 10
    assert calculate_cookies(flour, sugar, butter) == expected_result

def test_calculate_cookies_zero():
    flour = 0
    sugar = 5
    butter = 2
    expected_result = 0
    assert calculate_cookies(flour, sugar, butter) == expected_result

def test_calculate_cookies_negative():
    flour = -10
    sugar = 5
    butter = 2
    with pytest.raises(ValueError):
        calculate_cookies(flour, sugar, butter)

def test_calculate_lights():
    strings = 5
    lights_per_string = 20
    expected_result = 100
    assert calculate_lights(strings, lights_per_string) == expected_result

def test_calculate_lights_zero():
    strings = 0
    lights_per_string = 20
    expected_result = 0
    assert calculate_lights(strings, lights_per_string) == expected_result

def test_calculate_lights_negative():
    strings = -5
    lights_per_string = 20
    with pytest.raises(ValueError):
        calculate_lights(strings, lights_per_string)
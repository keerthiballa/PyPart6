from typing import Iterable, Tuple
import temperature_utils


def convert_kelvin_to_celsius(kelvin_temp: float) -> float:
    """
    Given a float representing a temperature in kelvin, return the corresponding value in celsius.
    :param kelvin_temp: A float representing a temperature in kelvin
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    celsius = kelvin_temp-273.15
    return round(celsius,2)

def convert_kelvin_to_fahrenheit(kelvin_temp: float) -> float:
    """
    Given a float representing a temperature in kelvin, return the corresponding value in fahrenheit.
    :param kelvin_temp:
    :return:
    """
    fahrenheit = 9/5 * (kelvin_temp - 273.15) + 32
    return round (fahrenheit,2)

def convert_celsius_to_kelvin(celsius_temp: float) -> float:
    """
    Given a float representing a temperature in celsius, return the corresponding value in kelvin.
    :param celsius_temp:
    :return:
    """
    kelvin = (celsius_temp) + 273.15
    return round(kelvin, 2)

def convert_fahrenheit_to_kelvin(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in kelvin.
    :param fahrenheit_temp:
    :return:
    """
    kelvin = (fahrenheit_temp - 32) * 5/9 + 273.15
    return round(kelvin, 2)
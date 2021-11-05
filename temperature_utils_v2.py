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

def temperature_tuple_v2(temperatures: Iterable, input_unit_of_measurement: str, output_unit_of_measurement:str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    result=[]
    temp_tuple=tuple()

    for i in temperatures:
        if input_unit_of_measurement == 'c' and output_unit_of_measurement == 'f':
            temp_other_units = temperature_utils.convert_to_fahrenheit(i)

        elif input_unit_of_measurement == 'f' and output_unit_of_measurement == 'c':
            temp_other_units = temperature_utils.convert_to_celsius(i)

        elif input_unit_of_measurement == 'k' and output_unit_of_measurement == 'c':
            temp_other_units = convert_kelvin_to_celsius(i)

        elif input_unit_of_measurement == 'f' and output_unit_of_measurement == 'k':
            temp_other_units = convert_fahrenheit_to_kelvin(i)

        elif input_unit_of_measurement == 'k' and output_unit_of_measurement == 'f':
            temp_other_units = convert_kelvin_to_fahrenheit(i)

        elif input_unit_of_measurement == 'c' and output_unit_of_measurement == 'k':
            temp_other_units = convert_celsius_to_kelvin(i)

        else:
            break

        temp_tuple = (i, temp_other_units)
        result.append(temp_tuple)

    return tuple(result)
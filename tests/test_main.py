import os
# import pytest
from project.main import isOdd, firstPrime
from project.Animals import Cat, Dog

def test_env_loading():
    """Test if the environment variable is being read correctly."""
    # This checks if the logic you wrote to read keys actually returns a string
    api_key = os.getenv("API_KEY")
    assert api_key is not None
    assert isinstance(api_key, str)

def test_math_logic():
    """Example of testing a simple calculation."""
    result = 2 + 2
    assert result == 4

def test_isOdd():
    assert isOdd(3)

def test_firstPrive():
    assert (firstPrime()==  2);

def test_Dog():
    dog = Dog(name="Pluto",city="Walt",age=1930)
    assert (dog.display_info()=="Pluto Walt 1930")
    assert (dog.get_name()=="Dog's name is Pluto")


def test_Cat():
    cat = Cat(name="Garfield",city="Davis",age=1978)
    assert (cat.display_info()=="Garfield Davis 1978")
    assert (cat.get_name()=="Cat's name is Garfield")
"""
Main Function, example only
"""

import os
import json
from dotenv import load_dotenv
from .pets import Dog, Cat


def is_odd(inputted_number):
    """
    Returns whether the inputted number is odd
    """ 
    return inputted_number%2 == 1

def first_prime():
    with open('data/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data["Primes"][0]


cat = Cat(name="Garfield",city="Davis",age=1978)
cat.display_info()
cat.get_name()

dog = Dog(name="Pluto",city="Walt",age=1930)
dog.display_info()
dog.get_name()


# 1. Load the variables from the .env file
load_dotenv()

# 2. Access them using os.getenv()
# Use a default value as a backup if the variable is missing
api_key = os.getenv("API_KEY")
db_url = os.getenv("DATABASE_URL")
is_debug = os.getenv("DEBUG_MODE", "False") == "True"

if api_key:
    print(f"Connected successfully with key: {api_key[:5]}...")
else:
    print("Error: API_KEY not found!")

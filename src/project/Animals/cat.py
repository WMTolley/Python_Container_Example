"""
Part of the animals Module
This contains the Cat class and its related animal values and functions.
"""

class Cat:

    """
    Constructor for Cat Class
    """
    def __init__(self, name: str, city: str, age: int):
        self.name = name      # Instance attribute
        self.city = city      # Instance attribute
        self.age = age        # Instance attribute

    def display_info(self) -> str:
        """
        Outputs the values of the Cat Object
        """
        return f"{self.name} {self.city} {self.age}"

    def get_name(self) -> str:
        """
        Returns the name of the Cat Object
        """
        return f"Cat's name is {self.name}"

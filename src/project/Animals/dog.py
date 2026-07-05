class Dog:

    # Constructor
    def __init__(self, name: str, city: str, age: int):
        self.name = name      # Instance attribute
        self.city = city      # Instance attribute
        self.age = age        # Instance attribute

    def display_info(self) -> str:
        return f"{self.name} {self.city} {self.age}"
    
    def get_name(self) -> str:
        return f"Dog's name is {self.name}"

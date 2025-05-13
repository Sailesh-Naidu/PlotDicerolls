from random import randint

class Die:
    """A class representing a single die"""
    def __init__(self, num_of_sides =6):
        """Assuming the die as 6 sides. It can be changed by passing the value
        of number of sides when creating a die"""
        self.num_of_sides = num_of_sides

    def roll_die(self):
        """return a random value between 1 and the number of
        sides of the die"""
        return randint(1, self.num_of_sides)
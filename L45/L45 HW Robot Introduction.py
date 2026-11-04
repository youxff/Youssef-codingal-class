# Class definition
class Robot:
    def __init__(self, name, model, purpose):
        # Instance attributes
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print("Hello! My name is", self.name)
        print("My model is", self.model)
        print("My purpose is", self.purpose)


# Instantiate the object
robot1 = Robot("RoboMax", "RX-2026", "Helping people with daily tasks")

# Call the method
robot1.introduce()
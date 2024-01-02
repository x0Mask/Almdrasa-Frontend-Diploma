class Cat:
    def __init__(self, name, type, color, age, steps_per_run, steps_per_walk, does_meow):
        self.name = name
        self.type = type
        self.color = color
        self.age = age
        self.steps_per_run = steps_per_run
        self.steps_per_walk = steps_per_walk
        self.does_meow = does_meow

    def runs(self):
        result = f"My name is {self.name}, My type is {self.type}, My color is {self.color}, and I am {self.age} months old.\n"
        result += f"I can run {self.steps_per_run} steps/second."
        print(result)
    
    def walks(self):
        result = f"My name is {self.name}, My type is {self.type}, My color is {self.color}, and I am {self.age} months old.\n"
        result += f"I can walk {self.steps_per_walk} steps/second."
        print(result)

    def meows(self):
        result = f"My name is {self.name}, My type is {self.type}, My color is {self.color}, and I am {self.age} months old.\n"
        result += f"I can {self.does_meow}."
        print(result)
class Cat:
    def __init__(self, name, age, color, type, stepsPerWalk, stepsPerRun):
        self.name = name
        self.age = age
        self.color = color
        self.type = type
        self.stepsPerWalk = stepsPerWalk
        self.stepsPerRun = stepsPerRun

    def walks(self):
        print(f"{self.commonString()} and I walk {self.stepsPerWalk} steps/sec")
    
    def runs(self):
        print(f"{self.commonString()} and I run {self.stepsPerWalk} steps/sec")


    def commonString(self):
        result = f"I am {self.name}, "
        result += f"I am {self.age} months old, "
        result += f"My color is {self.color}, "
        result += f"I am a {self.type} cat, "
        return result


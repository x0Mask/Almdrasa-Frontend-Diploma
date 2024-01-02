class Screwdriver:
    def __init__(self, color, len, type, doesRotate, doesTest):
        self.color = color
        self.len = len
        self.type = type
        self.doesRotate = doesRotate
        self.doesTest = doesTest

    def rotates(self):
        result = f"I am a {self.len} cm {self.color} {self.type} screwdriver"
        if(self.doesRotate):
            print(result + " and I rotate")
        else:
            print(result + " and I don't rotate")

    def testsElectricity(self):
        result = f"I am a {self.len} cm {self.color} {self.type} screwdriver"
        if(self.doesTest):
            print(result + " and I test electricity")
        else:
            print(result + " and I don't test electricity")
            
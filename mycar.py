

class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model
        self.engine = "off"

    def startEngine(self):
        if self.engine == "off":
            print("starting engine")
            self.engine = "on"
        else:
            print("the engine is already running")
    def stopEngine(self):
        if self.engine == "on":
            print("stopping engine")
            self.engine = "off"
        else:
            print("the engine is already off")
    def drive(self):
        if self.engine == "on":
            print("driving the car!")
        else:
            print("the engine needs to be started first")
    def status(self):
        print("Color: " + self.color)
        print("Model: " + self.model)
        print("The engine is " + self. engine)

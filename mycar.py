

class Car:
    def __init__(self):
        self.engine = False

    def startEngine(self):
        if self.engine == False :
            print("starting engine")
            self.engine = True
        else:
            print("the engine is already running")

    def stopEngine(self):
        if self.engine == True:
            print("stopping engine")
            self.engine = False
        else:
            print("the engine is already off")

    def drive(self):
        if self.engine == True:
            print("driving the car!")
        else:
            print("the engine needs to be started first")

    def status(self):
        print("Color: " + self.color)
        print("Model: " + self.model)
        print("The engine is " + str(self.engine))

class BlueCar:
    color = 'Blue'

class Honda(Car, BlueCar):
    make = "Honda"

    def startEngine(self):
        super().startEngine()
        print("Starting the Honda engine!")

class HondaCivic(Honda):
    model = 'Civic'


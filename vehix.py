class Vehicle:

    def __init__(self, color, owner, seats):
        self.color = color
        self.owner = owner
        self.seats = seats

    def drive(self):
        print("Vroom!")

    def turn(self, direction):
        print(f"The vehicle turns {direction}")

    def stop(self):
        print(f"The vehicle has stopped")

class Beetle(Vehicle):

    def __init__(self):
        self.punch_buggie = True

    def drive(self):
        print("Beep Beep!")

    def turn(self, direction):
        print(f"The Beetle turns {direction}")

    def stop(self):
        print(f"The Beetle has halted")

class Jeep(Vehicle):

    def __init__(self):
        self.four_wheel_drive = True

    def drive(self):
        print("RRREEOOOWWW!")

    def turn(self, direction):
        print(f"The Jeep turns {direction}")

    def stop(self):
        print(f"The Jeep putters to an end")

class Corvet(Vehicle):

    def __init__(self):
        self.speed = "very fast"

    def drive(self):
        print("Fffff")

    def turn(self, direction):
        print(f"The Corvet turns {direction}")

    def stop(self):
        print(f"The Corvet cannot stop and will continue to Vvrroom!")

class Elantra(Vehicle):

    def __init__(self):
        self.rating = "5 stars"

    def drive(self):
        print("Hello!")

    def turn(self, direction):
        print(f"The Elantra turns {direction}")

    def stop(self):
        print(f"Joe stopped his car")

class Truck(Vehicle):

    def __init__(self):
        self.bed_size = "4 by 4"

    def drive(self):
        print("Wub wub wub wub")

    def turn(self, direction):
        print(f"The Truck turns {direction}")

    def stop(self):
        print(f"The Truck never moved to begin with")

bug = Beetle()
grand_cherokee = Jeep()
sporty = Corvet()
my_car = Elantra()
chevy = Truck()

bug.drive()
grand_cherokee.drive()
sporty.drive()
my_car.drive()
chevy.drive()

bug.turn("left")
grand_cherokee.turn("left")
sporty.turn("left")
my_car.turn("left")
chevy.turn("left")

bug.stop()
grand_cherokee.stop()
sporty.stop()
my_car.stop()
chevy.stop()


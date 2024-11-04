class Human:

    def __init__(self, name="Human"):
        self.name = name

class Auto:

    def __init__(self, brand):
        self.brand = brand
        self.passengeres = []

    def add_passengeres(self, *args):
        for passengeres in args:
            self.passengeres.append(passengeres)

    def print_passengeres_names(self):
        if self.passengeres !=[]:
            print(f"Names of {self.brand} passengeres: ")
            for passengeres in self.passengeres:
                print(passengeres.name)

        else:
            print(f"Thera no passengeres in {self.brand}. ")

andrei = Human("Andrei")
masha = Human("Masha")
car = Auto("McLaren")
car.add_passengeres(andrei,masha)
car.print_passengeres_names()

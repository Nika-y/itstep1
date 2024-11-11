import random
class Human:
    def __init__(self, name="None", job=None, home=None, car=None, personality_description=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car
        self.personality_description = personality_description

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_personality_description(self):
            self.personality_description = PersonalityDescription(personality_list)

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.selary = job_list[self.job]["gladness_less"]

class PersonalityDescription:
     def __init__(self, personality_list):
        self.description = random.choice(list(personality_list))


brands_of_car = {"Mclaren":{"fuel":100, "strength":100,"consumption": 6},
"Mercedes":{"fuel":50, "strength":40,"consumption": 10},
"Porshe":{"fuel":70, "strength":150,"consumption": 8},
"Ferrari":{"fuel":80, "strength":120,"consumption": 14},}

job_list = {"Java developer":{"salary":50, "gladness_less": 10 },
"Python developer":{"salary":40, "gladness_less": 3 },
"C++ developer":{"salary":45, "gladness_less": 25 },
"Rust developer":{"salary":70, "gladness_less": 1 },}

personality_list = [
    "Introvert",
    "Extrovert",
    "Ambivert",
    "Analytical",
    "Creative",
    "Adventurous"]
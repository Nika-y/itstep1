class Student:
    def __init__(self, name, money=100):
        self.name = name
        self.money = money

    def work(self):
        self.money += 20
        print(f"{self.name} працює і заробляє гроші. Грошей тепер: {self.money}")

    def rest(self):
        if self.money >= 10:
            self.money -= 10
            print(f"{self.name} відпочиває. Грошей тепер: {self.money}")
        else:
            print(f"{self.name} не має достатньо грошей для відпочинку!")

student = Student("Іван")
student.work()
student.rest()

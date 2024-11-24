class МоваПрограмування:
    def __init__(self, ім_я):
        self.ім_я = ім_я

    def вивести_привітання(self):
        print(f"Привіт! Я {self.ім_я} - мова програмування!")

class Python(МоваПрограмування):
    def __init__(self):
        super().__init__("Python")

class Java(МоваПрограмування):
    def __init__(self):
        super().__init__("Java")

class JavaScript(МоваПрограмування):
    def __init__(self):
        super().__init__("JavaScript")

python = Python()
java = Java()
javascript = JavaScript()

python.вивести_привітання()
java.вивести_привітання()
javascript.вивести_привітання()

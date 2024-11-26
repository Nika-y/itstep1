print("Task 2")
def power_of_two():
    n = 0
    while True:
        yield 2 ** n
        n += 1

gen = power_of_two()
for _ in range(10):
    print(next(gen))

print("Task 4")

import random
import string

def random_letters():
    while True:
        yield random.choice(string.ascii_letters)

gen = random_letters()
for _ in range(10):
    print(next(gen))

print("Task 1")

class WordLengthIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        length = len(self.words[self.index])
        self.index += 1
        return length

words = ["The Killers", "Foo Fighters", "Muse", "Blur", "Weezer", "Blink-182"]
iterator = WordLengthIterator(words)

for length in iterator:
    print(length)

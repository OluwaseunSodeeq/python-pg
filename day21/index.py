class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says hello")

    def breath(self):
        print(f"{self.name} is breathing")

class Fish (Animal):
    def __init__(self):
        super().__init__("Fish")
        print("Fish class created")


    def swim(self):
        print(f"{self} is swimming")

demo = Fish()
demo.speak()
demo.breath()
demo.swim()
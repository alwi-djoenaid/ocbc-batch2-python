class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is a dog"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

class Bulldog(Dog):
    pass

    species = "Bulldog"

    def description(self):
        return f"{self.name} is a Bulldog"

dog1 = Bulldog('Brian', 9)
dog2 = Dog('Bolay', 7)

print("Dog 1 = ", dog1.name, dog1.age)
print("Dog 2 = ", dog2.name, dog2.age)

print(dog1.description())
print(dog1.speak("I am a dog"))
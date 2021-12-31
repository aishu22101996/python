class Animal:
    def speak(self):
        print("animal speaking")
class Dog(Animal):
    def bark(self):
        print("dog barking")
class Dogchild(Dog):
    def eat(self):
        print("eating bread")
d=Dogchild()
d.bark()
d.speak()
d.eat()                        
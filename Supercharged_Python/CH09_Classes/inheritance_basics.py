class Mammal:

    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def speak(self):
        print('My name is', name)
    
    def call_out(self):
        self.speak()
        self.speak()
        self.speak()
    
class Dog(Mammal):
    def speak(self):
        print('ARF!!')

class Cat(Mammal):
    def speak(self):
        print('Purrrrrr!!!!!')


my_cat = Cat('Precious', 17.5)
my_cat.call_out()
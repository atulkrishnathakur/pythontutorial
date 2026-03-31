class Computer(object):
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage
        print("Computer class constructor called")

class Mobile(Computer):
    def __init__(self,ram,storage):
        self.mobile = "iphone X"
        super().__init__(ram,storage) # by help of super() use property and method of parent class in child class
        print("mobile class constructor called")


apple = Mobile()
print(apple.__dict__)
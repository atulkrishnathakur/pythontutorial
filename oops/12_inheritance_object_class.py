class Employee(object):  # All classes in python are derrived from a built in `Object` class. If you not write in Employee(object) then it also work. it is default
    bonos = 2000
    def display(self):
        print("This is employee class method")


class Manager(Employee):
    bonus1 = 5000
    def show():
        print("This is manager class method")

e1 = Employee()
m1 = Manager()

print(m1.bonos)


class Employee:
    ''' This is employee class to maintain employee data '''
    def __init__(self,nm,ag):
        self.name = nm
        self.age = ag


print(Employee.__doc__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__) # __main__ value represent for current module




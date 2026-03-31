class Finance:
    def __init__(self):
        self.__revenue = 10000 # private 
        self._number_of_sales = 114 # protected


f1 = Finance()
print(f1.__dict__)


class Hr:
    def __init__(self):
        self.number_of_emp = 32
        print(f1.__revenue)


h1 = Hr()

print(f1.__dict__)
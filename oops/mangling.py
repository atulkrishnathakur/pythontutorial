class Calculation:
    num = 10
    def __init__(self,myname,myage):
        self.name = myname
        self.__age  = myage
    def yourname(self):
        return self.__age
obj = Calculation('Atul',15)
##print(obj.__age) ## can not access outside of class
print(obj.yourname())

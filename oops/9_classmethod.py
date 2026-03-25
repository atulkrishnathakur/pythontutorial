class Employee:
    company_name = "MyComp" # class variable
    def __init__(self,nm,sal):
        self.name = nm
        self.salary = sal

    @classmethod
    def get_company_name(cls):
        print(cls.company_name)
        cls.get_company_name = "Infosys"
        print(cls.company_name)



e1 = Employee("Atul", 21)
e2 = Employee("Krishna",31)

Employee.get_company_name() # access the class method



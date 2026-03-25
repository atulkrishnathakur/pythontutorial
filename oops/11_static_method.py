class Bank:
    bank_name = "BOI"
    rate_of_interest = 12.25

    @staticmethod
    def simple_interest(prin,n): # static method work on external data. here prin and n both are data of object or class because here self or cls not used
        si = (prin*n*Bank.rate_of_interest)/100
        print(si)

prin = float(input("Enter principle amount:"))
n = int(input("Enter number of years:"))
Bank.simple_interest(prin,n) # static method call using class reference

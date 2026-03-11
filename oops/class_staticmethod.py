class Calculation:
    
    @staticmethod
    def sum(a,b):
        r = a + b
        return r
    
    @staticmethod
    def sub(a,b):
        r = a - b
        return r
        
        
r1 = Calculation.sum(10,2)
r2 = Calculation.sub(10,2)
print(r1)
print(r2)
            

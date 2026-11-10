'''
Normally in Python, when you use the simple float data type, the computer stores it in binary (Base 2). Because of this, small errors (called precision errors) happen in calculations.
For example, if you do 0.1 + 0.2 in Python, you do not get 0.3. Instead, you get 0.30000000000000004. The decimal module fixes this exact problem.

'''
from decimal import Decimal

a = 0.1
b = 0.2
c = a + b
print(c) # Output:  0.30000000000000004

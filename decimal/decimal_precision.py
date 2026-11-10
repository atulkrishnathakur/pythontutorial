from decimal import Decimal, getcontext

# Set total precision to 4 digits
#getcontext().prec = 4

result = Decimal('0.1') + Decimal('0.2')
print(result)  # Output: 0.3

result = Decimal('1') / Decimal('3')
print(result)  # Output: 0.3333333333333333333333333333


#************************************************
#  You can control the total number of digits using getcontext().prec
#************************************************
getcontext().prec = 4
result = Decimal('1') / Decimal('3')
print(result)  # Output: 0.3333

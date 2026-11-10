from decimal import Decimal
#******************** example 1 ***************
a = 0.1 + 0.2
print('a=',a)
# Always wrap your numbers in strings when use Decimal().
a = Decimal('0.1') + Decimal('0.2')
print('a=', a)

#******************** example 2 ***************
b = 1.1 + 1.2
print("b=",b)
# Always wrap your numbers in strings when use Decimal().
b = Decimal('1.1') + Decimal('1.2')
print("b=",b)

#******************** example 3 ***************
c = 0.01 + 0.02
print("c=",c)
# Always wrap your numbers in strings when use Decimal().
c = Decimal('0.01') + Decimal('0.02')
print("c=",c)

#******************** example 4 ***************
d = 0.1*0.2
print('d=',d)
# Always wrap your numbers in strings when use Decimal().
d = Decimal('0.1')*Decimal('0.2')
print('d=',d)

#******************** example 5 ***************
e = 1/3
print('e=',e)
# Always wrap your numbers in strings when use Decimal().
# You can control the total number of digits using getcontext().prec
e = Decimal('1')/Decimal('3') 
print('e=',e)

#******************** example 6 ***************
f = 0.1/3
print('f=',f)
# Always wrap your numbers in strings when use Decimal().
f = Decimal('0.1')/Decimal('3')
print('f=',f)


#******************** example 7 ***************
g = 'NaN'
print('g=',g)
# Always wrap your numbers in strings when use Decimal().
g = Decimal('NaN')
print('g=',g)
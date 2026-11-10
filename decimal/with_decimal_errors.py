from decimal import Decimal

print(Decimal(0.1)+Decimal(0.2)) #Output: 0.3000000000000000166533453694

# Always wrap your numbers in strings when use Decimal().
print(Decimal('0.1')+Decimal('0.2')) #Output: 0.3
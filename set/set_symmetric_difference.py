set1 = {10,20,200,50,1000}
set2 = {100,200,300,400,1000}
newset1 = set1 ^ set2 # ^ This is symmetric difference operator in set
newset2 = set1.symmetric_difference(set2) #  use the symmetric_difference() method
print(newset1)
print(newset2)

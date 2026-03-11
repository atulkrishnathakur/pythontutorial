set1 = {10,20,200,50,1000}
set2 = {100,200,300,400,1000}
newset1 = set1 - set2 # - This is difference operator in set
newset2 = set2 - set1
print(newset1)
print(newset2)
newset3 = set1.difference(set2) # use the difference() method
newset4 = set2.difference(set1)
print(newset3)
print(newset4)

set1 = {10,20,200,50,1000}
set2 = {100,200,300,400,1000}
set3 = {1000,2000,3000,200}
newset1 = set1 & set2 & set3 # & is intersection operator
print(newset1)
newset2 = set1.intersection(set2,set3) # use the intersection() method
print(newset2)

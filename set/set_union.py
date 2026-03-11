set1 = {10,20,200,50}
set2 = {100,200,300,400}
set3 = {1000,2000,3000}
newset1 = set1|set2|set3 # | is union operator
print(newset1)
newset2 = set1.union(set2,set3) # use the union() method
print(newset2)

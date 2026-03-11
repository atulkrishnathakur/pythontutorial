my_set = {100,200,'Hi',300,600}
my_set.remove("Hi") # remove() function give error if element not exist
my_set.discard("hello") # discard() function does not give an error if element is not exist
a = my_set.pop() # You do not know which element will be removed by pop() function
print(my_set)
print(a)

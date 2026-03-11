def fun1(a):
   print(a)	
   a = a -1
   if(a > 0): 
      fun1(a)
      
fun1(10)      

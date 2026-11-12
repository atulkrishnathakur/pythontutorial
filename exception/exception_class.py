try:
    print(a)

# write other exception class before `Exception` class because 
# all other class iherites 'Exception'
# If you write 'Exception' before 'NameError' then 'Exception' will be execute not 'NameError'

except NameError as ne:
    print("Variable not defined")

#If you want to catch all exceptions that program(coding) errors, you can use Exception in except.
except Exception as e:
    print("Exception found")      

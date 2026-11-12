# It will execute
print("************Start***************")
try:
    print("before a")
    print(a)

    # It will not execute because it written after exception error statment
    print("after a")

except Exception as e:
    print("Exception details: ",e)

# It will execute because exception handled
# And it written out of try and except
print("**********End************")
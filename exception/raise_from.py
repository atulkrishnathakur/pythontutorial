def divide(a, b):
    try:
        return a / b
    except Exception as ex:
        raise ValueError('b must not be zero') from ex


try:
    divide(10, 0)
except Exception as ex:
    print('cause:', ex.__cause__) # It show the reason of error if you use in 'from' in divide() function definition
    print('exception:', ex) # it show the message that you raise in divide() function
def divide(a, b):
    try:
        return a / b
    except Exception as ex:
        raise ValueError('b must not be zero') from None


try:
    divide(10, 0)
except Exception as ex:
    print('cause:', ex.__cause__) # It hide the reason because 'from None' used when raise exception
    print('exception:', ex) # it show the message that you raise in divide() function
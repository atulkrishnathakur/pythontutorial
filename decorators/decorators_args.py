def sichange(func):
    def wrapper(*args):
        interest = func(*args)
        return interest + args[0]
    return wrapper

@sichange
def si(p,r,t):
    return (p*r*t)/100


print(si(100,2,5))
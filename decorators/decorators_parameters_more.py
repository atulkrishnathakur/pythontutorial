
def sichange(func):
    def wrapper(p,r,t):
        interest = func(p,r,t)
        return interest + p
    return wrapper

@sichange
def si(p,r,t):
    return (p*r*t)/100


print(si(100,2,5))
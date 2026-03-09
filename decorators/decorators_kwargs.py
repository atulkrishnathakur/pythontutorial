def sichange(func):
    def wrapper(**kwargs):
        interest = func(**kwargs)
        return interest + kwargs["p"]
    return wrapper

@sichange
def si(p,r,t):
    return (p*r*t)/100

print(si(p=100,r=2,t=5))
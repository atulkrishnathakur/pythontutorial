def wrapper(f):
    def fun(l):
        outlist = []
        for i,num in enumerate(l):
            numlist = list(num)
            if(len(numlist) > 10 and numlist[0] == "0"):
                numlist[0] = "+91 "
                numlist.insert(6," ")
                res1 = "".join(numlist)
                outlist.insert(0,res1)
            elif(len(numlist) == 10):
                numlist.insert(0,"+91 ")
                numlist.insert(6," ")
                res2 = "".join(numlist)
                outlist.insert(2,res2)
            elif(len(numlist) > 10 and numlist[0] == "9" and numlist[1] == "1"):
                numlist[0] = "+9"
                numlist[1] = "1 "
                numlist.insert(7," ")
                res3 = "".join(numlist)
                outlist.insert(1,res3)
        
        outlist.sort()
        for _,mob in enumerate(outlist):
            print(mob)
            
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 




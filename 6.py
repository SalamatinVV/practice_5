def mostchar(x) :
    c=0
    ans=""
    for i in x.lower() :
        if (c<x.count(i)):
            c=x.count(x)
            ans=i
    return ans
x=input ("sd")
print (mostchar(x.lower()))
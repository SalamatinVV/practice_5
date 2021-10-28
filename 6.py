p= str(input("Введите текст").lower())
x=list(p)
def sog(c=int(0), j=int(0),z=int(0)):
    for i in x:
        sogl = "qwrtypsdfghjklzxcvbnmeyuioa`~1234567890-=]['/\.;,l"
        l = list(sogl)
        k = l[c].count(x[c])
        c += 1
        if k == 1:
            j += 1
    print(j)
sog()

press = int(input("Выберите функцию(1-гласные, 2-согласные)"))
p= str(input("Введите текст").lower())
x=list(p)

def gl(c=int(0), j=int(0)):
        for i in x:
            gll = "eyuioa"
            l = list(gll)
            k = l.count(x[c])
            c += 1
            if k == 1:
                j += 1

        print(j)
def sog(c=int(0), j=int(0)):
        for i in x:
            sogl = "qwrtypsdfghjklzxcvbnm"
            l = list(sogl)
            k = l.count(x[c])
            c += 1
            if k == 1:
                j += 1

        print(j)
if press== 1 : gl()
elif press == 2: sog()
else : print ("1 или 2")

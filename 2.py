x=[]
y=[]
z=[]

s=[x,y,z]
for i in range (3) :
    a=int(input("Chisla v 1 stroke:"))
    x.append(a)
for i in range (3) :
    a=int(input("Chisla vo 2:"))
    y.append(a)
for i in range (3) :
    a=int(input("Chisla v 3:"))
    z.append(a)
[print(*line) for line in s]
i=0
k=0
c=0
enb=(s[0][0] + s[1][1]+ s[2][2])
if (s[2][0] + s[1][1]+ s[0][2])==enb :
    c+=1

while i<=2 :

    if (s[i][k] + s[i][k+1] + s[i][k+2])==enb :
        c+=1
        i+=1
    else:
        break
i=0
while k<=2 :
    if (s[i][k] + s[i+1][k] + s[i+2][k])==enb :
        c+=1
        k+=1
    else:
        break
if c==7 :
    print ("mag")
else: print ("ne mag")
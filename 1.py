def func(s=[], n=int(input("chisli n:"))):
    print(' для окончания ввода просто напишите 0')
    a = int(input('-->> '))
    while True:
        if a==0 :
           break
        else :
            s.append(a)
            a = int(input('-->> '))
    for i in s:
        if n < i:
            print(i)

f = func ([]);


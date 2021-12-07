#liczy n-ty wyraz ciągu Fibonacciego

def wyraz_f(n):
    if n<3:
        return 1
    else:
        return wyraz_f(n-1)+wyraz_f(n-2)

def wyraz_F(n):
    if n<3:
        return 1
    else:
        a=b=1
        for i in range(n-2):
            a, b=b, a + b
        return b





for n in range(1, 101):
    print(n, wyraz_F(n))

def gcd(a_1,b_1):
    a_2,b_2=a_1,b_1
    x1,y1=1,0
    x2,y2=0,1
    while b_2!=0:
        q=a_2//b_2
        a_2,b_2=b_2,a_2-q*b_2
        x1,y1=y1,x1-q*y1
        x2, y2 = y2, x2 - q * y2
    return f"{x1}*{a_1}+({x2}*{b_1})={a_2}"
n=int(input('введите первое число: '))
m=int(input('введите второе число: '))
print(gcd(n,m))

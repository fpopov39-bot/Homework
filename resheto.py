def prime(number):
    if number<2:return 0
    for i in range(2,int(number**0.5)+1):
        if number%i==0:return 0
    return True
def f(n):
    a=[]
    for i in range(2,n+1):
        if prime(i):
            a.append(i)
    return a
n=int(input("введите число:"))
print(f(n))
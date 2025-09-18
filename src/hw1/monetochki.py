def razmen(n):
    d,h,j='-42!','Кол-во монет по 5: ','Кол-во монет по 9: '
    if n<1:return 0
    elif n%5==0:return h+str(n//5)
    elif n%9==0:return j+str(n//9)
    elif n>=32 and n%10<5:return j+str(5-n%10)+' и '+h+str((n-9*(5-n%10))//5)
    elif n>=32:return j+str(10-n%10)+' и '+h+str((n-9*(10-n%10))//5)
    elif 10<=n<=29 and (n%10==9 or n%10==4):return j+'1 и '+h+str((n-9)//5)
    elif n==23 or n==28:return j+'2 и '+h+str((n-18)//5)
    else:return d
n=int(input('Ваше кол-во монет: '))
print(razmen(n))
#14) 19) 23¿ 24) 28¿ 29)
#Федор(5букв)=Попов(5букв)

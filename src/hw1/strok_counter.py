def obrat(a,b):
    first=[ord(strok) for strok in a]
    second=[ord(strok) for strok in b]
    for i in range(min([len(a),len(b)])):
        char1=first[i]
        char2=second[i]
        if char1!=char2:return char1-char2
    
    return len(b)-len(a)
def answer(k,p):
    if obrat(k,p)>0:return 'строка «'+k+ '» < '+'строки «'+p+'»'
    elif obrat(k,p)<0:return 'строка «'+k+ '» > '+'строки «'+p+'»'
    return 'строка «'+k+ '» = '+'строке «'+p+'»'
n=str(input('введите первую строку: '))
m=str(input('введите вторую строку: '))
print(answer(n,m))

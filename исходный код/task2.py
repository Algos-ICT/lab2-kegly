f=open('input.txt')
line=f.readline()
l=[1]
last=0
count=0 #считаем количество перестановок одного числа
a=list(map(int, line.split()))

for i in range(1,len(a)):
    for k in range(i,0,-1):
        if a[k-1]>a[k]:
            a[k], a[k-1] = a[k-1], a[k]
            last=k # запомниться последний индекс после перестановок
            count+=1
    if count==0:  # если число осталось на месте запоминаем его изначальный номер
        l+=[i+1]
    else: # иначе номер после последней перестановки
        l+=[last]
    count=0
   
file=open('output.txt', 'w')
for i in l:
    file.write(str(i)+' ')
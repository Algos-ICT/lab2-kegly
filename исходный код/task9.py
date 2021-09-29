f=open('input.txt')
a, b = input().split() # считали два двоичных числа
arr1=[]+a # занесли первое число в n-битовый массив
arr2=[]+b # анесли второе число в n-битовый массив
v1=''
v2=''
for i in arr1:  # обратно создаем 2 строки с двочными числами
    v1+=arr1[i]
for i in arr2:
    v2+=arr2[i]
sum=int(v1,2)+int(v2,2)
sum=bin(sum) # перевели сумму в двоичную СС
sum=sum[2:len(sum)] #убрали префикс 0b с помощью среза
l=list()
l+=sum #занесли сумму в (n-1)-элементный масссив
file=open('output.txt', 'w')
file.write(sum)
file.close()

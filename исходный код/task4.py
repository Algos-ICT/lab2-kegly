file=open('input.txt')
line=file.readline()
a=list(map(int, line.split())) 
V=int(file.readline()) # число которое надо найти
result=list() # список нужных индексов
f=open('output.txt', 'w')
for i in range(len(a)):
    if a[i]==V:
        result+=[i]
if(len(result)==0): # если не нашлось V
    f.write('-1')
else:
    f.write(str(len(result))+'\n') #количество V в списке
    for i in result:
        f.write(str(i)+',') #сами индексы
  
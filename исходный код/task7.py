file=open('input.txt')
line=file.readline()
a=list(map(int,line.split()))
b=sorted(list(a)) # хранит отсортированный переданный список

f=open('output.txt', 'w')

f.write(str(a.index(min(b))+1)+' ')  #индекс наименьшего значения ...
f.write(str(a.index(b[len(a)//2])+1)+ ' ') # среднего
f.write(str(a.index(max(b))+1)) # максимального

f.close()


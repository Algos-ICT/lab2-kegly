file=open('input.txt')
line=file.readline()
a=list(map(int,line.split()))
for i in range(len(a)):
    for k in range(len(a)-i-1):
        if a[k]>a[k+1]:
            a[k], a[k+1] = a[k+1], a[k]
f=open('output.txt', 'w')
for i in a:
    f.write(str(i)+' ')
f.close()

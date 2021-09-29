f=open('input.txt')
line1=f.readline()
line2=f.readline()
a=list(map(int, line2.split()))
for i in range(1,len(a)):
    for k in range(i,0,-1):
        if a[k-1]<a[k]:
            a[k], a[k-1] = a[k-1], a[k]
file=open('output.txt', 'w')
for i in a:
    file.write(str(i)+' ')


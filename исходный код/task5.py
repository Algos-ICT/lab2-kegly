file=open('input.txt')
line=file.readline()
A=list(map(int,line.split()))

#temp=list()
#for i in range(len(A)):
#    temp+=[min(A)]
#    A.remove(min(A))
#print(temp)

for i in range(len(A)-1):
    for k in range(i+1, len(A)):
        if A[k]<A[i]:
            A[k], A[i] = A[i], A[k]
f=open('output.txt', 'w')
for i in A:
    f.write(str(i)+' ')
f.close()

f=open('input.txt')
line1=f.readline()
line2=f.readline()
arr1=list(map(int, line1.split()))
arr2=list(map(int, line2.split()))
v1=''
v2=''
for i in arr1:
    v1+=str(arr1[i])
for i in arr2:
    v2+=str(arr2[i])
sum=int(v1,2)+int(v2,2)
sum=bin(sum)
sum=sum[2:len(sum)]
l=list()
l+=sum
print(l)
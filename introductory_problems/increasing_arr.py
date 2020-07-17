n= int(input())
t = 0
l=[int(j) for j in input().split(" ")]
for i  in range(1,n):
    if l[i]<l[i-1]:
        t = t + l[i-1]-l[i]
        l[i]=l[i-1]
print(t)
s = input()
d={}
res = list(i for i in s)
for i in s:
    d[i]= d.get(i,0)+1
c=0
for k,v in d.items():
    if v%2!=0:
        c+=1
if c>1:
    print("NO SOLUTION")
else:
    p=0
    for k,v in d.items():
        if v%2!=0:
            res[int(len(res)/2)]=k    
        for i in range(0,int(v/2)):
            res[p]=k
            res[len(res)-1-p]=k
            p+=1
    print("".join(res))
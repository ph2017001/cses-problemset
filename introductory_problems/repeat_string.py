s=input()
l,m=1,1
for j in range(1, len(s)): 
    if s[j]==s[j-1]:
        l+=1
    else:
        if l>=m:
            m=l
        l=1
if l > m:
    m=l
print(m)
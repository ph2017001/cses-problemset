# t = int(input())
# for i in range(0,t):
#     a = input().split(" ")
#     y = int(a[0])
#     x = int(a[1])
#     n = max(y,x)
#     if n%2 == 0:
#         print(n*n - x + y - n + 1)
#     else:
#         print(n*n - y + x - n + 1)
t = int(input())
while t:
    a = input().split(" ")
    n = max(int(a[1]),int(a[0]))
    if n%2 == 0:
        print(n*n - int(a[1]) + int(a[0]) - n + 1)
    else:
        print(n*n - int(a[0]) + int(a[1]) - n + 1)
    t-=1
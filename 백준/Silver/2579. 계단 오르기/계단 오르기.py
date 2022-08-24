n = int(input())
lst = [int(input()) for i in range(n)]

d=[]

d.append(lst[0])
if n>=2:
    d.append(lst[0]+lst[1])
if n>=3:
    d.append(max(lst[0]+lst[2], lst[1]+lst[2]))

for i in range(3, n):
    d.append(max(d[i-2] + lst[i] , d[i-3] + lst[i] + lst[i - 1]))

print(d[n-1])
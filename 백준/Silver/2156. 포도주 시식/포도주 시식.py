n = int(input())

w_list = []
for i in range(n):
    w_list.append(int(input()))

d = []
d.append(w_list[0])
if n > 1:
    d.append(w_list[0]+w_list[1])
    
if n > 2:
    d.append(max(d[1], w_list[0]+w_list[2], w_list[1]+w_list[2]))

for i in range(3, n):
    d.append(max(d[i-1], d[i-3]+w_list[i-1]+w_list[i], d[i-2]+w_list[i]))

print(d[n-1])
n = int(input())
arr = list(map(int, input().split()))

max_sum=[arr[0]]

for i in range(n-1):
    max_sum.append(max(max_sum[i] + arr[i + 1], arr[i + 1]))

print(max(max_sum))
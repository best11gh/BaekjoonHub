x, y = map(int, input().split())

month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

days=0

for i in range(1, x):
    days += month_list[i - 1]

days += y

print(week_list[days % 7])
    
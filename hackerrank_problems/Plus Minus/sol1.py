n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

total_positive = len([i for i in arr if i > 0])
total_negative = len([i for i in arr if i < 0])
total_zero = len([i for i in arr if i == 0])

print(format(total_positive, '.6f'))
print(format(total_negative, '.6f'))
print(format(total_zero, '.6f'))

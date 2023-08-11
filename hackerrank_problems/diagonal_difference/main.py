array_2d = list()

array_length = int(input())

for i in range(array_length):
    rows = list(map(int, input().rstrip().split()))
    array_2d.append(rows)
left_diagonal_sum = 0
right_diagonal_sum = 0
for i in range(array_length):
    left_diagonal_sum += array_2d[i][i]
    right_diagonal_sum += array_2d[i][array_length-i-1]
print(abs(left_diagonal_sum-right_diagonal_sum))
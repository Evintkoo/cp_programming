arr = list(map(int, input().rstrip().split()))

sum_arr = sum(arr)

min_val = min([sum_arr - i for i in arr])
max_val = max([sum_arr - i for i in arr])

print(min_val, max_val)
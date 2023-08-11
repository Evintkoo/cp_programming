arr = list(map(int, input().rstrip().split()))
sum_arr = sum(arr)
min_val = 10**12 # maximum number possible
max_val = 0 # minimum number possible
for i in arr:
    cur_sum = sum_arr - i
    min_val = min(cur_sum, min_val)
    max_val = max(cur_sum, max_val)
print(min_val, max_val)
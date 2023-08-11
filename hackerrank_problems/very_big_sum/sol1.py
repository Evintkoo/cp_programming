len_arr = int(input())
arr = list(map(int, input().rstrip().split()))
big_sum = 0
for i in arr:
    big_sum += i
print(big_sum)
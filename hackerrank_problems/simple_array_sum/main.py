arr_len = int(input())
arr = list(map(int, input().rstrip().split()))
sum = 0
for i in arr:
    sum += i
print(sum)
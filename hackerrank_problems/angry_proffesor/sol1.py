
t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))
    for i in a:
        if i <= 0:
            k -= 1
    if k > 0:
        print("YES")
    else: 
        print("NO")

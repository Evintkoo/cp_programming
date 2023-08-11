
t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))
    
    on_time_student = [i for i in a if i <= 0]
    
    print("YES") if k-len(on_time_student) > 0 else print("NO")

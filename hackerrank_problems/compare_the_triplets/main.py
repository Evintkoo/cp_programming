arr = list(map(int, input().rstrip().split()))
arr2 = list(map(int, input().rstrip().split()))

alice_point = 0
bob_point = 0

for i1, i2 in zip(arr,arr2):
    if i1 > i2:
        alice_point += 1 
    elif i2 > i1:
        bob_point += 1

print(alice_point, bob_point)
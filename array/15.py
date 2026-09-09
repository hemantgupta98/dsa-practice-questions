n = int(input())

arr = list(map(int, input().split()))


result = []

for num in arr:
    if num != 0:
        result.append(num)

# Add zeros at the end
while len(result) < n:
    result.append(0)

print(*result)
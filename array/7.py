# move to all zero in end
arr = list(map(int, input("Enter your element : ").split()))

index = 0

for i in range(len(arr)):
      if arr[i] != 0:
            arr[index], arr[i] = arr[i] , arr[index]
            index += 1

print("Move all zero in end", arr)            
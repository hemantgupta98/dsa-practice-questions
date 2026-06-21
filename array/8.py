# Remove duplicates from sorted array 
arr = list(map(int , input("Enter you sorted elements : ").split()))

index = 0

for i in range(1, len(arr)):
      if arr[i] != arr[index]:
            index += 1
            arr[index] = arr[i]

print("sorted element : ", arr[:index + 1])            
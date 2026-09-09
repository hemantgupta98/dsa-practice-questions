arr1 = list(map(int, input("Enter your first set : ").split()))
arr2 = list(map(int, input("Enter your Second set : ").split()))

result = set(arr1).intersection(arr2)

print("Intersection", *result)
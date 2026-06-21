# sorted list

arr = list(map(int , input("Enter your elements : ").split()))

arr.sort(reverse=True)
print("Decending Sorted array", arr)

arr.sort()
print("Accending Sorted array", arr)
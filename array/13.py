# intersection of two arrays

arr1 = list(map(int , input("Enter first set : ").split()))
arr2 = list(map(int , input("Enter second set : ").split()))

intersection = set(arr1).intersection(arr2)

print("Intersection elements : ", *intersection)
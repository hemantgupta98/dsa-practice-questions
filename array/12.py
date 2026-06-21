# 	Find union of two arrays 

arr = list(map(int , input("Enter your first set : ").split()))
arr2 = list(map(int , input("Enter your second set : ").split()))

union = set(arr) | set(arr2)
print("Union element : ", *union)
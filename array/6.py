# k rotationm left
n = list(map(int , input("Enter your element : ").split()))

k = int(input("Enter you k postion : "))

k = k % len(n)

arr = n[k:] + n[:k]
print("Rotated element", arr)
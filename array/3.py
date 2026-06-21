# second largest

n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest element =", second_largest)
n = int(input("Enter a number: "))

count = 0

while n > 0:
      digit = n % 10
      count += digit
      n = n // 10

print("Total sum = ", count)      

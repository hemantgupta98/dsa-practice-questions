def digit_sum(n):
      if n == 0:
            return 0
      return (n % 10) + digit_sum(n // 10)

n = int(input("Enter your number: "))
print("Digit Sum = ", digit_sum(n))
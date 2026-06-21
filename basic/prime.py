# check number is prime or not

a = int(input("Enter a number : "))

if a <=1:
      print("Number must be greater of 1")
else:
      is_Prime = True
      for i in range(2 , int(a ** 0.5) + 1):
            if(a % i == 0):
                 is_Prime = False
                 break

      if is_Prime:
            print("It is prime number")
      else:
            print("Not prime number")      
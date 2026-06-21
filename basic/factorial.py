# factorial



a = int(input("Enter you number : "))
fact = 1

for i in range(1 , a + 1):
      fact *= i
      
print("fact", fact)  

def factorial(n):
      fac = 1 
      for i in range(1 , n + 1):
            fac *= i
      return fac
      
      
print(factorial(5))


# 	Find missing number 
arr = list(map(int , input("Enter your element : ").split()))
n = int(input("Enter your N value : "))

for i in range(1 , n + 1):
      if i not in arr:
            print("Missing number : ", i)
            break
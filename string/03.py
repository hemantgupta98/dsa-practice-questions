n = input("Enter your string : ")

for char in n:
      if n.count(char) == 1:
            print("Non repeating character ", char)
            break
else:
      print("No found") 
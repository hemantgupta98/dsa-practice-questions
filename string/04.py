n = input("Enter your string : ")
res = []

for char in n:
      if n.count(char) > 1 and char not in res:
            res.append(char)
            
if res:
      print("Duplicates", res)
else:
      print("No found")


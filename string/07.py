s = input("Enter your string : ")
result = ""

for char in s:
      if char not in result:
            result += char


print("Answer : ", result)            
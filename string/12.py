str1 = input("Enter your string : ")
str2 = input("Enter your second string : ")

if len(str1) == len(str2) and str2 in (str1 + str1):
      print("Rotated")
else:
      print("Not rotated")
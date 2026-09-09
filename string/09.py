s = input("Enter your string : ")
frequncy = {}

for char in s:
      if char in frequncy:
            frequncy[char] += 1
      else:
            frequncy[char] = 1

for char in frequncy:
      print(char , "->" , frequncy[char])            
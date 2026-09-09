n = input("Enter your string : ")

vowel = 0
constanat = 0
digit = 0
special = 0

for char in n:
      if char.isalpha():
            if char.lower() in "aeiou":
                  vowel += 1
            else:
                  constanat += 1

      elif char.isdigit():
            digit += 1
      else:
            special += 1

print("Vowels", vowel)
print("Constant", constanat)
print("Digit", digit)
print("specail", special)
                                
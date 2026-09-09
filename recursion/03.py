def reverse_string(s):
      if len(s) <= 1:
            return s
      return s[-1] + reverse_string(s[:-1])

s =  input("Enter your string: ")
print("Reverse string = ", reverse_string(s))
      
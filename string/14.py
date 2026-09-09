s = input("Enter your string : ")
words = s.split()
duplicates = []

for word in words:
      if words.count(word) > 1 and word not in duplicates:
            duplicates.append(word)

            
print("Duplicates", duplicates)              
# find duplicate number

arr = list(map(int , input("Enter your element : ").split()))

seen = set()
duplicate = set()

for i in arr:
      if i in seen:
            duplicate.add(i)
      else:
            seen.add(i)

if duplicate:
      print("Duplicate number : ", duplicate)
else:
      print("Not any duplicate element")
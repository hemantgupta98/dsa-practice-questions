#smallest element

numbers = [4,5,69,8,6,2]

smallest = numbers[0]

for num in numbers:
      if num < smallest:
            smallest = num
            break
print("Samllest element : ", smallest)      
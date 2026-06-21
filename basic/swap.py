# First type

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

temp = a
a = b
b = temp

print("A after swaping :" , a)
print("B after swaping : ", b)

# second type 

a = 9 
b = 4

a , b = b , a
print("Ater swaping", a)
print("Ater swaping", b)
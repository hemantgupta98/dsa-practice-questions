# prymarid
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()
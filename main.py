import random as rd

height = int(input("Height?"))
char = input("Char?")

for i in range(height):
    print((height - i) * " " + (2 * i + 1) * char)

## if else

a = [1,2,3,4,5]
rd.shuffle(a)
print(a)
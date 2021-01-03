# Exercise 33: Sort Three Integers

num1, num2, num3 = map(int, input("Please enter three integers: ").split())

smallest = min(num1, num2, num3)
biggest = max(num1, num2, num3)

middle = num1+num2+num3 - smallest - biggest

print("The numbers from smallest to largest are:")
print(smallest, middle, biggest)
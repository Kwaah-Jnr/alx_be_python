number = int(input("Enter a number to see its multiplication:"))

print(f"The multiplication table for {number} is:")

for i in range(1,11):
  product = number * i
  print(f"{number} * {i} = {product}")



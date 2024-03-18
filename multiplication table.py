

num = int(input("Enter the number for which you want the multiplication table: "))
limit = int(input("Enter the limit for the multiplication table: "))


print(f"Multiplication table for {num} :")
for i in range(1, limit + 1):
    result = num * i
    print(f"{num} x {i} = {result}")
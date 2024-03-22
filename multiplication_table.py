num = int(input("enter the number for which you want the multiplication table : "))
limit = int(input("enter the limit of number you want to multiply:"))
print(f"the multiplication of {num} till {limit} is:")
for i in range(limit+1):
    print(f"{num}*{i} = {int(num)}")
print("Enter 3 numbers")
a, b, c = int(input(">>>")), int(input(">>>")), int(input(">>>"))
set1 = {a, b, c}
if a > b and a > c:
    print(f"{a} is the largest number in the set {set1}")
elif b > c and b > a:
    print(f"{b} is the largest number in the set {set1}")
else:
    print(f"{c} is the largest number in the set {set1}")

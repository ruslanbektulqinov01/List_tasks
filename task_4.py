k = int(input("butun son : "))
num = int(input("son kiriting, 0 kiritilsa tugaydi: "))
counter = 0
while (num > 0):
    if num < k:
        counter += 1
    num = int(input("son kiriting, 0 kiritilsa tugaydi: "))

print(counter)

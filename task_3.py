a = int(input("Dastlabki hadni kiriting: "))
d = int(input("Ayirmani kiriting: "))
n = int(input("Hadlar sonini kiriting: "))
arif_prog = [i for i in range(a, (a + (n - 1) * d) + 1, 6) if a > 1]
print(arif_prog)

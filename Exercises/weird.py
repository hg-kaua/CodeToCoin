n = int(input("type a number: "))
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n >= 2 and n <= 5:
    print("Not Weird")
elif n >= 6 and n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

# another exercise
j = int(input())
count = 0
for i in range(j):
    count = i
    print(count**2)
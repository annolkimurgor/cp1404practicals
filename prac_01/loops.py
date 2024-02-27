for i in range(1, 21, 2):
    print(i, end=' ')
print()


# a. count in 10s from 0 to 100
i = 0
while i <= 100:
    print(i)
    i += 10


# b. count down from 20 to 1
i = 20
while i >= 1:
    print(i)
    i -= 1


# c. print n stars
n = int(input("Enter a number: "))
for i in range(n):
    print("*", end="")
print()


# d. print n lines of increasing stars.
n = int(input("Enter a number: "))
i = 1
while i <= n:
    print("*" * i)
    i += 1
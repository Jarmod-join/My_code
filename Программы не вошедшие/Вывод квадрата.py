while True:
    num1 = int(input("Number first: "))
    num2 = int(input("Number second: "))
    if num1 > 0 and num2 > 0:
        break
    else:
        print("error, retry your numbers!")

for i in range(num1):
    print("I  " * num2)

print("it mean:", num1 * num2, "e.d.c.")
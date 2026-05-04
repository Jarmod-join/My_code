def math(num,ch):
    if num % 2 == 0:
        num //= 2
        ch += 1

    else:
        num = num * 3 + 1
        ch += 1

    return num,ch

chek = 0
number = None

while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Error, please enter a number.")
        continue

while True:
    number,chek = math(number,chek)
    print(number)
    if number == 1:
        print("Finally! All try:", chek)
        break
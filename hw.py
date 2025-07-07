decimal_number = int(input("Enter a decimal number: "))


if decimal_number == 0:
    print("Binary representation: 0")
else:
    binary = ""

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary = str(remainder) + binary
        decimal_number = decimal_number // 2

    print("Binary representation:", binary)
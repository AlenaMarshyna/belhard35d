def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary


def binary_to_decimal(binary):
    decimal = 0
    for i in binary[::-1]:
        decimal += int(i)
        decimal *= 2
    return decimal


def binary_to_decimal2(binary):
    decimal = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2 ** i
    return decimal


print(binary_to_decimal2(decimal_to_binary(decimal=18)))

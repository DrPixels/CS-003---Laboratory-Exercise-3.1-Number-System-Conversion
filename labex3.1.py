fromConversion = input("From [Decimal, Binary, Octal, Hexadecimal]: ")
fromValue = input(f"Enter the {fromConversion} value: ")
toConversion = input("To: [Decimal, Binary, Octal, Hexadecimal]: ")

input_base = {
    "decimal": 10,
    "binary": 2,
    "octal": 8,
    "hexadecimal": 16
}[fromConversion.lower()]

def to_decimal(value: str, base):

    #For Hexadecimal Digit
    hex_value = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,       
    }

    total_value = 0
    n = len(value)

    for index, x in enumerate(value, start = 1):
        current_exponent = n - index

        if x.isdigit():
            digit_value = int (x)
            
        else:
            digit_value = hex_value[x]
        
        total_value += digit_value * (base ** current_exponent) 
    
    return total_value

print(to_decimal(fromValue, input_base))


def to_othersystem():
    pass

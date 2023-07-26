HEX_DIVIDER = 16
HEX_ARRAY = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
user_int_number = int(input("Please enter int number: "))


def convert_int_to_hex(int_number: int, hex_divider: int, hex_array: list) -> str:
    str_hex_number = ''
    while int_number > 0:
        str_hex_number += str(hex_array[(int_number % hex_divider)])
        int_number //= hex_divider
    str_hex_number = str_hex_number[::-1]
    return str_hex_number


print(hex(user_int_number), convert_int_to_hex(user_int_number, HEX_DIVIDER, HEX_ARRAY))

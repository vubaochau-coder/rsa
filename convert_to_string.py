import binascii
def ConvertToStr(integer_value):
    hex_string = '0x{:x}'.format(integer_value)
    return binascii.unhexlify(hex_string[2:]).decode('unicode-escape')
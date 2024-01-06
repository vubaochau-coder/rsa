import binascii

def ConvertToStr(integer_value):
    hex_from_int = hex(integer_value)[2:]
    if len(hex_from_int) % 2 != 0:
        hex_from_int = '0' + hex_from_int
    byte_value = binascii.unhexlify(hex_from_int)
    return byte_value.decode('utf-8', errors='backslashreplace')
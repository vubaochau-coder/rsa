import binascii
def ConvertToInt(message):
    a = binascii.hexlify(message.encode('cp1258', errors='backslashreplace'))
    integer_value = int.from_bytes(binascii.unhexlify(a), byteorder='big')
    return integer_value
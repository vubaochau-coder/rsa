import binascii

def ConvertToInt(message):
    hex_from_byte = binascii.hexlify(message.encode('utf-8')).decode('utf-8')
    integer_value = int(hex_from_byte, 16)
    return integer_value
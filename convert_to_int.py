import binascii
def ConvertToInt(message): #Base on UTF-8
    a = binascii.hexlify(message.encode('cp1258', errors='backslashreplace'))
    print(a)
    integer_value = int.from_bytes(binascii.unhexlify(a), byteorder='big')
    return integer_value

if __name__ == "__main__":
    a = ConvertToInt("hello")
    print(a)
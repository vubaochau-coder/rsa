from convert_to_int import ConvertToInt
from pow_mod import PowMod

def encrypt(msg, e, n):
    C = PowMod(msg,e,n)
    return C
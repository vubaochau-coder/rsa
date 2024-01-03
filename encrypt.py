from convert_to_int import ConvertToInt
from pow_mod import PowMod

def encrypt(message,e,n):
    msg = ConvertToInt(message);
    C = PowMod(msg,e,n);
    return C
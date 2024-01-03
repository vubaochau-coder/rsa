from pow_mod import PowMod
from convert_to_string import ConvertToStr

def decrypt(C, d, n):
    M = PowMod(C,d,n)
    return M
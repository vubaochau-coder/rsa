import time
from convert_to_int import ConvertToInt
from convert_to_string import ConvertToStr
from crt_rsa_decrypt import crt_rsa
from get_key import private_key, public_key_1, public_key_2
from invert_module import InvertModulo
from pow_mod import PowMod
from prime_generate import prime_generate
from rsa_encrypt import encrypt


def multikey(message, bit):
    
    p = prime_generate(int(bit))
    q = prime_generate(int(bit))
    r = prime_generate(int(bit))
    s = prime_generate(int(bit))
    start_time = time.time()
    m1 = (p-1)*(q-1)
    m2 = (r-1)*(s-1)
    
    n1 = public_key_1(p,q)
    n2 = public_key_1(r,s)
    
    e1 = public_key_2(p,q)
    e2 = public_key_2(r,s)
    
    d1 = private_key(m1,e1)
    d2 = private_key(m2,e2)
    
    cytxt = ""
    per_char = 50
    s_message = message
    for i in range(0, len(message), +per_char):
        s1 = s_message[:per_char]
        int_str = ConvertToInt(s1)
        c1 = PowMod(int_str, e1, n1) #ma hoa lan 1
        c2 = PowMod(c1, e2, n2) #ma hoa lan 2
        cytxt1 = str(c2)
        cytxt = cytxt + cytxt1 + "|"
        s_message = s_message[per_char:]
    
    m = ""
    temp = cytxt
    while "|" in temp:
        temp1, temp = map(str.strip, temp.split("|", 1))
        int_str = int(temp1)
        m2 = crt_rsa(int_str, d2, r, s) #giai ma lan 1
        m1 = crt_rsa(m2, d1, p, q) #giai ma lan 2
        m += ConvertToStr(m1)
    print(f'Decrypted message with mutil key and crt:', m, 'with time ', time.time() - start_time, ' s') 
    return m

if __name__ == "__main__":
    multikey("Hello world!", 512)
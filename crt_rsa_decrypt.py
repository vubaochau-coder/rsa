from pow_mod import PowMod
from convert_to_string import ConvertToStr
from invert_module import InvertModulo
import base64
import time

def crt_rsa(c, d, prime1, prime2): 
    base1 = PowMod(c, 1, prime1)
    base2 = PowMod(c, 1, prime2)

    exponent1 = PowMod(d, 1, prime1 - 1)
    exponent2 = PowMod(d, 1, prime2 - 1)

    res1 = PowMod(base1, exponent1, prime1)
    res2 = PowMod(base2, exponent2, prime2)
    
    red_private1 = PowMod(prime1, 1, prime2)
    red_res1 = PowMod(res1, 1, prime2)
    
    invert = InvertModulo(red_private1, prime2)
    x = PowMod(invert * (res2 - red_res1), 1, prime2)
    result = prime1 * x + res1
    return result

def decrypt_crt(ciphertext, d, prime1, prime2):
    msg_str= base64.b64decode(ciphertext).decode('utf-8')
    s = msg_str
    m = ""
    while "|" in s:
        s1, s = map(str.strip, s.split("|", 1))
        b = int(s1)
        m += ConvertToStr(crt_rsa(b,d, prime1, prime2))
    return m

def main():
    msg_encrypt= input('Enter encrypt message: ')
    private_key_base64 = input('\nEnter private key: \n')
    private_key_str = base64.b64decode( private_key_base64).decode('utf-8')
    parts = private_key_str.split("|")
    private_key_int = int(parts[0])
    prime_1=  int(parts[2])
    prime_2=  int(parts[3])
    start_time_decrypt_crt_rsa = time.time()
    print(f'\nDecrypt text: {decrypt_crt(msg_encrypt, private_key_int, prime_1, prime_2)}')
    print(f'Time decrypt: {
        time.time()-start_time_decrypt_crt_rsa
    }')
if __name__ == "__main__":
    main()
from pow_mod import PowMod
from prime_generate import prime_generate 
from get_key import public_key_1, public_key_2, private_key
from crt import crt_rsa 
from convert_to_int import ConvertToInt
from convert_to_string import ConvertToStr
from encrypt import encrypt
from decrypt import decrypt
import time

def main():
    p = prime_generate(1024)
    q = prime_generate(1024)
    r = prime_generate(1024)
    s = prime_generate(1024)
    
    print(f'Prime 1:{p}')
    print(f'Prime 2:{q}')
    print(f'Prime 3:{r}')
    print(f'Prime 4:{s}')
    
    m = (p - 1) * (q - 1)
    m1 = (r - 1) * (s - 1)
    
    n = public_key_1(p, q)
    e = public_key_2(p, q)
    d = private_key(m, e)  
    
    n1 = public_key_1(r, s)
    e1 = public_key_2(r, s)
    d1 = private_key(m1, e1)
    
    print(f'public key 1:{n}')
    print(f'public key 2:{e}')
    print(f'private key:{d}')
    
    print(f'public key 3:{n1}')
    print(f'public key 4:{e1}')
    print(f'private key 2:{d1}')

    # plain text
    msg = input(('Enter message: '))
    message = ConvertToInt(msg)
    
    # encryption
    C = encrypt(message, e, n)
    C2 = encrypt(C, e1, n1)
    print(f'Encrypted message: {C2}',)
    
    # decryption with RSA 
    start_time_decrypt_rsa = time.time()
    M1 = decrypt(C2, d1, n1)
    M = decrypt(M1, d, n)
    result = ConvertToStr(M)
    print(f'Decrypted message with rsa: {result}', 'with time ', time.time()-start_time_decrypt_rsa, ' s')  

    # decryption with CRT-RSA
    start_time_decrypt_crt = time.time()
    M1 = crt_rsa(C2, d1, r, s)
    M = crt_rsa(M1, d, p, q)
    
    result = ConvertToStr(M)
    print(f'Decrypted message with crt:', result, 'with time ', time.time()-start_time_decrypt_crt, 's') 

if __name__ == "__main__":
    main()

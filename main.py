from pow_mod import PowMod
from prime_generate import prime_generate 
from get_key import public_key_1, public_key_2, private_key
from crt_rsa_decrypt import decrypt_crt 
from rsa_encrypt import encrypt
from rsa_decrypt import decrypt
from mutil_key import multikey
import time

def main():
    bit = input('Enter bit to generate primes: ')
    # plain text
    msg = input('Enter message: ')

    
    p= prime_generate(int(bit))
    q= prime_generate(int(bit))
    start_time_encrypt= time.time()
    m= (p-1)* (q-1)
    n= public_key_1(p,q)
    e= public_key_2(p,q)
    d= private_key(m, e)  

    # encryption
    C = encrypt(msg, e, n)
    print(f'Encrypted message: {C}',)
    end_time_encrypt= time.time()
    
    # decryption with RSA 
    start_time_decrypt_rsa = time.time()
    print(f'Decrypted message with rsa:               {decrypt(C,d,n)}', 'with time ', (time.time() - start_time_decrypt_rsa) + (end_time_encrypt - start_time_encrypt), ' s')  

    # decryption with CRT-RSA
    start_time_decrypt_crt = time.time()
    print(f'Decrypted message with crt-rsa:          ', decrypt_crt(C,d,p,q), 'with time ', (time.time()- start_time_decrypt_crt) + (end_time_encrypt - start_time_encrypt), ' s') 
    
    #encrypt and decrypt with mutil key
    multikey(msg, bit)

if __name__ == "__main__":
    main()
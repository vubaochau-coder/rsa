from pow_mod import PowMod
from prime_generate import prime_generate 
from get_key import public_key_1, public_key_2, private_key
from crt import crt_rsa 
import time

def main():
    p= prime_generate(1024)
    q= prime_generate(1024)
    print(f'Prime 1:{p}')
    print(f'Prime 2:{q}')
    m= (p-1)* (q-1)
    n= public_key_1(p,q)
    e= public_key_2(p,q)
    d= private_key(m, e)  
    print(f'public key 1:{n}')
    print(f'public key 2:{e}')
    print(f'private key:{d}')

    # plain text
    msg = 123456789
    print(f'Original message:{msg}')
    
    # encryption
    C = PowMod(msg,e,n)
    print(f'Encrypted message: {C}',)
    
    # decryption with RSA 
    start_time_decrypt_rsa = time.time()
    M = PowMod(C,d,n)
    print(f'Decrypted message with rsa: {M}', 'with time ', time.time()-start_time_decrypt_rsa, ' s')  

    # decryption with CRT-RSA
    start_time_decrypt_crt = time.time()
    print(f'Decrypted message with crt:', crt_rsa(C,d,p,q), 'with time ', time.time()-start_time_decrypt_crt, 's') 

if __name__ == "__main__":
    main()

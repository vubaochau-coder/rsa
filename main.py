from PrimeGenerate import getLowLevelPrime 
from GetKey import public_key_1, public_key_2, private_key
from Crt import crt_rsa
import math
import decimal


def main():
    p= getLowLevelPrime(23)
    q= getLowLevelPrime(23)
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
    msg = 11
    print(f'Original message:{msg}')
    
    # encryption
    C = (msg ** e) % n
    print(f'Encrypted message: {C}')
    
     # decryption
   
    print(f'Decrypted  crt message: ', crt_rsa(C,d,p,q)) 

    # decryption
    # M =(C ** d) % n
    # print(f'Decrypted message: {M}')     

if __name__ == "__main__":
    main()
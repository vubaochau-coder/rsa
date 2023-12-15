from PrimeGenerate import getLowLevelPrime 
from GetKey import public_key_1, public_key_2, private_key
from Crt import crt_rsa
import math
import decimal


def main():
    print('Input key size: ')
    a_input = int(input())
    
    p = getLowLevelPrime(a_input)
    q = getLowLevelPrime(a_input)
    # p = 3
    # q = 5
    
    print(f'Prime 1: {p}')
    print(f'Prime 2: {q}')
    
    m = (p - 1) * (q - 1)
    n = public_key_1(p, q)
    e = public_key_2(p, q)
    d = private_key(m, e)  
    print(f'public key 1: {n}')
    print(f'public key 2: {e}')
    print(f'private key: {d}')
    
    # plain text
    msg = 1712144
    print(f'Original message: {msg}')
    
    # encryption
    C = (msg ** e) % n
    print(f'Encrypted message: {C}')
    
     # decryption
   
    print(f'Decrypted crt message: ', crt_rsa(C,d,p,q))    

if __name__ == "__main__":
    # print(4 ** 255 % 5)
    # first = 2661838 ** 1 % 2821103
    # i = 0
    # j = 2
    # while i != 1712144:
    #     j += 1
    #     i = 2661838 ** j % 2821103
    #     print(f'j: {j}     i: {i}')
        
    # for i in range(21):
    #     print(f'{i}: {2661838 ** i % 2821103}')
    main()
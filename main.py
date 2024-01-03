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
    # p = 107062488691457833679658000885017143145834250692774403164918258685239725623883881864132461554832362994592970280234425755449460339857499658695414598152155611866048153709545499404029674804493705124690443767341637874176166264616365363261990786851793570570434704494471623909328244836864197528853763771502504560961
    # q = 155710935327927907180403878657546858498578638379909002052482108220592155648808968463241622836295875635686691963729705809445599202451855095164412467082339309431750440819572901638238740148871236119709103724667922578874085225089342288948076343661721987838943318493087555507674138370101010771301452483640127639139
    p = prime_generate(1024)
    q = prime_generate(1024)
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
    msg = input(('Enter message: '))
    
    # encryption
    C = encrypt(msg, e, n)
    print(f'Encrypted message: {C}',)
    
    # decryption with RSA 
    start_time_decrypt_rsa = time.time()
    M = decrypt(C,d,n)
    print(f'Decrypted message with rsa: {M}', 'with time ', time.time()-start_time_decrypt_rsa, ' s')  

    # decryption with CRT-RSA
    start_time_decrypt_crt = time.time()
    print(f'Decrypted message with crt:', crt_rsa(C,d,p,q), 'with time ', time.time()-start_time_decrypt_crt, 's') 

if __name__ == "__main__":
    main()

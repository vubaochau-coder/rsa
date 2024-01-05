import math
import crt
from math import gcd
from prime_generate import prime_generate 
from invert_module import InvertModulo
from get_key import private_key
from pow_mod import PowMod


def find_e(euler_sum_n, n):
    for e in range(2, n):
        if gcd(e, euler_sum_n) == 1:
            return e
    return None

if __name__ == '__main__':
    print('RSA Process')
    
    p = prime_generate(12)
    q = prime_generate(12)
    r = prime_generate(12)
    s = prime_generate(12)

    print(f'Fours prime: \n\tp: {p} \n\tq: {q} \n\tr: {r} \n\ts: {s}')

    n = p * q * r * s
    phi_n = (p - 1) * (q - 1) * (r - 1) * (s - 1)
    
    print(f'n = {n}, phi_n = {phi_n}')

    e = 2
    while(math.gcd(phi_n,e)!=1):
        e = e + 1
    print(f'e = {e}')
    
    d = InvertModulo(e, phi_n)
    print(f'd = {d}')

    dp = d % (p - 1)
    dq = d % (q - 1)
    dr = d % (r - 1)
    ds = d % (s - 1)

    print(f'dp: {dp}, dq: {dq}, dr: {dr}, ds: {ds}')
    print(f'public key <(e, n)>: <({e}, {n})>')
    print(f'private key <d, p, q, r, s, dp, dq, dr, ds>: <{d}, {p}, {r}, {s}, {dp}, {dq}, {dr}, {ds}>')

    print('\nExample encrypt message: 1234:')
    m = 1234
    a = 2
    while(math.gcd(n,a)!=1):
        a = a + 1
    
    c1 = a ** e % n
    print(f'c1: {c1}')
    c2 = (m ** e) * a % n
    print(f'c2: {c2}')

    print(f'\nExample decrypt ciphertext: {c2}')
    cp = c1 % p
    cq = c1 % q
    cr = c1 % r
    cs = c1 % s
    print(f'cp : {cp}, cq: {cq}, cr: {cr}, cs: {cs}')
    mp = cp * dp % p
    mq = cq * dq % q
    mr = cr * dr % r
    ms = cs * ds % s
    print(f'ap : {mp}, aq: {mq}, ar: {mr}, as: {ms}')
    
    find_a = mp*InvertModulo((q*r*s),p) +  mq*InvertModulo((p*r*s),q) + mr*InvertModulo((q*p*s),r) + ms*InvertModulo((q*r*p),s)
    print(f'find_a: {find_a}')
    
    b = InvertModulo(find_a, n)
    print(f'b: {b}')
     
    M2 = PowMod(c2 * b, 1, n)
    
    c_p = M2 % p
    c_q = M2 % q
    c_r = M2 % r
    c_s = M2 % s
    PowMod(c_p, (d*p), p)
    Mp = PowMod(c_p, (dp), p)
    Mq = PowMod(c_q, (dq), q)
    Mr = PowMod(c_q, (dr), r) 
    Ms = PowMod(c_q, (ds), s)
    
    final = Mp*InvertModulo((q*r*s), p) + Mq*InvertModulo((p*r*s), q) + Mr*InvertModulo((q*p*s), r) + Ms*InvertModulo((q*r*p), s)
    print(f'Message: {final}')
    #Start the encryption process
        #Input message => (Text)
     
        #Convert message to number (*1)
        
        #Generate prime number (4 prime to Multi-key)
        
        #Generate public-key, private key
        
        #Encrypt message
        
        #Show message => (Number)
        
    #Start the decryption process
        #Input message => (Number)
        
        #Message pre-processing (optional) (*1)
        
        #Decrypt message (using CRT)
        
        #Message post-processing (optional) (*1)
        
        #Show message => (Text)
        
#(*1): Phụ thuộc vào quy cách chuyển đổi message -> number
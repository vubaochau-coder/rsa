import init_prime
import Crt
from math import gcd

def find_e(euler_sum_n, n):
    for e in range(2, n):
        if gcd(e, euler_sum_n) == 1:
            return e
    return None

if __name__ == '__main__':
    print('Enter the bit size of the prime number:')
    a = int(input())
    p = init_prime.initPrime(a)
    q = init_prime.initPrime(a)
    r = init_prime.initPrime(a)
    s = init_prime.initPrime(a)
    
    print(f'Fours prime: p: {p}, q: {q}, r: {r}, s: {s}')
    
    n = p * q
    z = r * s
    print(f'n = {n}, z = {z}')
    euler_sum_n = (p - 1) * (q - 1)
    euler_sum_z = (r -1) * (s - 1)
    
    e = find_e(euler_sum_n, n)
    g = find_e(euler_sum_z, z)
    
    print(f'e = {e}, g = {g}')
    
    d = Crt.solve_equation(e, 1, euler_sum_n)
    t = Crt.solve_equation(g, 1, euler_sum_z)
    
    print(f'd = {d}, t = {t}')
    
    dp = d % (p - 1)
    dq = d % (q - 1)
    dr = d % (r - 1)
    ds = d % (s - 1)
    
    print(f'dp: {dp}, dq: {dq}, dr: {dr}, ds: {ds}')
    print(f'public key <(e, n), (g, z)>: <({e}, {n}), ({g}, {z})>')
    print(f'private key <t, z, dp, dq, dr, ds>: <{t}, {z}, {dp}, {dq}, {dr}, {ds}>')
    
    print('\nExample encrypt message: 123456:')
    m = 123456
    c1 = m ** e % n
    print(f'c1: {c1}')
    c = c1 ** g % z
    print(f'c: {c}')
    
    print(f'\nExample decrypt ciphertext: {c}')
    c1 = c ** t % z
    print(f'c1: {c1}')
    cp = c1 % p
    cq = c1 % q
    cr = c1 % r
    cs = c1 % s
    print(f'cp : {cp}, cq: {cq}, cr: {cr}, cs: {cs}')
    mp = cp * dp % p
    mq = cq * dq % q
    mr = cr * dr % r
    ms = cs * ds % s
    print(f'mp : {mp}, mq: {mq}, mr: {mr}, ms: {ms}')
    
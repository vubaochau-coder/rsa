import init_prime
import Crt
import random
from math import gcd

def find_e(euler_sum_n, n):
    for e in range(2, n):
        if gcd(e, euler_sum_n) == 1:
            return e
    return None

def find_a(n):
    for e in range(2, n - 2):
        if gcd(e, n) == 1:
            return e
    return None

def find_b(a, n):
    for e in range (2, n - 1):
        if (e * a) % n == 1:
            return e
    return None

if __name__ == '__main__':
    print(2**10**9)
    # print('Enter the bit size of the prime number:')
    # a = int(input())
    # p = init_prime.initPrime(a)
    # q = init_prime.initPrime(a)
    # r = init_prime.initPrime(a)
    # s = init_prime.initPrime(a) 
    # print(f'Step 1: Fours prime \n\tp: {p} \n\tq: {q} \n\tr: {r} \n\ts: {s}')
    
    # n = p * q * r * s
    # euler_n = (p - 1) * (q - 1) * (r - 1) * (s - 1)
    # print(f'Step 2: \n\tn: {n} \n\teuler_n: {euler_n}')
    
    # e = find_e(euler_n, n)
    # print(f'Step 3: Find e \n\te: {e} \n\tgcd(e, euler_n): {gcd(e, euler_n)}')
    
    # k = random.randint(2, e)
    # j = k * e
    # print(f'Step 4: Random j, k | j/k = e \n\tj: {j} \n\tk: {k}')
    
    # d = Crt.solve_equation(e, 1, euler_n)
    # print(f'Step 5: \n\td: {d}')
    
    # dp = d % (p - 1)
    # dq = d % (q - 1)
    # dr = d % (r - 1)
    # ds = d % (s - 1)
    # print(f'Step 6: \n\tdp: {dp} \n\tdq: {dq} \n\tdr: {dr} \n\tds: {ds}')
    
    # print(f'Step 7: \n\tPublic key KU=<e,n>: <{e},{n}> \n\tPrivate key KV=<d,p,q,r,s,dp,dq,dr,ds>: <{d},{p},{q},{r},{s},{dp},{dq},{dr},{ds}>')
    # #Complete generate key
    
    # #Encrypt
    # print('\nSTART ENCRYPT MESSAGE: 123')
    # m = 123
    # a = find_a(n)
    # print(f'a: {a}')
    
    # c1 = (a ** e) % n
    # c2 = (m ** e) * a % n
    # print(f'Cipher text: \n\tc1: {c1} \n\tc2: {c2}')
    
    # #Decrypt
    # print(f'\nSTART DECRYPT MESSAGE: <c1,c2>: <{c1},{c2}>')
    
    # cp = c1 % p
    # cq = c1 % q
    # cr = c1 % r
    # cs = c1 % s
    
    # _ap = cp ** dp % p
    # _aq = cq ** dq % q
    # _ar = cr ** dr % r
    # _as = cs ** ds % s
    # print(f'Step 1: \n\tcp: {cp} \n\tcq: {cq} \n\tcr: {cr} \n\tcs: {cs}')
    # print(f'\tap: {_ap} \n\taq: {_aq} \n\tar: {_ar} \n\tas: {_as}')
    
    # _p = _ap * ((q * r * s)**(p - 1)) % n
    # _q = _aq * ((p * r * s)**(q - 1)) % n
    # _r = _ar * ((p * q * s)**(r - 1)) % n
    # _s = _as * ((p * q * r)**(s - 1)) % n
    
    # find_a = _p + _q + _r + _s
    # print(f'Step 2: \n\ta: {_p} + {_q} + {_r} + {_s} = {find_a}')
    
    # b = Crt.solve_equation(find_a, 1, n)
    # # b = find_b(find_a, n)
    # print(f'a: {find_a}, n: {n}')
    # print(f'Step 3: \n\tb: {b}')

    # m_jk = ((c2 * b) % n)
    # print(f'Step 4: \n\tM^(j/k): {m_jk}')
    
    # _cp = m_jk % p
    # _cq = m_jk % q
    # _cr = m_jk % r
    # _cs = m_jk % s
    
    # mp = _cp ** dp % p
    # mq = _cq ** dq % q
    # mr = _cr ** dr % r
    # ms = _cs ** ds % s
    # print(f'Step 5: \n\tMp: {mp} \n\tMq: {mq} \n\tMr: {mr} \n\tMs: {ms}')
    
    # temp_p = mp * ((q * r * s) ** (p - 1))
    # temp_q = mq * ((p * r * s) ** (q - 1))
    # temp_r = mr * ((p * q * s) ** (r - 1))
    # temp_s = ms * ((p * q * r) ** (s - 1))
    # final_message = temp_p % n + temp_q % n + temp_r % n + temp_s % n
    # print(f'Step 6: Final message \n\t{final_message}')
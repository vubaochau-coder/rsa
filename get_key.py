import math
import base64
from prime_generate import prime_generate 

def public_key_1(p, q):
    return p*q

def public_key_2(p,q):
    m= (p-1)*(q-1)
    e= 2
    while(math.gcd(m,e)!=1):
        e = e + 1
    return e

def private_key(m, e):
    stack1 = []
    stack2 = []
    stack3 = []
    sodu = 0
    while sodu != 1:
        stack1.append(m)
        stack2.append(e)
        stack3.append(m // e)
        sodu = m % e
        m, e = e, sodu
    
    d = -stack3[-1]
    m = stack1[-1]
    x = sodu
    e = stack2[-1]
    stack1.pop()
    stack2.pop()
    stack3.pop()

    temp = 0
    while stack1:
        m = stack1[-1]
        temp = x
        x = d
        d = -1 * d * stack3[-1] + temp
        e = stack2[-1]
        stack1.pop()
        stack2.pop()
        stack3.pop()
    return m + d

def main():
    bit = input('Enter bit to generate primes: ')
    p= prime_generate(int(bit))
    q= prime_generate(int(bit))
    n= public_key_1(p,q)
    m= (p-1)* (q-1)
    e= public_key_2(p,q)
    d= private_key(m,e)
    public_key_str = str(e) + "|" +str(n)
    private_key_str= str(d) + "|" +str(n)+ "|" +str(p)+ "|" +str(q)
    print(f'\nprivate key:\n {base64.b64encode(private_key_str.encode('utf-8'))}')
    print(f'\npublic key:\n {base64.b64encode(public_key_str.encode('utf-8'))}')
if __name__ == "__main__":
    main()

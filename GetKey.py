import math


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
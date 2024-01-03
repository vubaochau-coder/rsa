from datetime import datetime
from pow_mod import PowMod
from invert_module import InvertModulo
from convert_to_string import ConvertToStr
def crt_rsa(c, d, prime1, prime2):  # m = c^d mod (prime1 * prime2)
    # print(f'Input: {c}^{d} mod {prime1 * prime2}')
    
    #Reducing base 
    # base1 = c % prime1
    # base2 = c % prime2
    base1 = PowMod(c, 1, prime1)
    base2 = PowMod(c, 1, prime2)
    
    # print('\nAfter reducing the base:')
    # print(f'{base1}^{d} mod {prime1}')
    # print(f'{base2}^{d} mod {prime2}')
    
    #Reducing exponent 
    # exponent1 = d % (prime1 - 1)
    # exponent2 = d % (prime2 - 1)
    exponent1 = PowMod(d, 1, prime1 - 1)
    exponent2 = PowMod(d, 1, prime2 - 1)
    
    # print('\nAfter reducing the exponent:')
    # print(f'{base1}^{exponent1} mod {prime1}')
    # print(f'{base2}^{exponent2} mod {prime2}')

    # res1 = base1 ** exponent1 % prime1
    # res2 = base2 ** exponent2 % prime2
    res1 = PowMod(base1, exponent1, prime1)
    res2 = PowMod(base2, exponent2, prime2)
    
    # print(f'result 1: {res1} mod {prime1}')
    # print(f'result 2: {res2} mod {prime2}')
    
    red_private1 = PowMod(prime1, 1, prime2) #prime1 % prime2
    red_res1 = PowMod(res1, 1, prime2) #res1 % prime2
    # print(f'Function: {red_private1}x + {red_res1} = {res2} mod {prime2}')
    # print(f'Function: {red_private1}x = {res2 - red_res1} mod {prime2}')
    
    invert = InvertModulo(red_private1, prime2)
    x = PowMod(invert * (res2 - red_res1), 1, prime2)
    # x = solve_equation(red_private1, res2 - red_res1, prime2)
    # print(x)
    
    result = prime1 * x + res1
    # print(result)
    result = ConvertToStr(result)
    return result

def find_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def solve_equation(a, b, m):
    inverse_a = find_inverse(a, m)
    if inverse_a is None:
        return "No inverse exists."

    x = (inverse_a * b) % m
    return x

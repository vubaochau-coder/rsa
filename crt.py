from datetime import datetime
from pow_mod import PowMod
from invert_module import InvertModulo
from convert_to_string import ConvertToStr
def crt_rsa(c, d, prime1, prime2):  # m = c^d mod (prime1 * prime2)
    
    #Reducing base 
    base1 = PowMod(c, 1, prime1)
    base2 = PowMod(c, 1, prime2)
    
    #Reducing exponent 
    exponent1 = PowMod(d, 1, prime1 - 1)
    exponent2 = PowMod(d, 1, prime2 - 1)

    res1 = PowMod(base1, exponent1, prime1)
    res2 = PowMod(base2, exponent2, prime2)
    
    red_private1 = PowMod(prime1, 1, prime2)
    red_res1 = PowMod(res1, 1, prime2)

    print(f'Function: {red_private1}x = {res2 - red_res1} mod {prime2}')
    
    invert = InvertModulo(red_private1, prime2)
    x = PowMod(invert * (res2 - red_res1), 1, prime2)
    
    result = prime1 * x + res1
    return result

# def find_inverse(a, m):
#     for x in range(1, m):
#         if (a * x) % m == 1:
#             return x
#     return None

# def solve_equation(a, b, m):
#     inverse_a = find_inverse(a, m)
#     if inverse_a is None:
#         return "No inverse exists."

#     x = (inverse_a * b) % m
#     return x

if __name__ == '__main__':
    # print('InvertModulo(60, 17)')
    # a = InvertModulo(60, 17)
    # print(a)
    # t1 = datetime.now()
    # crt_rsa(17639, 3089, 37, 89)
    # t2 = datetime.now()
    # print(t2 - t1)
    # m = 37 * 89
    # m1 = m / 37 #89
    # m2 = m / 89 #37 476 198
    x = PowMod(17639, 3089, 3293)
    
    # y1 = InvertModulo(m1, 37)
    # y2 = InvertModulo(m2, 89)
    # # x = InvertModulo(37, 89)
    # x = 11 * m1 * y1 + 47    * m2 * y2
    # 138798 + 0 * (37 * 89)
    print(x)

#eea: Extended Euclidean Algorithm
#Hàm tìm UCLN của a, b dựa trên thuật toán Euclid mở rộng
#Trả về gcd là UCLN, s, t
#Sao cho: gcd = (s * a) + (t * b)
def eea(a, b):
    # print(f'\nstart eea({a}, {b})') #Remove when complete
    if (a % b == 0):
        return (b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s - ((a // b) * t)
        return (gcd, t, s)

#Description: Nghịch đảo Module của e theo phi là một số s, sao cho (e * s) mod phi = 1
#Đây là hàm tìm s theo e, phi
#Note: Trong RSA, đây là bước tìm d
def InvertModulo(e, phi):
    gcd, s, _ = eea(e, phi)
    if (gcd != 1):
        return None
    else:
        return s % phi
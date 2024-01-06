

def mod_ex(b, k, m):
    i = 1
    j = 0
    while (j <= k):
        b = (b * i) % m 
        i = b 
        j += 1
    return b

def PowMod(b, e, m):
    bin_e = bin(e)
    bin_e = bin_e[::-1]
    ln = len(bin_e)
    result = 1
    for i in range(0, ln - 2, + 1):
        if (bin_e[i] == '1'):
            result *= mod_ex(b, i, m)
    return result % m

if __name__ == '__main__':
    print(f'{PowMod(102, 13, 20)}')
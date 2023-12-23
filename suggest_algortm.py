import crt
from math import gcd

def find_e(euler_sum_n, n):
    for e in range(2, n):
        if gcd(e, euler_sum_n) == 1:
            return e
    return None

if __name__ == '__main__':
    print('RSA Process')       
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
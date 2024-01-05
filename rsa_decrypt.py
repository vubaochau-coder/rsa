from pow_mod import PowMod
from convert_to_string import ConvertToStr
import base64
import time

def decrypt(ciphertext, d, modulo):
    msg_str= base64.b64decode(ciphertext).decode('utf-8')
    s =  msg_str
    m = ""
    while "|" in s:
        s1, s = map(str.strip, s.split("|", 1))
        b = int(s1)
        m += ConvertToStr(PowMod(b, d, modulo))
    return m
def main():
    msg_encrypt= input('Enter encrypt message: ')
    private_key_base64 = input('Enter private key: ')
    private_key_str = base64.b64decode( private_key_base64).decode('utf-8')
    parts = private_key_str.split("|")
    private_key_int = int(parts[0])
    public_key_2= int(parts[1])
    start_time_decrypt_rsa = time.time()
    print(f'Decrypt text: {decrypt( msg_encrypt, private_key_int, public_key_2)}')
    print(f'Time decrypt: {
        time.time()-start_time_decrypt_rsa
    }')
if __name__ == "__main__":
    main()
from convert_to_int import ConvertToInt
from pow_mod import PowMod
import base64

def encrypt(message,e,modulo):
    cytxt = ""
    per_char = 50
    s = message
    for i in range(0, len(message), +per_char):
        s1 = s[:per_char]
        b = ConvertToInt(s1)
        cytxt1 = str(PowMod(b, e, modulo))
        cytxt = cytxt + cytxt1 + "|"
        s = s[per_char:]
    return base64.b64encode(cytxt.encode('utf-8'))
def main():
    msg= input('Enter message: ')
    public_key = input('Enter public key: ')
    public_key_str = base64.b64decode(public_key).decode('utf-8')
    public_key_1= int(public_key_str.split("|")[0].strip())
    public_key_2= int(public_key_str.split("|")[1].strip())
    encrypt_text= encrypt(msg,public_key_1,public_key_2)
    print(f'Encrypt text: {encrypt_text}')
if __name__ == "__main__":
    main()

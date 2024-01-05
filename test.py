import unittest
from pow_mod import PowMod
from prime_generate import prime_generate 
from get_key import public_key_1, public_key_2, private_key
from crt_rsa_decrypt import decrypt_crt 
from rsa_encrypt import encrypt
from rsa_decrypt import decrypt
import time

class TestRSA(unittest.TestCase):

    def test_encryption_decryption(self):
        bit_length = 32  # Choose an appropriate bit length for testing
        msg = "Hello, World!"  # Test message

        p = prime_generate(bit_length)
        q = prime_generate(bit_length)
        m = (p - 1) * (q - 1)
        n = public_key_1(p, q)
        e = public_key_2(p, q)
        d = private_key(m, e)

        # encryption
        C = encrypt(msg, e, n)

        # decryption with RSA
        decrypted_rsa = decrypt(C, d, n)
        self.assertEqual(decrypted_rsa, msg)

        # decryption with CRT-RSA
        decrypted_crt = decrypt_crt(C, d, p, q)
        self.assertEqual(decrypted_crt, msg)

    def test_performance(self):
        bit_length = 32  # Choose an appropriate bit length for testing
        msg = "Hello, World!"  # Test message

        p = prime_generate(bit_length)
        q = prime_generate(bit_length)
        m = (p - 1) * (q - 1)
        n = public_key_1(p, q)
        e = public_key_2(p, q)
        d = private_key(m, e)

        # encryption
        C = encrypt(msg, e, n)

        # measure decryption time with RSA
        start_time_decrypt_rsa = time.time()
        decrypt(C, d, n)
        time_rsa = time.time() - start_time_decrypt_rsa

        # measure decryption time with CRT-RSA
        start_time_decrypt_crt = time.time()
        decrypt_crt(C, d, p, q)
        time_crt = time.time() - start_time_decrypt_crt

        self.assertLess(time_crt, time_rsa)  # CRT-RSA should be faster

if __name__ == "__main__":
    unittest.main()

import unittest
from pow_mod import PowMod
from prime_generate import prime_generate 
from get_key import public_key_1, public_key_2, private_key
from crt_rsa_decrypt import decrypt_crt 
from rsa_encrypt import encrypt
from rsa_decrypt import decrypt
import time

class TestRSA(unittest.TestCase):

    def test_encryption_decryption(self):
        bit_length = 32  # Choose an appropriate bit length for testing
        msg = "Hello, World!"  # Test message

        p = prime_generate(bit_length)
        q = prime_generate(bit_length)
        m = (p - 1) * (q - 1)
        n = public_key_1(p, q)
        e = public_key_2(p, q)
        d = private_key(m, e)

        # encryption
        C = encrypt(msg, e, n)

        # decryption with RSA
        decrypted_rsa = decrypt(C, d, n)
        self.assertEqual(decrypted_rsa, msg)

        # decryption with CRT-RSA
        decrypted_crt = decrypt_crt(C, d, p, q)
        self.assertEqual(decrypted_crt, msg)

    def test_performance(self):
        bit_length = 32  # Choose an appropriate bit length for testing
        msg = "Hello, World!"  # Test message

        p = prime_generate(bit_length)
        q = prime_generate(bit_length)
        m = (p - 1) * (q - 1)
        n = public_key_1(p, q)
        e = public_key_2(p, q)
        d = private_key(m, e)

        # encryption
        C = encrypt(msg, e, n)

        # measure decryption time with RSA
        start_time_decrypt_rsa = time.time()
        decrypt(C, d, n)
        time_rsa = time.time() - start_time_decrypt_rsa

        # measure decryption time with CRT-RSA
        start_time_decrypt_crt = time.time()
        decrypt_crt(C, d, p, q)
        time_crt = time.time() - start_time_decrypt_crt

        self.assertLess(time_crt, time_rsa)  # CRT-RSA should be faster

if __name__ == "__main__":
    unittest.main()


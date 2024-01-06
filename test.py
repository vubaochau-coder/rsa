
import unittest
from prime_generate import prime_generate 
from get_key import public_key_1, public_key_2, private_key
from crt_rsa_decrypt import decrypt_crt 
from rsa_encrypt import encrypt
from rsa_decrypt import decrypt
import time

class TestRSA(unittest.TestCase):

    def run_test_case(self, bit_length, msg):
        p = prime_generate(bit_length)
        q = prime_generate(bit_length)
        m = (p - 1) * (q - 1)
        n = public_key_1(p, q)
        e = public_key_2(p, q)
        d = private_key(m, e)

        # encryption
        C = encrypt(msg, e, n)

        # decryption with RSA
        start_time_decrypt_rsa = time.time()
        decrypted_rsa = decrypt(C, d, n)
        time_rsa = time.time() - start_time_decrypt_rsa
        self.assertEqual(decrypted_rsa, msg)
        

        # decryption with CRT-RSA
        start_time_decrypt_crt = time.time()
        decrypted_crt = decrypt_crt(C, d, p, q)
        time_crt = time.time() - start_time_decrypt_crt
        self.assertEqual(decrypted_crt, msg)
        self.assertLess(time_crt, time_rsa) 


    def test_encryption_decryption_custom(self):
        # List of custom test cases (bit_length, message)
        test_cases = [(256, "Hello, World!"), (256, "Seminar các vấn đề hiện đại của CNPM"), (256, "1234567890-=!@#$%^&*()_+{}[]|\":>?<,./"),
                      (512, "Hello, World!"), (512, "Seminar các vấn đề hiện đại của CNPM"),(512, "1234567890-=!@#$%^&*()_+{}[]|\":>?<,./")]

        # Run test for each custom test case
        for bit_length, msg in test_cases:
            with self.subTest(bit_length=bit_length, msg=msg):
                self.run_test_case(bit_length, msg)


if __name__ == "__main__":
    unittest.main()


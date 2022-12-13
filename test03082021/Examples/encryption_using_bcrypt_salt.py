"""
https://zetcode.com/python/bcrypt/

"""

import bcrypt
import time

passwd = b's$cret12'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)

print(salt)
print(hashed)

def check_password():
    passwd = b's$cret12'

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd, salt)

    if bcrypt.checkpw(passwd, hashed):
        print("match")
    else:
        print("does not match")

def bcrypt_cost_factor():
    passwd = b's$cret12'

    start = time.time()
    salt = bcrypt.gensalt(rounds=16)
    hashed = bcrypt.hashpw(passwd, salt)
    end = time.time()

    print(end - start)

    print(hashed)

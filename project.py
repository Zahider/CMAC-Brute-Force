import string, random
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms

# List of all ASCII characters
characters = list(string.printable)

# Tag, Message and Incomplete key
tag = b's\xaf\x12\n\xdc\xc6\x16~\xd0\xcaI\xf3o\x9au0'
message = b"message to authenticate"
key = b'0123456789abcd'

# Loop for brute forcing
while True:
    # Complete key by appending 2 random characters from ASCII list
    key_complete = key + (random.choice(characters) + random.choice(characters)).encode()
    # Calculate CMAC tag
    c = cmac.CMAC(algorithms.AES(key_complete))
    c.update(message)
    # If CMAC tag is same as given tag, print the key
    if c.finalize() == tag:
        print("Key:", key_complete)  # Key: b'0123456789abcdi/'
        break
import hashlib
import secrets
import string
 
class Key():
    def __init__(self) -> None:
        self.key = bytes("".join(secrets.choice(string.digits + string.ascii_letters) for i in range(32)), "UTF-8")
        
    def __str__(self):
        return self.key.hex()
    
    def get_key(self):
        return self.key
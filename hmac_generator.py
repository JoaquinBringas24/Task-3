from hmac import HMAC
from key import Key
import hashlib
import random
import sys

class HMAC(HMAC):
    def __init__(self, key:Key, algorithm) -> None:
        super().__init__(key.key, digestmod=algorithm)  
        self.choice = None
    
    def choose(self, options: list[str]):
        self.choice = random.choice(options[1:])
        self.update(bytes(self.choice, "UTF-8"))
        
    def get_hmac(self):
        return bytes(self.choice, "UTF-8")
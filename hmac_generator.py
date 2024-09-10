from hmac import HMAC
from key import Key
import hashlib

class HMAC(HMAC):
    def __init__(self, key:Key, algorithm) -> None:
        super().__init__(key.key, digestmod=algorithm)     
    
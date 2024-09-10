import sys
from tabulate import tabulate
import hashlib
import random
import string
from table import Table
from hmac_generator import HMAC
from key import Key
import secrets
from rules import Rules

def main() -> None:    
    
    table: Table = Table(sys.argv[1:])
    
    game: Rules = Rules(table) 
    
    game.play()

if __name__ == "__main__":
    main()
    
    

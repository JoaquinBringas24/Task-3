import sys
from tabulate import tabulate
import hashlib
import random
import string
from table import Table
from hmac_generator import HMAC
from key import Key
import secrets
from hmac import compare_digest, digest

def display_moves() -> None:
    print("Available moves:")
    
    for i, arg in enumerate(sys.argv[1:]):
        print(f"{i + 1} - {arg}")
    
    print("0 - exit")
    print("? - help")

def main() -> None:    
        
    if len(sys.argv[1:]) % 2 != 1 or len(sys.argv[1:]) == 1:
        raise ValueError("The amount of arguments must be an odd number greater or equal than 3.") 

    if len(set(sys.argv[1:])) != len(sys.argv[1:]):
        raise ValueError("Arguments must be non-repeating strings.")
    
    table: Table = Table(sys.argv[1:])
    table.show()
    
    key: Key = Key()
    
    hmac: HMAC = HMAC(key, algorithm=hashlib.sha3_256)
    
    choice = bytes(random.choice(sys.argv[1:]), "UTF-8")
    
    hmac.update(choice)
    
    print(f"HMAC: \n {hmac.hexdigest()}")
    
    display_moves()
    
    move:str = input("Enter your move: ")

    if move == "?":
        table.show()
        display_moves()
        move:str = input("Enter your move: ")
        
    elif move == "0":
        return

    elif int(move) <= len(sys.argv) :
        print(f"Your move: {sys.argv[int(move)]}")
    
    else:
        print("---------------------------------------")
        print("Option is not valid. Please try again.")
        print("---------------------------------------")
        display_moves()
        move:str = input("Enter your move:")
    
    print(f"HMAC key: \n {key}")
    print(f"Computer move: {choice.decode()}")
    
    guess_hmac = digest(key.get_key(), choice, digest=hashlib.sha3_256).hex()
    
    print("---------------------------------------")
    print(f"Computer did not change move: {compare_digest(hmac.hexdigest(), guess_hmac)}") 
    print("---------------------------------------")
    
if __name__ == "__main__":
    main()
    
    

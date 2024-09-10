import sys
from tabulate import tabulate
import hashlib
import random
import string
from table import Table

def display_moves() -> None:
    print("Available moves:")
    
    for i, arg in enumerate(sys.argv[1:]):
        print(f"{i + 1} - {arg}")
    
    print("0 - exit")
    print("? - help")

def main() -> None:    
        
    if len(sys.argv[1:]) % 2 != 1:
        raise ValueError("The amount of arguments must be an odd number. \n Check -help for more help. ") 

    if len(set(sys.argv[1:])) != len(sys.argv[1:]):
        raise ValueError("Arguments must be non-repeating strings.")
    
    table: Table = Table(sys.argv[1:])
    table.show()
    
    
    computer_move:str = random.choice(sys.argv[1:])
    
    hash = hashlib.sha3_256()
    
    hash.update(computer_move.encode())
    
    print(f"HMAC: \n {hash.hexdigest()}")
    
    display_moves()
    
    move:str = input("Enter your move:")

    if move == "?":
        table.show()
        display_moves()
        move:str = input("Enter your move:")
        
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
    
    
    print(f"Computer move: {computer_move}")
    
    
if __name__ == "__main__":
    main()
    
    

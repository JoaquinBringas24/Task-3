from key import Key
from hmac_generator import HMAC
from table import Table
import sys
from hmac import compare_digest, digest
import hashlib
from key import Key
from colorama import Fore

class Rules():
    def __init__(self, table: Table) -> None:
        self.key = None
        self.hmac = None
        self.table = table
        self.playing = False
        self.user_move = None 
    
    @staticmethod
    def check_initial_conditions():
        if len(sys.argv[1:]) % 2 != 1 or len(sys.argv[1:]) == 1:
            raise ValueError("The amount of arguments must be an odd number greater or equal than 3.") 

        if len(set(sys.argv[1:])) != len(sys.argv[1:]):
            raise ValueError("Arguments must be non-repeating strings.")    
        
    def play(self):
        self.playing = True
        
        while self.playing:
            
            self.check_initial_conditions()
            
            while True: 
                
                self.key = Key()
                
                self.hmac = HMAC(self.key, algorithm=hashlib.sha3_256)
            
                print(f"HMAC: \n{self.hmac.hexdigest()}")
                
                self.input_evaluation()
            
                print(f"HMAC key: \n{self.key}")
            
                self.hmac.choose(sys.argv[1:])

                result = self.table.get_win(self.user_move, self.hmac.choice)
            
                print(Fore.YELLOW + f"Computer move: {self.hmac.choice}")

                color = ""
                if result == "Draw":
                    color = Fore.WHITE
                
                if result == "You win!":
                    color = Fore.GREEN
                
                if result == "You lose!":
                    color = Fore.RED
                
                print(color + result)
            
                guess_hmac = digest(self.key.get_key(), self.hmac.get_hmac(), digest=hashlib.sha3_256).hex()
    
                print(Fore.CYAN + f"Computer did not change move: {compare_digest(self.hmac.hexdigest(), guess_hmac)}") 
            
                if result == "You lose!" or result == "You win!":
                    self.playing = False
                    break
    
                self.set_move(None)
                
    @staticmethod
    def display_moves() -> None:
        print("Available moves:")
        for i, arg in enumerate(sys.argv[1:]):
            print(f"{i + 1} - {arg}")
        
        print("0 - exit")
        print("? - help") 
            
    def set_move(self, move):
        self.user_move = move
            
    def input_evaluation(self):
        while self.user_move == None:
            self.display_moves()     
            move = input("Enter your move: ")
                
            if move == "?":
                self.table.show()

            elif move == "0":
                sys.exit(0)

            try:
                print(f"Your move: {sys.argv[int(move)]}")
                self.set_move(sys.argv[int(move)])
    
            except:
                print(Fore.RED + "Option is not valid. Please try again.")
            
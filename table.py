from tabulate import tabulate
from math import ceil


class Table():
    def __init__(self, options: list[str]) -> None:
        
        self.win_count = ceil(len(options) / 2)
        
        self.dictionary = {}
        for i, option in enumerate(options):
            if i + self.win_count + 1 > len(options):
                lenght = len(options) - i
                self.dictionary[option] = options[i+1:] + options[0:self.win_count - lenght]
                
            else:
                self.dictionary[option] = options[i+1:i+self.win_count]
        
        
        self._table: list[list[str]] = [["v PC | User >"] + options]
        for i, option in enumerate(options):
            self._table.append([option])
            for j, item in enumerate(options):
                if i == j:
                    self._table[i+1].append("Draw")
                
                elif item in self.dictionary[option]:
                    self._table[i+1].append("Win")
                    
                else:
                    self._table[i+1].append("Lose")
         
    
    def show(self, tablefmt:str="grid"):
        print(tabulate(self._table, tablefmt=tablefmt))
        
    def get_win(self, user_move: str, computer_move: str):
        if user_move in self.dictionary[computer_move]:
            return "You win!"
        
        elif computer_move in self.dictionary[user_move]:
            return "You lose!"
        
        else:
            return "Draw" 
from tabulate import tabulate
class Table():
    def __init__(self, options: list[str]) -> None:
        
        self._table: list[list[str]] = [["v PC | User >"]]
        for option in options:
            self._table[0].append(option)
            self._table.append([option, *list(range(0,3))])
        
        for i in range(len(options)):
            self._table[i+1][i+1] = "Draw"
    
    def show(self, tablefmt:str="grid"):
        print(tabulate(self._table, tablefmt=tablefmt))
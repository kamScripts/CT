import keyboard
import os
from termcolor import colored, cprint


class Grid:
    """Grid class creates size x size matrix, enables grid manipulation."""
    
    def __init__(self, size: int, item:int=0, contents=None) -> None:
        self.size = size,
        self.item = item,

        self.grid = [
            [0 for _ in range(size)] for _ in range(size)
         ] if contents is None else contents
    def clear_terminal(self)->None:
        """Clear a terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')

    
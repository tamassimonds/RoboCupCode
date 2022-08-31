import curses
from curses import wrapper

import time


class Test():
    
        

    def main(self, stdscr):
        
        for i in range(1000):
            stdscr.clear()
            stdscr.addstr("hello world")
            time.sleep(0.01)
            
            stdscr.refresh()
    
    def __init__(self):
        wrapper(self.main)

test = Test()

# wrapper(main)
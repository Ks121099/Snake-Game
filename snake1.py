import random
import curses
from curses import textpad
import time

stdcsr= curses.initscr()

def main2(stdcsr):
    curses.curs_set(0)
    stdcsr.nodelay(1)
    stdcsr.timeout(100)
    sh, sw =stdcsr.getmaxyx()
    box=[[3,3],[sh-3,sw-3]]
    textpad.rectangle(stdcsr,box[0][0], box[0][1],box[1][0],box[1][1])
    snake=[[sh//2,sw//2 + 1],[sh//2,sw//2],[sh//2,sw//2 -1]]
    direction= curses.KEY_RIGHT
    
    for y, x in snake:
        stdcsr.addstr(y,x, "⭖")
    
    while 1:

        newdir= stdcsr.getch()
        if newdir in [curses.KEY_UP,curses.KEY_LEFT,curses.KEY_DOWN,curses.KEY_RIGHT]:
            direction=newdir
        
        head=snake[0]

        if direction == curses.KEY_UP:
            nhead=[head[0]-1,head[1]]
       
        elif direction == curses.KEY_LEFT:
            nhead=[head[0],head[1]-1]

        elif direction == curses.KEY_DOWN:
            nhead=[head[0]+1,head[1]]
        
        elif direction == curses.KEY_RIGHT:
            nhead=[head[0],head[1]+1]

        if nhead[0]<=box[0][0] or nhead[0]>= box[1][0] or nhead[1]<=box[0][1] or nhead[1]>= box[1][1]:
            stdcsr.addstr(sh//2,sw//2,"GAME OVER !!!")    
            k=stdcsr.getch()
            break
        snake.insert(0,nhead)
        stdcsr.addstr(nhead[0],nhead[1],"⭖")
        stdcsr.addstr(snake[-1][0],snake[-1][1]," ")
        snake.pop()
        stdcsr.refresh()
        curses.curs_set(1)
curses.wrapper(main2)
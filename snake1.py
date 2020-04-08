import random
import curses
from curses import textpad
import time

stdcsr= curses.initscr()
def printscore(stdcsr,score):
    p,q =stdcsr.getmaxyx()
    stdcsr.addstr( 1,q//2-len("Current Score is 100")//2,"Current Score is {}".format(score))
    stdcsr.refresh()

def cfood(snake,box):
    food=None
    while food is None:
        food=[random.randint(box[0][0]+1,box[1][0]-1),
              random.randint(box[0][1]+1,box[1][1]-1)]
        if food in snake:
            food=None
    return food

def main2(stdcsr):
    curses.curs_set(0)
    stdcsr.nodelay(1)
    stdcsr.timeout(100)
    sh, sw =stdcsr.getmaxyx()
    box=[[3,3],[sh-3,sw-3]]
    textpad.rectangle(stdcsr,box[0][0], box[0][1],box[1][0],box[1][1])
    snake=[[sh//2,sw//2 + 1],[sh//2,sw//2],[sh//2,sw//2 -1]]
    direction= curses.KEY_RIGHT
    score=0
    for y, x in snake:
        stdcsr.addstr(y,x, "⭖")
    
    food=cfood(snake,box)
    stdcsr.addstr(food[0],food[1],"*")
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

        snake.insert(0,nhead)
        stdcsr.addstr(nhead[0],nhead[1],"⭖")

        if snake[0]==food:
            food =cfood(snake, box)
            stdcsr.addstr(food[0],food[1],"*")
            score=score+1
        else:
            stdcsr.addstr(snake[-1][0],snake[-1][1]," ")
            snake.pop()

        if nhead[0]<=box[0][0] or nhead[0]>= box[1][0] or nhead[1]<=box[0][1] or nhead[1]>= box[1][1]:
            stdcsr.addstr(sh//2,sw//2-len("GAME OVER !!!")//2,"GAME OVER !!!")    
            stdcsr.refresh()    
            time.sleep(5)
            break
        printscore(stdcsr,score)
        stdcsr.refresh()
curses.wrapper(main2)
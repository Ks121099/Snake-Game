import time
import curses
stdcsr=curses.initscr()

menu=['Home', 'Play','Score', 'Exit']
def mai_menu(stdcsr, select_id):
    stdcsr.clear()
    h,w=stdcsr.getmaxyx()
    for i,row in enumerate(menu):
        x=w//2-len(row)//2
        y=h//2- len(menu)//2+ i
        if i==select_id:
            stdcsr.attron(curses.color_pair(1))
            stdcsr.addstr(y,x,row)
            stdcsr.attroff(curses.color_pair(1))
        else:
            stdcsr.addstr(y,x,row)
    stdcsr.refresh()


def main(stdcsr):
    curses.curs_set(0)  
    curr_row_id=0
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    mai_menu(stdcsr, curr_row_id)
    while 1:
        ip=stdcsr.getch()
        stdcsr.clear()
        if ip==curses.KEY_DOWN:
           curr_row_id=(curr_row_id+1)%len(menu)  

        elif ip==curses.KEY_UP:
            if curr_row_id==0:
                curr_row_id=len(menu)-1
            else:
                curr_row_id=curr_row_id-1 
                
        elif ip==curses.KEY_ENTER or ip in [10,13]:
            stdcsr.addstr(0,0,"You have pressed the {} button".format(menu[curr_row_id]))
            stdcsr.refresh()
            stdcsr.getch()
            if curr_row_id==len(menu)-1:
                break
             
        mai_menu(stdcsr, curr_row_id)
        stdcsr.refresh()
    curses.curs_set(1)  

curses.wrapper(main)



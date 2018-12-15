import sys
import math
import numpy as np
import time

from search import Search

from tkinter import * 
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
import re



root = Tk()
root.title("8-PUZZLE SOLVER")
root.geometry("600x100")


class eightPuzzle:
    
    def __init__(self, puzzle_status, parent=None,  state="Initial"):
        self.parent = parent
        self.children = []
        self.puzzle_status = np.array(puzzle_status)
        self.column_size = int(math.sqrt(len(puzzle_status)))
        self.state = state

    def goal_test(self):
        if np.array_equal(self.puzzle_status, np.arange(9)):
            return True

    def move_down(self, i):
        if i - self.column_size >= 0:
            puzzle_new, parent = self.swap(i, i - 3)
            return eightPuzzle(puzzle_new, parent, state='Down')

    def move_up(self, i):
        if i + self.column_size <= len(self.puzzle_status) - 1:
            puzzle_new, parent = self.swap(i, i + 3)
            return eightPuzzle(puzzle_new, parent, state='Up')

    def move_right(self, i):
        if i % self.column_size > 0:
            puzzle_new, parent = self.swap(i, i - 1)
            return eightPuzzle(puzzle_new, parent, state='Right')

    def move_left(self, i):
        if i % self.column_size < self.column_size - 1:
            puzzle_new, parent = self.swap(i, i + 1)
            return eightPuzzle(puzzle_new, parent, state='Left')

    def swap(self, index_one, index_two):
        puzzle_new = self.puzzle_status.copy()
        puzzle_new[index_one], puzzle_new[index_two] = puzzle_new[index_two], puzzle_new[index_one]
        return puzzle_new, self

    def print_puzzle(self):
        a = 0
        while (a < 9):
            print()
            print(str(self.puzzle_status[a]) +
                  ' ' +
                  str(self.puzzle_status[a +
                                        1]) +
                  ' ' +
                  str(self.puzzle_status[a +
                                        2]))
            a += 3
        print()

    def print_puzzle2(self):
        timestr = time.strftime("%H%M")
       
        f = open(timestr,"a")
        m = 0
        while (m < 9):
            f.write(str(self.puzzle_status[m]) +
                  ' ' +
                  str(self.puzzle_status[m +
                                        1]) +
                  ' ' +
                  str(self.puzzle_status[m +
                                        2])+'\n' + '\n')
            m += 3
        f.write('******' + '\n')



    def expand(self):
        x = list(self.puzzle_status).index(0)
        self.children.append(self.move_down(x))
        self.children.append(self.move_up(x))
        self.children.append(self.move_right(x))
        self.children.append(self.move_left(x))
        self.children = list(filter(None, self.children))
        return self.children

    def write_output(self, search_depth, slist):
        with open('output.txt', "w") as file:
            m = 0
            file.write('Puzzle is : '  + '\n')

            while (m < 9):
         
                file.write(str(self.puzzle_status[m]) + 
                    ' ' +
                    str(self.puzzle_status[m +
                                            1]) +
                    ' ' +
                    str(self.puzzle_status[m +
                                            2]) +'\n' + '\n')
                m += 3
            
            file.write('\n'+'Solution is : ' + str(slist) + '\n'+ '\n'+ '\n')
           # file.write('cost_of_path: ' + str(len(slist)) + '\n')
            file.write('Search Depts is : ' + str(search_depth) + '\n'+ '\n')
            

def input_field(algorithm_type):
    user_input = e1.get()
    user_input_str = str(user_input)
    puzzle_str = user_input_str.split(",")
    puzzle_status = list(map(int, puzzle_str))
    pb = eightPuzzle (puzzle_status)
    if algorithm_type == 1:
        search_depth, states = Search().bfs(pb)
    elif algorithm_type == 2: 
        search_depth, states = Search().dfs(pb)

    slist=[]
    slist.append(states[::-1])
    slist.reverse()
    pb.write_output(search_depth, slist)


    info = "Solution is:"+ str(slist)+ "\n" +"\n" + "Search Depts is :"+ str(search_depth)+ "\n"
    
    #main_info = info+info2+info3
    tkinter.messagebox.showinfo("SUCCESS",info)



    


def main():
    global e1
    e1 = Entry(root)
    e1.grid(row=25,column=10,ipadx=100,ipady=20)
    Button(root,bg="#BEBEBE", text='BFS', width=10, font='Helvetica 12 bold',command=lambda:input_field(1)).grid(row=8, column=5)
    Button(root,bg="#BEBEBE", text='DFS', width=10, font='Helvetica 12 bold',command=lambda:input_field(2)).grid(row=3, column=5)
    
    root.mainloop()


if __name__ == '__main__':
    main()

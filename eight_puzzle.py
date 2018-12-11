import sys
import math
import numpy as np

from search import Search

from tkinter import * 
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
import re



root = Tk()
root.geometry("500x300")


class PuzzleBoard:
    
    def __init__(self, puzzle_state, parent=None, state="Initial"):
        self.parent = parent
        self.children = []
        self.puzzle_state = np.array(puzzle_state)
        self.column_size = int(math.sqrt(len(puzzle_state)))
        self.state = state

    def goal_test(self):
        if np.array_equal(self.puzzle_state, np.arange(9)):
            return True

    def move_up(self, i):
        if i - self.column_size >= 0:
            puzzle_new, parent = self.swap(i, i - 3)
            return PuzzleBoard(puzzle_new, parent, state='Down')

    def move_down(self, i):
        if i + self.column_size <= len(self.puzzle_state) - 1:
            puzzle_new, parent = self.swap(i, i + 3)
            return PuzzleBoard(puzzle_new, parent, state='Up')

    def move_left(self, i):
        if i % self.column_size > 0:
            puzzle_new, parent = self.swap(i, i - 1)
            return PuzzleBoard(puzzle_new, parent, state='Right')

    def move_right(self, i):
        if i % self.column_size < self.column_size - 1:
            puzzle_new, parent = self.swap(i, i + 1)
            return PuzzleBoard(puzzle_new, parent, state='Left')

    def swap(self, index_one, index_two):
        puzzle_new = self.puzzle_state.copy()
        puzzle_new[index_one], puzzle_new[index_two] = puzzle_new[index_two], puzzle_new[index_one]
        return puzzle_new, self

    def print_puzzle(self):
        m = 0
        while (m < 9):
            print()
            print(str(self.puzzle_state[m]) +
                  ' ' +
                  str(self.puzzle_state[m +
                                        1]) +
                  ' ' +
                  str(self.puzzle_state[m +
                                        2]))
            m += 3
        print()

    def expand(self):
        x = list(self.puzzle_state).index(0)
        self.children.append(self.move_up(x))
        self.children.append(self.move_down(x))
        self.children.append(self.move_left(x))
        self.children.append(self.move_right(x))
        self.children = list(filter(None, self.children))
        return self.children

    def write_output(self, search_depth, slist):
        with open('output.txt', "w") as file:
            m = 0
            file.write('Puzzle is : '  + '\n')

            while (m < 9):
         
                file.write(str(self.puzzle_state[m]) + 
                    ' ' +
                    str(self.puzzle_state[m +
                                            1]) +
                    ' ' +
                    str(self.puzzle_state[m +
                                            2]) +'\n' + '\n')
                m += 3
            
            file.write('Solution is : ' + str(slist) + '\n')
           # file.write('cost_of_path: ' + str(len(slist)) + '\n')
            file.write('Search Depts is : ' + str(search_depth) + '\n')
            

def get_entry_field(algorithm_type):
    user_input = e1.get()
    user_input_str = str(user_input)
    puzzle_str = user_input_str.split(",")
    puzzle_state = list(map(int, puzzle_str))
    pb = PuzzleBoard (puzzle_state)
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
    e1.grid(row=0,column=1)
    Button(root,bg="#BEBEBE", text='BFS', font='Helvetica 12 bold',command=lambda:get_entry_field(1)).grid(row=2, column=5)
    Button(root,bg="#BEBEBE", text='DFS', font='Helvetica 12 bold',command=lambda:get_entry_field(2)).grid(row=3, column=5)

    root.mainloop()


if __name__ == '__main__':
    main()

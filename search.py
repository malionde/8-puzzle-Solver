from collections import deque 
import numpy as np 
import sys 

class Search:
 

    def __init__(self):
        self.path_to_solution = []
        self.states = []

    def bfs(self, puzzle_board): 
        global first
        first=puzzle_board
        border = deque() 
        visited = set()
        border.append(puzzle_board) 

        while border:
            puzzle = border.popleft() 
            visited.add(tuple(puzzle.puzzle_status)) 

            if puzzle.goal_test():
                self.path_to_solution = []
                self.track(self.path_to_solution, puzzle)
                return len(self.path_to_solution), self.states

            children = puzzle.expand()

            for c in children[::-1]:
                if tuple(c.puzzle_status) not in visited:
                    border.append(c)
                    visited.add(tuple(c.puzzle_status))

    def dfs(self, puzzle_board):
        border = []
        visited = set()
        border.append(puzzle_board)

        while border:
            puzzle = border.pop()
            visited.add(tuple(puzzle.puzzle_status))

            if puzzle.goal_test():
                self.path_to_solution = []
                self.track(self.path_to_solution, puzzle)
                return len(self.path_to_solution), self.states

            children = puzzle.expand()

            for c in children[::-1]:
                if tuple(c.puzzle_status) not in visited:
                    border.append(c)
                    visited.add(tuple(c.puzzle_status))


    def track(self, path_to_solution, child):
        global alist
        alist = []
        print("Tracing path...")
        while child.parent:
            parent = child.parent
            alist.append(child)


            self.states.append(child.state)
            path_to_solution.append(child)
            child = parent
     

        alist.reverse()

        first.print_puzzle()
        
        for i in alist:
            i.print_puzzle2()

            

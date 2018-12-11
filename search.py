from collections import deque
import numpy as np

class Search:

    def __init__(self):
        self.path_to_solution = []
        self.states = []

    def bfs(self, puzzle_board):
        global first
        first=puzzle_board
        frontier = deque()
        explored = set()
        frontier.append(puzzle_board)

        while frontier:
            puzzle = frontier.popleft()
            explored.add(tuple(puzzle.puzzle_state))

            if puzzle.goal_test():
                self.path_to_solution = []
                self.path_trace(self.path_to_solution, puzzle)
                return len(self.path_to_solution), self.states

            children = puzzle.expand()

            for c in children[::-1]:
                if tuple(c.puzzle_state) not in explored:
                    frontier.append(c)
                    explored.add(tuple(c.puzzle_state))

    def dfs(self, puzzle_board):
        frontier = []
        explored = set()
        frontier.append(puzzle_board)

        while frontier:
            puzzle = frontier.pop()
            explored.add(tuple(puzzle.puzzle_state))

            if puzzle.goal_test():
                self.path_to_solution = []
                self.path_trace(self.path_to_solution, puzzle)
                return len(self.path_to_solution), self.states

            children = puzzle.expand()

            for c in children[::-1]:
                if tuple(c.puzzle_state) not in explored:
                    frontier.append(c)
                    explored.add(tuple(c.puzzle_state))


    def path_trace(self, path_to_solution, child):
       
        alist = []
        print("Tracing path...")
        while child.parent:
            parent = child.parent
            alist.append(child)

            #child.print_puzzle()
            #child.print_puzzle()
            self.states.append(child.state)
            path_to_solution.append(child)
            child = parent
        #if parent.goal_test() != True:
        alist.reverse()
        first.print_puzzle()
        for i in alist:
            i.print_puzzle()

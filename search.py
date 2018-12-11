from collections import deque #liste, sözlük ve tuple üzerinde build-in methodlar sağlar
import numpy as np # Diziler üzerinde hızlı işlem yapılmasını sağlar
import sys #sistem modüllerini içerir.

class Search:
 

    def __init__(self): #ilk değerleri initialize etmeye yarar.
        self.path_to_solution = []
        self.states = []

    def bfs(self, puzzle_board): #Bread First Search 
        global first
        first=puzzle_board
        frontier = deque() #frontier adında bir deque objesi oluşturduk.
        explored = set() # explored adında bir sırası önemli olmayan bir obje oluşturduk. 
        frontier.append(puzzle_board) # puzzle boardda bulunan verileri sırasıyla frontier değişkenine atıyoruz. 

        while frontier:
            puzzle = frontier.popleft() # popleft kullanarak puzzle board'dan eklediğimiz verileri soldan sağa doğru sırayla çıkartıyoruz.
            explored.add(tuple(puzzle.puzzle_state)) # 

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
        global alist
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
        #f = open("output2.txt", "a")
        
        for i in alist:
            #i.print_puzzle()
            i.print_puzzle2()

            
          #  f.write('OLDUUUUUUUUU: ' + i.print_puzzle() + '\n')

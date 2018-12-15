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
        border = deque() #border adında bir deque objesi oluşturduk.
        visited = set() # visited adında bir sırası önemli olmayan bir obje oluşturduk. 
        border.append(puzzle_board) # puzzle boardda bulunan verileri sırasıyla border değişkenine atıyoruz. 

        while border:
            puzzle = border.popleft() # popleft kullanarak puzzle board'dan eklediğimiz verileri soldan sağa doğru sırayla çıkartıyoruz.
            visited.add(tuple(puzzle.puzzle_status)) # 

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

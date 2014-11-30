import maze
import mazeIO
import sys
import random
#the deque class supports pops from both ends
from collections import deque 

#Tan Hao Qin 1000521

###A class for solving mazes###

class MazeSolver:

    #Initializes the solver with the maze to solve
    #The maze class contains (see maze.py):
        # 1) matrix: the matrix of characters ('W', 'O', 'B', or 'E') 
        #            representing the maze
        # 2) start: the starting square as [row, column]
        # 3) end: the ending square as [row, column]
    def __init__(self, maze):

        self.maze = maze

    #Solves a maze.
    #search_type can be either DFS or BFS,
    #depending on whether you want the maze solved
    #using depth first search or breadth first search,
    #respectively.
    #
    #Returns a path through the maze as a list of [row, column]
    #squares where path[0] = maze.start and
    #path[len(path)-1] = maze.end
    #For every square i, path[i] should be adjacent to
    #path[i+1] and maze.matrix[i] should not be 'W'
    #
    #Also returns all the nodes expanded as a [row, column]
    #list.  These need not be in any particular order and
    #should include the nodes on the path.

    def solve_maze(self, search_type):

        #Prepares the nodes for the dps/bfs search
        class Node:
            
            #Node constructor
            def __init__(self,x,y,parent = None,depth = 0):
                self.x = x
                self.y = y
                self.parent = parent
                self.depth = depth
            
            #Returns position of the nodes
            def pos(self):
                return (self.x,self.y)
        
        if (search_type != "DFS" and search_type != "BFS"):
            print "Invalid search type"
            return [], []
        
        if (self.maze.start == []):
            print "Maze does not have starting square"
            return [], []

        if (self.maze.end == []):
            print "Maze does not have ending square"
            return [], []
        
        #All possible direction
        directions = {0:(0,1),1:(0,-1),2:(1,0),3:(-1,0)}
        #Contains the solution to the maze
        path = []
        #Contains all traversed nodes
        expanded = []

        #Property that determines end of function
        self.maze_solved = False
        #Sets the start point and creates the starting node
        start = self.maze.start
        start_node = Node(start[0],start[1])
        #Adds starting nodes to expanded list
        expanded.append(start_node.pos())
        #Creates a deque used for both BFS/DFS, stack for DFS, queue for BFS
        queue = deque()
        queue.append(start_node)

        def BFS_solve():
            #Loop terminates when solved or when all no more nodes to explore
            while len(queue) > 0 and self.maze_solved == False:
                #Using popleft uses the deque as a queue
                current_node = queue.popleft()
                visit(queue,current_node)

        def DFS_solve():
                        
            while len(queue) > 0 and self.maze_solved == False:
                #Using pop uses the deque as a stack
                current_node = queue.pop()
                visit(queue,current_node)

        def visit(queue,node):          
            #Marks node as visited
            x,y = node.pos()
            self.maze.matrix[x][y] = 'V'

            possible_steps = [i for i in range(4)]
            #Tries every single step
            while len(possible_steps)>0:
                #Takes a random step first
                new_pos = step(node,possible_steps.pop(random.randint(0,len(possible_steps)-1)))
                #Checks if maze solved
                if solved(new_pos):
                    new_node = Node(new_pos[0],new_pos[1],node,node.depth+1)
                    retrace(new_node)
                    self.maze_solved = True
                    print "END OF MAZE FOUND"
                    return
                #Checks if next node is valid
                elif not visited(new_pos) and is_valid_pos(new_pos):
                    new_node = Node(new_pos[0],new_pos[1],node,node.depth+1)            
                    queue.append(new_node)
                    expanded.append(new_pos)
        
        #Takes a step towards direction i
        def step(node,i):
                x,y = node.pos()
                newx,newy = directions[i] 
                return (x+newx,y+newy)

        #Checks if we are visiting a visited node
        def visited(pos):
            return pos in expanded
        
        #Check if we are visiting a valid location
        def is_valid_pos(pos):
            return self.maze.matrix[pos[0]][pos[1]] == 'O'
        
        #Check if we are visiting the ending point
        def solved(pos):
            return self.maze.matrix[pos[0]][pos[1]] == 'E'

        #Retraces the steps taken when maze solved by finding parents            
        def retrace(node):
                path.append(node.pos())
                a,b = node.pos()
                self.maze.matrix[a][b] = 'X'
                if node.parent!=None:                
                    retrace(node.parent)            
        
        #Runs the appropriate search
        if search_type == "BFS":
            BFS_solve()
        elif search_type == "DFS":
            DFS_solve()
        #Reverses the path
        path.reverse()
        path = path[1:-1]

        self.maze.matrix[self.maze.end[0]][self.maze.end[1]] = 'E'
        self.maze.matrix[self.maze.start[0]][self.maze.start[1]] = 'B'
        return path, expanded 

        

        

#This main function will allow you to test your maze solver
#by printing your solution to a ppm image file or ascii text file.
#
#Usage: maze_solver input_filename output_filename <image scaling>
#
#You must specify the input file name and the output file name. 
#The input should be a .ppm or .txt file in the form output by
#the mazeIO class.  See test_maze.ppm and many_paths.txt for examples.
#
#You also need to specify a search type:
#BFS: solves the maze using breadth first search
#DFS: solves the maze using depth first search
#
#For small mazes, a one-to-one
#correspondence between maze squares and pixels will be too small to see
#(ie a 10x10 maze gives an image of 10x10 pixels)
#so the ppm image is scaled when written out.  If you are trying to
#read in a scaled ppm image, you MUST specify image scaling to be
#the correct scaling or you will get a very strange looking solution.
#For example, the scaling used to print out test_maze.ppm was 6 so
#to solve test_maze.ppm using breadth first search and write it out to
#test_path.ppm you would use:
#
#python maze_solver_skeleton.py newMaze.ppm solvedMaze.ppm BFS 6
#
#If you read in an image, the same scaling will be used to output the
#image so in the example test_path.ppm will also be scaled by a factor
#of 6.  The actual maze is 50x50 so both ppm images are 300x300 pixels.
#
#You may read in a maze as a text file and output it as an image file or
#vice-versa.  If you read a maze in as a text file, you can specify a
#scaling just for the output file.

def main(argv):

    if (len(argv) < 4):
        print "Usage: maze_solver input_file output_file search-type <image scaling>"
        return
    infilename = argv[1]
    innameparts = infilename.split('.')
    if (len(innameparts) != 2 or (innameparts[1] != "ppm" \
                                  and innameparts[1] != "txt")):
        print "Must enter an input file name ending in .ppm or .txt"
        return
    outfilename = argv[2]
    outnameparts = outfilename.split('.')
    if (len(outnameparts) != 2 or (outnameparts[1] != "ppm" \
                                   and outnameparts[1] != "txt")):
        print "Must enter an output file name ending in .ppm or .txt"
        return
    if (argv[3] != "DFS" and argv[3] != "BFS"):
        print "Please enter valid search type.  Choose one of: BFS, DFS"
        return
    searchtype = argv[3]
    scaling = 1
    if (len(argv) > 4):
        try:
            scaling = int(argv[4])
        except:
            scaling = 1
    if (scaling <= 0):
        scaling = 1
    if (innameparts[1] == "ppm"):
        maze = mazeIO.ppmIO.read_maze_from_ppm(infilename, scaling)
    else:
        maze = mazeIO.asciiIO.read_maze_from_ascii(infilename)
    solver = MazeSolver(maze)
    path, expanded = solver.solve_maze(searchtype)
    print "Length of path:", len(path), \
        "\nNumber of nodes expanded: ", len(expanded)
    if (outnameparts[1] == "ppm"):
        mazeIO.ppmIO.write_visited_to_ppm(outfilename, maze, expanded, path, scaling)
    else:
        mazeIO.asciiIO.write_visited_to_ascii(outfilename, maze, expanded, path)

if __name__ == "__main__":
    main(sys.argv)


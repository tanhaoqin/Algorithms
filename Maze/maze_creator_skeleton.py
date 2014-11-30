import maze as maze_class
import mazeIO
import random
import sys

#Tan Hao Qin 1000521

###A class for creating mazes###

class MazeCreator:

    #Constructs a maze creator, which
    #just stores the size of the maze
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols


    #You will return a maze object, maze, from this function such that:
    # 1) maze.matrix is size rows X cols
    # 2) maze.end = end and maze.matrix[end[0]][end[1]] = 'E'
    # 3) maze.start = some square you pick and 
    #    maze.matrix[maze.start[0]][maze.start[1]] = 'B'
    # 4) There is an open path from start to end, marked out by 'O's
    #    and the maze is an interesting maze created using DFS
    
    #Input: end: the goal square as [row, column]
    def create_maze(self, end):

        #this creates a rows X cols matrix of all walls
        matrix = [['W' for i in range(self.cols)] \
                   for j in range(self.rows)]        
        
        #this creates a new maze (see maze.py)
        #the maze class stores:
        # 1) the matrix we have just created
        # 2) the starting square, which is the empty list right now
        # 3) the ending square, which was passed into the function
        #you can set the starting square using
        # maze.start = start

        maze = maze_class.Maze(matrix, [], end)

        #Saving the ending points as variable for easy access
        i,j = (end[0],end[1])
        #Saves visited nodes
        visited_nodes = []
        #Possible directions the maze can step towards
        directions = {0:(0,1),1:(0,-1),2:(1,0),3:(-1,0)}
        #Generates a random step given a vertex
        #Returns both vertices that we will step towards
        def step(vertex):
            x,y = vertex
            #Generates random direction
            direction = random.randint(0,3)
            newx,newy = directions[direction] 
            return (x+newx,y+newy),(x+2*newx,y+2*newy)
        #Checks if a given node is within the grid for the maze       
        def withinGrid(vertex):
            x,y = vertex
            return x>0 and x<self.rows-1 and y>0 and y<self.cols-1
        #Checks if a given node has already been visited before the node
        def visited(vertex):
            return vertex in visited_nodes
        #DFS-Visit a vertex for maze creation
        def visit(vertex,matrix):
            x,y = vertex
            print "Visiting node "+str(x)+","+str(y)
            matrix[x][y] = 'O'
            visited_nodes.append(vertex)
            tries = 0
            #Tries ten times to see if there is a possible step around the current node
            while tries<10:
                newgrid = step(vertex)
                tries+=1
                #Checks the two condition before recursively running visit on the new node
                if withinGrid(newgrid[1]):
                    if not visited(newgrid[1]):
                        matrix[newgrid[0][0]][newgrid[0][1]] = 'O'
                        visit(newgrid[1],matrix)
                        
        visit((i,j),maze.matrix)
        #My code overwrites the original "E" so it get rewritten
        maze.matrix[i][j] = 'E'
        #Finds a random point and assign it as the starting point. While loop terminates when a proper point is selected
        while True:
            x,y = random.randint(1,self.rows-2),random.randint(1,self.rows-2)
            if matrix[x][y] == 'O':
                maze.start = [x,y]
                matrix[x][y] = 'B'
                break
        
        print maze.start

        return maze

#This main function will allow you to test your maze creator
#by printing your maze to a ppm image file or ascii text file.
#
#Usage: maze_creator rows cols output_filename <image scaling>
#
#You must specify the size of the maze (rows X cols) and the
#output file name.  This name should end in .ppm for a ppm image
#and .txt for an ascii file.  
#
#If you have a small maze, a one-to-one
#correspondence between maze squares and pixels will be too small to see
#(ie a 10x10 maze gives an image of 10x10 pixels)
#so the optional argument image scaling allows you to set the number of
#pixels per maze square so that each maze square is actually scaling X scaling
#pixels.  Generally, images of 300 x 300 to 600 x 600 pixels 
#are easiest to look at so for a maze of size 10x10, a scaling of 30-60
#is appropriate.

def main(argv):
    if (len(argv) < 4):
        print "Usage: maze_creator rows cols output_filename <image scaling>"
        return

    rows = int(argv[1])
    cols = int(argv[2])
    nameparts = argv[3].split('.')
    if (len(nameparts) != 2 or \
        (nameparts[1] != "txt" and nameparts[1] != "ppm")):
        print "You must specify either ASCII output (.txt filename) or PPM output (.ppm filename)"
        return
    creator = MazeCreator(rows, cols)
    maze = creator.create_maze([random.randint(1, rows-2), \
                                random.randint(1, cols-2)])
    if (nameparts[1] == "txt"):
        mazeIO.asciiIO.write_maze_to_ascii(argv[3], maze)
    else:
        scaling = 1
        if (argv > 4):
            try:
                scaling = int(argv[4])
            except:
                scaling = 1
        if (scaling <= 1):
            scaling = 1
        mazeIO.ppmIO.write_maze_to_ppm(argv[3], maze, scaling)

if __name__ == "__main__":
    main(sys.argv)
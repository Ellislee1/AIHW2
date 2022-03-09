import numpy as np



class Environment:
    tile_n = 4

    def __init__(self, landscape, state = None, closed = {}, assignments = None):
        self.landscape = landscape                          # Initial Landscape
        self.n = landscape.shape[0]                         # Landscape size

        if state is None:
            self.state = np.zeros((self.n, self.tile_n, self.tile_n))     # Empty array that we add our solution to
            self.assignments = np.zeros(self.n)
        else:
            self.state = state.copy()
            self.assignments = assignments
        
        
        self.closed = closed

    def getBlock(self, i):
        return self.landscape[i].copy()

    def getSize(self):
        return self.n
    
    def getState(self):
        return self.state.copy()

    def getClosed(self):
        return self.closed.copy()

    def getAssignments(self):
        return self.assignments.copy()

    def checkVisited(self, _hash):
        return _hash in self.closed
    
    def fillRemaining(self, value):
        self.assignments[self.assignments == 0] = value

    def isValidProblem(self, total_tiles):
        return total_tiles >= self.n

    def addAssignment(self, i, value):
        self.assignments[i] = value
    
    def removeAssignment(self, i):
        self.assignments[i] = 0

    def getSolution(self, csp):
        solution_string = "\n----------\n SOLUTION\n----------\n"

        for i, assignment in enumerate(self.assignments):
            solution_string  += f'{i}:\t{csp.names[assignment]}\n'
        
        return solution_string


    def copy(self):
        return Environment(self.landscape, self.state, self.getClosed(), self.assignments)
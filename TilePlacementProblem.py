import numpy as np

from src.csp import CSP
from src.Environment import Environment
from src.filehandling import openfile
from src.util import hashState, checkSolution, get_h, checkHolds
from time import perf_counter as time

"""PROBLEM SPECIFIC PARAMETERS"""
FILE = "test/tilesproblem_1326658913086500.txt" # Change this file

class Search:
    """ The search alg class
    """
    def __init__(self):
        self.closed = {}    # queue of closed items
        self.queued = {}    # queue of active

    def search(self, env, csp, i=0):

        if i == env.getSize()-csp.num_full:  # If all items have been placed, end
            return ((0 == env.assignments).any() == False) and get_h(csp.goals, env.state, env.state) == 0
        domain = csp.genChildren(env.getState(), env, env.assignments, self.queued, self.closed)    # generate all children of this space

        while len(domain) > 0: # While there is a child
            _, d = domain.pop() # remove the one with the lowest h
            key = d['key']

            del self.queued[hashState(d['s'])] 
        

            env.addAssignment(d['i'],key)   # Update state

            if hashState(env.getAssignments()) in self.closed:  # If state has been visited undo and check next in queue
                env.removeAssignment(d['i'])
                continue

            self.closed[hashState(env.getAssignments())] = 0 # Add state to closed set

            if d['h'] == 0: # if h is 0 then we are supposedly at the end state begin checking that
                if checkSolution(csp.goals, d['s'], d['Y'], csp.total_tiles): # Check if solution
                    env.fillRemaining(3)    # If it is fill the remaining tiles to 3
                    return True
                else:
                    env.removeAssignment(d['i']) # if it isnt then false solution revert and continue
                    continue

        
            env_2 = env.copy()  # Prepare next env state
            env_2.state = d['Y']


            if self.search(env_2, csp, (i+1)):  # carry on search
                return True
        
            env.removeAssignment(d['i'])    # If no solution undo and check next
        return False    # If no solution return false


def main(landscape, tile_constraints, goals):
    env = Environment(landscape)
    csp = CSP(tile_constraints, goals)

    s = Search()

    total = np.sum(goals)
    if total == 0 and not csp.num_full == env.n:
        print("NO SOLUTION")
        return False
    elif total == 0 and csp.num_full == env.n:
        env.assignments = np.full((env.n), 3)
        printSolution(env,csp)
        return True

    if not checkHolds(env.landscape, csp.goals):
        print("NO SOLUTION")
        return False
        



    if not env.isValidProblem(csp.total_tiles):
        print("NO SOLUTION\n::[Message]:: Too few tiles not a valid problem")
        return False
    elif s.search(env, csp):
        printSolution(env,csp)
        return True
    else:
        print("NO SOLUTION")
        return False

def printSolution(env,csp):
    for i in range(len(env.assignments)):
        env.landscape[i] = env.landscape[i] * csp.masks[env.assignments[i]]

        vals = {}

    for i in range(4):
        vals[i+1] = np.count_nonzero(env.landscape == (i+1))
            
    print(vals)
    print(env.getSolution(csp))



if __name__ == "__main__":
    file = FILE
    l,C,T = openfile(file)

    # Use this for random tests
    # np.random.seed(114)
    # l = np.random.randint(0,5,(4,4,4))
    # l = np.ones((4,4,4))
    # C = {
    #     "OUTER_BOUNDARY": 1,
    #     "FULL_BLOCK": 1,
    #     "EL_SHAPE": 1
    # }

    # T = [1,0,0,0]
    print(l)
    print(C)
    print(T)
    
    start = time()
    main(l,C,T)
    stop = time()

    print(f'That took {(stop-start):.1f} Seconds')

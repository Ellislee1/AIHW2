import numpy as np
import numba as nb
from src.util import hashState, get_h


class CSP:
    masks = {
        1: np.array([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]), # OUTER
        2: np.array([[0,0,0,0],[0,1,1,1],[0,1,1,1],[0,1,1,1]]), # EL
        3: np.zeros((4,4)) # FULL BLOCK
    }

    names = {
        1: "OUTER_BOUNDARY",
        2: "EL_SHAPE",
        3: "FULL_BLOCK",
    }

    def __init__(self, tile_constraints, goals: np.array):
        self.initilise(tile_constraints)    # The constraints on the number of tiles
        self.goals = goals                  # The goals to reach in the order 1,2,3,4
        
        self.path = []                      # The current path
        self.closed_states = {}             # All states that have been closed (valid and non valid)
        self.num_full = tile_constraints['FULL_BLOCK']

    def initilise(self, tile_constraints):
        self.constraints = {}
        self.total_tiles = 0
        for i, name in self.names.items():
            max_tiles = tile_constraints[name]
            self.total_tiles += max_tiles
            self.constraints[i] = max_tiles


    def ac3(self, state, h):
        if h == -1:
            return False

        for key, val in self.constraints.items():

            if np.count_nonzero(state == key) > val:
                return False

        return True

    # def genChildren(self, X, block, state, i):
    #     domain = {}

    #     for key, mask in self.masks.items():
    #         Y = X.copy()
    #         area = block.copy()
    #         s = state.copy()

    #         Y[i] = area * mask
    #         s[i] = key

    #         h = self.get_h(Y)

    #         if not self.ac3(s, h):  # Check the validity of this domain before adding it
    #             continue    # If not valid dont add it 

    #         domain[key] = {
    #             'Y': Y,
    #             's': s,
    #             'h': h
    #         }

    #     return sorted(domain.items(), key=lambda k_v: k_v[1]['h'])

    def genChildren(self, X, env, state, queued, closed):
        domain = {}

        count = 0
        for i in range(env.n):
            if state[i] > 0:
                continue
            for key, mask in self.masks.items():
                if key == 3:
                    continue
                Y = X.copy()
                area = env.getBlock(i)
                s = state.copy()

                Y[i] = area * mask
                s[i] = key

                h = get_h(self.goals, Y,X)

                if not self.ac3(s, h):  # Check the validity of this domain before adding it
                    continue    # If not valid dont add it 
                
                hashed = hashState(s)

                if  hashed in queued or hashed in closed:
                    continue

                queued[hashState(s)] = 0


                domain[count] = {
                    'i': i,
                    'key': key,
                    'Y': Y,
                    's': s,
                    'h': h
                }
                count += 1

        return sorted(domain.items(), key=lambda k_v: k_v[1]['h'])
    
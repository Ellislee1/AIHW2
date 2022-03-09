import numpy as np
import numba as nb

def hashState(state):
    h_string = ""

    count = 0
    for v in state:
        count += 1
        h_string += f'_{v}'
    return hash(h_string)

@nb.njit()
def get_h(goals: np.array, array:  np.array, previous: np.array):
        out = 0
        

        for i, target in enumerate(goals):
            count =  np.count_nonzero(array == (i+1))
            if target == 0:
                out +=count
                continue

            count =  np.count_nonzero(array == (i+1))
            prev_count = np.count_nonzero(previous == (i+1))

            if count-target > 0:
                return -1     # If we have added too many of a number we need to make sure we dont expand this
            if count == 0:
                count = 0.9
            a = ((target/count)-(prev_count/target))*(target-count)
            out += a
        out = np.ceil(np.sqrt(out))
        return out

# @nb.njit()
# def get_h(goals: np.array, array:  np.array,  previous: int):
#         out = 0
        

#         for i, target in enumerate(goals):
#             count =  np.count_nonzero(array == (i+1))
#             if target == 0:
#                 out +=count
#                 continue

#             count =  np.count_nonzero(array == (i+1))
#             # prev_count = np.count_nonzero(previous == (i+1))

#             if count-target > 0:
#                 return -1     # If we have added too many of a number we need to make sure we dont expand this
#             if count == 0:
#                 count = 0.9
#             # a = ((target/count)-(prev_count/target))*(target-count)
#             a = ((target/count)*(target-count))
#             out -= a
#         out = np.ceil(np.sqrt(out)) + previous
#         return out

def checkSolution(goals: np.array, assignments: np.array, state: np.array, full: np.array):
        for i, val in enumerate(goals):
            if not np.count_nonzero(state == (i+1)) == val:
                return False
        
        left = np.count_nonzero(assignments == 0)

        if left > full:
            return False
        return True


def checkHolds(state, goals):
        for i in range(len(goals)):
            if np.count_nonzero(state == i+1) < goals[i]:
                return False
        return True

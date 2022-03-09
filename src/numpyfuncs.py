import numpy as np

def rolling_window(a):
    """Return each window in an array (window of six nxn)"""
    final = []
    x,y = a.shape

    for j in range(0,x,4):
        for i in range(0,y,4):
            t = np.array(a[i:i+4,j:j+4]).reshape((4,4))
            final.append(t)
    return np.array(final)
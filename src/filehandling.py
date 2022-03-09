"""filehandling.py holds methods to open and parse files (including test files) as well as save outputs where applicible.
openfile: Opens a file, parses and returns its elements as a dictionary.

Ellis Thompson
"""
import numpy as np
from src.numpyfuncs import rolling_window

def openfile(filepath):
    """Open a file and return its contents as a dictionary to generate a class from"""
    filecontents = {"landscape": [], "tiles": {}, "targets": [], "solution": []}

    f = open(filepath, "r")
    final = []

    temp = []
    for line in f:
        if line.startswith("#"):
            if not temp == []:
                final.append(temp)
                temp = []
        else:
            x = line.replace("\n", "")
            if not x == "":
                temp.append(x)
    if not temp == []:
        final.append(temp)
        temp = []

    landscape = rolling_window(parselandscape(final[0]))
    tiles = parse_tiles(final[1][0])
    targets = parse_targets(final[2])

    return(landscape,tiles,targets)

def parse_targets(targets):
    constraints = np.zeros(4)

    for t in targets:
        vals = t.split(':')

        constraints[int(vals[0])-1] = int(vals[1])
    return constraints

def parse_tiles(tiles):
    tiles = tiles.replace('{','').replace('}','').split(', ')
    t = {}

    for tile in tiles:
        tile = tile.split('=')
        mask = np.ones((4,4))

        if tile[0] == 'OUTER_BOUNDARY':
            out = int(tile[1])
        elif tile[0] == 'EL_SHAPE':
            out = int(tile[1])
        elif tile[0] == 'FULL_BLOCK':
            out = int(tile[1])
        
        t[tile[0]] = out

    return t


def parselandscape(landscape):
    width, height = len(
        landscape[0].replace(" ", "_").replace("__", "_0").replace("_", "")
    ), len(landscape)

    ls_array = []
    for row in landscape:

        if row[0] == " ":
            row = list(row)
            row[0] = "0"
            row = "".join(row)
        r = np.array(
            list(map(int, row[:-1].replace(" ", "_").replace("__", "_0").split("_")))
        )
        ls_array.append(r)

    return np.array(ls_array)

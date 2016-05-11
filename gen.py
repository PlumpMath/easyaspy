from ._main import *
from .seq import *

def file(filename, struct, *data):
    lines = zip(*data)
    with write(filename) as f:
        for line in lines:
            f.write(struct.format(*line))

def cube(n=2):
    X,Y,Z = [range(2)]*3
    return [[[z*n*n + y*n + x
        for x in X]
            for y in Y]
                for z in Z]

def graph(n=2):
    def ifapp(a,x,y,z):
        try:
            E.append((a,C[z][y][x]))
        except:
            return

    C = cube(n)
    E = []
    for z,Z in enumerate(C):
        for y,Y in enumerate(Z):
            for x,X in enumerate(Y):
                ifapp(X,x+1,y,z)
                ifapp(X,x,y+1,z)
                ifapp(X,x,y,z+1)
    return E


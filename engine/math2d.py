import numpy as np

deg2rad = np.pi/180

# Distance or Difference functions used in simple collision
def DistanceXY(pos0,pos1):return (np.abs(pos0[0]-pos1[0]),np.abs(pos0[1]-pos1[1]))
def Distance(pos0,pos1):return np.sum(DistanceXY(pos0,pos1))

# Sine and Cosine rotation in degrees
def RotatePoint(orgin, pos, rotation):
    s = np.sin(rotation*deg2rad)
    c = np.cos(rotation*deg2rad)
    return ((orgin[0]+(pos[0]*c))-(orgin[1]+(pos[1]*s)),(orgin[0]+(pos[0]*s))+(orgin[1]+(pos[1]*c)))
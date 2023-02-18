import numpy as np

deg2rad = np.pi/180

def clamp(x,xmin,xmax):return min(xmax,max(x,xmin))
def SliceLimit(s,smin,smax):
    if (type(s) == slice):
        step = s.step
        start = s.start
        stop = s.stop
        if step == None:step = 1
        if start == None:start = smin
        if stop == None:stop = smax
        return slice(round(clamp(start,smin,smax)),round(clamp(stop,smin,smax)),int(step))
    else:
        if (s < smin):return None
        elif (s > smax):return None
        return s
def ClipIndex(a,b,amin,amax,bmin,bmax):
    a = SliceLimit(a,amin,amax)
    b = SliceLimit(b,bmin,bmax)
    if not((a == None) or (b == None)):return (a,b)
    return None


# Distance or Difference functions used in simple collision
def DistanceXY(pos0,pos1):return (np.abs(pos0[0]-pos1[0]),np.abs(pos0[1]-pos1[1]))
def Distance(pos0,pos1):return np.sum(DistanceXY(pos0,pos1))

# Sine and Cosine rotation in degrees
def RotatePoint(orgin, pos, rotation):
    s = np.sin(rotation*deg2rad)
    c = np.cos(rotation*deg2rad)
    return ((orgin[0]+(pos[0]*c))-(orgin[1]+(pos[1]*s)),(orgin[0]+(pos[0]*s))+(orgin[1]+(pos[1]*c)))
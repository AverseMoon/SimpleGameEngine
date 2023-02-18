from .math2d import ClipIndex
import numpy as np

class Frame():
    def __init__(self,arr):
        self.arr = np.array(arr)
    
    def __len__(self):
        return self.arr.shape[1]

    @property
    def size(self):
        s = self.arr.shape
        return (s[1],s[0])
    
    @property
    def array(self):return self.arr
    
    def __getitem__(self, item):
        item = ClipIndex(item[1],item[0],0,self.arr.shape[0],0,self.arr.shape[1])
        if (item != None):return self.arr[item[0],item[1]]
        return 0
    def __setitem__(self, item, value):
        item = ClipIndex(item[1],item[0],0,self.arr.shape[0],0,self.arr.shape[1])
        if (item != None):self.arr[item[0],item[1]] = value
        return 0
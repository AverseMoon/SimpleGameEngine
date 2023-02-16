import numpy as np

class Frame():
    def __init__(self,arr):
        self.arr = arr

    def __len__(self):
        return self.arr.length

    @property
    def size(self):
        s = self.arr.shape
        return (s[1],s[0])
    
    @property
    def array(self):return self.arr
    
    def __getitem__(self, item):
        return self.arr[item[1],item[0]]
    def __setitem__(self, item, value):
        self.arr[item[1],item[0]] = value
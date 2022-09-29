import random
import matplotlib
import matplotlib.pyplot as plt
from numba import jit
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class RSOS:
    def __init__(self):
        self.interAct=1000
        self.monteCarloTime=1000
        self.Lenth=64
        self.height=np.zeros((self.Lenth,self.Lenth))
        self.point=np.linspace(0,self.Lenth-1,self.Lenth)
        self.xvalue,self.yvalue=np.meshgrid(self.point,self.point)

    def side(self,x):
        if x==self.Lenth-1:right=0
        else :right=x+1
        if x==0:left=self.Lenth-1
        else :left=x-1
        return left,right

    def slide(self,a,x,y):
        if a==x+2 or a==y+2:
            return a-1
        else:
            return a

    def monteCarlo(self):
        for i in range (0,self.interAct*self.monteCarloTime):
            dropX=random.randint(0,self.Lenth-1)
            dropY=random.randint(0,self.Lenth-1)
    
            leftX,rightX=self.side(dropX)
            leftY,rightY=self.side(dropY)
            s=(self.height[dropX][dropY]+1)
            s=self.slide(s,self.height[leftX][dropY],self.height[rightX][dropY])
            self.height[dropX][dropY]=self.slide(s,self.height[dropX][leftY],self.height[dropX][rightY])

    def plot(self):
        d3=plt.figure()
        d3ax=plt.axes(projection='3d')
        d3ax.set_xlabel('X axis')
        d3ax.set_ylabel('y axis')
        d3ax.plot_surface(self.xvalue,self.yvalue,self.height)
        plt.show()

a=RSOS()
a.monteCarlo()
a.plot()

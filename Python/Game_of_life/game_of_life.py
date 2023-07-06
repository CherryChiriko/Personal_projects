import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
 
# First set up the figure, the axis, and the plot element we want to animate
M = np.full((10,10), 0)
fig, ax = plt.subplots()
matrix = ax.matshow(M)
cb = plt.colorbar(matrix)
cb.remove() 
x, y = [], []
# initialization function: plot the background of each frame
def init():
    # M[5,5:8] = 1                          # BLINKER CONFIGURATION (period 2)
    M[0:3,2] = 1; M[1,0] = 1;  M[2,1] = 1   # GLIDER CONFIGURATION
    matrix.set_array(M)
    return matrix,

class Ma:
    def __init__(self):
        global M
        self.M = M
        
    def __call__(event):
        global M
        print('click', event)
        if event.inaxes!= M.axes: return
        x.append(event.xdata)
        y.append(event.ydata)
        M[event.xdata,event.ydata] = 1
        matrix.set_array(M)
        return matrix,
m = Ma()

# animation function.  This is called sequentially
def animate(i):
    global M
    N = M.copy()
    for x0, row in enumerate(M):
        for y0, _ in enumerate(row):
            n_sum = M[max(0, x0-1) : x0 + 2, max(0, y0-1) : y0 + 2].sum() - M[x0,y0]
            if n_sum == 3: N[x0,y0] = 1
            elif n_sum == 2 and M[x0,y0] == 1: N[x0,y0] = 1
            else: N[x0,y0] = 0
    M = N.copy()
    matrix.set_array(M)
    return matrix,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=500, blit=True)

plt.show()

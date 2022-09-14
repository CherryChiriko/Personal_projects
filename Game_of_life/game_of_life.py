import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
 


# First set up the figure, the axis, and the plot element we want to animate
M = np.full((10,10), 0)
fig, ax = plt.subplots()
matrix = ax.matshow(M)
plt.colorbar(matrix)


# initialization function: plot the background of each frame
def init():
    M[5,5] = 1
    M[5,6] = 1
    M[5,7] = 1
    matrix.set_array(M)
    return matrix,

# animation function.  This is called sequentially
def animate(i):
    N = M.copy()
    for x0, row in enumerate(M):
        for y0 in row:
            if M[max(0, x0-1) : x0 + 2, max(0, y0-1) : y0 + 2].sum() == 2: N[x0,y0] = 1
     
    x = i
    y = i*2
    M[x,y] = 1
    matrix.set_array(M)
    return matrix,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(M), interval=50, blit=True)

# plt.matshow(matrix, fignum=0)
plt.show()
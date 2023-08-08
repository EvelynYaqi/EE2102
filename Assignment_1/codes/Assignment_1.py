import sys
sys.path.insert(0, "/home/lancelot/Latex/EE2102/CoordGeo")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen




A=np.array([1, -1])
B=np.array([-4, 6])
C=np.array([-3, -5])

x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

[I,r] = icircle(A,B,C)
x_icirc= circ_gen(I,r)
x_AI = line_gen(A ,I)



plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AI[0,:],x_AI[1,:],label='$AI$')


tri_coords = np.vstack((A,B,C,I)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','I']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
                 (tri_coords[0,i], tri_coords[1,i]),
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center') 


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig('/home/lancelot/Latex/EE2102/Assignment_1/figs/angular_bisector.png')
#code for finding angular bisector.
A=np.array([1, -1])
B=np.array([-4, 6])
C=np.array([-3, -5])
D=B-A
n3=np.array([D[1],D[0]*(-1)])
norm_n3 = np.linalg.norm(D)
vec_c3= n3 * A
c3 = vec_c3[0]+vec_c3[1]
E=C-A
n2=np.array([E[1],E[0]*(-1)])
norm_n2 = norm_vec(C,A)
n2=np.array([E[1]*(-1),E[0]])
norm_n2 = np.linalg.norm(E)
vec_c2= n2 * C
c2 = vec_c2[0]+vec_c2[1]
print("Internal Angular bisector of angle A is:\n",(n3/norm_n3)-(n2/norm_n2),"x = ",(c3/norm_n3)-(c2/norm_n2))

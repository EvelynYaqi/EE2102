import numpy as np
import sys                                         
sys.path.insert(0, '/home/lancelot/Latex/EE2102/Assignment_4/CoordGeo')        #path to my scripts
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
def Q1_1_3(A,B,C):
	x_AB = line_gen(A,B)
	x_BC = line_gen(B,C)
	x_CA = line_gen(C,A)

#Plotting all lines
	plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
	plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
	plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')


#Labeling the coordinates
	A = A.reshape(-1,1)
	B = B.reshape(-1,1)
	C = C.reshape(-1,1)

	tri_coords = np.block([[A, B, C]])
	plt.scatter(tri_coords[0, :], tri_coords[1, :])
	vert_labels = ['A', 'B', 'C']
	for i, txt in enumerate(vert_labels):
	    offset = 10 if txt == 'C' else -10
	    plt.annotate(txt,
	                 (tri_coords[0, i], tri_coords[1, i]),
	                 textcoords="offset points",
	                 xytext=(0, offset),
        	         ha='center')
	plt.xlabel('$x$')
	plt.ylabel('$y$')
	plt.legend(loc='best')
	plt.grid() # minor
	plt.axis('equal')


	plt.savefig('/home/lancelot/Latex/EE2102/Assignment_4/figs/question-1_1_3.png')
def AreaCalc(A, B, C):
    AB = A - B
    AC = A - C
#cross_product calculation
    cross_product = np.cross(AB,AC)
#magnitude calculation
    magnitude = np.linalg.norm(cross_product)

    area = 0.5 * magnitude

    return area
def Q1_2_1(A , B , C):
	x_AB = line_gen(A,B)
	x_BC = line_gen(B,C)
	x_CA = line_gen(C,A)
	D = (B + C)/2
	E = (A + C)/2
	F = (A + B)/2

	
	
	#Plotting all lines
	plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
	plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
	plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
	
	
	#Labeling the coordinates
	A = A.reshape(-1,1)
	B = B.reshape(-1,1)
	C = C.reshape(-1,1)
	D = D.reshape(-1,1)
	E = E.reshape(-1,1)
	F = F.reshape(-1,1)
	tri_coords = np.block([[A,B,C,D,E,F]])
	plt.scatter(tri_coords[0,:], tri_coords[1,:])
	vert_labels = ['A','B','C','D','E','F']
	for i, txt in enumerate(vert_labels):
	    plt.annotate(txt, # this is the text
        	         (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
	                 textcoords="offset points", # how to position the text
                 	xytext=(0,10), # distance from text to points (x,y)
	                 ha='center') # horizontal alignment can be left, right or center
	
	plt.xlabel('$x$')
	plt.ylabel('$y$')
	plt.legend(loc='best')
	plt.grid() # minor
	plt.axis('equal')
	plt.savefig('/home/lancelot/Latex/EE2102/Assignment_4/figs/question-1_2_1.png')
def Q1_2_2(A , B , C):
	D = (B + C)/2
	E = (A + C)/2
	F = (A + B)/2
	x_AB = line_gen(A,B)
	x_BC = line_gen(B,C)
	x_CA = line_gen(C,A)
	
	
	
	x_AD = line_gen(A, D)
	plt.plot(x_AD[0, :], x_AD[1, :], label='$AD$')
	
	x_BE = line_gen(B, E)
	plt.plot(x_BE[0, :], x_BE[1, :], label='$BE$')
	
	x_CF = line_gen(C, F)
	plt.plot(x_CF[0, :], x_CF[1, :], label='$CF$')
	
	A = A.reshape(-1,1)
	B = B.reshape(-1,1)
	C = C.reshape(-1,1)
	D = D.reshape(-1,1)
	E = E.reshape(-1,1)
	F = F.reshape(-1,1)
	tri_coords = np.block([[A,B,C,D,E,F]])
	plt.scatter(tri_coords[0,:], tri_coords[1,:])
	vert_labels = ['A','B','C','D','E','F']
	for i, txt in enumerate(vert_labels):
	    plt.annotate(txt, # this is the text
	                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
	                 textcoords="offset points", # how to position the text
	                 xytext=(-10,10), # distance from text to points (x,y)
	                 ha='center') # horizontal alignment can be left, right or center
	plt.xlabel('$x$')
	plt.ylabel('$y$')
	plt.legend(loc='best')
	plt.grid() # minor
	plt.axis('equal')
	plt.savefig('/home/lancelot/Latex/EE2102/Assignment_4/figs/question-1_2_2.png')
def Q_1_2_3(A,B,C):
	D = (B + C)/2
	E = (A + C)/2
	F = (A + B)/2
	G = line_intersect( norm_vec(F,C) , C , norm_vec(E,B) , B)
	x_AB = line_gen(A,B)
	x_BC = line_gen(B,C)
	x_CA = line_gen(C,A)
	x_BE = line_gen(B,E)
	x_CF = line_gen(C,F)
	
	
	#Plotting all lines
	plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
	plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
	plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
	plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')
	plt.plot(x_CF[0,:],x_CF[1,:],label='$CF$')

	#Labeling the coordinates
	A = A.reshape(-1,1)
	B = B.reshape(-1,1)
	C = C.reshape(-1,1)
	D = D.reshape(-1,1)
	E = E.reshape(-1,1)
	F = F.reshape(-1,1)
	G = G.reshape(-1,1)
	tri_coords = np.block([[A, B, C, D, E, F, G]])
	plt.scatter(tri_coords[0, :], tri_coords[1, :])
	vert_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
	for i, txt in enumerate(vert_labels):
	    offset = 10 if txt == 'G' else -10
	    plt.annotate(txt,
	                 (tri_coords[0, i], tri_coords[1, i]),
	                 textcoords="offset points",
        	         xytext=(0, offset),
	                 ha='center')
	plt.xlabel('$x$')
	plt.ylabel('$y$')
	plt.legend(loc='best')
	plt.grid() # minor
	plt.axis('equal')
	plt.savefig('/home/lancelot/Latex/EE2102/Assignment_4/figs/question-1_2_3.png')
def Q1_2_7(A, B , C):
	np.set_printoptions(precision=2)
	#Now we calculate the co-ordinates of the mid-points D,E,F of the sides AB,BC,CA respectively

	D = (B + C)/2
	E = (A + C)/2
	F = (A + B)/2

	

	#Hence verified that A - F = E - D and AFDE is a parallelogram

	#Generating all lines
	x_AB = line_gen(A,B)
	x_BC = line_gen(B,C)
	x_CA = line_gen(C,A)
	x_DE = line_gen(D,E)
	x_DF = line_gen(D,F)
	
	
	#Plotting all lines
	plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
	plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
	plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
	plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
	plt.plot(x_DF[0,:],x_DF[1,:],label='$DF$')
	
	#Labeling the coordinates
	A = A.reshape(-1,1)
	B = B.reshape(-1,1)
	C = C.reshape(-1,1)
	D = D.reshape(-1,1)
	E = E.reshape(-1,1)
	F = F.reshape(-1,1)
	tri_coords = np.block([[A,B,C,D,E,F]])
	plt.scatter(tri_coords[0,:], tri_coords[1,:])
	vert_labels = ['A','B','C','D','E','F']
	for i, txt in enumerate(vert_labels):
	    plt.annotate(txt, # this is the text
	                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
	                 textcoords="offset points", # how to position the text
	                 xytext=(0,10), # distance from text to points (x,y)
	                 ha='center') # horizontal alignment can be left, right or center
	
	plt.xlabel('$x$')
	plt.ylabel('$y$')
	plt.legend(loc='best')
	plt.grid() # minor
	plt.axis('equal')
	plt.savefig('/home/lancelot/Latex/EE2102/Assignment_4/figs/question-1_2_7.png')

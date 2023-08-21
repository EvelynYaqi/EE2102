import numpy as np
import sys                                         
sys.path.insert(0, '/home/lancelot/Latex/EE2102/Assignment_4/CoordGeo')        #path to CoordGeo
sys.path.insert(0, '/home/lancelot/Latex/EE2102/Assignment_4/codes_for_figs')		#path to codes_for_figs
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
from Plot_codes import *
import subprocess
import shlex
simlen = 2
y = np.random.randint(-6,6, size=(3, simlen))
A = y[0]
B = y[1]
C = y[2]
print(y)
#question-1
d = B- A
e = C - B
f = A - C

print("The direction vector of AB is ",d)
print("The direction vector of BC is ",e)
print("The direction vector of CA is ",f)

#question-2
V1 = A - B
V2 = V1.reshape(-1,1)
print("The length of AB is:")
print(math.sqrt(V1@V2))

V3 = B - C
V4 = V3.reshape(-1,1)
print("The length of BC is:")
print(math.sqrt(V3@V4))

V5 = A - C
V6 = V5.reshape(-1,1)
print("The length of AC is:")
print(math.sqrt(V5@V6))

#question-3
Mat = np.array([[1,1,1],[A[0],B[0],C[0]],[A[1],B[1],C[1]]])

rank = np.linalg.matrix_rank(Mat)

if (rank<=2):
	print("Hence proved that points A,B,C are collinear")
else:
	print("The given points are not collinear and form a triangle")
Q1_1_3(A , B , C)

#question-4
m1=(B-A)
m2=(C-B)
m3=(A-C)
print("parametric of AB form is x:",A,"+ k",m1)
print("parametric of BC form is x:",B,"+ k",m2)
print("parametric of CA form is x:",C,"+ k",m3)

#question-5
n=norm_vec(C,B)
pro = n@B.T
print(n,"x=",pro)
n=norm_vec(B,A)
pro = n@A.T
print(n,"x=",pro)
n=norm_vec(A,C)
pro = n@C.T
print(n,"x=",pro)

#question-6
print("Area of triangle ABC:", AreaCalc(A, B, C))

#question-7
dotA = ((d*(-1)).T) @f
NormA=(np.linalg.norm(B-A))*(np.linalg.norm(C-A))
print('value of angle A: ', np.degrees(np.arccos((dotA)/NormA)))

dotB=(d*(-1)).T @e
NormB=(np.linalg.norm(A-B))*(np.linalg.norm(C-B))
print('value of angle B: ', np.degrees(np.arccos((dotB)/NormB)))

dotC=(f*(-1)).T@e
NormC=(np.linalg.norm(A-C))*(np.linalg.norm(B-C))
print('value of angle C: ', np.degrees(np.arccos((dotC)/NormC)))
############################################################################################################################################################


#question-1.2.1
D = (B + C)/2
E = (A + C)/2
F = (A + B)/2

print("Midpoint of side AB , D:", list(D))
print("Midpoint of side CA , E:", list(E))
print("Midpoint of side BC , F:", list(F))
Q1_2_1(A, B, C)

#question-1.2.2
Q1_2_2(A , B , C)

#question-1.2.3
G=line_intersect(norm_vec(F,C),C,norm_vec(E,B),B)
print("Centroid, G = ("+str(G[0])+","+str(G[1])+")")
Q_1_2_3(A , B , C)

#question-1.2.4
AG = np.linalg.norm(G - A)
GD = np.linalg.norm(D - G)

BG = np.linalg.norm(G - B)
GE = np.linalg.norm(E - G)
 
CG = np.linalg.norm(G - C)
GF = np.linalg.norm(F - G)

print("AG/GD= "+str(AG/GD))
print("BG/GE= "+str(BG/GE))
print("CG/GF= "+str(CG/GF))

#question-1.2.5
D=(B+C)/2

print(f"The mid point of B and C is {D}")

G=(A+B+C)/3

print(f"The centroid of triangleABC is {G}")

Mat = np.array([[1,1,1],[A[0],D[0],G[0]],[A[1],D[1],G[1]]])

rank = np.linalg.matrix_rank(Mat)

if (rank==2):
	print("Hence proved that points A,G,D in a triangle are collinear")
else:
	print("Error")
	
#question-1.2.7
print(f"A - F = {A-F}")
print(f"E - D = {E-D}")
Q1_2_7(A , B , C)

#question-1.3.1


# -*- coding: utf-8 -*-
import numpy as np

def scale_matrix(D_orig,D_scale,size):
    Dn = np.full((size,size),1)
    for i in range(2):
        for j in range(2): 
            print(i,j)
            temp1=(4*D_orig)+(D2[i,j]*Dn)
            print(D_orig)
            print (temp1[0:size,0:size])
            D_scale[i*size:i*size+size,j*size:j*size+size] = temp1[0:size,0:size]
            print(D_scale)

D2 = np.array([[0,2],[3,1]])
D4 = np.full((4,4),0)
D8 = np.full((8,8),0)
print(D2)
print(D4)
print(D8)

scale_matrix(D2,D4,2)
scale_matrix(D4,D8,4)

print("\n\n=======Result=======")
print("2x2 Dither matrix: \n",str(D2))
print("4x4 Dither matrix: \n",str(D4))
print("8x8 Dither matrix: \n",str(D8))
print("=======END OF PROGRAM=======")
import numpy as np
import cv2

def halftone(img,m):
    max = 255
    min = 0
    
    output = img.copy()
    size = m.shape[0]
    print("Size of Matrix = ",size)
    
    #Matrix fixing
    temp = m.copy()
    n = 2**size
    colorSpace = int(256/n)
    temp *= colorSpace
    if 256 in temp:
        for i in range(size):
            for j in range(size):
                if temp[i,j] >= 255:
                    temp[i,j] = max
    print("Fixed Matrix:\n",temp)
    
    mx = 0
    my = 0
    y,x,z = img.shape
    for i in range(y):
        for j in range(x):
            for k in range(z):
                if img[i,j,k] > temp[mx,my] :
                    output[i,j,k] = max
                else:
                    output[i,j,k] = min
            my = (my+1) % size
        mx = (mx+1) % size
    return output

dict = {}
dict["matrix2"] = np.array([[0,2],
                    [3,1]])    

dict["matrix3"] = np.array([[6,8,4],
                    [1,0,3],
                    [5,2,7]])
    
dict["matrix4"] = np.array([[ 0, 8, 2,10],
                    [12, 4,14, 6],
                    [ 3,11, 1, 9],
                    [15, 7,13, 5]])

dict["matrix4_line"] = np.array([[ 1, 2, 3, 4],
                         [ 4, 5, 6, 7],
                         [ 8, 9,10,11],
                         [12,13,14,15]])

input_fname={}
input_fname[0] = 'icon.jpg'
input_fname[1] = 'icon2.jpg'
input_fname[2] = 'icon3.jpg'


for j in range(0,3):
    print("fname = ",input_fname[j])
    for i in range(2,6):
        if (i == 5):
            name = 'matrix'+str(i-1)+'_line'
        else:
            name = 'matrix'+str(i)
        print(name+" :")
        print(dict[name])
        
        img = cv2.imread(input_fname[j])
        output = halftone(img,dict[name])
        output_fname = input_fname[j]+'_output_'+name+'.jpg'
        cv2.imwrite(output_fname, output)
        print("PROCESS FINSIH : "+input_fname[j]+"_"+name+"\n")

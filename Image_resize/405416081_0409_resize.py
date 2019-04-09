from skimage import io
import matplotlib.pyplot as plt
import numpy as np

def resize(rows,cols,times,img):
    row2 = int(rows/times)
    col2 = int(cols/times)
    img2 = np.uint8(np.zeros((row2,col2,dims)))

    for i in range(0,row2):
        for j in range(0,col2):
            for k in range(0,dims):
                sum = 0
                for l in range(0,times):
                    for m in range(0,times):
                        sum = sum + img[times*i+l,times*j+m,k]
                        
                img2[i,j,k] = np.uint8(sum/times**2)
                
    new_fname = 'resized_div_by_'+ str(times) + '_times_' + fname
    plt.imsave(new_fname,img2)
    print('Process Done:'+new_fname+' exported')

fname = '405416081_0409_origin.jpg'
img = io.imread(fname)
plt.figure(figsize = (16,16))
plt.subplot(2,1,1)
plt.imshow(img)
rows,cols,dims = img.shape

times = 4    #resize scale

resize(rows,cols,times,img)
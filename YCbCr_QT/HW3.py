from scipy.fftpack import dct,idct
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import cv2

def rgb2ycbcr(im):
    xform = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    ycbcr = im.dot(xform.T)
    ycbcr[:,:,[1,2]] += 128
    return np.uint8(ycbcr)

def ycbcr2rgb(im):
    xform = np.array([[1, 0, 1.402], [1, -0.34414, -.71414], [1, 1.772, 0]])
    rgb = im.astype(np.float)
    rgb[:,:,[1,2]] -= 128
    rgb = rgb.dot(xform.T)
    np.putmask(rgb, rgb > 255, 255)
    np.putmask(rgb, rgb < 0, 0)
    return np.uint8(rgb)

def dct2(block):
    return dct(dct(block.T, norm = 'ortho').T, norm = 'ortho')

def idct2(block):
    return idct(idct(block.T, norm = 'ortho').T, norm = 'ortho')

def quanStep(block,quanTable):
    dct_block = dct2(block.T.T)
    qdct_block = np.zeros((8,8))
    for i in range(0,8):
        for j in range(0,8):
            qdct_block[i,j] = np.round(float(dct_block[i,j]/quanTable[i,j]))*quanTable[i,j]
    rect_qdct_block = np.uint8(idct2(qdct_block.T.T))
    return rect_qdct_block

def Dis_Res(block):
    rows,cols = block.shape
    for i in range(0,rows):
        for j in range(0,cols):
            print(block[i,j])
        print()
        
def imageDCT_to_D(image,quanTable):
        rows,cols = image.shape
        dct_image = np.zeros((rows,cols))
        rows_times = np.uint8(rows/8)
        cols_times = np.uint8(cols/8)
        
        for i in range(0,rows_times):
            for j in range(0,cols_times):
                block = image[8*i+0:8*i+8,8*j+0:8*j+8]
                qblock = quanStep(block,quanTable)
                dct_image[8*i+0:8*i+8,8*j+0:8*j+8] = qblock
        
        return dct_image
    
def PSNR_calc(image,qimage):
    print(image.shape)
    rows,cols,dims = image.shape
    dif=0.0
    for i in range(0,rows):
        for j in range(0,cols):
            dif = dif + (image[i,j] - qimage[i,j]) * (image[i,j] - qimage[i,j])
    MSE = dif / (rows*cols)
    PSNR = 10*np.log10(255*255/MSE)
    return PSNR

def QF(QT,qu):
    QT2 = np.zeros((8,8))
    
    if (qu <= 0):
        qu = 1
    if (qu > 100):
        qu = 100
        
    if (qu <50):
        qu = 5000/qu
    else:
        qu = 200-qu*2
        
    for i in range(0,8):
        for j in range(0,8):
            QT2[i][j] = QT[i][j]* qu/100
            
    return QT2

img = io.imread('image.jpg')
plt.figure(num=2,figsize=(6,6))
quality = 5

quanTable = np.array([
  [16, 11, 10, 16, 24, 40, 51, 61],
  [12, 12, 14, 19, 26, 58, 60, 55], 
  [14, 13, 16, 24, 40, 57, 69, 56],
  [14, 17, 22, 29, 51, 87, 80, 62],
  [18, 22, 37, 56, 68, 109, 103, 77],
  [24, 35, 55, 64, 81, 104, 113, 92],
  [49, 64, 78, 87, 103, 121, 120, 101],
  [72, 92, 95, 98, 112, 100, 103, 99]])
    
quanTable2 = np.int64(QF(quanTable,quality))

plt.subplot(1,2,1)
plt.title('Original iamge')
plt.imshow(img,cmap='gray')

imgYcc = rgb2ycbcr(img)
imgTemp= np.uint32(imageDCT_to_D(imgYcc[:,:,0],quanTable2))
imgYcc[:,:,0] = imgTemp
img2 = ycbcr2rgb(imgYcc)

plt.subplot(1,2,2)
plt.title('DCT Quantized Result')
plt.imshow(img2,cmap='gray')

io.imsave('output.jpg',img2)

print('PSNR1',PSNR_calc(img,img2),'dB')
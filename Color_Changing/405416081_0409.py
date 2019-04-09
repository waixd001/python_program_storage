from skimage import io,data
import matplotlib.pyplot as plt
import numpy as np

img = data.chelsea()
rows,cols,dims = img.shape
plt.figure(num='chelsea',figsize=(16,16))
plt.subplot(2,2,1)
plt.title('Origin image')
plt.imshow(img)


# 減色(紅)
mod_img = img.copy()
plt.subplot(2,2,2)
plt.title('Modified image')
for i in range(0,rows):
    for j in range(0,cols):
        mod_img[i,j,0] = 0
plt.imshow(mod_img)
io.imsave('405416081_0409_practice1.jpg',mod_img)


# 負片
mod_img = img.copy()
plt.subplot(2,2,3)
plt.title('Origin image')
plt.imshow(img)

plt.subplot(2,2,4)
plt.title('Modified image')
for i in range(0,rows):
    for j in range(0,cols):
        for k in range(0,dims):
            mod_img[i,j,k] = 255-img[i,j,k]
plt.imshow(mod_img)
io.imsave('405416081_0409_practice2.jpg',mod_img)
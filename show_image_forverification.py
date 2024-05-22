import matplotlib.pyplot as plt
import numpy as np

img = np.load('00new_img.npy')
plt.imshow(img[0, :, :, 0], cmap='gray')
plt.show()
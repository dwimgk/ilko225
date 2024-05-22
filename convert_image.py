from PIL import Image, ImageGrab, ImageOps, ImageEnhance
import numpy as np

img = Image.open("00turtle.png")

img = img.convert('L')
img = img.resize((28, 28), Image.Resampling.LANCZOS)
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(2.0)
img = ImageOps.invert(img)
img = np.array(img)
img = img / 255.0
img = img.reshape(1, 28, 28, 1)

np.save("00new_img", img)
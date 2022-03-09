import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../data/img/image.png')

plt.imshow(img)
plt.show()

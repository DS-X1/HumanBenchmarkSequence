# Program for partial screenshot
import time
import pyscreenshot
import numpy as np

# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
image = pyscreenshot.grab(bbox=(10, 10, 500, 500))

# To view the screenshot
image.show()

# To save the screenshot
image.save("word.png")

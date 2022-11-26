# Program for partial screenshot
import time
import pyscreenshot
import numpy as np
from PIL import Image

for i in range(3)
	# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
	screenshot = pyscreenshot.grab(bbox=(10, 10, 500, 500))

	# To view the screenshot
	screenshot.show()

	# To save the screenshot
	screenshot.save(f"word{i}.png")

	im = Image.open(sample_path.bmp)
	p = np.array(im
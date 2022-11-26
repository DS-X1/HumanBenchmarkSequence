# Program for partial screenshot
import time
import pyscreenshot
import numpy as np
from PIL import Image
image_list = []

for i in range(3):
	time.sleep(4)
	# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
	screenshot = pyscreenshot.grab(bbox=(340, 371, 1040, 451))

	# To view the screenshot
	#screenshot.show()

	# To save the screenshot
	screenshot.save(f"word{i}.png")

	im = Image.open(f"word{i}.png")
	p = str(np.array(im))

	if p in image_list:
		print("seen image")
		pass
	elif p not in image_list:
		image_list.append(p)
		print("new image")

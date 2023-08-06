#!!! needs more testing !!!
from PIL import Image
import matplotlib.pyplot as plt

Height=300
Width=300

loc= Image.open(r'images/rainbow1.png')
loc=loc.convert('RGB')
loc=loc.resize((Height,Width))

pixel_RGB=loc.getdata()

#separating r, g and b

red=[pixel[0]for pixel in pixel_RGB]
green=[pixel[1]for pixel in pixel_RGB]
blue=[pixel[2]for pixel in pixel_RGB]
plt.figure(figsize=(20, 10))
plt.plot(red, color='red', label='Red')
plt.plot(green, color='green', label='Green')
plt.plot(blue, color='blue', label='Blue')
plt.xlabel('Pixel')
plt.ylabel('Intensity')
plt.title('Color Spectrum')
plt.legend()
plt.show()


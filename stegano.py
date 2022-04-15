#Import the required library
from PIL import Image
import stepic

 #Open Image or file in which you want to hide your data
im = Image.open('catoon.png')
 #Encode some text into your Image file and save it in another file
im1 = stepic.encode(im, b'Hello Python')
im1.save('catoon.png', 'PNG')

 #Now is the time to check both images and see if there is any visible changes
im1 = Image.open('catoon.png')
im1.show()

#Decode the image so as to extract the hidden data from the image
im2 = Image.open('catoon.png')
stegoImage = stepic.decode(im2)
stegoImage
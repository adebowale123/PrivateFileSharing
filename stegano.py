#Import the required library
from PIL import Image
import stepic

 #Open Image or file in which you want to hide your data
img = Image.open('catoon.png')
 #Encode some text into your Image file and save it in another file
img1 = stepic.encode(img, b'Hello Python')
img1.save('catoon.png', 'PNG')

 #Now is the time to check both images and see if there is any visible changes
img1 = Image.open('catoon.png')
img1.show()

#Decode the image so as to extract the hidden data from the image
img2 = Image.open('catoon.png')
stegoImage = stepic.decode(img2)
stegoImage
from PIL import Image,ImageEnhance,ImageFilter
import os

# change extension of image

#img1=Image.open("image1.jpg")  # class Image 
#img1.save('image1.png')   # this will save image with png extension
#img1.save('image1.pdf')
#img1.show()  

# changing size of image= 250 pixels

#MAX_SIZE=(250,250)
#img1.thumbnail(MAX_SIZE)  # here img2 is object and thumbnail is method
#img1.save('image1small.jpg')
#img1.show()

"""for item in os.listdir():   # same to resize
    if item.endswith('.jpg'):
        img1=Image.open(item)
        filename,extension=os.path.splitext(item) # filename and extension name both stored separately
        img1.save(f'{filename}.png')   """

# to change sharpness, brigtness, and contrast

img1=Image.open('image2.jpg')
#enhancer=ImageEnhance.Sharpness(img1)
#enhancer=ImageEnhance.Color(img1)
#enhancer=ImageEnhance.Brightness(img1)
#enhancer=ImageEnhance.Contrast(img1)
#enhancer.enhance(5).save('image3edited.jpg') # inside bracket we have to fill factor by which we have to change sharpness
#0 = blury, black white
# 1= original
# 2 ,3 = sharpness increases
img1.filter(ImageFilter.GaussianBlur(radius=4)).save('image22edited.jpg')  # by defaulr radius is 2



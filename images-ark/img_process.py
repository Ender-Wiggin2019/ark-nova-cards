from PIL import Image
import PIL
import os
import glob
print(f"The current working directory: {os.getcwd()} ")
# The current working directory: /Users/jamesaphoenix/Desktop/Imran_And_James/Python_For_SEO/7_image_compression 
images = [file for file in os.listdir() if file.endswith(('jpg', 'png' ))]
print(f" Example images: {images}")
# Example images: ['example-image.jpg', 'example-image-3.jpg', 'example-image-2.jpg']
# How to get the image name:
for image in images:
    print(image.split('.')[0])
for image in images:
    # 1. Open the image
    img = Image.open(image)
    if img.mode == 'CMYK':
        img = img.convert('RGB')
    # print(img.size)


    zoom = 3
    img = img.resize((int(img.size[0]/zoom),int(img.size[1]/zoom)),Image.ANTIALIAS)
    # 2. Compressing the image
    img.save("./compress/"+image,
             optimize=True,
             quality=85)
    
    
    # zoom = 2
    # img = img.resize((int(img.size[0]/zoom),int(img.size[1]/zoom)),Image.ANTIALIAS)
    # # 2. Compressing the image
    # img.save("./low-resolution/"+image,
    #         #  optimize=True,
    #          quality=80)
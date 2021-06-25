from PIL import Image, ImageFilter

img = Image.open('./Lawplug.jpeg')

filter_img = img.filter(ImageFilter.SHARPEN)
filter_img.save("sharpen.png", 'png')
# filter_img.rotate(90)

resize = img.resize((100, 100))
resize.save("sharpen.png", 'png')


# img = Image.open('./.jpg')
# img.thumbnail((400, 400))
# img.save('thumbnail.jpg')

print(filter_img())

# if __name__ == '__main__':
#     print(img.mode)
#     print(img.size)  

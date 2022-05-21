# from IPython.display import HTML
from PIL import Image  # , ImageFilter

img = Image.open('./images/yellowstoneRiver.jpg')
# flt_img = img.filter(ImageFilter.SHARPEN)
# smImg.save('./images/pikachuSm.png', 'png')
# img.show()

img.size
img.thumbnail([800, 800])
img.size
img

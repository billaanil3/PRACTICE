import random
import string
from PIL import Image, ImageDraw, ImageFont

# print random.random()
captcha_string =  random.choice(string.letters) + random.choice(string.digits) + \
                  random.choice(string.letters) + random.choice(string.letters) + \
                  random.choice(string.digits)
# print captcha_string

fh = open("imageToSave.png", "wb")
fh.write(captcha_string)
fh.close()

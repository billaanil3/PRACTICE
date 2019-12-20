import random
import string
# from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageDraw
from PIL import Image
import pytesseract

# print random.random()
captcha_string =  random.choice(string.letters) + random.choice(string.digits) + \
                  random.choice(string.letters) + random.choice(string.letters) + \
                  random.choice(string.digits)
print captcha_string

img = Image.new('P', (100, 30), color = (73, 109, 137))
d = ImageDraw.Draw(img)
d.text((10,10),captcha_string , fill=(255,255,0))
img.save('pil_text.png')

# im = Image.open("/home/anil/Desktop/13062-Your-Life-Is-A-Message.jpg")
# im = Image.open("/home/anil/PRACTICE/Practices/PYTHON/Programs/CAPTCHA/coin_switch.png")
im = Image.open("pil_text.png")
print im
print type(im)
text = pytesseract.image_to_string(im, lang = 'eng')
print text

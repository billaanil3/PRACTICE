from PIL import Image
import pytesseract

# im = Image.open("/home/anil/Desktop/13062-Your-Life-Is-A-Message.jpg")
im = Image.open("/home/anil/PRACTICE/Practices/PYTHON/Programs/CAPTCHA/pil_text.jpg")
text = pytesseract.image_to_string(im, lang = 'eng')
print text


# from PIL import Image, ImageDraw

# # img = Image.new('RGB', (100, 30), color = (73, 109, 137))

# d = ImageDraw.Draw(img)
# d.text((10,10), "Hello World", fill=(255,255,0))

# img.save('pil_text.png')


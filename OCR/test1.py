from PIL import Image
import pytesseract

# im = Image.open("/home/anil/Desktop/13062-Your-Life-Is-A-Message.jpg") 
im = Image.open("/home/anil/Desktop/Desk_Files/WhatsApp Image 2018-12-05 at 2.51.43 PM.jpeg")
text = pytesseract.image_to_string(im,lang = 'eng')
print text

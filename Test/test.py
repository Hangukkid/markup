try:
    import Image
except:
    from PIL import Image

import pytesseract

print(pytesseract.image_to_string(Image.open('Test0.JPG')))

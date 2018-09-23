from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.views.decorators.csrf import csrf_exempt
import os, sys
from .gcloud import detect_handwritten_ocr
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
# Create your views here.
try:
    import Image
except:
    from PIL import Image

import pytesseract

@csrf_exempt
def index (request):
    if request.method == "GET":
        scrape_page()
        return HttpResponse("fucku")
    elif request.method == "POST":
        print (request.body)
        return HttpResponse(request.body)

def scrape_page ():
    test_root = os.path.join(FILE_PATH, '..', '..', 'Test')
    image_root = os.path.join(test_root, 'Answers')
    for image in os.listdir(image_root):
        image_path = os.path.join(image_root, image)
        text = scrape_text(image_path).strip(' ')
        if (text != ''):
            print (text)
        else:
            print('Google cloud has failed me.')
            print (pytesseract.image_to_string(Image.open(image_path)))

def compare_answers (quiz_name, answer_key):
    pass

def scrape_text (image_path):
    return detect_handwritten_ocr(image_path)
        # print image
    
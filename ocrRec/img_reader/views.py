from django.shortcuts import render,HttpResponse,redirect
import numpy
import json
import cv2 
import pytesseract
from pytesseract import pytesseract ,Output
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  Images,ImageForm,image_text
from PIL import Image
from .seriazable import ImageSerializer

class ImageList(APIView):

    def get(self,request):
        image=image_text.objects.all()
        serilizar=ImageSerializer(image,many=True)
        return Response(serilizar.data)

    def post(self):
        pass


def home(request):

    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
        
        if form.is_valid(): 
            id=form.save() 
            img=form.cleaned_data['img']
            image = 'media/profile_image/'+str(img)
            im = Image.open(image)
            d = pytesseract.image_to_data(im, output_type=Output.DICT)
            image_text.objects.create(img=Images(id.id),text=d)
            return HttpResponse("okk")
    else: 
        form = ImageForm() 
    return render(request, 'index.html', {'form' : form})

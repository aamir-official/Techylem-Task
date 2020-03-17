from django.db import models
from django import forms

 
    
class Images(models.Model):

    img=models.ImageField(upload_to='profile_image',blank=True)
    def __str__(self):
        return str(self.id)

class image_text(models.Model):
    img=models.OneToOneField(to=Images,on_delete=models.CASCADE)
    text=models.TextField()


class ImageForm(forms.ModelForm): 
  
    class Meta: 
        model = Images 
        fields = ['id', 'img'] 
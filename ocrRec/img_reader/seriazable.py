from rest_framework import serializers
from .models import image_text

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model=image_text
        fields=['id','text',]

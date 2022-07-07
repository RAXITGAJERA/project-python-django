import imp
from rest_framework import serializers
from .models import pages

class pagesserializers(serializers.ModelSerializer):
    class Meta:
        model = pages
        fields = ['page_title','page_content','Page_status']
from django.db import models
from  embed_video.fields  import  EmbedVideoField
from tinymce import models as tinymce_models


STATUS_CHOICES = [
    ('published', 'Published'),
    ('active', 'Active'),
]
# Create your models here.
class newProduct(models.Model):
    product_name = models.CharField(max_length=50)
    product_disc = models.CharField(max_length=500)
    youtube_link = EmbedVideoField()
    Product_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    def __str__(self):
        return self.product_name

class pages(models.Model):
    page_title = models.CharField(max_length=50)
    page_content = tinymce_models.HTMLField()
    Page_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    def __str__(self):
        return self.page_title

class contectusemail(models.Model):
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import datetime
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

CHOICES2 = (
    ('completed', 'completed'),
    ('draft', 'draft'),
)
PROJE  = (
    ('WEB SITE', 'WEB SITE'),
    ('DIJITAL TASARIM', 'DIJITAL TASARIM'),
)
MONTH = (
    ('OCAK','OCAK'),
    ('ŞUBAT','ŞUBAT'),
    ('MART', 'MART'),
    ('NİSAN', 'NİSAN'),
    ('MAYIS', 'MAYIS'),
    ('HAZİRAN', 'HAZİRAN'),
    ('TEMMUZ', 'TEMMUZ'),
    ('AĞUSTOS', 'AĞUSTOS'),
    ('EYLÜL', 'EYLÜL'),
    ('EKİM', 'EKİM'),
    ('KASIM', 'KASIM'),
    ('ARALIK', 'ARALIK'),
)

class Usermessage(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Ad Soyad',null= True, blank=False)
    content = models.TextField(max_length=500, verbose_name='Yorum',null= True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True,null= True)
    mail=models.EmailField(max_length=100, null= True, blank=False)
    score = models.IntegerField(editable=False, null= True, blank=False,verbose_name='score') 
    telefon = models.CharField(max_length=12, verbose_name='telefon',null= True, blank=False)
    publishing_date =models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True, null= True )
    

    def __str__(self):
        return self.name

    class Meta:
        ordering  = ['-publishing_date', 'id']


class CustomerComments(models.Model):
    customer_name = models.CharField(max_length=300, verbose_name='Customer Name',null= True, blank=False)
    content = models.TextField(max_length=500, verbose_name='Customer comment',null= True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True,null= True)
    customer_image = models.ImageField(null=True, upload_to='image/')
    customer_profession=models.CharField(null= True, max_length=200, blank=False)
    website_name=models.CharField(null= True, max_length=200, blank=False)
    website_url=models.CharField(null= True, max_length=500, blank=False)

    def __str__(self):
        return self.customer_name
    
class Category(models.Model):
    name=models.CharField(null= True,blank=False, max_length=200)
    slug = models.SlugField(max_length=200, default="", null= True, blank=False)

    def __str__(self):
        return self.name
    
class Post (models.Model):
    title=models.CharField(null= True, max_length=200)
    summary=models.CharField(null= True, max_length=500, blank=False)
    image = models.ImageField(null=True, upload_to='image/')
    publishing_date =models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True, null= True )
    month = models.CharField(choices=MONTH,default='NONE',max_length=200)
    read = models.IntegerField(default = 0)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='category',null= True, blank=False)
    completed=models.CharField(choices=CHOICES2,default='completed',max_length=200)
    slug = models.SlugField(max_length=300, default="", null= True, blank=False)
    read_time=models.CharField(null= True, max_length=10, blank=False,default="5 dk")
    author=models.ForeignKey(
        'auth.User', on_delete=models.CASCADE,
    )
    body=RichTextField(null= True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug":self.slug})

    class Meta:
        ordering  = ['-publishing_date', 'id']

class Website(models.Model):
    url=models.CharField(null= True,blank=False, max_length=200)
    image = models.ImageField(null=True, upload_to='image/')
    category=models.CharField(null= True, max_length=30, default = "web")
    publishing_date =models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True, null= True )
    def __str__(self):
        return self.url
    
    
class Job(models.Model):

    image = models.ImageField(null=True, upload_to='image/')
    job_name=models.CharField(null= True, max_length=250, blank=False)
    description=RichTextField(null= True)
    def __str__(self):
        return self.job_name
    

class About(models.Model):

    left_title = models.CharField(null= True, max_length=250, blank=False)
    left_detail=RichTextField(null= True, blank=False)
    def __str__(self):
        return self.left_title
    
    
class Detail_Image(models.Model):

    image = models.ImageField(null=True, upload_to='image/')
    def __str__(self):
        return self.image.url
    
    
    
class Duyuru(models.Model):
    name = models.CharField(null= True, max_length=50)
    image = models.ImageField(null=True, upload_to='image/')
    body = models.CharField(null= True, max_length=2000)
    publishing_date =models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True, null= True )
    pure_date = models.CharField( editable=False, max_length=200, default = str(datetime.now().day)+ '.' +str(datetime.now().month) + '.' + str(datetime.now().year))
    def __str__(self):
        return self.name
    
    
class Instagram(models.Model):
    name = models.CharField(null= True, max_length=50)
    url = models.CharField(null= True, max_length=200)
    image = models.ImageField(null=True, upload_to='image/')
    body = models.CharField(null= True, max_length=2000)
    publishing_date =models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True, null= True )
    date = models.CharField(null= True, max_length=10)
    date_num = models.IntegerField(null= True, verbose_name = "YYYYAAGG")
    def __str__(self):
        return self.name
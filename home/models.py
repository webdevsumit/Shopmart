from django.db import models

# Create your models here.

class profile(models.Model):
    Username = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='uploadedprofileimage',null=True)
    Address = models.TextField(null=True)
    Phoneno = models.IntegerField(null=True)

class catagory(models.Model):
    Catagory = models.CharField(max_length=70)
    onHomeScreen = onHomeScreen = models.BooleanField(default=True)

class product(models.Model):
    Image = models.ImageField(upload_to='uploadedimages')
    Image1 = models.ImageField(upload_to='uploadedimages',null=True,blank=True)
    Image2 = models.ImageField(upload_to='uploadedimages',null=True,blank=True)
    Image3 = models.ImageField(upload_to='uploadedimages',null=True,blank=True)
    Image4 = models.ImageField(upload_to='uploadedimages',null=True,blank=True)
    Image5 = models.ImageField(upload_to='uploadedimages',null=True,blank=True)
    Name = models.CharField(max_length=1000)
    Description = models.TextField()
    Price = models.FloatField()
    OfferPrice = models.FloatField(null=True)
    Catagory = models.OneToOneField(catagory, on_delete=models.SET_NULL,null=True)
    Offer = models.BooleanField()
    SpecialOffer = models.BooleanField()
    onHomeScreen = models.BooleanField()
    Rating = models.FloatField()
    Title1 = models.CharField(max_length=1000,null=True,blank=True)
    Description1 = models.TextField(null=True,blank=True)
    Title2 = models.CharField(max_length=1000,null=True,blank=True)
    Description2 = models.TextField(null=True,blank=True)
    Title3 = models.CharField(max_length=1000,null=True,blank=True)
    Description3 = models.TextField(null=True,blank=True)
    Title4 = models.CharField(max_length=1000,null=True,blank=True)
    Description4 = models.TextField(null=True,blank=True)
    Title5 = models.CharField(max_length=1000,null=True,blank=True)
    Description5 = models.TextField(null=True,blank=True)
    Title6 = models.CharField(max_length=1000,null=True,blank=True)
    Description6 = models.TextField(null=True,blank=True)
    Title7 = models.CharField(max_length=1000,null=True,blank=True)
    Description7 = models.TextField(null=True,blank=True)
    Title8 = models.CharField(max_length=1000,null=True,blank=True)
    Description8 = models.TextField(null=True,blank=True)
    Title9 = models.CharField(max_length=1000,null=True,blank=True)
    Description9 = models.TextField(null=True,blank=True)
    Title10 = models.CharField(max_length=1000,null=True,blank=True)
    Description10 = models.TextField(null=True,blank=True)

class ratings(models.Model):
    Username = models.CharField(max_length=100)
    Product = models.OneToOneField(product, on_delete=models.SET_NULL,null=True)
    Rating = models.FloatField(null=True)

class videos(models.Model):
    Video = models.FileField(upload_to='uploadedvideo')
    Trending = models.BooleanField()

class searched(models.Model):
    Username = models.CharField(max_length=100)
    SearchedName = models.CharField(max_length=100)
    SearchDate = models.DateTimeField(auto_now=True)

class cartitem(models.Model):
    Username = models.CharField(max_length=100)
    Product = models.CharField(max_length=100)
    Quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now=True)
    Ordered = models.BooleanField(default=False)
    Price = models.FloatField(null=True)

class carts(models.Model):
    Username = models.CharField(max_length=100)
    Address = models.TextField()
    Phoneno = models.IntegerField()
    PaymentMethod = models.CharField(max_length=50)
    Items = models.ManyToManyField(cartitem)

class favorite(models.Model):
    Username = models.CharField(max_length=100)
    FavItems = models.ManyToManyField(product)
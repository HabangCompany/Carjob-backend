from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#일반 회원
class User(AbstractUser):
    nickname = models.CharField(max_length =10,unique = True, null = True)
    address = models.CharField(max_length = 50)
    phonenumber = models.CharField(max_length = 20, null=True)
    is_store = models.BooleanField(default=False)
    class Meta:
        db_table = "User"
    def __str__(self):
        return self.username

#업체회원
class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    storeName = models.CharField(max_length =20, blank =False )
    storeTel = models.CharField(max_length =20, blank =False )
    storeDescription = models.CharField(max_length =20, blank =False)
    storeImage = models.ImageField(upload_to='store_images/')
    storeAddress = models.CharField(max_length =20, blank =False )
    storeSkill = models.CharField(max_length =20, blank =False )


    class Meta:
        db_table ="Store"
    
    def __str__(self):
        return self.storeName

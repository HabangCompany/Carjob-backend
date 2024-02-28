from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#일반 회원
class User(AbstractUser):
    nickname = models.CharField(max_length =10,unique = True, null = True)
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
    address = models.CharField(max_length=30, blank=False)
    zonecode = models.CharField(max_length=6 ,blank=False)
    detailAddress = models.CharField(max_length=30, blank=False)
    storeThumbnail = models.ImageField()

    class Meta:
        db_table ="Store"

    def __str__(self):
        return self.storeName

#업체 이미지
class StoreImage(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE , related_name='image')
    storeimage = models.ImageField()

    class Meta:
        db_table = "StoreImage"

#업체 시공기술들
class StoreSkill(models.Model):
    store = models.OneToOneField(Store, on_delete = models.CASCADE,related_name='skill' ,null=True)
    tinting = models.BooleanField(default = False)
    wraping = models.BooleanField(default = False)
    ppf = models.BooleanField(default = False)
    carwash = models.BooleanField(default = False)
    gloss = models.BooleanField(default = False)
    detail_carwash = models.BooleanField(default = False)
    car_repair = models.BooleanField(default = False)
    painting = models.BooleanField(default = False)
    autoglass = models.BooleanField(default = False)
    tire = models.BooleanField(default = False)

    class Meta:
        db_table ='StoreSkill'


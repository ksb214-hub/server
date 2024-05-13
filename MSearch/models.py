from django.db import models
import json
from django.utils.translation import gettext as _

# 크롤링한 데이터 
class CrawledData(models.Model):
    title = models.CharField(max_length = 100)
    url = models.URLField()
    img = models.URLField()

    def __str__(self):
        return self.title
    
# 검색 데이터 저장 및 호출하는 모델 
class MySearchData(models.Model):
    searchData = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.searchData    
# 푸드 뱅크 모델  
class MyFoodBankModel(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    location = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)    
    division = models.CharField(max_length = 100)
    support = models.CharField(max_length = 100)
    organization = models.CharField(max_length = 100)    
    coporation = models.CharField(max_length = 100)
    ceo = models.CharField(max_length = 100)
    number = models.CharField(max_length = 100)    
    address = models.CharField(max_length = 100)

    def __str__(self):
        return self.location
# 아동 급식카드 모델 
class FoodCard(models.Model):
   id = models.AutoField(_("id"), primary_key=True)
   name = models.CharField(_("name"), max_length=100)
   location = models.CharField(_("location"), max_length=100)
   address = models.CharField(_("address"), max_length=100)
   x = models.CharField(_("x"), max_length=100)
   y = models.CharField(_("y"), max_length=100)
   number = models.CharField(_("number"), max_length=100)
   
   def __str__(self):
       return self.name
# 레시피 모댈  
class FoodRecipy(models.Model):
    id = models.AutoField(primary_key=True)
    clss = models.CharField(max_length = 1000)
    ingt = models.CharField(max_length = 1000)
    foodnm = models.CharField(max_length = 1000)
    foodscrt = models.CharField(max_length= 1000)
    foodmntr = models.CharField(max_length= 1000)
    cookmth = models.CharField(max_length= 1000)
    cookdsrt = models.CharField(max_length= 1000)
    url = models.CharField(max_length= 1000)
    
    def __str__(self):
        return self.clss
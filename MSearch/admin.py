from django.contrib import admin
from .models import *

class MYSearchAdmin(admin.ModelAdmin):
    list_display = ('searchData', 'time')

class MyFoodBankModelAdmin(admin.ModelAdmin):
    list_display = ('location', 'city', 'division', 'support', 'organization', 'coporation', 'ceo', 'number', 'address')
class FoodCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'address', 'x', 'y', 'number')
class FoodRecipyAdmin(admin.ModelAdmin):
    list_display = ('clss', 'ingt', 'foodnm', 'foodscrt', 'foodmntr', 'cookmth', 'cookdsrt', 'url')
class CrawledDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')    
admin.site.register(MySearchData, MYSearchAdmin)
admin.site.register(MyFoodBankModel, MyFoodBankModelAdmin)
admin.site.register(FoodCard, FoodCardAdmin)
admin.site.register(FoodRecipy, FoodRecipyAdmin)
admin.site.register(CrawledData, CrawledDataAdmin)
"""
URL configuration for Maps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MSearch import views
from YoutubeApp import views as Yv
from Naver import views as Nv

urlpatterns = [
    path('admin/', admin.site.urls),
    # android 버전
    path('save_data_android/', views.Data, name ='save_search_data'),
    path('get_data_android/', views.Data, name = 'get_search_data'),
    # ios 버전
    path('save_data_ios/', views.Data, name ='save_search_data'),
    path('get_data_ios/', views.Data, name = 'get_search_data'),

    path('foodBankGet/', views.FoodBanK.foodBankDataGet, name = 'foodBankGet'),
    path('foodcard/', views.FoodBanK.foodCardDataGet, name= 'foodCardGet'),

    # 네이버 로그인 api
    path('naverlogin/', Nv.NaverLoginAPIView.as_view()),
    path('navercallback/', Nv.NaverCallbackAPIView.as_view(), name='naver_callback'),
    
    # 네이버 검색 api
    path('naversearch/', Nv.naver_blog_search, name = 'naversearch'),

    path('save_crawling/', views.Crawled.save_crawled_data, name = 'save_crawling'),
    path('get_crawling/', views.Crawled.get_crawled_data, name = 'get_crawling')
]

from django.shortcuts import render
from datetime import datetime
from .models import MySearchData, MyFoodBankModel, FoodCard, CrawledData
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
from django.http import JsonResponse, HttpResponse
import json

from .crawling import crawling


# 푸드 뱅크 view class로 정의함
class FoodBanK():
    @csrf_exempt
    def foodBankDataGet(request):
        if request.method == 'GET':
            data = MyFoodBankModel.objects.all()
            data_list = [
                            {
                                'id': item.id, 
                                'location' : item.location, 
                                'city' : item.city, 
                                'division': item.division,
                                'support': item.support, 
                                'organization': item.organization, 
                                'coporation': item.coporation,
                                'ceo' : item.ceo, 
                                'number': item.number, 
                                'address': item.address
                            } 
                        for item in data
                        ]
            return JsonResponse(data_list, safe = False)
        else:
            return JsonResponse({'error': 'message 요청이 아닙니다.'}, status = 400)
    
    @csrf_exempt
    def foodCardDataGet(request):

        if request.method == 'GET':
            data = FoodCard.objects.all()
            data_list = [
                            {
                                'id': item.id, 
                                'name': item.name,
                                'location' : item.location, 
                                'address' : item.address, 
                                'x': item.x,
                                'y': item.y, 
                                'number': item.number
                            } 
                        for item in data
                        ]
            return JsonResponse(data_list, safe = False)
        else:
            return JsonResponse({'error': 'message 요청이 아닙니다.'}, status = 400)    


@csrf_exempt
def Data(request):
    if request.method == 'POST' and request.method != 'GET':
        data = json.loads(request.body)        
        search_data = data.get('search_data')
        if search_data:
            MySearchData.objects.create(searchData = search_data)
            return JsonResponse({"message":"검색 데이터가 성공적으로 저장되었습니다."}, status = 200)
        else:
            return JsonResponse({"error":"검색 데이터가 아닙니다."}, status = 400)
    elif request.method != 'POST' and request.method != 'GET':
        return JsonResponse({'error': 'POST 요청이 아닙니다.'}, status = 405)   
    
    elif request.method == 'GET' and request.method != 'POST':
        saved_data = MySearchData.objects.all()
        data_list = [{'id': item.id, 'search_data': item.searchData, 'time': timezone.localtime(timezone.make_aware(item.time)).strftime("%Y-%m-%d %H:%M:%S")} for item in saved_data]
        # json 형식으로 반환
        return JsonResponse(data_list, safe=False)
    elif request.method != 'GET' and request.method != 'POST':
        return JsonResponse({'error': 'GET 요청이 아닙니다.'}, status=400)

# 크롤링 view class로 정의함
class Crawled():
    @csrf_exempt
    def save_crawled_data(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            search = data.get('data')
            data_to_delete = CrawledData.objects.all()
            # 조회된 데이터를 삭제합니다.
            data_to_delete.delete()
            
            titles, urls, imgs = crawling(search)
            for title, url, img in zip(titles, urls, imgs):
                
                crawled_data = CrawledData.objects.create(
                    title=title,
                    url=url,
                    img = img
                )
                crawled_data.save()
        
            return HttpResponse('크롤링 작업이 잘 실행됩니다.')
        else:
            return HttpResponse(status = 405)    

    @csrf_exempt
    def get_crawled_data(request):
        data = CrawledData.objects.all()
        datas = list(data.values())

        return JsonResponse(datas, safe=False)
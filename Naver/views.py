from django.shortcuts import render
from django.conf import settings
import requests
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.permissions import *

# main domain(http://127.0.0.1:8000)
main_domain = settings.MAIN_DOMAIN

# DRF의 APIView를 상속받아 View를 구성
class NaverLoginAPIView(APIView):
    # 로그인을 위한 창은 누구든 접속이 가능해야 하기 때문에 permission을 AllowAny로 설정
    permission_classes = (AllowAny,)
    
    def get(self, request, *args, **kwargs):
        client_id = settings.NAVER_CLIENT_ID
        response_type = "code"
        # Naver에서 설정했던 callback url을 입력해주어야 한다.
        # 아래의 전체 값은 http://127.0.0.1:8000/user/naver/callback 이 된다.
        uri = main_domain + "navercallback/"
        state = settings.STATE
        # Naver Document 에서 확인했던 요청 url
        url = "https://nid.naver.com/oauth2.0/authorize"
        
        # Document에 나와있는 요소들을 담아서 요청한다.
        return redirect(
            f'{url}?response_type={response_type}&client_id={client_id}&redirect_uri={uri}&state={state}'
        )


class NaverCallbackAPIView(APIView):
    def get(self, request):
        # 네이버 OAuth 콜백에서 받은 인증 코드
        code = request.query_params.get('code')

        # 네이버 OAuth 액세스 토큰 요청 URL
        token_url = "https://nid.naver.com/oauth2.0/token"
        
        # 클라이언트 ID, 시크릿 키, 콜백 URL 설정
        client_id = settings.NAVER_CLIENT_ID
        client_secret = settings.NAVER_CLIENT_SECRET
        uri = settings.MAIN_DOMAIN

        # 엑세스 토큰 요청을 위한 파라미터 설정
        params = {
            'grant_type': 'authorization_code',
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': uri,
            'code': code,
        }

        # 엑세스 토큰 요청 보내기
        response = requests.post(token_url, params=params)

        if response.status_code == 200:
            # 엑세스 토큰이 성공적으로 발급된 경우
            token_data = response.json()
            access_token = token_data['access_token']

            # 사용자 정보 URL
            user_info_url = "https://openapi.naver.com/v1/nid/me"

            # 네이버 API에 사용자 정보 보내기
            headers = {'Authorization': f'Bearer {access_token}'}
            user_info_response = requests.get(user_info_url, headers=headers)

            if user_info_response.status_code == 200:
                # 사용자 정보를 성공적으로 받은 경우
                user_info = user_info_response.json()
                # 여기서 사용자 정보를 처리하고 필요한 작업을 수행합니다.
                return JsonResponse(user_info)
            else:
                # 사용자 정보 요청이 실패한 경우
                return JsonResponse({'error': 'Failed to get user info'}, status=400)
        else:
            # 엑세스 토큰 요청이 실패한 경우
            return JsonResponse({'error': 'Failed to obtain access token'}, status=400)

def naver_blog_search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            client_id = 'TwyTMclXeQfxfiOnm25x'
            client_secret = 'Rtdu4sfp0n'
            url = f'https://openapi.naver.com/v1/search/blog?query={query}'
            headers = {
                'X-Naver-Client-Id': client_id,
                'X-Naver-Client-Secret': client_secret,
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return JsonResponse(response.json(), safe=False)
            else:
                return JsonResponse({"error": "Failed to fetch data from Naver API."}, status=500)
        else:
            return JsonResponse({"error": "Query parameter is missing."}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed."}, status=405)
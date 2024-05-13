import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

class YouTubeDataAPIView(APIView):
    def get(self, request):
        # settings에서 API 키 가져오기
        api_key = settings.YOUTUBE_API_KEY
        
        # API 키가 없는 경우 에러 반환
        if not api_key:
            return Response({"error": "YouTube API key is not configured."}, status=500)

        # YouTube Data API에 요청을 보낼 URL 및 매개변수 설정
        url = 'https://www.googleapis.com/youtube/v3/video'
        params = {
            'key': api_key,
            'part': 'snippet',
            'q': 'python programming',  # 검색어 설정
            'maxResults': 10  # 최대 결과 수 설정
        }
        
        # YouTube API에 GET 요청 보내기
        response = requests.get(url, params=params)
        print(response)
        # 요청이 성공적으로 이루어졌는지 확인
        if response.status_code == 200:
            # 응답 데이터 가져오기
            data = response.json()
            # 클라이언트에게 JSON 형식으로 응답 반환
            
            return Response(data)
        else:
            # 요청이 실패한 경우 에러 반환
            return Response({"error": "Failed to fetch data from YouTube API."}, status=response.status_code)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs

def crawling(search):
    # 검색어 입력
    driver = webdriver.Chrome()
    title = []
    img = []
    url = []    
    # 크롬 드라이버 설치
    try:
        driver.get("https://www.10000recipe.com/recipe/list.html?q="+search)
        element = WebDriverWait(driver, 1000)
        # 요리들 크롤링
        html = driver.page_source
        soup = bs(html, 'html.parser')
        # print(soup)
        names = soup.select('#contents_area_full > ul > ul > li')
        for name in names:
            # 요리 이름
            titles = name.select_one('div.common_sp_caption > div.common_sp_caption_tit')
            urls = name.select_one('div.common_sp_thumb > a.common_sp_link')
            imgs = name.select_one('div.common_sp_thumb > a.common_sp_link > img')
            title.append(titles.get_text())
            url.append('https://www.10000recipe.com' + urls.get('href'))
            img.append(imgs.get('src'))

        return title, url, img
    except:
        driver.close()

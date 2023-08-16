from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

import re
import time
import pandas as pd
import itertools
import traceback

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-usb-devices')
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

# 크롤링 url, 키워드
url = 'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword='
keyword = ''

try: # 이미 설치된 크롬드라이버가 있으면 
    driver = webdriver.Chrome(options=options)
except: # 없으면 설치
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 5)

def scroll_down(iter=max):
        '''
        동적 웹 페이지의 모든 컨텐츠를 로드하기 위해 스크롤을 내리는 메서드
        iter: 내리는 횟수
        '''
        if iter == max:
            last_position = 0
            while True:
                driver.execute_script("window.scrollBy(0, window.innerHeight);")
                current_position = driver.execute_script("return window.pageYOffset;")

                if current_position == last_position:
                    break
                else:
                    last_position = current_position
                
                time.sleep(0.75)

        else:
            for _ in range(iter):
                driver.execute_script("window.scrollBy(0, window.innerHeight);")
                time.sleep(0.75)
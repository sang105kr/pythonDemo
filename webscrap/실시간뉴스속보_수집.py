# http 요청,응답 수행
import requests
# html문서 파싱 (DOM 요소 다루듯 쉽게 접근하는 기능 제공)
from bs4 import BeautifulSoup
import time
# 정규표현식
import re

import pandas as pd
import matplotlib.pyplot as plt

import pyautogui

# 폰트설정
plt.rc("font", family='Malgun Gothic')
# 마이너스폰트 설정
plt.rc("axes", unicode_minus=False)


req_page =  int(pyautogui.prompt('몇 페이지를 읽어올까요?'))
df = pd.DataFrame()
for page in range(1, req_page+1 ) :

    # http요청
    url=(
        f'https://finance.naver.com/news/news_list.naver?'
        f'mode=LSS2D&section_id=101&section_id2=258&page={page}'
    )

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    params = {}
    res = requests.get(url,headers=headers, params=params)
    print(res.status_code)

    html = BeautifulSoup(res.text,'html.parser')

    # %%
    # 실시간뉴스속보 목록
    news_list = html.select_one('#contentarea_left > ul')
    print(type(news_list))

    # %%
    articleSubject_list = news_list.select('.articleSubject')
    articleSummary_list = news_list.select('.articleSummary')
    len(articleSubject_list), len(articleSummary_list)

    # %%
    # 뉴스 제목 목록 가져오기
    news_subjects = [ subject.text for subject in articleSubject_list ]
    # 뉴스 링크 목록 가져오기
    news_home_url = 'https://finance.naver.com'
    news_link = [ f"{news_home_url}{subject.select_one('a')['href']}" for subject in articleSubject_list ]
    # 뉴스 요약 목록 가져오기
    news_summaries = [ summary.get_text() for summary in articleSummary_list ]
    # 뉴스 언론사 목록 가져오기
    media_companies = [ summary.select_one('.press').text for summary in articleSummary_list ]
    # 뉴스 작성일
    news_cdates = [ summary.select_one('.wdate').text for summary in articleSummary_list ]

    # %%
    """
    * bs4.element.Tag.text  :  엘리먼트 컨텐츠의 모든 텍스트 가져오기
    * bs4.element.Tag.get_text() : 엘리먼트 컨텐츠의 첫번째노드의 텍스트 가져오기
    * bs4.element.Tag.contents : 엘리먼트 컨텐즈를 html로 가져오기
    """

    # %%
    # zip()함수를 사용해서 여러 리스트의 요소를 묶기
    zipped_lists = zip(news_subjects,news_link,news_summaries,media_companies,news_cdates)
    # zip객체를 리스트로 변환
    result_list = list(zipped_lists)

    # %%
    print(result_list[0:3])

    # %%
    # [ num for num in range(5)]
    # list( num for num in range(5) )
    # tuple( num for num in range(5) )

    # %%
    # \n \t 제거하기
    # [ tuple(ele.replace('\n','').replace('\t','').strip() for ele in t) for t in result_list ]

    # %%
    result = [ tuple( re.sub(r'[\t\n]|^\s+|\s+$','',ele)  for ele in t) for t in result_list ]

    # %%
    columns = ['제목','URL','요약','언론사','작성일시']
    df_tmp = pd.DataFrame(result,columns = columns)

    # 데이터프레임 추가
    # df.append(df_tmp,ignore_index=True)
    df = pd.concat([df, df_tmp],ignore_index=True)

    #지연시간 주기 2초
    time.sleep(2)

# %%
df.to_excel(f'실시간뉴스속보{req_page}.xlsx',index=False)
df.to_csv(f'실시간뉴스속보{req_page}.csv',index=False)

# %%
df = pd.read_excel(f'실시간뉴스속보{req_page}.xlsx')
df2 = pd.read_csv(f'실시간뉴스속보{req_page}.csv')

# %%
df.shape, df2.shape
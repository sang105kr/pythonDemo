# selenium 라이브러리에서 webdriver 모듈 임포트, 웹 브라우저를 자동으로 제어하기 위한 기능을 제공
from selenium import webdriver
# 크롬 웹드라이버를 위한 서비스 객체를 사용하기 위해 Service 모듈 임포트
from selenium.webdriver.chrome.service import Service
# 크롬 드라이버의 자동 업데이트를 위해 webdriver_manager에서 ChromeDriverManager를 임포트
from webdriver_manager.chrome import ChromeDriverManager
# 크롬 옵션을 설정하기 위한 Options 모듈을 임포트 일반적으로 브라우저의 특정 옵션을 설정할 때 사용
from selenium.webdriver.chrome.options import Options
# html요소 접근
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import pyautogui
import pyperclip

from bs4 import BeautifulSoup

# 크롬 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
# 불필요한 에레 메세지 제거
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

# ChromeDriverManager를 사용해 버전에 맞는 웹드라이버를 다운로드하여 해당 경로를 셀레니움에 전달
# case1)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# case2)
# dirver = webdriver.Chrome(ChromeDriverManager().install())

# 웹페이지가 로딩될대까지 5초대기
driver.implicitly_wait(5)
# 브라우저 크기 최대화
driver.maximize_window()

# 접근하고자 하는 웹 페이지의 URL을 정의합니다.
url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
# webdriver 인스턴스를 사용해 해당 URL의 웹 페이지를 엽니다.
driver.get(url)

# 아이디
id = driver.find_element(By.CSS_SELECTOR,"#id")
id.click()
# id.send_keys('sang105kr')
pyperclip.copy('sang105kr2')
pyautogui.hotkey('ctrl','v')
time.sleep(2)
#비밀번호
pw = driver.find_element(By.CSS_SELECTOR,"#pw")
pw.click()
# pw.send_keys('')
pyperclip.copy('1az0161az016')
pyautogui.hotkey('ctrl','v')
time.sleep(2)

# 로그인
login_btn = driver.find_element(By.CSS_SELECTOR,"#log\.login")
login_btn.click()
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs
from bs4 import BeautifulSoup

# pip install mysql-connector-python
import mysql.connector

# DB 접속을 위한 정보 세팅
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='mysql',
    database='jpa'
)

# sql 실행을 위한 커서 생성
mycursor = mydb.cursor()

# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options=option, service=service)

driver.get('https://www.aladin.co.kr')

t.sleep(2)

# 베스트셀러 탭 클릭
driver.find_element(By.XPATH, '//*[@id="Wa_header1_headerTop"]/div[2]/div[3]/ul[1]/li[3]/a').click()


cur_page_num = 2 # 현재 페이지 번호
target_page_num = 9 # 목적지 페이지 번호
rank = 1 # 순위

while cur_page_num <= target_page_num:

    # selenium으로 현재 페이지의 html 소스 코드를 전부 불러오기
    src = driver.page_source

    soup = BeautifulSoup(src, 'html.parser')

    div_list = soup.find_all('div', class_='ss_book_box')
    # div_list = soup.select('div.ss_book_box') -> 가능
    
    
    for div in div_list:
        book_info = div.find_all('li')

        if book_info[0].find('span', class_='ss_ht1') == None:
            book_title = book_info[0].text 
            book_author = book_info[1].text
            book_price = book_info[2].text

        else:
            book_title = book_info[1].text 
            book_author = book_info[2].text
            book_price = book_info[3].text

        auth_info = book_author.split(' | ')

        author_name, company, pub_day = [info.strip() for info in auth_info]

        # sql을 문자열로 작성하고, 변수가 들어갈 위치를 %s, %d 등으로 표현합니다.
        # 값은 tuple에 순서대로 세팅해서 mycursor.execute()에 전달합니다. 
        query = 'INSERT INTO tbl_crawling (data_rank, title, author, company, publish_date, price) VALUES(%s, %s, %s, %s, %s, %s)'
        values = (rank, book_title, author_name, company, pub_day, book_price.split(', ')[0])

        mycursor.execute(query, values)

        '''
        SELECT를 했다면...?
        execute로 sql을 실행하고 나서 

        for row in mycursor:
            print(str(row[컬럼명]))
        '''

        rank += 1

    # 다음 페이지(탭)로 전환
    cur_page_num += 1
    driver.find_element(By.XPATH, f'//*[@id="newbg_body"]/div[3]/ul/li[{cur_page_num}]/a').click()
    del soup
    t.sleep(3)

mydb.commit()
# mydb.rollback() -> 예외 처리와 함꼐 사용해서, 중간에 에러가 발생했을 시 롤백 처리.

driver.close()
mycursor.close()
mydb.close()


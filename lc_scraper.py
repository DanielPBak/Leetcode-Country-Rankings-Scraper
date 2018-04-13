from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import sys

csv_name = sys.argv[1]

import requests
from bs4 import BeautifulSoup
print('imports done')
login_url = "https://leetcode.com/accounts/login/"
url = "https://leetcode.com/contest/globalranking/"
page_num = 1

driver = webdriver.Chrome()
print('driver made')
driver.get(login_url)
print('driver got url')
html = driver.page_source
soup = BeautifulSoup(html)
print('done')
username_xpath = '//*[@id="id_login"]'
password_xpath = '//*[@id="id_password"]'
submit_xpath = '//*[@id="login_form"]/div[2]/div/div/div/div[1]/div/div/div/form/button'

username = driver.find_element(By.XPATH, username_xpath)
password = driver.find_element(By.XPATH, password_xpath)
print(username, password)

username.send_keys("scraper_user")
password.send_keys("lookatmypasswordwow")
driver.find_element(By.XPATH, submit_xpath).click()
page_num = 1

row_xpath = '//*[@id="contest-app"]/div/div/div/div/div[2]/div[2]/div[2]/div[*]/div'
while True:
    if page_num % 100 == 0:
        print(page_num)
    target_url = url + str(page_num)
    driver.get(url)

    while(True):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, row_xpath))
        )
        all_rows = driver.find_elements(By.XPATH, row_xpath)
        for i in all_rows:
            ranking = i.find_element(By.CSS_SELECTOR, "div.ranking.col").text
            username = i.find_element(By.CSS_SELECTOR, "div.user.col.clickable > div.username").text
            try:
                nationality = i.find_element(By.CSS_SELECTOR, "div.nationality.col.pull-right > span").get_attribute('data-original-title')
            except NoSuchElementException as e:
                nationality = "No Nationality"
            db.insert({'ranking':ranking,'username':username,'nationality':nationality,'timestamp':time.time()})
        driver.find_element(By.CSS_SELECTOR, "#contest-app > div > div > div > div > nav > ul > li.next-btn").click()

        if EC.presence_of_element_located((By.CSS_SELECTOR, "#contest-app > div > div > div > div > nav > ul > li.next-btn.disabled")):
            break

# with requests.Session() as s:
#     s.get(login_url)
#     if 'csrftoken' in s.cookies:
#         print('me!')
#         csrftoken = s.cookies['csrftoken']
#     else:
#         exit("no csrf token found ):")
#     # todo: use a config file for this stuff
#     data = {
#     "login":"dotsondots@gmail.com",
#     "password":"lookatmypasswordwow",
#     "csrfmiddlewaretoken":csrftoken
#     }
#     # log in
#     p = s.post(login_url, data=data, headers=dict(Referer=login_url))


#     while page_num < 1800:
#         target_url = url + str(page_num) + "/"
#         print(target_url)
#         page = s.get(target_url)
        
#         file = open("page.html","wb").write(bytes(page.text, "utf-8"))
#         page_num = 10000

    
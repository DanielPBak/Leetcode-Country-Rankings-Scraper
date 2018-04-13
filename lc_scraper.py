from lxml import html
import requests
login_url = "https://leetcode.com/accounts/login/"
url = "https://leetcode.com/contest/globalranking/"
page_num = 1


with requests.Session() as s:
    s.get(login_url)
    if 'csrftoken' in s.cookies:
        print('me!')
        csrftoken = s.cookies['csrftoken']
    else:
        exit("no csrf token found ):")
    # todo: use a config file for this stuff
    data = {
    "login":"dotsondots@gmail.com",
    "password":"lookatmypasswordwow",
    "csrfmiddlewaretoken":csrftoken
    }
    # log in
    p = s.post(login_url, data=data, headers=dict(Referer=login_url))
    
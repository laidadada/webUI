# -*- encoding:utf-8 -*-

from selenium import webdriver

import time

dirver = webdriver.Firefox()
dirver.maximize_window()
dirver.set_page_load_timeout(30)

dirver.get('http://www.baidu.com')

search_input = dirver.find_element_by_id("kw")
search_input.send_keys(u"王老吉")

time.sleep(10)

h3_titles = dirver.find_elements_by_tag_name("h3")
for titles in h3_titles:
    print (titles.text)
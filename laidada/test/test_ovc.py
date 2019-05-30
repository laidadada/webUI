# -*- encoding:utf-8 -*-
import unittest
import time
from selenium import webdriver

class TestOvc(unittest.TestCase):
    def test_new_ovc(self):
        #
        dirver = webdriver.Firefox()
        dirver.get("http://39.107.232.193:9527/")

        new_login = dirver.find_element_by_xpath("/html/body/div[1]/div/div[3]/ul/li[2]/a")
        new_login.click()
        user_name_input = dirver.find_element_by_id("user_login")
        user_name_input.send_keys("382135230@qq.com")
        user_passwd_input = dirver.find_element_by_id("user_password")
        user_passwd_input.send_keys("Ljc960614")
        user_login_button = dirver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div[4]/input")
        user_login_button.click()
        time.sleep(3)
        test_socity = dirver.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[1]/a")
        test_socity.click()
        time.sleep(3)
        create_tall = dirver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div/a")
        create_tall.click()
        button_title = dirver.find_element_by_xpath("//*[@id='node-selector-button']")
        button_title.click()
        select_title = dirver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[4]/span/span[2]/a")
        select_title.click()
        create_title = dirver.find_element_by_id("topic_title")
        create_title.send_keys(u"测试webui自动化")
        create_NR = dirver.find_element_by_id("topic_body")
        create_NR.send_keys(u"测试成功")
        keep = dirver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[4]/input")
        keep.click()
        time.sleep(3)
        return_NR = dirver.find_element_by_id("reply_body")
        return_NR.send_keys(u"6666666666")
        respond_button = dirver.find_element_by_xpath("//*[@id='reply-button']")
        respond_button.click()


if __name__ == '__main__':
    unittest.main()

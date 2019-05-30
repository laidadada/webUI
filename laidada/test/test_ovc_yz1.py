# -*- encoding:utf-8 -*-
import unittest
from selenium import webdriver
import time

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dirver = webdriver.Firefox()

    def test_something(self):

        target_elements = {
            'topic_link': {"xpath": "//ul[@id='main-nav-menu']/li[1]", "keyword": "topics"},
            'jobs_link': {"xpath": "//ul[@id='main-nav-menu']/li[2]", "keyword": "jobs"},
            'sites_link': {"xpath": "//ul[@id='main-nav-menu']/li[3]", "keyword": "sites"},
            'wiki_link': {"xpath": "//ul[@id='main-nav-menu']/li[4]", "keyword": "wiki"},
            'posts_link': {"xpath": "//ul[@id='main-nav-menu']/li[5]", "keyword": "posts"}
        }

        for ele_key in target_elements.keys():
            target_element = target_elements[ele_key]
            target_element_xpath = target_element['xpath']
            target_element_keyword = target_element['keyword']

            self.dirver.get("http://39.107.232.193:9527/")
            yz_test = self.dirver.find_element_by_xpath(target_element_xpath)
            yz_test.click()
            time.sleep(5)
            current_url = self.dirver.current_url
            if_end_with_keyword = current_url.endswith(target_element_keyword)
            self.assertTrue(if_end_with_keyword,
                    ("act_target_element_xpath=%s, exp_target_element_keyword=%s" %(current_url,target_element_keyword)))

if __name__ == '__main__':
    unittest.main()

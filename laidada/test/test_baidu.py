# -*- encoding:utf-8 -*-
import unittest
import time
from selenium import webdriver

class MyTestCase(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.dirver = webdriver.Firefox()

        @classmethod
        def tearDownClass(cls):
            cls.dirver.quit()

        def setUp(self):
            self.dirver.get('http://www.baidu.com')

        def test_wanglaoji(self):
            search_input = self.dirver.find_element_by_id("kw")
            search_input.clear()
            search_input.send_keys(u"王老吉")
            time.sleep(10)
            h3_titles = self.dirver.find_elements_by_tag_name("h3")

            exp_contain_keyword = u"王老吉"
            for i in range(2):
                item_title = h3_titles[i].text
                print (item_title)
                self.assertIn(exp_contain_keyword, item_title)

        def test_selenium(self):
            search_input = self.dirver.find_element_by_id("kw")
            search_input.clear()
            search_input.send_keys(u"selenium")
            time.sleep(10)
            h3_titles = self.dirver.find_elements_by_tag_name("h3")

            exp_contain_keyword = u"selenium"
            for i in range(2):
                item_title = h3_titles[i].text
                print (item_title)
                self.assertIn(exp_contain_keyword, item_title)

        def test_9527(self):
            search_input = self.dirver.find_element_by_id("kw")
            search_input.clear()
            search_input.send_keys(u"9527")
            time.sleep(10)
            h3_titles = self.dirver.find_elements_by_tag_name("h3")

            exp_contain_keyword = u"9527"
            for i in range(2):
                item_title = h3_titles[i].text
                print (item_title)
                self.assertIn(exp_contain_keyword, item_title)

if __name__ == '__main__':
    unittest.main()

# -*- encoding:utf-8 -*-
import unittest
import time
from selenium import webdriver

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dirver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.dirver.quit()

    def setUp(self):
        self.dirver.get("https://www.baidu.com/")

    def test_01(self):
        name_new = self.dirver.find_element_by_xpath("//*[@id='u1']/a[1]")
        exp_keyword = u"新闻"
        act_keyword = name_new.text
        self.assertEqual(exp_keyword, act_keyword)

        exp_url = "http://news.baidu.com/"
        name_new.click()
        act_url = self.dirver.current_url
        self.assertEqual(exp_url, act_url)

    def test_02(self):
        name_hao123 = self.dirver.find_element_by_xpath("//*[@id='u1']/a[2]")
        exp_keyword = u"hao123"
        act_keyword = name_hao123.text
        self.assertEqual(exp_keyword, act_keyword)

        exp_url = "https://www.hao123.com/"
        name_hao123.click()
        act_url = self.dirver.current_url
        self.assertEqual(exp_url, act_url)

    def test_03(self):
        name_map = self.dirver.find_element_by_xpath("//*[@id='u1']/a[3]")
        exp_keyword = u"地图"
        act_keyword = name_map.text
        self.assertEqual(exp_keyword, act_keyword)

        exp_url = "https://map.baidu.com/@12725273.29,3558757.28,12z"
        name_map.click()
        time.sleep(10)
        act_url = self.dirver.current_url
        self.assertEqual(exp_url, act_url)

    def test_04(self):
        name_shipin = self.dirver.find_element_by_xpath("//*[@id='u1']/a[4]")
        exp_keyword = u"视频"
        act_keyword = name_shipin.text
        self.assertEqual(exp_keyword, act_keyword)

        exp_url = "http://v.baidu.com/?fr=bd"
        name_shipin.click()
        time.sleep(10)
        act_url = self.dirver.current_url
        self.assertEqual(exp_url, act_url)

    def test_05(self):
        name_tieba = self.dirver.find_element_by_xpath("//*[@id='u1']/a[5]")
        exp_keyword = u"贴吧"
        act_keyword = name_tieba.text
        self.assertEqual(exp_keyword, act_keyword)

        exp_url = "https://tieba.baidu.com/index.html"
        name_tieba.click()
        time.sleep(10)
        act_url = self.dirver.current_url
        self.assertEqual(exp_url, act_url)

    def test_06(self):
        name_xs = self.dirver.find_element_by_xpath("//*[@id='u1']/a[6]")
        exp_keyword = u"学术"
        act_keyword = name_xs.text
        self.assertEqual(exp_keyword, act_keyword)

        exp_url = "http://xueshu.baidu.com/"
        name_xs.click()
        time.sleep(10)
        act_url = self.dirver.current_url
        self.assertEqual(exp_url, act_url)
if __name__ == '__main__':
    unittest.main()

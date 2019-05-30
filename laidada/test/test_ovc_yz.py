# -*- encoding:utf-8 -*-
import unittest
from selenium import webdriver
import time

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dirver = webdriver.Firefox()

    def test_something(self):
        #验证关键字
        topics_ulr_keyword = "topics"
        jobs_ulr_keyword = "jobs"
        sites_ulr_keyword = "sites"
        wiki_ulr_keyword = "wiki"
        posts_ulr_keyword = "posts"

        self.dirver.get("http://39.107.232.193:9527/")
        yz_topics = self.dirver.find_element_by_xpath("//ul[@id='main-nav-menu']/li[1]")
        yz_topics.click()
        time.sleep(5)
        topics_ulr = self.dirver.current_url
        if_end_with_keyword = topics_ulr.endswith(topics_ulr_keyword)
        self.assertTrue(if_end_with_keyword,("act_topics_ulr=%s, exp_topics_ulr_keyword=%s",(topics_ulr,topics_ulr_keyword)))

        self.dirver.get("http://39.107.232.193:9527/")
        yz_jobs = self.dirver.find_element_by_xpath("//ul[@id='main-nav-menu']/li[2]")
        yz_jobs.click()
        time.sleep(5)
        jobs_ulr = self.dirver.current_url
        if_end_with_keyword = jobs_ulr.endswith(jobs_ulr_keyword)
        self.assertTrue(if_end_with_keyword,("act_jobs_ulr=%s, exp_jobs_ulr_keyword=%s",(jobs_ulr,jobs_ulr_keyword)))

        self.dirver.get("http://39.107.232.193:9527/")
        yz_sites = self.dirver.find_element_by_xpath("//ul[@id='main-nav-menu']/li[3]")
        yz_sites.click()
        time.sleep(5)
        sites_ulr = self.dirver.current_url
        if_end_with_keyword = sites_ulr.endswith(sites_ulr_keyword)
        self.assertTrue(if_end_with_keyword,("act_sites_ulr=%s, exp_sites_ulr_keyword=%s",(sites_ulr,sites_ulr_keyword)))

        self.dirver.get("http://39.107.232.193:9527/")
        yz_wiki = self.dirver.find_element_by_xpath("//ul[@id='main-nav-menu']/li[4]")
        yz_wiki.click()
        time.sleep(5)
        wiki_ulr = self.dirver.current_url
        if_end_with_keyword = wiki_ulr.endswith(wiki_ulr_keyword)
        self.assertTrue(if_end_with_keyword,("act_wiki_ulr=%s, exp_wiki_ulr_keyword=%s",(wiki_ulr,wiki_ulr_keyword)))

        self.dirver.get("http://39.107.232.193:9527/")
        yz_posts = self.dirver.find_element_by_xpath("//ul[@id='main-nav-menu']/li[5]")
        yz_posts.click()
        time.sleep(5)
        posts_ulr = self.dirver.current_url
        if_end_with_keyword = posts_ulr.endswith(posts_ulr_keyword)
        self.assertTrue(if_end_with_keyword,("act_posts_ulr=%s, exp_posts_ulr_keyword=%s",(posts_ulr,posts_ulr_keyword)))

if __name__ == '__main__':
    unittest.main()

target_elements = {
            'topic_link': {"xpath":"//ul[@id='main-nav-menu']/li[1]/a", "keyword":"topics"},
            'jobs_link': {"xpath": "//ul[@id='main-nav-menu']/li[2]/a", "keyword": "jobs"},
            'sites_link': {"xpath": "//ul[@id='main-nav-menu']/li[3]/a", "keyword": "sites"},
            'wiki_link': {"xpath": "//ul[@id='main-nav-menu']/li[4]/a", "keyword": "wiki"},
            'posts_link': {"xpath": "//ul[@id='main-nav-menu']/li[5]/a", "keyword": "posts"}
         }
print(target_elements.keys())
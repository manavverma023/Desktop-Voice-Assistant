from selenium import webdriver

class movie():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\MANAV\\Downloads\\chromedriver.exe")

    def movie_review(self, name):
        self.driver.get(url="https://www.bing.com")
        search=self.driver.find_element_by_xpath('//*[@id="sb_form_q"]')
        search.click()
        search.send_keys(name+" movie reviews")
        submit=self.driver.find_element_by_xpath('//*[@id="sb_form"]/label')
        submit.click()

#bot=movie()
#bot.movie_review("parasite")

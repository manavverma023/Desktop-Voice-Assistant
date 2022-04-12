from selenium import webdriver
import pyttsx3 as p


class mean():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\MANAV\\Downloads\\chromedriver.exe")

    def word_mean(self, query):
        self.query = query
        self.driver.get(url="https://www.yourdictionary.com")
        search = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/input')
        search.click()
        search.send_keys(query)

        enter=self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/div[2]/div[3]/button')
        enter.click()

        info=self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div[1]/div/div[3]/div[1]/div/div/div[1]/div[1]/div[1]/div')
        readable_text=info.text
        engine=p.init()
        engine.say("the meaning is"+ readable_text)
        engine.runAndWait()


#bot = mean()
#bot.word_mean("happiness")

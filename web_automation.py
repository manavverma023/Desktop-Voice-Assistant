from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\MANAV\\Downloads\\chromedriver.exe")

    def play(self, name):
        self.name=name
        self.driver.get(url="https://www.youtube.com/results?search_query="+ name)
        video=self.driver.find_element_by_xpath('//*[@id="meta"]')
        video.click()

#bot=music()
#bot.play("jingle bell")
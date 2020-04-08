
from selenium import webdriver

driver =  webdriver.Firefox(executable_path="/Users/ricascross/Desktop/projects/youtube_search/geckodriver")

driver.get('https://www.youtube.com')

driver.quit()

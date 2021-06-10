#coding=utf-8                                                                                                                                                                              
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
filename = 'list.txt'
lines = open(filename,'r').read().splitlines()

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

for count, line in enumerate(lines):
    if 'https://' not in line:
        line = 'https://twitter.com/itdoesnotmatter/status/'+line
    URL = 'https://publish.twitter.com/?buttonType=HashtagButton&query='+ line
    driver.get(URL)
    time.sleep(2)

    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    driver.find_element_by_id('WidgetConfigurator-preview').screenshot('web_screenshot'+str(count)+'.png')

driver.quit()
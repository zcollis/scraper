#simple job automation using selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys     #module to automatically insert search terms, simulate enter key being pressed
import time

PATH = "/usr/local/bin/chromedriver"    #path to chromedriver
driver = webdriver.Chrome(PATH)

driver.get("https://www.indeed.com/")        #open requested page
# print(driver.title)

searchWhat = driver.find_element_by_id('text-input-what')   #locating search bar element
searchWhat.send_keys("entry level software developer")
  #inputting search criteria and submitting

# search2 = driver.find_element_by_id('text-input-where').find_element_by_xpath()
# if search2 is not None:
#     while search2 is not None:
#         search2.send_keys(Keys.BACKSPACE)

#try WebDriverWait + .clear() to remove input here
whereInput = driver.find_element_by_xpath('//input[contains(@id, "text-input-where")]').find_element_by_xpath('//input[contains(@value, "Charlotte, NC")]')
whereInput.send_keys(Keys.COMMAND + 'a')
whereInput.send_keys(Keys.DELETE)

searchWhere = driver.find_element_by_id('text-input-where')
searchWhere.send_keys("", Keys.RETURN)



# print(driver.page_source)
divs = driver.find_elements_by_tag_name("div")

for i in divs:
    a_tags = driver.find_elements_by_tag_name('h2')
    for j in a_tags:
        titles = driver.find_elements_by_class_name('title')
    # for j in a_tags:
    #     titles = driver.find_elements_by_class_name('title')

for title in titles:
    print(title.text)

# to do:
# 1. figure out how to exclude 'new' in job title results
# 2. create list of summaries for each corresponding job title
# 3. map job listings to titles
# 4. export results to excel file
# 5. figure out how to remove text from input box (ie Charlotte, NC -> empty input box)


driver.quit()

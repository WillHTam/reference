from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://selenium-python.readthedocs.io/locating-elements.html')

assert 'Python' in driver.title

thing = driver.find_element_by_tag_name('h1')

print(thing)

# doc = open('thang.txt', 'w')
#
# doc.write(thing)
#
# doc.close()

driver.close()

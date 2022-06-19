from random import random
import urllib.request
from selenium import webdriver

list = ['Nature', 'Animal', 'Beach']

for type in list:
    driver = webdriver.Chrome()

    driver.get(f'https://unsplash.com/s/photos/{type}')
    d = driver.find_element_by_css_selector("#app")
    imgs = d.find_elements_by_tag_name("img")
    count = 1
    for i in imgs:
        link = i.get_attribute("src")
        link1 = i.get_attribute("class")
        if link1 == "YVj9w":
            Path = f'{type}\\' + str(random()) + '.jpg'
            urllib.request.urlretrieve(link, Path)
            if count == 10:
                break
            count += 1
    driver.close()

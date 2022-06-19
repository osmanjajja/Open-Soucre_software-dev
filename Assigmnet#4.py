import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://lms.umt.edu.pk/login/index.php')

driver.find_element_by_id('username').send_keys('f2018065186')
driver.find_element_by_id('password').send_keys('SAyy4Sv@')
driver.find_element_by_id('loginbtn').click()  # Login Successful

driver.find_element_by_class_name('float-sm-left').click()  # Click the nav toggle button
list_of_elements = driver.find_elements_by_class_name('list-group-item')
# print(list_of_elements)
courses = [course.text for course in list_of_elements]

index = 4  # we dont need first 5 li

while index in range(len(courses)):
    print(courses[index])
    index += 1

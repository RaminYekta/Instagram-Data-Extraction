from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
saved_users = []
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://instagram.com')
time.sleep(5)
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
username.send_keys('Put your username here')
password.send_keys('Put your password here')
password.send_keys(Keys.RETURN)
time.sleep(3)
notnow = driver.find_element_by_class_name('yWX7d')
notnow.click()
time.sleep(3)
notnow2nd = driver.find_element_by_class_name('HoLwm')
notnow2nd.click()
time.sleep(3)
search = driver.find_element_by_class_name('x3qfX')
search.send_keys('#طراحی_داخلی')
time.sleep(2)
page = driver.find_element_by_class_name('-qQT3')
page.click()
time.sleep(5)

posts = driver.find_elements_by_class_name('v1Nh3')
for post in posts:
    post.click()
    time.sleep(2)

    try:
        plus = driver.find_element_by_class_name('afkep')
        plus.click()
        users = driver.find_elements_by_class_name('_8A5w5')
        for user in users:
            saved_users.append(user.text)
        close = driver.find_element_by_css_selector('div.yiMZG > button > div > svg')
        close.click()

    except:
        users = driver.find_elements_by_class_name('_8A5w5')
        for user in users:
            saved_users.append(user.text)
        close = driver.find_element_by_css_selector('div.yiMZG > button > div > svg')
        close.click()


lst1 = []

count = 0

# traverse the array
for i in saved_users:
    if i not in lst1:
        count = count + 1
        lst1.append(i)
print('number of users :', count)
print(lst1)

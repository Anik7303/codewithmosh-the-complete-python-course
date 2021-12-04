from selenium import webdriver
from selenium.webdriver.common.by import By

# try:
#     with webdriver.Chrome() as driver:
#         driver.get('https://github.com')
#         driver.find_element(By.LINK_TEXT, 'Sign in').click()
#         driver.find_element(By.ID, 'login_field').send_keys('ninjacoder22')
#         driver.find_element(By.ID, 'password').send_keys(
#             'todayismonday1').submit()

#         link_label = driver.find_element(
#             By.CLASS_NAME, 'user-profile-link').get_attribute('innerHTML')
#         assert 'ninjacoder22' in link_label

# except Exception as ex:
#     print(ex)


try:
    browser = webdriver.Chrome()

    browser.get('https://github.com')
    browser.find_element_by_link_text('Sign in').click()
    username_box = browser.find_element_by_id('login_field')
    username_box.send_keys('ninjacoder22')
    password_box = browser.find_element_by_id('password')
    password_box.send_keys('todayismonday1')
    password_box.submit()

    # assert 'ninjacoder22' in browser.page_source

    profile_link = browser.find_element_by_class_name('user-profile-link')
    link_label = profile_link.get_attribute('innerHTML')
    assert 'ninjacoder22' in link_label
except Exception as ex:
    print(ex)
finally:
    browser.quit()

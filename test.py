import time
from bdb import Breakpoint

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from const import DEFAULT_TIMEOUT, USER_EMAIL, PASSWORD, JOBS_PAGE_URL, SEARCH_TEXT, BASE_TIMEOUT

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/feed/")
driver.maximize_window()

user_name = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
sign_in_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Sign in"]')

user_name.send_keys(USER_EMAIL)
password.send_keys(PASSWORD)
sign_in_button.click()

jobs_button = driver.find_element(By.CSS_SELECTOR, '[title="Jobs"]')
jobs_button.click()

time.sleep(BASE_TIMEOUT)

assert driver.current_url == JOBS_PAGE_URL

search_input_field = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search by title, skill, or company"]')
search_input_field.send_keys(SEARCH_TEXT)
search_input_field.send_keys(Keys.ENTER)

time.sleep(BASE_TIMEOUT)

easy_apply_filter = driver.find_element(By.CSS_SELECTOR, '[aria-label="Easy Apply filter."]')
easy_apply_filter.click()

time.sleep(BASE_TIMEOUT)

jobs = driver.find_elements(By.XPATH, './/*[starts-with(@class, "job-card-list__logo")]')
apply_button = driver.find_element(By.XPATH, './/button//*[text()="Easy Apply"]')

for job in jobs:
    job.click()
    time.sleep(BASE_TIMEOUT)
    apply_button.click()
    while True:
        try:
            next_button = driver.find_element(By.XPATH, './/*[text()="Next"]')
            next_button.click()
            time.sleep(BASE_TIMEOUT)
        except Exception as e:
            break
    review_button = driver.find_element(By.XPATH, './/*[text()="Review"]')
    review_button.click()
    time.sleep(BASE_TIMEOUT)
    submit_button = driver.find_element(By.XPATH, './/*[text()="Submit application"]')
    submit_button.click()

time.sleep(DEFAULT_TIMEOUT)


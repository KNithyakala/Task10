""" Automating the url "https://www.saucedemo.com/" and fetching the details of title,
url and content of page using Python Selenium.
Written positive and negative testcases for title,current url and home page
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_SwagLabs():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)

        #positive test cases for title and url
        assert "Swag Labs"==driver.title, "Title of page is mismatched"
        assert "https://www.saucedemo.com/inventory.html"==driver.current_url, "Url Page is mismatched"

        #negative testcases for title and url
        assert ""!=driver.title, f"Title of page is not expected. It is displayed as '{driver.title}'"
        assert "https://www.saucedemo.com/"!=driver.current_url,f"Url of Page is not expected.Url of page '{driver.current_url}'"

        page_data=driver.find_element(By.XPATH,'//body').text
        myfile_webpage= open(file='Webpage_task10.txt',mode='w')
        myfile_webpage.write(page_data)
        driver.back()

        # positive test case for home page
        assert "https://www.saucedemo.com/"==driver.current_url,"Home page is not expected page"

        #negative test case for home page
        assert "https://www.saucedemo.com/inventory.html"!=driver.current_url,"Home is not expect page"

        time.sleep(5)
    finally:
        driver.quit()


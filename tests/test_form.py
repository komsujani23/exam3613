import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup_teardown():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def get_alert(driver):
    alert = Alert(driver)
    text = alert.text
    alert.accept()
    return text 


def test_username(setup_teardown):
    driver = setup_teardown
    driver.get('127.0.0.1:5000/')
    driver.find_element(By.ID,'uname').clear()
    driver.find_element(By.ID,'pwd').send_keys("12344")
    driver.find_element(By.NAME,'sb').click()
    alert_text = get_alert(driver)
    assert alert_text=="Username cannot be empty"


def test_password(setup_teardown):
    driver = setup_teardown
    driver.get('127.0.0.1:5000/')
    driver.find_element(By.ID,'uname').send_keys("Alice")
    driver.find_element(By.ID,'pwd').clear
    driver.find_element(By.NAME,'sb').click()
    alert_text = get_alert(driver)
    assert alert_text=="Password cannot be empty"

def test_length(setup_teardown):
    driver = setup_teardown
    driver.get('127.0.0.1:5000/')
    driver.find_element(By.ID,'uname').send_keys("Alice")
    driver.find_element(By.ID,'pwd').send_keys("123")
    driver.find_element(By.NAME,'sb').click()
    alert_text = get_alert(driver)
    assert alert_text=="Password should be atleast 6 characters"

def test_all(setup_teardown):
    driver = setup_teardown
    driver.get('127.0.0.1:5000/')
    driver.find_element(By.ID,'uname').send_keys("Sujani")
    driver.find_element(By.ID,'pwd').send_keys("1234567")
    driver.find_element(By.NAME,'sb').click()
    current_url = driver.current_url
    assert '/submit' in current_url, f"Welcome test failed."
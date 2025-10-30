import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def get_alert(driver):
    alert = Alert(driver)
    text = alert.text
    alert.accept()
    return text

def test_username(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "pwd").send_keys("1234")
    driver.find_element(By.NAME, "sb").click()
    time.sleep(1)
    alert_text = get_alert(driver)
    assert alert_text == "Username cannot be empty"

def test_password(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.NAME, "username").send_keys("Sujani")
    driver.find_element(By.NAME, "pwd").clear()
    driver.find_element(By.NAME, "sb").click()
    time.sleep(1)
    alert_text = get_alert(driver)
    assert alert_text == "Password cannot be empty"

def test_length(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.NAME, "username").send_keys("Sujani")
    driver.find_element(By.NAME, "pwd").send_keys("123")
    driver.find_element(By.NAME, "sb").click()
    time.sleep(1)
    alert_text = get_alert(driver)
    assert alert_text == "Password must be atleast 6 characters long"

def test_valid_input(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.NAME, "username").send_keys("Sujani")
    driver.find_element(By.NAME, "pwd").send_keys("1234567")
    driver.find_element(By.NAME, "sb").click()

    time.sleep(2)
    current_url = driver.current_url
    assert "/submit" in current_url, f"Expected redirect to greeting.html"
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Welcome Sujani!!" in body_text, f"Greeting not found"



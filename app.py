from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize a new Chrome browser instance
browser = webdriver.Chrome()
browser.get("https://github.com")

# Find and click the "Sign in" link
signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()

# Wait for the login page to load
time.sleep(2)  # Adjust the time as needed

# Fill the login form
# Use By.NAME to find the username field
username_box = browser.find_element(By.NAME, "login")
username_box.send_keys("your-email")

# Use By.NAME to find the password field
password_box = browser.find_element(By.NAME, "password")
password_box.send_keys("your-password")
password_box.send_keys(Keys.RETURN)  # Submit the form

# Keep the script running until you manually stop it
while True:
    pass

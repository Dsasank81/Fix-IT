from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace 'your_username' and 'your_password' with your actual Instagram username and password
username = 'your_username'
password = 'your_password'

# Path to your webdriver. Download chromedriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
webdriver_path = '/path/to/chromedriver'

# Initialize Chrome webdriver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Navigate to the Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Wait for the login page to load
time.sleep(2)

# Find username and password input fields and enter credentials
username_field = driver.find_element_by_name("username")
username_field.clear()
username_field.send_keys(username)

password_field = driver.find_element_by_name("password")
password_field.clear()
password_field.send_keys(password)

# Press Enter to submit the form
password_field.send_keys(Keys.RETURN)

# Wait for login process to complete
time.sleep(5)

# Check if login was successful by looking for the presence of the 'Explore' link (indicating we are logged in)
if "explore" in driver.current_url.lower():
    print("Login successful!")
else:
    print("Login failed.")

# Close the webdriver
driver.quit()

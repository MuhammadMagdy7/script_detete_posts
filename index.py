from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace 'path_to_webdriver_executable' with the actual path to your WebDriver executable
driver = webdriver.Firefox()

# Open Instagram and log in
driver.get("https://www.instagram.com/")
time.sleep(3)  # Adding a delay to ensure the page loads completely

# Replace 'your_username' and 'your_password' with your Instagram credentials
username_input = driver.find_element(By.NAME, 'username')
username_input.send_keys('EnterYourUsername')

password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys('EnterYourPassword')
password_input.send_keys(Keys.ENTER)

time.sleep(8)  # Adding a delay to ensure the login process completes

# Navigate to your profile
driver.get("https://www.instagram.com/styyle_way/")  # Replace 'your_username' with your Instagram username
time.sleep(5)  # Adding a delay to ensure the login process completes

# Open the first post
def scraping ():
    posts = driver.find_elements(By.CLASS_NAME, "_aagw")
    for i in posts:
        i.click()
        time.sleep(3)  # Adding a delay to ensure the post loads completely
        # Click on the options menu
        options_button = driver.find_elements(By.XPATH, "//*[name()='svg' and @class='x1lliihq x1n2onr6 x5n08af']")[12]
        print(options_button)
        time.sleep(2)  # Adding a delay to ensure the post loads completely

        options_button.click()
        time.sleep(1)
        # Click on the 'Delete' option
        delete_button = driver.find_element(By.XPATH,"//button[@class='_a9-- _ap36 _a9-_']")
        delete_button.click()
        time.sleep(1)

        # Click on the 'Delete' confirmation button
        delete_confirm_button = driver.find_element(By.XPATH,"//button[text()='حذف']")
        delete_confirm_button.click()

        # Wait for post deletion process to complete
        time.sleep(3)

        # Close the browser window
    driver.quit()

posts = driver.find_elements(By.CLASS_NAME, "_aagw")
while(posts):
    try:
        scraping()
    except:
        print("there is error")
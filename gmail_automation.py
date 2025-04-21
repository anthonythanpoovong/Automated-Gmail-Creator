from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://accounts.google.com/v3/signin/identifier?ifkv=AXH0vVsh2_dbfMMPhsF4uXH9es3Gygma-YfXSeDa51a3NevlgGMekedz05YIqDUOskwfd1_RKcJQBw&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S120139723%3A1745211357911729")
time.sleep(10)
drive.quit()

# This code is a simple automation script using Selenium to open the Gmail login page.
# It initializes a Chrome WebDriver, navigates to the Gmail login page, waits for 10 seconds, and then closes the browser.
import json
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unidecode import unidecode

def save_credentials(username, password, filename="credentials.json"):
    credentials = {
        "username": username,
        "password": password
    }
    with open(filename, "w") as file:
        json.dump(credentials, file, indent=4)
    print(f"Credentials saved to {filename}")

def load_credentials(filename="credentials.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

# Chrome options to reduce detection
chrome_options = ChromeOptions()
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Name lists truncated for brevity
first_names = ["Jack", "David", "Emma", "Olivia", "Liam"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown"]

# Generate random name and username
your_first_name = random.choice(first_names)
your_last_name = random.choice(last_names)
random_number = random.randint(1000, 9999)
your_username = f"{unidecode(your_first_name).lower()}.{unidecode(your_last_name).lower()}{random_number}"
your_birthday = "02 3 1989"  # dd m yyyy
your_gender = "1"  # Female

# Load credentials from file if available
credentials = load_credentials()
if credentials:
    your_username = credentials["username"]  # Use saved username
    your_password = credentials["password"]  # Use saved password
else:
    your_password = "default_password123"  # Default password

# Function to fill the sign-up form
def fill_form(driver):
    try:
        driver.get("https://signup.live.com/")
        wait = WebDriverWait(driver, 20)

        # Human-like delays
        time.sleep(random.uniform(1, 2))
        first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))

        # Fill in user details
        first_name.send_keys(your_first_name)
        driver.find_element(By.NAME, "lastName").send_keys(your_last_name)
        driver.find_element(By.XPATH, "//input[@name='memberName']").send_keys(your_username)  # Email field for username
        driver.find_element(By.XPATH, "//input[@name='Passwd']").send_keys(your_password)  # Password field
        driver.find_element(By.XPATH, "//input[@name='ConfirmPasswd']").send_keys(your_password)  # Confirm password field
        driver.find_element(By.XPATH, "//button[.//span[text()='Next']]").click()

        # Wait for the birthday section and fill in the date
        birthday_parts = your_birthday.split()
        Select(wait.until(EC.presence_of_element_located((By.ID, "birthMonth")))).select_by_value(birthday_parts[1])
        driver.find_element(By.ID, "birthDay").send_keys(birthday_parts[0])
        driver.find_element(By.ID, "birthYear").send_keys(birthday_parts[2])
        Select(driver.find_element(By.ID, "gender")).select_by_value(your_gender)
        driver.find_element(By.XPATH, "//button[.//span[text()='Next']]").click()

        # Wait for the CAPTCHA to appear and require manual solving
        print("Please solve the CAPTCHA manually in the browser window.")

        # Wait for the CAPTCHA to be solved manually
        input("Press Enter after completing CAPTCHA.")

        # Final steps
        driver.find_element(By.XPATH, "//button[.//span[text()='Next']]").click()  # Skip recovery email
        driver.find_element(By.XPATH, "//button[.//span[text()='I agree']]").click()  # Accept terms

        print(f"Account created successfully: {your_username}@outlook.com")

        # Save the credentials after account creation
        save_credentials(your_username, your_password)

    except Exception as e:
        print(f"Failed to create account: {str(e)}")
    finally:
        driver.quit()

# Execute the function to create the account
fill_form(driver)

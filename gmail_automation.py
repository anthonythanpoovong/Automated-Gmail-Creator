from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chome.options import Options as ChromeOptions

import random
import time
from unicode import unidecode

#chrome options
chrome_options = ChromeOptions()
chrome_options.add_argument("--disable-infobars")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

first_names = [
    "Jack", "David", "Emma", "Olivia", "Liam", "Noah", "Ava", "Sophia", "Ethan", "Jacob",
    "Isabella", "Mia", "Lucas", "Charlotte", "Benjamin", "William", "Grace", "James", "Alexander", "Harper", "Samuel",
    "Zoe", "Leah", "Nathan", "Amelia", "Matthew", "Ella", "Logan", "Lily", "Daniel", "Victoria", "Michael", "Chloe",
    "Jackson", "Emma", "Olivia", "Lucas", "Abigail", "Sophia", "Lily", "Ryan", "Hannah", "Aiden", "Ella", "Chloe", "Carter",
    "Lucy", "Leo", "Mason", "Emily", "Grace", "Gabriel", "Jacky", "Owen", "Scarlett", "Benjamin", "Noah", "Maya", "Thomas",
    "Joshua", "Addison", "Abigail", "Elijah", "Jameson"
]
last_names = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez", "Hernandez", "Lopez",
    "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "White", "Harris", "Martin", "Thompson", "Young",
    "Allen", "Sanchez", "King", "Scott", "Green", "Baker", "Adams", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Evans",
    "Turner", "Collins", "Graham", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Ross", "Morris", "Murphy", "Bell", "Powell",
    "Campbell", "Patel", "Parker"
]

#randomly select a first name and last name
your_first_name = random.choice(first_names)
your_last_name = random.choice(last_names)

#generate a random number
random_number = random.randint(1000, 9999)
#normalize the first and last names
your_first_name_normalized = unidecode(your_first_name).lower()
your_last_name_normalized = unidecode(your_last_name).lower()


your_username = f"{your_first_name_normalized}.{your_last_name_normalized}{random_number}"


your_birthday = "02 3 1989" #dd m yyyy exp : 24 11 2003
your_gender = "1" # 1:F 2:M 3:Not say 4:Custom
your_password = "x,nscldsj123...FDKZ"

def fill_form(driver):
    try:
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        #fill in name fields
        first_name = driver.find_element(By.NAME, "firstName")
        last_name = driver.find_element(By.NAME, "lastName")
        first_name.clear()
        first_name.send_keys(your_first_name)
        last_name.clear()
        last_name.send_keys(your_last_name)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        print("full name fields filled successfully")

        #wait for birthday fields to be visible
        wait = WebDriverWait(driver, 20)
        day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))

        #fill in birthday
        birthday_elements = your_birthday.split()
        month_dropdown = Select(driver.find_element(By.ID, "month"))
        month_dropdown.select_by_value(birthday_elements[1])
        day_field = driver.find_element(By.ID, "day")
        day_field.clear()
        day_field.send_keys(birthday_elements[0])
        year_field = driver.find_element(By.ID, "year")
        year_field.clear()
        year_field.send_keys(birthday_elements[2])

        #select gender
        gender_dropdown = Select(driver.find_element(By.ID, "gender"))
        gender_dropdown.select_by_value(your_gender)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        print("Birthday filled successfully")

        
        #create custom email
        time.sleep(2)
        if driver.find_elements(By.CLASS_NAME, "uxXgMe"):
            create_own_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[jsname='CeL6Qc']")))
            create_own_option.click()
        
        wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
        username_field = driver.find_element(By.NAME, "Username")
        username_field.clear()
        username_field.send_keys(your_username)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()
        


        #enter and confirm password
        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        password_field.clear()
        password_field.send_keys(your_password)
        #locate the parent div element with the ID "confirm-passwd"
        confirm_passwd_div = driver.find_element(By.ID, "confirm-passwd")
        #find the input field inside the parent div
        password_confirmation_field = confirm_passwd_div.find_element(By.NAME, "PasswdAgain")
        password_confirmation_field.clear()
        password_confirmation_field.send_keys(your_password)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()


        #check if the phone number is needed
        time.sleep(2)
        if driver.find_elements(By.ID, "phoneNumberId"):
            wait.until(EC.element_to_be_clickable((By.ID, "phoneNumberId")))
            phonenumber_field = driver.find_element(By.ID, "phoneNumberId")
            phonenumber_field.clear()
            phonenumber_field.send_keys("+2126"+str(random.randint(10000000,99999999)))
            next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
            next_button.click()
            time.sleep(2)
            ok = ok = not driver.find_element(By.CLASS_NAME, "AfGCob")
            while not ok:
                try:
                    phonenumber_field.clear()
                    phonenumber_field.send_keys("+2126"+str(random.randint(10000000,99999999)))
                    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
                    next_button.click()
                    time.sleep(2)
                    ok = ok = not driver.find_element(By.CLASS_NAME, "AfGCob")
                    ok = not driver.find_element(By.CLASS_NAME, "AfGCob")
                except:
                    pass
        else:
            #skip phone number and recovery email steps
            skip_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
            for button in skip_buttons:
                button.click()

        #agree to terms
        agree_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        agree_button.click()


        print(f"Your Gmail successfully created:\n{{\ngmail: {your_username}@gmail.com\npassword: {your_password}\n}}")

    except Exception as e:
        print("Failed to create your Gmail, Sorry")
        print(e)
    finally:
        driver.quit()

#execute the function to fill out the form
fill_form(driver)

# This code is a simple automation script using Selenium to open the Gmail login page.
# It initializes a Chrome WebDriver, navigates to the Gmail login page, waits for 10 seconds, and then closes the browser.
import time

import pyautogui
from selenium.webdriver import Keys

from locators.Client_general_information_locators import  ClientGeneralInformationLocators

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClientGeneral(ClientGeneralInformationLocators):
    def __init__(self ,driver,logger=None):
        self.driver = driver
        self.logger = logger




    def login(self, username, password):
        self.driver.get("https://staging.zoobooksystems.com/")
        username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.USERNAME_INPUT))
        username_input.clear()
        username_input.send_keys(username)

        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()






        # except TimeoutException:
        #     print("Login successful but the success message didn't appear within the specified time.")


    def add(self,add_client):
        try:

            pyautogui.moveTo(x=450, y=440, duration=0.5)
            time.sleep(3)

            pyautogui.moveTo(x=450, y=610, duration=0.5)
            # Add some delay if needed
            pyautogui.click()
            # add_client_btn = WebDriverWait(self.driver, 20).until(
            #     EC.element_to_be_clickable(self.ADD_CLIENT)
            # )
            pyautogui.typewrite(add_client)
            pyautogui.press(Keys.ENTER)

        except Exception as e:
            print(f"Press on Add Client from Header once hover : {e}")




    def client_page_form_detail(self,firstname,lastname,dob,status,check_status):

        try:
            firstname_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.FIRST_NAME))
            firstname_input.clear()
            firstname_input.send_keys(firstname)

            lastname_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.LAST_NAME))
            lastname_input.clear()
            lastname_input.send_keys(lastname)

            dob_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.DOB_INPUT))
            dob_input.clear()
            dob_input.send_keys(dob)
            time.sleep(2)

        #     now for martial status selecting

            status_dropdown = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.MARTIAL_STATUS))
            status_dropdown.click()

            # Locate the input field within the dropdown and input the status
            status_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.MARTIAL_SELECT))
            status_input.send_keys(status)
            status_input.send_keys(Keys.ENTER)


        # check status
            check_status_dropdown = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.STATUS_INPUT))
            check_status_dropdown.click()

            # Locate the input field within the  input the status
            status_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.STATUS_SELECT))
            status_input.send_keys(check_status)
            status_input.send_keys(Keys.ENTER)






        except Exception as e:
            print(f"first name and last name and DOB : {e}")


    def ssn_numbers(self,ssn_number):
        try:

            ssn_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.SSN_INPUT))
            ssn_input.clear()
            ssn_input.send_keys(ssn_number)
            time.sleep(2)


        except Exception as e:
            print(f"Error filling SSN Number: {e}")



    def fill_gender(self,gender_value):
        try:

            gender_dropdown = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.SELECT_GENDER))
            gender_dropdown.click()

            # Locate the input field within the dropdown and input the status
            gender_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.GENDER_IS))
            gender_input.send_keys(gender_value)
            gender_input.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Error for  Gender: {e}")

    def requested_services(self,checkbox):

        try:
            checkbox_xpath = f"//input[@type='checkbox' and @data-text='{checkbox}']"
            checkbox_element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, checkbox_xpath)))

            if not checkbox_element.is_selected():
                checkbox_element.click()
        except Exception as e:
            print(f"Error occurred while selecting checkbox for '{checkbox}': {e}")

    def primary_race(self,primary_value):
        try:

            primary_dropdown = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.PRIMARY_RACE))
            primary_dropdown.click()

            # Locate the input field within the dropdown and input the status
            primary_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.PRIMARY_OPTION))
            primary_input.send_keys(primary_value)
            primary_input.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Error for  Primary Race: {e}")

    def secondary_race(self,secondary_value):
        try:

            secondary_dropdown = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.SECONDARY_RACE))
            secondary_dropdown.click()

            # Locate the input field within the dropdown and input the status
            secondary_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.SECONDARY_OPTION))
            secondary_input.send_keys(secondary_value)
            secondary_input.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Error for  Secondary Race: {e}")

    def save_buttons(self):
        save_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        save_button.click()

        try:
            # Navigate back to the "View Client" section
            self.view_client()
        except Exception as e:
            print(f"Error navigating back to View Client after saving: {e}")
    def yes_buttons(self):
        yes_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.YES_BUTTON))
        yes_button.click()
        time.sleep(3)
        self.view_client()


    def view_client(self):
        try:

            pyautogui.moveTo(x=500, y=480, duration=0.5)
            time.sleep(3)

            pyautogui.moveTo(x=450, y=570, duration=0.5)
            # Add some delay if needed
            pyautogui.click()
            client_btn = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.VIEW_CLIENT)
            )
            client_btn.click()




        except Exception as e:

            error_message = f"Error occurred when we View Client: {str(e)}"

            print(error_message)


    def click_name(self):

        try:
            # Click on the name element to open a new tab
            name_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.CLICK_NAME))
            name_button.click()
            time.sleep(3)  # Adjust the delay as needed

            # Switch to the newly opened tab
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[1])



        except Exception as e:
            print(f"Error occurred while clicking the client name: {e}")


    def status_pending(self,check):
        try:

            secondary_dropdown = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.STATUS_INPUT))
            secondary_dropdown.click()

            # Locate the input field within the dropdown and input the status
            secondary_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.STATUS_PENDING))
            secondary_input.send_keys(check)
            secondary_input.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Error for  Secondary Race: {e}")

    def verify_client_name_after_status(self):
        try:
            # XPath for the client's name

            clname_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.CLICK_NAME))
            clname_button.click()
            time.sleep(3)

            # Get the text of the element
            clname_text = clname_button.text

            # Check if the client's name matches the expected value
            if clname_text == "Khan , saad":
                self.logger.info("Khan is present in the list")
                assert True
            else:
                self.logger.info("Khan is not present in the list")
                assert False

            time.sleep(5)

        except Exception as e:
            print(f"Error while checking client's name: {e}")




    def quit_driver(self):

        self.driver.quit()








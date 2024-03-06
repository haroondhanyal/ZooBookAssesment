

from selenium import webdriver

from logs.Log import Logger
from seleniumbase import BaseCase


from pages.Client_general_information_pages import ClientGeneral

class TestCases(BaseCase):
    logger = Logger(log_folder="C:\\Users\\rajah\\PycharmProjects\\ProjectZoobook\\logs")
    logger.create_logger()

    def setup_method(self, request):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.maximize_window()
            self.driver.get("https://staging.zoobooksystems.com/")
            page_title = self.driver.title
            print(page_title)

        except Exception as e:
            print(f"Error occurred during setup: {e}")

    def teardown_method(self, method):
        try:
            if self.driver:
                self.driver.quit()
        except Exception as e:
            print(f"Error occurred during teardown: {e}")



    #  Test Cases 1 and 2
    #  i am login to the website, then go to client tadd new client , and fill all the fields which is required then it will save that client

    def test_add_client(self):
        username = "ttt_admin"
        password = "@zb1234!"
        first_name = "Saad"
        last_name = "Khan"
        dob = "01/11/1990"
        status = "Never"
        check_status = "Active"
        ssn_number = "063151925"
        gender_value = "Male"
        checkboxes_to_select = ["Substance Abuse Assessment", "Mental Health", "Outpatient", "Sober Housing"]
        primary_value = "Declined to Specify"
        secondary_value = "Declined to Specify"
        add_client = "Add Client"

        # check_status = "Pending"


        try:
            # Login
            client_page = ClientGeneral(self.driver)
            client_page.login(username, password)
            client_page.add(add_client)
            client_page.client_page_form_detail(first_name, last_name,dob,status,check_status)
            client_page.ssn_numbers(ssn_number)
            client_page.fill_gender(gender_value)
            for checkbox in checkboxes_to_select:
                client_page.requested_services(checkbox)
            client_page.primary_race(primary_value)
            client_page.secondary_race(secondary_value)
            client_page.save_buttons()
            client_page.yes_buttons()

        except Exception as e:

            print(f"An unexpected error occurred: {e}")

    #         test cases 3 4 and 5

    #         in this Test i am view the client  which is registered

    #         then  click that (open that client) and changes status to the pending  then it will again view that client that update client is preseent or not

    def test_verify_client_status(self):
        try:
            username = "ttt_admin"
            password = "@zb1234!"
            check = "pending"

            # Login
            client_page = ClientGeneral(self.driver)
            client_page.login(username, password)

            # Navigate to the "View Client" section
            client_page.view_client()
            client_page.click_name()
            client_page.status_pending(check)
            client_page.save_buttons()

            client_page.verify_client_name_after_status()



            print("View Client page loaded successfully")


        except Exception as e:

            print(f"An unexpected error occurred during the View Client test: {e}")

            # Print the detailed exception information

            import traceback

            traceback.print_exc()














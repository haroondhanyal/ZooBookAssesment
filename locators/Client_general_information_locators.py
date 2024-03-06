from selenium.webdriver.common.by import By


class ClientGeneralInformationLocators:
    #login page locators
    USERNAME_INPUT = (By.XPATH, "//input[@name='zb-username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='zb-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-success btn-block login-button']")



    ADD_CLIENT = (By.XPATH, "//a[@target='_self'][normalize-space()='Add Client']")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME = (By.XPATH, " //input[@placeholder='Last Name']")
    DOB_INPUT = (By.XPATH,"//input[@id='birth_Date']")
    MARTIAL_STATUS = (By.XPATH,"//span[@id='select2-maritalStatus-container']")
    MARTIAL_SELECT = (By.XPATH, "//body/span[3]/span[1]/span[1]/input[1]")
    STATUS_INPUT = (By.XPATH,"//span[@id='select2-statusId-container']")
    STATUS_SELECT = (By.XPATH, "//body/span[3]/span[1]/span[1]/input[1]")


    SSN_INPUT = (By.XPATH,"//input[@id='SSN']")
    SELECT_GENDER =(By.XPATH,"//span[@id='select2-gender-container']")
    GENDER_IS = (By.XPATH, "//body/span[3]/span[1]/span[1]/input[1]")

    # Requested Services option select
    SUBSTANCE_CLICK = (By.XPATH,"//input[@data-text='Substance Abuse Assessment']")
    MENTAL_CLICK = (By.XPATH,"//input[@data-text='Mental Health']")
    SOBER_CLICK = (By.XPATH,"//input[@data-text='Sober Housing']")
    OUT_CLICK = (By.XPATH,"//input[@data-text='Outpatient']")

    PRIMARY_RACE = (By.XPATH,"//span[@id='select2-primaryRace-container']")

    PRIMARY_OPTION = (By.XPATH, "//body/span[3]/span[1]/span[1]/input[1]")
    SECONDARY_RACE = (By.XPATH,"//span[@id='select2-secondaryRace-container']")

    SECONDARY_OPTION = (By.XPATH, "//body/span[3]/span[1]/span[1]/input[1]")

    SAVE_BUTTON =(By.XPATH,"//div[@id='details']//div[@class='panel-footer']//button[1]")
    YES_BUTTON= (By.XPATH,"//button[normalize-space()='Yes']")




    VIEW_CLIENT = (By.XPATH, "//a[@target='_self'][normalize-space()='View Clients']")
    # (By.XPATH, "//a[normalize-space()='View Clients']")
    # (By.XPATH, "//a[@target='_self'][normalize-space()='Add Client']")
    CLICK_NAME = (By.XPATH,"//tr[@class='odd']//a[contains(text(),'Khan , Saad')]")

    STATUS_PENDING = (By.XPATH,"//input[@role='textbox']")












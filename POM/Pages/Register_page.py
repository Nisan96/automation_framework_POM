from selenium.webdriver.common.by import By
from POM.Pages.base_page import BasePage
from POM.utils.locators import RegisterPage_Locators

class RegisterPage(BasePage):
    # define register actions
    def click_elements(self):
        self.click_element(*RegisterPage_Locators.SUBSCRIBE_RADIO_BUTTON)
        self.click_element(*RegisterPage_Locators.AGREE_CHECKBOX)
        self.click_element(*RegisterPage_Locators.CONTINUE_BUTTON)

    def enter_firstname(self,firstname):
        self.input_text(*RegisterPage_Locators.FIRSTNAME_INPUT, firstname)

    def enter_lastname(self,lastname):
        self.input_text(*RegisterPage_Locators.LASTNAME_INPUT, lastname)

    def enter_email(self,email):
        self.input_text(*RegisterPage_Locators.EMAIL_INPUT, email)

    def enter_telephone(self,telephone):
        self.input_text(*RegisterPage_Locators.TELEPHONE_INPUT,telephone)

    def enter_password(self,password):
        self.input_text(*RegisterPage_Locators.PASSWORD_INPUT,password)

    def enter_confirmPassword(self,confirm_password):
        self.input_text(*RegisterPage_Locators.CONFIRM_PASSWORD_INPUT,confirm_password)







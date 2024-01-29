import time
import pytest
from selenium import webdriver
from POM.Pages.Register_page import RegisterPage
from POM.Pages.base_page import BasePage
from POM.Data.RegisterPage_data import Register_test_data
from POM.utils.config import LOGGING_FORMAT,LOGGING_LEVEL,LOGGING_FILENAME_VALID,LOGGING_FILENAME_INVALID,logger,formatter
import logging



def test_RegisterPage_valid(setup):
    logger.setLevel(LOGGING_LEVEL)
    file_handler = logging.FileHandler(LOGGING_FILENAME_VALID)
    file_handler.setLevel(LOGGING_LEVEL)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    register_page = RegisterPage(setup)

    register_page.enter_firstname(Register_test_data.valid_firstname)
    register_page.enter_lastname(Register_test_data.valid_lastname)
    register_page.enter_email(Register_test_data.valid_email)
    register_page.enter_telephone(Register_test_data.valid_telephone)
    register_page.enter_password(Register_test_data.valid_password)
    register_page.enter_confirmPassword(Register_test_data.valid_confirmPassword)

    register_page.click_elements()

    register_page.control.implicitly_wait(5)
    logger.info("Input data done")
    register_page.capture_screenshot("RegisterPage_test_valid")
    logger.info("valid test done")
    #time.sleep(3)
    logger.removeHandler(file_handler)



def test_RegisterPage_invalid(setup):
    logger.setLevel(LOGGING_LEVEL)
    file_handler = logging.FileHandler(LOGGING_FILENAME_INVALID)
    file_handler.setLevel(LOGGING_LEVEL)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    register_page = RegisterPage(setup)

    register_page.enter_firstname(Register_test_data.invalid_firstname)
    register_page.enter_lastname(Register_test_data.invalid_lastname)
    register_page.enter_email(Register_test_data.invalid_email)
    register_page.enter_telephone(Register_test_data.invalid_telephone)
    register_page.enter_password(Register_test_data.invalid_password)
    register_page.enter_confirmPassword(Register_test_data.invalid_confirmPassword)

    register_page.click_elements()

    register_page.control.implicitly_wait(5)
    logger.info("Input data done")
    time.sleep(3)
    register_page.capture_screenshot("RegisterPage_test_invalid")
    logger.info("invalid test done")
    #time.sleep(3)
    logger.removeHandler(file_handler)

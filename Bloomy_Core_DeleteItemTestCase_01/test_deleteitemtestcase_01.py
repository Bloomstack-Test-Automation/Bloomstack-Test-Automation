import time

from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Bloomy_Core
    Package: TestProject.Generated.Tests.BloomyCore
    Test: DeleteItemTestCase_01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/26/2021, 03:33:49
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="DeleteItemTestCase_01")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """By Rahul."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

    # 3. Click 'Login'
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    login.click()

    # 4. Click 'Email Address'
    email_address = driver.find_element(By.CSS_SELECTOR,
                                        "#login_email")
    email_address.click()

    # 5. Type 'rahul.prakash@extrapreneursindia.com' in 'Email Address'
    email_address = driver.find_element(By.CSS_SELECTOR,
                                        "#login_email")
    email_address.send_keys("testautomationuser@bloomstack.com")

    # 6. Click 'Password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#login_password")
    password.click()

    # 7. Type 'epi@123' in 'Password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#login_password")
    password.send_keys("epi@123")

    # 8. Click 'Login1'
    login1 = driver.find_element(By.XPATH,
                                 "//button[. = '\n\t\t\t\tLogin']")
    login1.click()

    # 9. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 10. Type 'item' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("item")

    # 11. Click 'Item List1'
    item_list1 = driver.find_element(By.XPATH,
                                     "//li[. = 'Item List']")
    item_list1.click()

    # 12. Does 'Item5' contain 'Item'?
    item5 = driver.find_element(By.XPATH,
                                "//div[. = 'Item']")
    step_output = item5.text
    assert step_output and ("Item" in step_output)
    time.sleep(2)

    # 13. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 14. Click 'INPUT39'
    input39 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]/div/input")
    input39.click()

    # 15. Type 'Delete Item0009' in 'INPUT39'
    input39 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]/div/input")
    input39.send_keys("Delete Item0009")

    # 16. Click 'INPUT40'
    input40 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]//input")
    input40.click()

    # 17. Type 'Delete item009' in 'INPUT40'
    input40 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]//input")
    input40.send_keys("Delete item009")

    # 18. Get text from 'INPUT39'
    # Captured Item Code
    input39 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]/div/input")
    step_output = input39.get_attribute("value")

    # 19. Click 'Save'
    save = driver.find_element(By.XPATH,
                               "//button[. = 'Save']")
    save.click()
    time.sleep(2)

    # 20. Click 'INPUT129'
    input129 = driver.find_element(By.XPATH,
                                   "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script( "arguments[0].click();", input129)


    # 21. Click 'SPAN15'
    span15 = driver.find_element(By.XPATH,
                                 "//div[2]/div[2]/button/span[1]")
    span15.click()

    # 22. Click 'Delete6'
    delete6 = driver.find_element(By.XPATH,
                                  "//span[. = 'Delete']")
    delete6.click()

    # 23. Get text from 'Delete 1 items permanently?2'
    # Delete Message
    delete_1_items_permanently_question_mark_2 = driver.find_element(By.XPATH,
                                                                     "//p[. = 'Delete 1 items permanently?']")
    step_output = delete_1_items_permanently_question_mark_2.get_attribute(
        "value")

    # 24. Click 'Yes3'
    yes3 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes3.click()

    # 25. Click 'Settings1'
    settings1 = driver.find_element(By.XPATH,
                                    "//span[. = '      Settings']")
    settings1.click()

    # 26. Click 'Logout1'
    logout1 = driver.find_element(By.XPATH,
                                  "//a[. = '       Logout']")
    logout1.click()

    # 27. Get text from 'Login'
    # Logout Screen
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    step_output = login.get_attribute("value")

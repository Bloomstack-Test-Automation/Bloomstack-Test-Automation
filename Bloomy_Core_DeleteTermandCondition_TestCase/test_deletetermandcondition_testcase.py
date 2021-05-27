import time

from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
from password_generator import PasswordGenerator

import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Bloomy_Core
    Package: TestProject.Generated.Tests.BloomyCore
    Test: DeleteTermandCondition_TestCase
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/27/2021, 10:06:37
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="DeleteTermandCondition_TestCase")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()

def getPassword():
        pwo = PasswordGenerator()
        pwo.minlen = 8
        # pwo.shuffle_password( 'sdafasdfu', 20 )
        pwo.minuchars = 0  # (Optional)
        pwo.minlchars = 8  # (Optional)
        pwo.minnumbers = 0  # (Optional)
        pwo.minschars = 0  # (Optional)
        # pwo.excludenumbers = "012345"  # (Optional)
        # pwo.excludeschars = "!$%^.()"  # (Optional)

        password = pwo.generate()
        return password


@report_assertion_errors
def test_main(driver):
    """Generated By:Rahul."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Is 'Login3' visible?
    login3 = driver.find_element(By.XPATH,
                                 "//li[. = '\n\tLogin\n']")
    assert login3.is_displayed()

    # 3. Click 'Login'
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    login.click()

    # 4. Click 'Email Address'
    email_address = driver.find_element(By.CSS_SELECTOR,
                                        "#login_email")
    email_address.click()

    # 5. Type 'testautomationuser@bloomstack.com' in 'Email Address'
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

    # 10. Type 'term' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("term")

    # 11. Click 'Terms and Conditions List1'
    terms_and_conditions_list1 = driver.find_element(By.XPATH,
                                                     "//span[. = 'Terms and Conditions List']")
    terms_and_conditions_list1.click()

    # 11. Does 'Terms and Conditions1' contain 'Terms and Conditions'?
    terms_and_conditions1 = driver.find_element(By.XPATH,
                                                "//div[. = 'Terms and Conditions']")
    step_output = terms_and_conditions1.text
    assert step_output and ("Terms and Conditions" in step_output)
    time.sleep(2)

    # 12. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 13. Is 'DIV86' visible?
    div86 = driver.find_element(By.XPATH,
                                "//div[4]/div[2]/div/div[1]/div/div[1]")
    assert div86.is_displayed()

    # 14. Click 'INPUT67'
    input67 = driver.find_element(By.XPATH,
                                  "//form/div[1]/div/div//input")
    input67.click()

    # 15. Type 'Hihjhd' in 'INPUT67'
    input67 = driver.find_element(By.XPATH,
                                  "//form/div[1]/div/div//input")
    password = getPassword()
    input67.send_keys(password)

    # 16. Click 'Save'
    save = driver.find_element(By.XPATH,
                               "//button[. = 'Save']")
    save.click()
    time.sleep(2)

    # 17. Click 'INPUT145'
    input145 = driver.find_element(By.XPATH,
                                   "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script( "arguments[0].click();", input145 )

    # 18. Click 'Actions6'
    actions6 = driver.find_element(By.XPATH,
                                   "//span[. = 'Actions']")
    actions6.click()

    # 19. Click 'Delete1'
    delete1 = driver.find_element(By.XPATH,
                                  "//a[. = '\n\t\t\t\tDelete']")
    delete1.click()

    # 20. Does 'Delete 1 items permanently?2' contain 'Delete 1 items permanently?'?
    delete_1_items_permanently_question_mark_2 = driver.find_element(By.XPATH,
                                                                     "//p[. = 'Delete 1 items permanently?']")
    step_output = delete_1_items_permanently_question_mark_2.text
    assert step_output and ("Delete 1 items permanently?" in step_output)

    # 21. Click 'Yes3'
    yes3 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes3.click()

    # 22. Click 'Settings1'
    settings1 = driver.find_element(By.XPATH,
                                    "//span[. = '      Settings']")
    settings1.click()

    # 23. Click 'Logout1'
    logout1 = driver.find_element(By.XPATH,
                                  "//a[. = '       Logout']")
    logout1.click()

    # 24. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

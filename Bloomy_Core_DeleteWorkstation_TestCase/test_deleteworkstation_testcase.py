import time

from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
# import password_generator
from password_generator import PasswordGenerator
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Bloomy_Core
    Package: TestProject.Generated.Tests.BloomyCore
    Test: DeleteWorkstation_TestCase
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/27/2021, 06:56:42
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="DeleteWorkstation_TestCase")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()

# Add Random Data Generation code here
def getPassword():
    pwo = PasswordGenerator()
    pwo.minlen = 8
    # pwo.shuffle_password( 'sdafasdfu', 20 )
    pwo.excludenumbers = "012345"  # (Optional)
    pwo.excludeschars = "!$%^"  # (Optional)
    password = pwo.generate()
    return password

@report_assertion_errors
def test_main(driver):
    """Generated By:Rahul."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io"

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

    # 10. Type 'workstat' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("workstat")

    # 11. Click 'Workstation List'
    workstation_list = driver.find_element(By.XPATH,
                                           "//p[. = 'Workstation List']")
    workstation_list.click()

    # 12. Does 'Workstation4' contain 'Workstation'?
    workstation4 = driver.find_element(By.XPATH,
                                       "//div[. = 'Workstation']")
    step_output = workstation4.text
    assert step_output and ("Workstation" in step_output)
    time.sleep(2)

    # 13. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 14. Click 'INPUT52'
    input52 = driver.find_element(By.XPATH,
                                  "//form/div/div/div//input")
    password = getPassword()
    input52.send_keys(password)

    # 15. Type 'Deleted WK' in 'INPUT52'
    input52 = driver.find_element(By.XPATH,
                                  "//form/div/div/div//input")
    input52.send_keys("Deleted WK")

    # 16. Click 'Save44'
    save44 = driver.find_element(By.XPATH,
                                 "//button[. = 'Save']")
    driver.execute_script( "arguments[0].click();", save44 )
    time.sleep(1)

    # 17. Click 'INPUT108'
    input108 = driver.find_element(By.XPATH,
                                   "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script( "arguments[0].click();", input108 )
    time.sleep(2)

    # 18. Click 'Actions6'
    actions6 = driver.find_element(By.XPATH,
                                   "//span[. = 'Actions']")
    actions6.click()

    # 19. Click 'Delete2'
    delete2 = driver.find_element(By.XPATH,
                                  "//a[. = '\n\t\t\t\tDelete']")
    delete2.click()

    # 20. Does 'Delete 1 items permanently?' contain 'Delete 1 items permanently?'?
    delete_1_items_permanently_question_mark_ = driver.find_element(By.XPATH,
                                                                    "//p[. = 'Delete 1 items permanently?']")
    step_output = delete_1_items_permanently_question_mark_.text
    assert step_output and ("Delete 1 items permanently?" in step_output)

    # 21. Click 'Yes1'
    yes1 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes1.click()

    # 22. Click 'Settings1'
    settings1 = driver.find_element(By.XPATH,
                                    "//span[. = '      Settings']")
    settings1.click()

    # 23. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 24. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()
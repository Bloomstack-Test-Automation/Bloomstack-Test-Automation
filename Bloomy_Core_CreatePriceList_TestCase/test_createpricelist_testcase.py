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
    Test: CreatePriceList_TestCase
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/28/2021, 03:10:56
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="CreatePriceList_TestCase")
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

    # 10. Type 'price' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("price")

    # 11. Click 'Price List3'
    price_list3 = driver.find_element(By.XPATH,
                                      "//p[. = 'Price List']")
    price_list3.click()

    # 12. Is 'Price List4' visible?
    price_list4 = driver.find_element(By.XPATH,
                                      "//div[. = 'Price List']")
    assert price_list4.is_displayed()
    time.sleep(2)

    # 13. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 14. Is 'DIV47' visible?
    div47 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    assert div47.is_displayed()

    # 15. Click 'INPUT146'
    input146 = driver.find_element(By.XPATH,
                                   "//form/div[1]/div/div[2]/div/input")
    input146.click()

    # 16. Type 'dgdrghr' in 'INPUT146'
    input146 = driver.find_element(By.XPATH,
                                   "//form/div[1]/div/div[2]/div/input")
    password = getPassword()
    input146.send_keys(password)

    # 17. Click 'INPUT147'
    input147 = driver.find_element(By.XPATH,
                                   "//div[3]/div/label/span/input")
    driver.execute_script( "arguments[0].click();", input147 )

    # 18. Click 'Save26'
    save26 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    driver.execute_script( "arguments[0].click();", save26 )

    # 19. Does 'Saved33' contain 'Saved'?
    saved33 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved33.text
    assert step_output and ("Saved" in step_output)

    # 20. Does 'DIV47' contain '[NONE]'?
    div47 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div47.text
    assert step_output and ("" in step_output)

    # 21. Click 'Settings2'
    settings2 = driver.find_element(By.XPATH,
                                    "//span[. = '      Settings']")
    settings2.click()

    # 22. Click 'Logout1'
    logout1 = driver.find_element(By.XPATH,
                                  "//a[. = '       Logout']")
    logout1.click()

    # 23. Is 'Login3' visible?
    login3 = driver.find_element(By.XPATH,
                                 "//li[. = '\n\tLogin\n']")
    assert login3.is_displayed()

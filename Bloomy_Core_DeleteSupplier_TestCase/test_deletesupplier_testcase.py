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
    Test: DeleteSupplier_TestCase
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/27/2021, 09:28:08
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="DeleteSupplier_TestCase")
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
    """Generated BY:Rahul."""
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

    # 10. Type 'supplier' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("supplier")

    # 11. Click 'Supplier List'
    supplier_list = driver.find_element(By.XPATH,
                                        "//li[. = 'Supplier List']")
    supplier_list.click()

    # 12. Does 'Supplier5' contain 'Supplier'?
    supplier5 = driver.find_element(By.XPATH,
                                    "//div[. = 'Supplier']")
    step_output = supplier5.text
    assert step_output and ("Supplier" in step_output)
    time.sleep(2)

    # 13. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 14. Is 'New Supplier1' visible?
    new_supplier1 = driver.find_element(By.XPATH,
                                        "//h4[. = 'New Supplier']")
    assert new_supplier1.is_displayed()

    # 15. Click 'INPUT34'
    input34 = driver.find_element(By.XPATH,
                                  "//form/div[1]/div/div//input")
    input34.click()

    # 16. Type 'hfkjhf' in 'INPUT34'
    input34 = driver.find_element(By.XPATH,
                                  "//form/div[1]/div/div//input")
    password = getPassword()
    input34.send_keys(password)

    # 17. Click 'INPUT35'
    input35 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/div/div/input")
    input35.click()

    # 18. Click 'Raw goods'
    raw_goods = driver.find_element(By.XPATH,
                                    "//strong[. = 'Raw goods']")
    raw_goods.click()

    # 19. Click 'Save6'
    save6 = driver.find_element(By.XPATH,
                                "//button[. = 'Save']")
    save6.click()
    time.sleep(2)

    # 20. Click 'INPUT82'
    input82 = driver.find_element(By.XPATH,
                                  "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script( "arguments[0].click();", input82)

    # 21. Click 'SPAN10'
    span10 = driver.find_element(By.XPATH,
                                 "//div[2]/div[2]/button/span[1]")
    span10.click()

    # 22. Click 'Delete'
    delete = driver.find_element(By.XPATH,
                                 "//a[. = '\n\t\t\t\tDelete']")
    delete.click()

    # 23. Does 'Delete 1 items permanently?' contain 'Delete 1 items permanently?'?
    delete_1_items_permanently_question_mark_ = driver.find_element(By.XPATH,
                                                                    "//p[. = 'Delete 1 items permanently?']")
    step_output = delete_1_items_permanently_question_mark_.text
    assert step_output and ("Delete 1 items permanently?" in step_output)

    # 24. Click 'Yes5'
    yes5 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes5.click()

    # 25. Click 'Settings2'
    settings2 = driver.find_element(By.XPATH,
                                    "//span[. = '      Settings']")
    settings2.click()

    # 26. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 27. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

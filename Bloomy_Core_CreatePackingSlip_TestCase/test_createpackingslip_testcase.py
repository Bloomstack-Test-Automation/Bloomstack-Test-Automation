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
    Test: CreatePackingSlip_TestCase
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/28/2021, 10:13:11
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="CreatePackingSlip_TestCase")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


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

    # 10. Type 'packing' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("packing")

    # 11. Click 'Packing Slip List1'
    packing_slip_list1 = driver.find_element(By.XPATH,
                                             "//span[. = 'Packing Slip List']")
    packing_slip_list1.click()

    # 12. Does 'Packing Slip2' contain 'Packing Slip'?
    packing_slip2 = driver.find_element(By.XPATH,
                                        "//div[. = 'Packing Slip']")
    step_output = packing_slip2.text
    assert step_output and ("Packing Slip" in step_output)
    time.sleep(2)

    # 13. Click 'New1'
    new1 = driver.find_element(By.XPATH,
                               "//span[. = 'New']")
    new1.click()

    # 14. Does 'DIV4' contain '[NONE]'?
    div4 = driver.find_element(By.XPATH,
                               "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div4.text
    assert step_output and ("" in step_output)

    # 15. Click 'INPUT88'
    input88 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form//input")
    input88.click()

    # 16. Click 'P19'
    p19 = driver.find_element(By.XPATH,
                              "//div/div/div/ul/li[1]/a/p")
    p19.click()

    # 17. Click 'INPUT25'
    input25 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[1]/form//input")
    input25.click()

    # 18. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 19. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 20. Type '4' in 'INPUT25'
    input25 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[1]/form//input")
    input25.send_keys("4")

    # 21. Click 'DIV28'
    div28 = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div28.click()

    # 22. Click 'Create a new Item'
    create_a_new_item = driver.find_element(By.XPATH,
                                            "//p[. = ' Create a new Item']")
    create_a_new_item.click()

    # 23. Does 'New Item3' contain 'New Item'?
    new_item3 = driver.find_element(By.XPATH,
                                    "//h4[. = 'New Item']")
    step_output = new_item3.text
    assert step_output and ("New Item" in step_output)

    # 24. Click 'INPUT38'
    input38 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]/div/input")
    input38.click()

    # 25. Type 'Test' in 'INPUT38'
    input38 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]/div/input")
    input38.send_keys("Test")

    # 26. Click 'INPUT94'
    input94 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]/div/input")
    input94.click()

    # 27. Type 'Test' in 'INPUT94'
    input94 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]/div/input")
    input94.send_keys("Test")

    # 28. Click 'Save20'
    save20 = driver.find_element(By.XPATH,
                                 "//button[3][. = 'Save']")
    driver.execute_script( "arguments[0].click();", save20 )

    # 29. Click 'Quantity'
    quantity = driver.find_element(By.XPATH,
                                   "//input[@placeholder = 'Quantity']")
    quantity.click()

    # 30. Type '1.00' in 'Quantity'
    quantity = driver.find_element(By.XPATH,
                                   "//input[@placeholder = 'Quantity']")
    quantity.send_keys("1.00")

    # 31. Click 'Net Weight'
    net_weight = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Net Weight']")
    net_weight.click()

    # 32. Type '1.00' in 'Net Weight'
    net_weight = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Net Weight']")
    net_weight.send_keys("1.00")

    # 33. Click 'Save8'
    save8 = driver.find_element(By.XPATH,
                                "//span[. = 'Save']")
    driver.execute_script( "arguments[0].click();", save8 )

    # 34. Scroll window by ('0','-200')
    driver.execute_script("window.scrollBy(0,-200)")

    # 35. Does 'Saved17' contain 'Saved'?
    saved17 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved17.text
    assert step_output and ("Saved" in step_output)

    # 36. Does 'DIV4' contain '[NONE]'?
    div4 = driver.find_element(By.XPATH,
                               "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div4.text
    assert step_output and ("" in step_output)

    # 37. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 38. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 39. Does 'Login' contain 'Login'?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    step_output = login.text
    assert step_output and ("Login" in step_output)
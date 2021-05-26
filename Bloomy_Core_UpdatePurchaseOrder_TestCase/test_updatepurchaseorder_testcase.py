import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Bloomy_Core
    Package: TestProject.Generated.Tests.BloomyCore
    Test: UpdatePurchaseOrder_TestCase
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/26/2021, 07:36:34
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="UpdatePurchaseOrder_TestCase")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Generated By: Rahul."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Does 'Login' contain 'Login'?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    step_output = login.text
    assert step_output and ("Login" in step_output)

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

    # 10. Type 'purchase order' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("purchase order")

    # 11. Click 'Purchase Order List'
    purchase_order_list = driver.find_element(By.XPATH,
                                              "//span[. = 'Purchase Order List']")
    purchase_order_list.click()

    # 12. Is 'Purchase Order1' visible?
    purchase_order1 = driver.find_element(By.XPATH,
                                          "//div[. = 'Purchase Order']")
    assert purchase_order1.is_displayed()
    time.sleep(2)

    # 13. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 14. Is 'DIV47' visible?
    div47 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    assert div47.is_displayed()

    # 15. Click 'INPUT86'
    input86 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[3]//input")
    input86.click()

    # 16. Click 'LI12'
    li12 = driver.find_element(By.XPATH,
                               "//div[2]/div[1]/div/div/ul/li[9]")
    li12.click()

    # 17. Click 'License1'
    license1 = driver.find_element(By.XPATH,
                                   "//div[. = '\t\t\t\t\t\tLicense\t\t\t\t\t']")
    license1.click()

    # 18. Click 'INPUT136'
    input136 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div[2]/form/div[2]//input")
    input136.click()

    # 19. Click 'svg10'
    svg10 = driver.find_element(By.XPATH,
                                "//div[2]/nav/div[3]/*")
    svg10.click()

    # 20. Click '3012'
    _3012 = driver.find_element(By.XPATH,
                                "//div[32][. = '30']")
    _3012.click()

    # 21. Click 'INPUT87'
    input87 = driver.find_element(By.XPATH,
                                  "//div[1]/form/div[6]//input")
    input87.click()

    # 22. Type 'va' in 'INPUT87'
    input87 = driver.find_element(By.XPATH,
                                  "//div[1]/form/div[6]//input")
    input87.send_keys("va")

    # 23. Click 'VapeCo17'
    vapeco17 = driver.find_element(By.XPATH,
                                   "//p[. = 'VapeCo']")
    vapeco17.click()

    # 24. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 25. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 26. Click 'DIV82'
    div82 = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div82.click()

    # 27. Click 'VC-RM-FO-0001'
    vc_rm_fo_0001 = driver.find_element(By.XPATH,
                                        "//strong[. = 'VC-RM-FO-0001']")
    vc_rm_fo_0001.click()

    # 28. Scroll window by ('0','-58')
    driver.execute_script("window.scrollBy(0,-58)")

    # 29. Get text from 'Item Code'
    # Captured Item Name
    item_code = driver.find_element(By.XPATH,
                                    "//input[@placeholder = 'Item Code']")
    step_output = item_code.get_attribute("value")

    # 30. Click 'Save26'
    save26 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    save26.click()

    # 31. Scroll window by ('0','-342')
    driver.execute_script("window.scrollBy(0,-342)")

    # 32. Does 'Saved5' contain 'Saved'?
    saved5 = driver.find_element(By.XPATH,
                                 "//div[. = 'Saved']")
    step_output = saved5.text
    assert step_output and ("Saved" in step_output)

    # 33. Click 'Purchase Order2'
    purchase_order2 = driver.find_element(By.XPATH,
                                          "//div[1]/ul//a[. = 'Purchase Order']")
    purchase_order2.click()
    time.sleep(2)

    # 34. Click 'INPUT137'
    input137 = driver.find_element(By.XPATH,
                                   "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script( "arguments[0].click();", input137 )

    # 35. Click 'SPAN16'
    span16 = driver.find_element(By.XPATH,
                                 "//div[2]/div[1]/div/div/div[2]/div[2]/button/span/span[2]")
    span16.click()

    # 36. Click 'Edit1'
    edit1 = driver.find_element(By.XPATH,
                                "//a[. = '\n\t\t\t\tEdit']")
    edit1.click()

    # 37. Click 'SELECT20'
    select20 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select20.click()

    # 38. Select the 'Currency' option in 'SELECT20'
    select20 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    Select(select20).select_by_value("Currency")

    # 39. Click 'SELECT20'
    select20 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select20.click()

    # 40. Click 'INPUT76'
    input76 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//input")
    input76.click()

    # 41. Click 'USD'
    usd = driver.find_element(By.XPATH,
                              "//p[. = 'USD']")
    usd.click()

    # 42. Click 'Update2'
    update2 = driver.find_element(By.XPATH,
                                  "//button[. = 'Update']")
    update2.click()

    # 43. Does 'Updated successfully15' contain 'Updated successfully'?
    updated_successfully15 = driver.find_element(By.XPATH,
                                                 "//div[. = 'Updated successfully']")
    step_output = updated_successfully15.text
    assert step_output and ("Updated successfully" in step_output)

    # 44. Click 'Settings2'
    settings2 = driver.find_element(By.XPATH,
                                    "//span[. = '      Settings']")
    settings2.click()

    # 45. Click 'Logout1'
    logout1 = driver.find_element(By.XPATH,
                                  "//a[. = '       Logout']")
    logout1.click()

    # 46. Is 'Login3' visible?
    login3 = driver.find_element(By.XPATH,
                                 "//li[. = '\n\tLogin\n']")
    assert login3.is_displayed()
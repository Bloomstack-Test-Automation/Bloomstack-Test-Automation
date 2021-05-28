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
    Test: UpdateQuotation_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/27/2021, 05:09:45
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="UpdateQuotation_TestCase01")
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

    # 10. Type 'quo' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("quo")

    # 11. Click 'Quotation List1'
    quotation_list1 = driver.find_element(By.XPATH,
                                          "//li[. = 'Quotation List']")
    quotation_list1.click()

    # 12. Does 'Quotation7' contain 'Quotation'?
    quotation7 = driver.find_element(By.XPATH,
                                     "//div[. = 'Quotation']")
    step_output = quotation7.text
    assert step_output and ("Quotation" in step_output)
    time.sleep(2)

    # 13. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 14. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 15. Scroll window by ('0','-100')
    driver.execute_script("window.scrollBy(0,-100)")

    # 16. Click 'INPUT141'
    input141 = driver.find_element(By.XPATH,
                                   "//div[2]/form/div[2]/div/div[2]/div[1]/div//input")
    input141.click()

    # 17. Type 'vap' in 'INPUT141'
    input141 = driver.find_element(By.XPATH,
                                   "//div[2]/form/div[2]/div/div[2]/div[1]/div//input")
    input141.send_keys("vap")

    # 18. Click 'VapeCo6'
    vapeco6 = driver.find_element(By.XPATH,
                                  "//strong[. = 'VapeCo']")
    vapeco6.click()

    # 19. Click 'INPUT142'
    input142 = driver.find_element(By.XPATH,
                                   "//div[1]/form/div[4]//input")
    input142.click()

    # 20. Click 'P55'
    p55 = driver.find_element(By.XPATH,
                              "//div[4]/div/div[2]/div[1]/div/div/ul/li[1]//p")
    p55.click()

    # 21. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 22. Click 'INPUT143'
    input143 = driver.find_element(By.XPATH,
                                   "//div[4]/div/div[2]/div/input")
    input143.click()

    # 23. Click 'svg3'
    svg3 = driver.find_element(By.XPATH,
                               "//div[3]/nav/div[3]/*")
    svg3.click()

    # 24. Click 'svg3'
    svg3 = driver.find_element(By.XPATH,
                               "//div[3]/nav/div[3]/*")
    svg3.click()

    # 25. Click '3013'
    _3013 = driver.find_element(By.XPATH,
                                "//div[34][. = '30']")
    _3013.click()

    # 26. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 27. Click 'Add Row'
    add_row = driver.find_element(By.XPATH,
                                  "//div[6]//button[. = '\n\t\t\t\t\t\t\tAdd Row']")
    add_row.click()

    # 28. Click 'DIV85'
    div85 = driver.find_element(By.XPATH,
                                "//form/div/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div85.click()

    # 29. Click 'Finished Oil, Dry Goods, Extracted Ja...3'
    finished_oil_dry_goods_extracted_ja_3 = driver.find_element(By.XPATH,
                                                                "//span[. = 'Finished Oil, Dry Goods, Extracted Jack Herer Cannabis Oil']")
    finished_oil_dry_goods_extracted_ja_3.click()

    # 30. Does 'DIV47' contain '[NONE]'?
    div47 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div47.text
    assert step_output and ("" in step_output)

    # 31. Click 'Save26'
    save26 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    save26.click()

    # 32. Scroll window by ('0','-400')
    driver.execute_script("window.scrollBy(0,-400)")

    # 33. Click 'Close3'
    close3 = driver.find_element(By.XPATH,
                                 "//span[. = 'Close']")
    close3.click()

    # 34. Does 'Saved5' contain 'Saved'?
    saved5 = driver.find_element(By.XPATH,
                                 "//div[. = 'Saved']")
    step_output = saved5.text
    assert step_output and ("Saved" in step_output)

    # 35. Does 'DIV47' contain '[NONE]'?
    div47 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div47.text
    assert step_output and ("" in step_output)

    # 36. Click 'Quotation2'
    quotation2 = driver.find_element(By.XPATH,
                                     "//div[1]/ul//a[. = 'Quotation']")
    quotation2.click()
    time.sleep(1)


    # 37. Click 'INPUT139'
    input139 = driver.find_element(By.XPATH,
                                   "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script( "arguments[0].click();", input139 )

    # 38. Click 'Actions4'
    actions4 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]//button[. = '               Actions                            ']")
    actions4.click()

    # 39. Click 'Edit1'
    edit1 = driver.find_element(By.XPATH,
                                "//a[. = '\n\t\t\t\tEdit']")
    edit1.click()

    # 40. Click 'SELECT23'
    select23 = driver.find_element(By.XPATH,
                                   "//div[1]/div/div[2]/div/select")
    select23.click()

    # 41. Select the 'Currency' option in 'SELECT23'
    select23 = driver.find_element(By.XPATH,
                                   "//div[1]/div/div[2]/div/select")
    Select(select23).select_by_value("Currency")

    # 42. Click 'SELECT23'
    select23 = driver.find_element(By.XPATH,
                                   "//div[1]/div/div[2]/div/select")
    select23.click()

    # 43. Click 'INPUT110'
    input110 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form//input")
    input110.click()

    # 44. Click 'USD3'
    usd3 = driver.find_element(By.XPATH,
                               "//li[. = 'USD']")
    usd3.click()

    # 45. Click 'Update'
    update = driver.find_element(By.XPATH,
                                 "//button[. = 'Update']")
    update.click()
    time.sleep(2)

    # 46. Click 'Close8'
    close8 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div//button[. = '\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\tClose\n\t\t\t\t\t\t\t\t']")
    close8.click()
    #driver.execute_script( "arguments[0].click();", close8 )

    # 47. Does 'Updated successfully13' contain 'Updated successfully'?
    updated_successfully13 = driver.find_element(By.XPATH,
                                                 "//div[. = 'Updated successfully']")
    step_output = updated_successfully13.text
    assert step_output and ("Updated successfully" in step_output)

    # 48. Click 'Settings2'
    settings2 = driver.find_element(By.XPATH,
                                    "//span[. = '      Settings']")
    settings2.click()

    # 49. Click 'Logout1'
    logout1 = driver.find_element(By.XPATH,
                                  "//a[. = '       Logout']")
    logout1.click()

    # 50. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

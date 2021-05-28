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
    Test: UpdatePaymentEntry_TestCase
    Generated by: Meenal Kardale (meenal.kardale@extrapreneurs-india.com)
    Generated on 05/28/2021, 20:44:08
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="3J0RNM_48lLt_KM5Ab6s6A_HZzddmktVs_HhX77AjTM",
                              project_name="Bloomy_Core",
                              job_name="UpdatePaymentEntry_TestCase")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'Login'
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    login.click()

    # 3. Click 'Email Address'
    email_address = driver.find_element(By.CSS_SELECTOR,
                                        "#login_email")
    email_address.click()

    # 4. Type 'testautomationuser@bloomstack.com' in 'Email Address'
    email_address = driver.find_element(By.CSS_SELECTOR,
                                        "#login_email")
    email_address.send_keys("testautomationuser@bloomstack.com")

    # 5. Click 'Password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#login_password")
    password.click()

    # 6. Type 'epi@123' in 'Password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#login_password")
    password.send_keys("epi@123")

    # 7. Click 'Login1'
    login1 = driver.find_element(By.XPATH,
                                 "//button[. = '\n\t\t\t\tLogin']")
    login1.click()

    # 8. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 9. Type 'payment e' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("payment e")

    # 10. Click 'Payment Entry List1'
    payment_entry_list1 = driver.find_element(By.XPATH,
                                              "//p[. = 'Payment Entry List']")
    payment_entry_list1.click()
    time.sleep(2)
    # 11. Click 'New4'
    new4 = driver.find_element(By.XPATH,
                               "//button[. = 'New']")
    time.sleep(2)
    new4.click()

    # 12. Click 'SELECT7'
    select7 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/select")
    select7.click()

    # 13. Select the 'Internal Transfer' option in 'SELECT7'
    select7 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/select")
    Select(select7).select_by_value("Internal Transfer")

    # 14. Click 'SELECT7'
    select7 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/select")
    select7.click()

    # 15. Click 'INPUT39'
    input39 = driver.find_element(By.XPATH,
                                  "//div[3]/div[2]/div[2]/form/div[2]//input")
    input39.click()

    # 16. Type 'v' in 'INPUT39'
    input39 = driver.find_element(By.XPATH,
                                  "//div[3]/div[2]/div[2]/form/div[2]//input")
    input39.send_keys("v")

    # 17. Click 'VapeCo'
    vapeco = driver.find_element(By.XPATH,
                                 "//strong[. = 'VapeCo']")
    vapeco.click()

    # 18. Click 'INPUT40'
    input40 = driver.find_element(By.XPATH,
                                  "//div[5]/div[2]/div[1]/form//input")
    input40.click()

    # 19. Type '[NONE]' in 'INPUT40'
    input40 = driver.find_element(By.XPATH,
                                  "//div[5]/div[2]/div[1]/form//input")
    input40.send_keys(" ")

    # 20. Click 'HDFC - VC'
    hdfc_vc = driver.find_element(By.XPATH,
                                  "//li[. = 'HDFC - VC']")
    hdfc_vc.click()

    # 21. Click 'INPUT41'
    input41 = driver.find_element(By.XPATH,
                                  "//div[5]/div[2]/div[2]//input")
    input41.click()

    # 22. Type '[NONE]' in 'INPUT41'
    input41 = driver.find_element(By.XPATH,
                                  "//div[5]/div[2]/div[2]//input")
    input41.send_keys(" ")

    # 23. Click 'EPI-Sales-Account1 - VC1'
    epi_sales_account1_vc1 = driver.find_element(By.XPATH,
                                                 "//div[1]/div/div[2]/div[1]/div/div/ul//strong[. = 'EPI-Sales-Account1 - VC']")
    epi_sales_account1_vc1.click()

    # 24. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 25. Click 'INPUT42'
    input42 = driver.find_element(By.XPATH,
                                  "//div[6]/div[2]/div[1]/form/div[1]//input")
    input42.click()

    # 26. Type '200.00' in 'INPUT42'
    input42 = driver.find_element(By.XPATH,
                                  "//div[6]/div[2]/div[1]/form/div[1]//input")
    input42.send_keys("200.00")

    # 27. Click 'INPUT43'
    input43 = driver.find_element(By.XPATH,
                                  "//div[6]/div[2]/div[2]/form/div[1]//input")
    input43.click()

    # 28. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 29. Scroll window by ('0','152')
    driver.execute_script("window.scrollBy(0,152)")

    # 30. Click 'INPUT44'
    input44 = driver.find_element(By.XPATH,
                                  "//div[10]/div[2]/div[1]/form//input")
    input44.click()

    # 31. Type '345' in 'INPUT44'
    input44 = driver.find_element(By.XPATH,
                                  "//div[10]/div[2]/div[1]/form//input")
    input44.send_keys("345")

    # 32. Click 'INPUT45'
    input45 = driver.find_element(By.XPATH,
                                  "//div[10]/div[2]/div[2]//input")
    input45.click()

    # 33. Click '31'
    _31 = driver.find_element(By.XPATH,
                              "//div[2]/div//div[. = '31']")
    _31.click()

    # 34. Click 'Save17'
    save17 = driver.find_element(By.XPATH,
                                 "//button[. = 'Save']")
    save17.click()

    # 35. Scroll window by ('0','-452')
    driver.execute_script("window.scrollBy(0,-452)")

    # 36. Does 'Draft' contain 'Draft'?
    draft = driver.find_element(By.XPATH,
                                "//span/span[. = 'Draft']")
    step_output = draft.text
    assert step_output and ("Draft" in step_output)

    # 37. Click 'Submit5'
    submit5 = driver.find_element(By.XPATH,
                                  "//button/span[. = 'Submit']")
    submit5.click()

    # 38. Click 'Yes'
    yes = driver.find_element(By.XPATH,
                              "//button[. = 'Yes']")
    yes.click()

    # 39. Does 'Submitted2' contain 'Submitted'?
    submitted2 = driver.find_element(By.XPATH,
                                     "//span/span[. = 'Submitted']")
    step_output = submitted2.text
    assert step_output and ("Submitted" in step_output)

    # 40. Click 'Payment Entry2'
    payment_entry2 = driver.find_element(By.XPATH,
                                         "//a[. = 'Payment Entry']")
    payment_entry2.click()
    time.sleep(2)
    # 41. Click 'INPUT46'
    #input46 = driver.find_element(By.XPATH,
     #                             "//div[2]/div[2]/div[1]/div[1]/div/input")
    #input46.click()

    input46 = driver.find_element(By.XPATH,
                                  "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script("arguments[0].click();", input46)

    # 42. Click 'Actions1'
    actions1 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]//button[. = '               Actions                            ']")
    actions1.click()

    # 43. Click 'Edit2'
    edit2 = driver.find_element(By.XPATH,
                                "//a[. = '\n\t\t\t\tEdit']")
    edit2.click()

    # 44. Click 'SELECT8'
    select8 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select8.click()

    # 45. Select the 'Company' option in 'SELECT8'
    select8 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    Select(select8).select_by_value("Company")

    # 46. Click 'SELECT8'
    select8 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select8.click()

    # 47. Click 'INPUT47'
    input47 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//input")
    input47.click()

    # 50. Type 'v' in 'INPUT47'
    input47 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//input")
    input47.send_keys("VapeCo")

    # 51. Click 'VapeCo1'
    vapeco1 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//li[. = 'VapeCo']")
    vapeco1.click()

    # 52. Click 'Update1'
    update1 = driver.find_element(By.XPATH,
                                  "//button[. = 'Update']")
    update1.click()

    # 53. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 54. Click 'Logout1'
    logout1 = driver.find_element(By.XPATH,
                                  "//a[. = '       Logout']")
    logout1.click()

    # 55. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

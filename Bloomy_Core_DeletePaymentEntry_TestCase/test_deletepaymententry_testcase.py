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
    Test: DeletePaymentEntry_TestCase
    Generated by: Meenal Kardale (meenal.kardale@extrapreneurs-india.com)
    Generated on 05/28/2021, 20:44:19
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="3J0RNM_48lLt_KM5Ab6s6A_HZzddmktVs_HhX77AjTM",
                              project_name="Bloomy_Core",
                              job_name="DeletePaymentEntry_TestCase")
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

    # 10. Click 'Payment Entry List2'
    payment_entry_list2 = driver.find_element(By.XPATH,
                                              "//span[. = 'Payment Entry List']")
    payment_entry_list2.click()
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

    # 17. Click 'VapeCo2'
    vapeco2 = driver.find_element(By.XPATH,
                                  "//li[. = 'VapeCo']")
    vapeco2.click()

    # 18. Click 'INPUT40'
    input40 = driver.find_element(By.XPATH,
                                  "//div[5]/div[2]/div[1]/form//input")
    input40.click()

    # 19. Type '[NONE]' in 'INPUT40'
    input40 = driver.find_element(By.XPATH,
                                  "//div[5]/div[2]/div[1]/form//input")
    input40.send_keys(" ")

    # 20. Click 'HDFC - VC1'
    hdfc_vc1 = driver.find_element(By.XPATH,
                                   "//strong[. = 'HDFC - VC']")
    hdfc_vc1.click()

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

    # 26. Type '1,200.00' in 'INPUT42'
    input42 = driver.find_element(By.XPATH,
                                  "//div[6]/div[2]/div[1]/form/div[1]//input")
    input42.send_keys("1,200.00")

    # 27. Click 'INPUT43'
    input43 = driver.find_element(By.XPATH,
                                  "//div[6]/div[2]/div[2]/form/div[1]//input")
    input43.click()

    # 28. Scroll window by ('0','252')
    driver.execute_script("window.scrollBy(0,252)")

    # 29. Click 'INPUT44'
    input44 = driver.find_element(By.XPATH,
                                  "//div[10]/div[2]/div[1]/form//input")
    input44.click()

    # 30. Type '564' in 'INPUT44'
    input44 = driver.find_element(By.XPATH,
                                  "//div[10]/div[2]/div[1]/form//input")
    input44.send_keys("564")

    # 31. Click 'INPUT45'
    input45 = driver.find_element(By.XPATH,
                                  "//div[10]/div[2]/div[2]//input")
    input45.click()

    # 32. Click '31'
    _31 = driver.find_element(By.XPATH,
                              "//div[2]/div//div[. = '31']")
    _31.click()

    # 33. Click 'Save17'
    save17 = driver.find_element(By.XPATH,
                                 "//button[. = 'Save']")
    save17.click()

    # 34. Scroll window by ('0','-452')
    driver.execute_script("window.scrollBy(0,-452)")

    # 35. Does 'Draft' contain 'Draft'?
    draft = driver.find_element(By.XPATH,
                                "//span/span[. = 'Draft']")
    step_output = draft.text
    assert step_output and ("Draft" in step_output)

    # 36. Click 'Submit6'
    submit6 = driver.find_element(By.XPATH,
                                  "//button[. = 'Submit']")
    submit6.click()

    # 37. Click 'Yes'
    yes = driver.find_element(By.XPATH,
                              "//button[. = 'Yes']")
    yes.click()

    # 38. Does 'Submitted2' contain 'Submitted'?
    submitted2 = driver.find_element(By.XPATH,
                                     "//span/span[. = 'Submitted']")
    step_output = submitted2.text
    assert step_output and ("Submitted" in step_output)

    # 39. Click 'Payment Entry2'
    payment_entry2 = driver.find_element(By.XPATH,
                                         "//a[. = 'Payment Entry']")
    payment_entry2.click()
    time.sleep(2)
    # 40. Click 'INPUT48'
    input48 = driver.find_element(By.XPATH,
                                  "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    time.sleep(2)
    driver.execute_script("arguments[0].click();", input48)
    time.sleep(2)

    #input48 = driver.find_element(By.XPATH,
     #                             "//div[2]/div[2]/div[1]/div[1]/div/input")
    #input48.click()

    # 41. Click 'Actions1'
    actions1 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]//button[. = '               Actions                            ']")
    actions1.click()

    # 42. Click 'Delete3'
    delete3 = driver.find_element(By.XPATH,
                                  "//span[. = 'Delete']")
    delete3.click()

    # 43. Click 'Yes4'
    yes4 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes4.click()

    # 44. Click 'Close8'
    close8 = driver.find_element(By.XPATH,
                                 "//button[. = '\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\tClose\n\t\t\t\t\t\t\t\t']")
    close8.click()

    # 45. Click 'T
    # 		           Settings'
    t_settings = driver.find_element(By.XPATH,
                                     "//a[. = '     \n\t\t\t\n\t\t\t\tT\n\t\t           Settings     ']")
    t_settings.click()

    # 46. Click 'Logout1'
    logout1 = driver.find_element(By.XPATH,
                                  "//a[. = '       Logout']")
    logout1.click()

    # 47. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()
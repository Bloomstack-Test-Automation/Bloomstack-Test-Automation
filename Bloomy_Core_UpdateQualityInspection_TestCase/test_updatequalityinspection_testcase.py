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
    Test: UpdateQualityInspection_TestCase
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/26/2021, 10:45:54
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="UpdateQualityInspection_TestCase")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Generated By : Rahul."""
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

    # 9. Type 'quality ins' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("quality ins")

    # 10. Click 'Quality Inspection List'
    quality_inspection_list = driver.find_element(By.XPATH,
                                                  "//span[. = 'Quality Inspection List']")
    quality_inspection_list.click()

    # 11. Does 'Quality Inspection3' contain 'Quality Inspection'?
    quality_inspection3 = driver.find_element(By.XPATH,
                                              "//div[. = 'Quality Inspection']")
    step_output = quality_inspection3.text
    assert step_output and ("Quality Inspection" in step_output)
    time.sleep(2)

    # 12. Click 'New1'
    new1 = driver.find_element(By.XPATH,
                               "//span[. = 'New']")
    new1.click()

    # 13. Click 'Edit in full page'
    edit_in_full_page = driver.find_element(By.XPATH,
                                            "//button[. = 'Edit in full page']")
    edit_in_full_page.click()

    # 14. Is 'DIV4' visible?
    div4 = driver.find_element(By.XPATH,
                               "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    assert div4.is_displayed()

    # 15. Click 'SELECT5'
    select5 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[1]//select")
    select5.click()

    # 16. Select the 'Incoming' option in 'SELECT5'
    select5 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[1]//select")
    Select(select5).select_by_value("Incoming")

    # 17. Click 'SELECT5'
    select5 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[1]//select")
    select5.click()

    # 18. Click 'INPUT16'
    input16 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[1]//input")
    input16.click()

    # 19. Click 'Extracted Jack Herer Cannabis Oil, Dr...'
    extracted_jack_herer_cannabis_oil_dr_ = driver.find_element(By.XPATH,
                                                                "//span[. = 'Extracted Jack Herer Cannabis Oil, Dry Goods']")
    extracted_jack_herer_cannabis_oil_dr_.click()

    # 20. Get text from 'INPUT16'
    # Item code Captured in not saved status
    input16 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[1]//input")
    step_output = input16.get_attribute("value")

    # 21. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 22. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 23. Click 'INPUT13'
    input13 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[4]//input")
    input13.click()

    # 24. Click 'P16'
    p16 = driver.find_element(By.XPATH,
                              "//div[4]/div/div[2]/div[1]/div/div/ul/li[1]//p")
    p16.click()

    # 25. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 26. Click 'SELECT6'
    select6 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[1]/form//select")
    select6.click()

    # 27. Select the 'Internal' option in 'SELECT6'
    select6 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[1]/form//select")
    Select(select6).select_by_value("Internal")

    # 28. Click 'SELECT6'
    select6 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[1]/form//select")
    select6.click()

    # 29. Click 'Save8'
    save8 = driver.find_element(By.XPATH,
                                "//span[. = 'Save']")
    save8.click()

    # 30. Scroll window by ('0','-500')
    driver.execute_script("window.scrollBy(0,-500)")

    # 31. Does 'Saved' contain 'Saved'?
    saved = driver.find_element(By.XPATH,
                                "//div[. = 'Saved']")
    step_output = saved.text
    assert step_output and ("Saved" in step_output)

    # 32. Is 'DIV4' present?
    div4 = driver.find_element(By.XPATH,
                               "//div[3]/div[1]/div/div/div[1]/h1/div[2]")

    # 33. Get text from 'INPUT16'
    # item code captured in draft status
    input16 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[1]//input")
    step_output = input16.get_attribute("value")

    # 34. Click 'Quality Inspection2'
    quality_inspection2 = driver.find_element(By.XPATH,
                                              "//a[. = 'Quality Inspection']")
    quality_inspection2.click()
    time.sleep(1)

    # 35. Click 'INPUT83'
    input83 = driver.find_element(By.XPATH,
                                  "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script( "arguments[0].click();", input83 )

    # 36. Click 'Actions7'
    actions7 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]//span[. = 'Actions']")
    actions7.click()

    # 37. Click 'Edit1'
    edit1 = driver.find_element(By.XPATH,
                                "//a[. = '\n\t\t\t\tEdit']")
    edit1.click()

    # 38. Click 'SELECT7'
    select7 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form/div[2]//select")
    select7.click()

    # 39. Select the 'Rejected' option in 'SELECT7'
    select7 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form/div[2]//select")
    Select(select7).select_by_value("Rejected")

    # 40. Click 'SELECT7'
    select7 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form/div[2]//select")
    select7.click()

    # 41. Click 'Update'
    update = driver.find_element(By.XPATH,
                                 "//button[. = 'Update']")
    update.click()

    # 42. Does 'Updated successfully' contain 'Updated successfully'?
    updated_successfully = driver.find_element(By.XPATH,
                                               "//div[. = 'Updated successfully']")
    step_output = updated_successfully.text
    assert step_output and ("Updated successfully" in step_output)

    # 43. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 44. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 45. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

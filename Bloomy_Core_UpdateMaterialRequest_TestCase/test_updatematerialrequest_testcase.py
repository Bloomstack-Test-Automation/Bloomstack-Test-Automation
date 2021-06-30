import time

from selenium.common.exceptions import NoSuchElementException
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
    Test: UpdateMaterialRequest_TestCase
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/27/2021, 03:45:49
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="UpdateMaterialRequest_TestCase")
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

    # 10. Type 'mat' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("mat")

    # 11. Click 'Material Request List1'
    material_request_list1 = driver.find_element(By.XPATH,
                                                 "//p[. = 'Material Request List']")
    material_request_list1.click()

    # 12. Is 'Material Request5' visible?
    material_request5 = driver.find_element(By.XPATH,
                                            "//div[. = 'Material Request']")
    assert material_request5.is_displayed()
    time.sleep(2)

    # 13. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 14. Is 'DIV47' present?
    div47 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")

    # 15. Click 'INPUT73'
    input73 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[1]/div/div[2]/div/input")
    input73.click()

    # 16. Click 'path5'
    path5 = driver.find_element(By.XPATH,
                                "(//div[@class='datepicker--nav-action'])[2]")
    driver.execute_script("arguments[0].click();", path5)

    # 17. Click 'path5'
    path5 = driver.find_element(By.XPATH,
                                "(//div[@class='datepicker--nav-action'])[2]")
    driver.execute_script("arguments[0].click();", path5)

    # 18. Click '307'
    _307 = driver.find_element(By.XPATH,
                               "//div[34][. = '30']")
    _307.click()

    # 19. Click 'INPUT74'
    input74 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[2]//input")
    input74.click()

    # 20. Type 'vap' in 'INPUT74'
    input74 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[2]//input")
    input74.send_keys("vap")

    # 21. Click 'VapeCo18'
    vapeco18 = driver.find_element(By.XPATH,
                                   "//li[. = 'VapeCo']")
    vapeco18.click()

    # 22. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 23. Click 'DIV48'
    div48 = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div48.click()

    # 24. Click 'P59'
    p59 = driver.find_element(By.XPATH,
                              "//div[1]/div/div/div/ul/li[1]/a/p")
    p59.click()

    # 25. Click 'Save20'
    save20 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    save20.click()

    # 26. Scroll window by ('0','-300')
    driver.execute_script("window.scrollBy(0,-300)")

    # 27. Click 'Close3'
    close3 = driver.find_element(By.XPATH,
                                 "//span[. = 'Close']")
    close3.click()

    # 28. Does 'Saved9' contain 'Saved'?
    saved9 = driver.find_element(By.XPATH,
                                 "//div[. = 'Saved']")
    step_output = saved9.text
    assert step_output and ("Saved" in step_output)

    # 29. Is 'DIV47' visible?
    div47 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    assert div47.is_displayed()

    # 30. Click 'Material Request3'
    material_request3 = driver.find_element(By.XPATH,
                                            "//li[2]/a[. = 'Material Request']")
    material_request3.click()
    time.sleep(2)

    # 31. Click 'INPUT81'
    input81 = driver.find_element(By.XPATH,
                                  "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script("arguments[0].click();", input81)

    # 32. Click 'SPAN8'
    span8 = driver.find_element(By.XPATH,
                                "//div[2]/div[1]/div/div/div[2]/div[2]/button/span/span[2]")
    span8.click()

    # 33. Click 'Edit'
    edit = driver.find_element(By.XPATH,
                               "//a[. = '\n\t\t\t\tEdit']")
    edit.click()

    # 34. Click 'SELECT12'
    select12 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select12.click()

    # 35. Select the 'Purpose' option in 'SELECT12'
    select12 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    Select(select12).select_by_value("Purpose")

    # 36. Click 'SELECT12'
    select12 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select12.click()

    # 37. Click 'SELECT22'
    select22 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form/div[2]//select")
    select22.click()

    # 38. Select the 'Material Transfer' option in 'SELECT22'
    select22 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form/div[2]//select")
    Select(select22).select_by_value("Material Transfer")

    # 39. Click 'SELECT22'
    select22 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form/div[2]//select")
    select22.click()

    # 40. Click 'Update1'
    update1 = driver.find_element(By.XPATH,
                                  "//button[. = 'Update']")
    update1.click()

    # 41. Click 'Close7'
    close7 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div//span[. = 'Close']")
    close7.click()

    # 42. Does 'Updated successfully1' contain 'Updated successfully'?
    updated_successfully1 = driver.find_element(By.XPATH,
                                                "//div[. = 'Updated successfully']")
    step_output = updated_successfully1.text
    assert step_output and ("Updated successfully" in step_output)

    try:
        eleme =driver.find_element(By.XPATH,
                                   "//div[2]/div/div//button[. = '\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\tClose\n\t\t\t\t\t\t\t\t']")
        if eleme.is_displayed() and eleme.is_enabled():
            eleme.click()  # this will click the element if it is there
            # print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
    except NoSuchElementException:
        print("No such Element")

    # 43. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 44. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 45. Is 'Login' present?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
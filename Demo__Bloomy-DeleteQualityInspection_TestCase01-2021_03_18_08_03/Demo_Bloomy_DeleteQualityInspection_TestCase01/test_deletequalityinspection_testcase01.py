from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Demo_ Bloomy
    Package: TestProject.Generated.Tests.DemoBloomy
    Test: DeleteQualityInspection_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/18/2021, 08:03:47
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="DeleteQualityInspection_TestCase01")
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

    # 4. Type 'rahul.prakash@extrapreneursindia.com' in 'Email Address'
    email_address = driver.find_element(By.CSS_SELECTOR,
                                        "#login_email")
    email_address.send_keys("rahul.prakash@extrapreneursindia.com")

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

    # 8. Click 'Stock'
    stock = driver.find_element(By.XPATH,
                                "//div[. = '\n                Stock\n              ']")
    stock.click()

    # 9. Does 'Stock1' contain 'Stock'?
    stock1 = driver.find_element(By.XPATH,
                                 "//div[. = 'Stock']")
    step_output = stock1.text
    assert step_output and ("Stock" in step_output)

    # 10. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 11. Type 'quality ins' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("quality ins")

    # 12. Click 'New Quality Inspection2'
    new_quality_inspection2 = driver.find_element(By.XPATH,
                                                  "//li[. = 'New Quality Inspection']")
    new_quality_inspection2.click()

    # 13. Click 'SELECT1'
    select1 = driver.find_element(By.XPATH,
                                  "//div[3]//select")
    select1.click()

    # 14. Select the 'Incoming' option in 'SELECT1'
    select1 = driver.find_element(By.XPATH,
                                  "//div[3]//select")
    Select(select1).select_by_value("Incoming")

    # 15. Click 'SELECT1'
    select1 = driver.find_element(By.XPATH,
                                  "//div[3]//select")
    select1.click()

    # 16. Click 'INPUT11'
    input11 = driver.find_element(By.XPATH,
                                  "//div[4]/div//input")
    input11.click()

    # 17. Click 'VC-RM-FO-00011'
    vc_rm_fo_00011 = driver.find_element(By.XPATH,
                                         "//strong[. = 'VC-RM-FO-0001']")
    vc_rm_fo_00011.click()

    # 18. Click 'INPUT12'
    input12 = driver.find_element(By.XPATH,
                                  "//div[5]/div/div[2]//input")
    input12.click()

    # 19. Type '4.00' in 'INPUT12'
    input12 = driver.find_element(By.XPATH,
                                  "//div[5]/div/div[2]//input")
    input12.send_keys("4.00")

    # 20. Click 'SELECT2'
    select2 = driver.find_element(By.XPATH,
                                  "//div[7]//select")
    select2.click()

    # 21. Select the 'Internal' option in 'SELECT2'
    select2 = driver.find_element(By.XPATH,
                                  "//div[7]//select")
    Select(select2).select_by_value("Internal")

    # 22. Click 'SELECT2'
    select2 = driver.find_element(By.XPATH,
                                  "//div[7]//select")
    select2.click()

    # 23. Click 'Edit in full page'
    edit_in_full_page = driver.find_element(By.XPATH,
                                            "//button[. = 'Edit in full page']")
    edit_in_full_page.click()

    # 24. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 25. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 26. Click 'INPUT13'
    input13 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[4]//input")
    input13.click()

    # 27. Click 'P4'
    p4 = driver.find_element(By.XPATH,
                             "//div[3]/div/div[1]/form/div[4]/div/div[2]/div[1]/div/div/ul/li[1]//p")
    p4.click()

    # 28. Does 'New Quality Inspection 1' contain 'New Quality Inspection 1'?
    new_quality_inspection_1 = driver.find_element(By.XPATH,
                                                   "//div[. = 'New Quality Inspection 1']")
    step_output = new_quality_inspection_1.text
    assert step_output and ("New Quality Inspection 1" in step_output)

    # 29. Click 'Save3'
    save3 = driver.find_element(By.XPATH,
                                "//span[. = 'Save']")
    save3.click()

    # 30. Scroll window by ('0','-200')
    driver.execute_script("window.scrollBy(0,-200)")

    # 31. Does 'Saved' contain 'Saved'?
    saved = driver.find_element(By.XPATH,
                                "//div[. = 'Saved']")
    step_output = saved.text
    assert step_output and ("Saved" in step_output)

    # 32. Does 'DIV4' contain '[NONE]'?
    div4 = driver.find_element(By.XPATH,
                               "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div4.text
    assert step_output and ("" in step_output)

    # 33. Click 'Quality Inspection'
    quality_inspection = driver.find_element(By.XPATH,
                                             "//li/a[. = 'Quality Inspection']")
    quality_inspection.click()

    # 34. Click 'INPUT17'
    input17 = driver.find_element(By.XPATH,
                                  "//div[2]/div[2]/div[1]/div[1]/div/input")
    input17.click()

    # 35. Click 'SPAN1'
    span1 = driver.find_element(By.XPATH,
                                "//div[4]/div[1]/div/div/div[2]/div[2]/button/span/span[2]")
    span1.click()

    # 36. Click 'Delete2'
    delete2 = driver.find_element(By.XPATH,
                                  "//a[. = '\n\t\t\t\tDelete']")
    delete2.click()

    # 37. Click 'Yes'
    yes = driver.find_element(By.XPATH,
                              "//button[. = 'Yes']")
    yes.click()

    # 38. Does '20 of 142' contain '20 of 142'?
    _20_of_142 = driver.find_element(By.XPATH,
                                     "//span/span[. = '20 of 142']")
    step_output = _20_of_142.text
    assert step_output and ("20 of 142" in step_output)

    # 39. Click 'R
    # 		           Settings'
    r_settings = driver.find_element(By.XPATH,
                                     "//a[. = '     \n\t\t\t\n\t\t\t\tR\n\t\t           Settings     ']")
    r_settings.click()

    # 40. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()
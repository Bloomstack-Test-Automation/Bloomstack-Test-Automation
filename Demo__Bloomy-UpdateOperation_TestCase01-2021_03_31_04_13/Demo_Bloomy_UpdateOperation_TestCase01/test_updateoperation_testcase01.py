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
    Test: UpdateOperation_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/31/2021, 04:13:00
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="UpdateOperation_TestCase01")
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
    ApplicationURL = "https://epitest-demo.bloomstack.io"

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

    # 8. Click 'Manufacturing'
    manufacturing = driver.find_element(By.XPATH,
                                        "//div[. = '\n                Manufacturing\n              ']")
    manufacturing.click()

    # 9. Does 'Manufacturing4' contain 'Manufacturing'?
    manufacturing4 = driver.find_element(By.XPATH,
                                         "//div[. = 'Manufacturing']")
    step_output = manufacturing4.text
    assert step_output and ("Manufacturing" in step_output)

    # 10. Click 'Operation'
    operation = driver.find_element(By.XPATH,
                                    "//a[. = 'Operation']")
    operation.click()

    # 11. Does 'Operation3' contain 'Operation'?
    operation3 = driver.find_element(By.XPATH,
                                     "//div[. = 'Operation']")
    step_output = operation3.text
    assert step_output and ("Operation" in step_output)

    # 12. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 13. Does 'New Operation' contain 'New Operation'?
    new_operation = driver.find_element(By.XPATH,
                                        "//h4[. = 'New Operation']")
    step_output = new_operation.text
    assert step_output and ("New Operation" in step_output)

    # 14. Click 'Edit in full page'
    edit_in_full_page = driver.find_element(By.XPATH,
                                            "//button[. = 'Edit in full page']")
    edit_in_full_page.click()

    # 15. Click 'INPUT54'
    input54 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div/form/div[1]//input")
    input54.click()

    # 16. Type 'Update Operation' in 'INPUT54'
    input54 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div/form/div[1]//input")
    input54.send_keys("Update Operation")

    # 17. Click 'TEXTAREA1'
    textarea1 = driver.find_element(By.XPATH,
                                    "//textarea")
    textarea1.click()

    # 18. Type 'Hi All Updated' in 'TEXTAREA1'
    textarea1 = driver.find_element(By.XPATH,
                                    "//textarea")
    textarea1.send_keys("Hi All Updated")

    # 19. Click 'Save'
    save = driver.find_element(By.XPATH,
                               "//span[. = 'Save']")
    save.click()

    # 20. Does 'Saved10' contain 'Saved'?
    saved10 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved10.text
    assert step_output and ("Saved" in step_output)

    # 21. Click 'Operation2'
    operation2 = driver.find_element(By.XPATH,
                                     "//li/a[. = 'Operation']")
    operation2.click()

    # 22. Click 'INPUT11'
    input11 = driver.find_element(By.XPATH,
                                  "//div[2]/div[2]/div[1]/div[1]/div/input")
    input11.click()

    # 23. Click 'SPAN'
    span = driver.find_element(By.XPATH,
                               "//div[3]/div[1]/div/div/div[2]/div[2]/button/span[1]")
    span.click()

    # 24. Click 'Edit'
    edit = driver.find_element(By.XPATH,
                               "//a[. = '\n\t\t\t\tEdit']")
    edit.click()

    # 25. Click 'SELECT15'
    select15 = driver.find_element(By.XPATH,
                                   "//div[2]/div/select")
    select15.click()

    # 26. Select the 'Description' option in 'SELECT15'
    select15 = driver.find_element(By.XPATH,
                                   "//div[2]/div/select")
    Select(select15).select_by_value("Description")

    # 27. Click 'SELECT15'
    select15 = driver.find_element(By.XPATH,
                                   "//div[2]/div/select")
    select15.click()

    # 28. Click 'TEXTAREA2'
    textarea2 = driver.find_element(By.XPATH,
                                    "//div[2]/div/div[2]//textarea")
    textarea2.click()

    # 29. Type 'Updated ' in 'TEXTAREA2'
    textarea2 = driver.find_element(By.XPATH,
                                    "//div[2]/div/div[2]//textarea")
    textarea2.send_keys("Updated ")

    # 30. Click 'Update'
    update = driver.find_element(By.XPATH,
                                 "//button[. = 'Update']")
    update.click()

    # 31. Does 'Updated successfully3' contain 'Updated successfully'?
    updated_successfully3 = driver.find_element(By.XPATH,
                                                "//div[. = 'Updated successfully']")
    step_output = updated_successfully3.text
    assert step_output and ("Updated successfully" in step_output)

    # 32. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 33. Click 'Update Operation'
    update_operation = driver.find_element(By.XPATH,
                                           "//a[. = '\n\t\t\t\tUpdate Operation\n\t\t\t\t']")
    update_operation.click()

    # 34. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 35. Click 'R
    # 		           Settings'
    r_settings = driver.find_element(By.XPATH,
                                     "//a[. = '     \n\t\t\t\n\t\t\t\tR\n\t\t           Settings     ']")
    r_settings.click()

    # 36. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 37. Scroll window by ('0','-200')
    driver.execute_script("window.scrollBy(0,-200)")
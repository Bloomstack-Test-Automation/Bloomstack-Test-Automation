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
    Project: Demo_ Bloomy
    Package: TestProject.Generated.Tests.DemoBloomy
    Test: UpdateWorkOrder_TestCase02
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/16/2021, 04:53:43
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="UpdateWorkOrder_TestCase02")
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

    # 8. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 9. Type 'item' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("item")

    # 10. Click 'New Item'
    new_item = driver.find_element(By.XPATH,
                                   "//p[. = 'New Item']")
    new_item.click()

    # 11. Click 'INPUT22'
    input22 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]//input")
    input22.click()

    # 12. Type 'Test2' in 'INPUT22'
    input22 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]//input")
    input22.send_keys("Test2")

    # 13. Click 'INPUT23'
    input23 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]//input")
    input23.click()

    # 14. Type 'Test2' in 'INPUT23'
    input23 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]//input")
    input23.send_keys("Test2")

    # 15. Click 'INPUT24'
    input24 = driver.find_element(By.XPATH,
                                  "//div[5]//input")
    input24.click()

    # 16. Click 'All Item Groups'
    all_item_groups = driver.find_element(By.XPATH,
                                          "//li[. = 'All Item Groups']")
    all_item_groups.click()

    # 17. Click 'Save4'
    save4 = driver.find_element(By.XPATH,
                                "//button[. = 'Save']")
    save4.click()
    time.sleep(3)

    # 18. Click 'Save11'
    save11 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    save11.click()

    # 19. Does 'Saved24' contain 'Saved'?
    saved24 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved24.text
    assert step_output and ("Saved" in step_output)

    # 20. Does 'Test2' contain 'Test2'?
    test2 = driver.find_element(By.XPATH,
                                "//h1//div[. = 'Test2']")
    step_output = test2.text
    assert step_output and ("Test2" in step_output)

    # 21. Click 'I5'
    i5 = driver.find_element(By.XPATH,
                             "//div[1]/div[1]/div[1]/button/i")
    i5.click()

    # 22. Click 'INPUT25'
    input25 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[2]//input")
    input25.click()

    # 23. Type 'Bom-Test2' in 'INPUT25'
    input25 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[2]//input")
    input25.send_keys("Bom-Test2")

    # 24. Click 'INPUT26'
    input26 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[4]//input")
    input26.click()

    # 25. Type 'va' in 'INPUT26'
    input26 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[4]//input")
    input26.send_keys("va")

    # 26. Click 'VapeCo3'
    vapeco3 = driver.find_element(By.XPATH,
                                  "//p[. = 'VapeCo']")
    vapeco3.click()

    # 27. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 28. Scroll window by ('0','400')
    driver.execute_script("window.scrollBy(0,400)")

    # 29. Click 'Add Row'
    add_row = driver.find_element(By.XPATH,
                                  "//div[6]//button[. = '\n\t\t\t\t\t\t\tAdd Row']")
    add_row.click()

    # 30. Click 'DIV10'
    div10 = driver.find_element(By.XPATH,
                                "//div[3]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div10.click()

    # 31. Click 'Item Code3'
    item_code3 = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Item Code']")
    item_code3.click()

    # 32. Click 'VC-RM-FO-0001'
    vc_rm_fo_0001 = driver.find_element(By.XPATH,
                                        "//strong[. = 'VC-RM-FO-0001']")
    vc_rm_fo_0001.click()

    # 33. Click 'Save5'
    save5 = driver.find_element(By.XPATH,
                                "//div[3]//button[. = 'Save']")
    save5.click()

    # 34. Scroll window by ('0','-600')
    driver.execute_script("window.scrollBy(0,-600)")

    # 35. Does 'Saved12' contain 'Saved'?
    saved12 = driver.find_element(By.XPATH,
                                  "//div[3]/div[. = 'Saved']")
    step_output = saved12.text
    assert step_output and ("Saved" in step_output)

    # 36. Does 'Bom-Test2' contain 'Bom-Test2'?
    bom_test2 = driver.find_element(By.XPATH,
                                    "//h1//div[. = 'Bom-Test2']")
    step_output = bom_test2.text
    assert step_output and ("Bom-Test2" in step_output)

    # 37. Click 'Submit2'
    submit2 = driver.find_element(By.XPATH,
                                  "//span[. = 'Submit']")
    submit2.click()

    # 38. Click 'Yes1'
    yes1 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes1.click()

    # 39. Does 'Saved25' contain 'Saved'?
    saved25 = driver.find_element(By.XPATH,
                                  "//div[4]/div[. = 'Saved']")
    step_output = saved25.text
    assert step_output and ("Saved" in step_output)

    # 40. Click 'Create3'
    create3 = driver.find_element(By.XPATH,
                                  "//button[. = '\t\t\t\tCreate ']")
    create3.click()

    # 41. Click 'Work Order5'
    work_order5 = driver.find_element(By.XPATH,
                                      "//div[2]/div[1]/div[1]/div/ul//a[. = 'Work Order']")
    work_order5.click()

    # 42. Click 'Create'
    create = driver.find_element(By.XPATH,
                                 "//button[. = 'Create']")
    create.click()

    # 43. Scroll window by ('0','400')
    driver.execute_script("window.scrollBy(0,400)")

    # 44. Scroll window by ('0','400')
    driver.execute_script("window.scrollBy(0,400)")

    # 45. Click 'Save12'
    save12 = driver.find_element(By.XPATH,
                                 "//div[4]//button[2][. = 'Save']")
    save12.click()

    # 46. Scroll window by ('0','-800')
    driver.execute_script("window.scrollBy(0,-800)")

    # 47. Does 'Saved22' contain 'Saved'?
    saved22 = driver.find_element(By.XPATH,
                                  "//div[5]/div[. = 'Saved']")
    step_output = saved22.text
    assert step_output and ("Saved" in step_output)

    # 48. Click 'Submit5'
    submit5 = driver.find_element(By.XPATH,
                                  "//div[4]//button[. = 'Submit']")
    submit5.click()

    # 49. Click 'Yes3'
    yes3 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes3.click()

    # 50. Does 'Saved23' contain 'Saved'?
    saved23 = driver.find_element(By.XPATH,
                                  "//div[6]/div[. = 'Saved']")
    step_output = saved23.text
    assert step_output and ("Saved" in step_output)

    # 51. Click 'Work Order4'
    work_order4 = driver.find_element(By.XPATH,
                                      "//li[2]/a[. = 'Work Order']")
    work_order4.click()

    # 52. Click 'INPUT34'
    input34 = driver.find_element(By.XPATH,
                                  "//div[2]/div[2]/div[1]/div[1]/div/input")
    input34.click()

    # 53. Click 'Actions2'
    actions2 = driver.find_element(By.XPATH,
                                   "//div[5]//button[. = '               Actions                            ']")
    actions2.click()

    # 54. Click 'Edit'
    edit = driver.find_element(By.XPATH,
                               "//a[. = '\n\t\t\t\tEdit']")
    edit.click()

    # 55. Click 'SELECT5'
    select5 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select5.click()

    # 56. Select the 'Expected Delivery Date' option in 'SELECT5'
    select5 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    Select(select5).select_by_value("Expected Delivery Date")

    # 57. Click 'SELECT5'
    select5 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select5.click()

    # 58. Click 'INPUT35'
    input35 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div/div[2]/div/input")
    input35.click()

    # 59. Click '301'
    _301 = driver.find_element(By.XPATH,
                               "//div[4]//div[. = '30']")
    _301.click()

    # 60. Click 'Update'
    update = driver.find_element(By.XPATH,
                                 "//button[. = 'Update']")
    update.click()

    # 61. Does 'Updated successfully4' contain 'Updated successfully'?
    updated_successfully4 = driver.find_element(By.XPATH,
                                                "//div[. = 'Updated successfully']")
    step_output = updated_successfully4.text
    assert step_output and ("Updated successfully" in step_output)

    # 62. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 63. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

import time

from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Demo_ Bloomy
    Package: TestProject.Generated.Tests.DemoBloomy
    Test: CreateWorkOrder_TestCase02
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/15/2021, 12:51:28
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="CreateWorkOrder_TestCase02")
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

    # 7. Click 'FORM'
    form = driver.find_element(By.XPATH,
                               "//section[1]//form")
    form.click()

    # 8. Click 'Login1'
    login1 = driver.find_element(By.XPATH,
                                 "//button[. = '\n\t\t\t\tLogin']")
    login1.click()

    # 9. Click 'Manufacturing'
    manufacturing = driver.find_element(By.XPATH,
                                        "//div[. = '\n                Manufacturing\n              ']")
    manufacturing.click()

    # 10. Does 'Manufacturing1' contain 'Manufacturing'?
    manufacturing1 = driver.find_element(By.XPATH,
                                         "//div[. = 'Manufacturing']")
    step_output = manufacturing1.text
    assert step_output and ("Manufacturing" in step_output)

    # 11. Click 'Work Order'
    work_order = driver.find_element(By.XPATH,
                                     "//div[2]/div/a[. = 'Work Order']")
    work_order.click()

    # 12. Does 'Work Order1' contain 'Work Order'?
    work_order1 = driver.find_element(By.XPATH,
                                      "//div[. = 'Work Order']")
    step_output = work_order1.text
    assert step_output and ("Work Order" in step_output)
    time.sleep(2)

    # 13. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 14. Click 'Manufacturing2'
    manufacturing2 = driver.find_element(By.XPATH,
                                         "//a[. = 'Manufacturing']")
    manufacturing2.click()

    # 15. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 16. Type 'item' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("item")

    # 17. Click 'New Item1'
    new_item1 = driver.find_element(By.XPATH,
                                    "//li[. = 'New Item']")
    new_item1.click()

    # 18. Click 'INPUT30'
    input30 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div[1]/div[2]/div/div/div/form/div[3]//input")
    input30.click()

    # 19. Type 'Test EPI New' in 'INPUT30'
    input30 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div[1]/div[2]/div/div/div/form/div[3]//input")
    input30.send_keys("Test EPI New")

    # 20. Click 'INPUT31'
    input31 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div[1]/div[2]/div/div/div/form/div[4]//input")
    input31.click()

    # 21. Type 'Test EPI New' in 'INPUT31'
    input31 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div[1]/div[2]/div/div/div/form/div[4]//input")
    input31.send_keys("Test EPI New")

    # 22. Click 'INPUT32'
    input32 = driver.find_element(By.XPATH,
                                  "//div[5]/div/div[2]/div//input")
    input32.click()

    # 23. Click 'All Item Groups1'
    all_item_groups1 = driver.find_element(By.XPATH,
                                           "//strong[. = 'All Item Groups']")
    all_item_groups1.click()

    # 24. Click 'Save8'
    save8 = driver.find_element(By.XPATH,
                                "//button[3][. = 'Save']")
    save8.click()

    # 25. Does 'Test EPI New' contain 'Test EPI New'?
    test_epi_new = driver.find_element(By.XPATH,
                                       "//h1//div[. = 'Test EPI New']")
    step_output = test_epi_new.text
    assert step_output and ("Test EPI New" in step_output)

    # 26. Click '1'
    _1 = driver.find_element(By.XPATH,
                             "//div[1]/div[1]/div[1]/button[. = '        ']")
    _1.click()

    # 27. Click 'INPUT33'
    input33 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[4]//input")
    input33.click()

    # 28. Type 'vap' in 'INPUT33'
    input33 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[4]//input")
    input33.send_keys("vap")

    # 29. Click 'VapeCo3'
    vapeco3 = driver.find_element(By.XPATH,
                                  "//p[. = 'VapeCo']")
    vapeco3.click()
    time.sleep(2)

    # 30. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 31. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 32. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 33. Click 'Add Row1'
    add_row1 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div/form/div[3]//button[. = '\n\t\t\t\t\t\t\tAdd Row']")
    add_row1.click()

    # 34. Click 'DIV13'
    div13 = driver.find_element(By.XPATH,
                                "//div[3]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div13.click()

    # 35. Click 'VC-RM-FO-0001'
    vc_rm_fo_0001 = driver.find_element(By.XPATH,
                                        "//strong[. = 'VC-RM-FO-0001']")
    vc_rm_fo_0001.click()
    time.sleep(3)

    # 36. Click 'Save9'
    save9 = driver.find_element(By.XPATH,
                                "//div[6]//span[. = 'Save']")
    save9.click()

    # 37. Scroll window by ('0','-800')
    driver.execute_script("window.scrollBy(0,-800)")

    # 38. Does 'Saved17' contain 'Saved'?
    saved17 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved17.text
    assert step_output and ("Saved" in step_output)

    # 39. Click 'Submit1'
    submit1 = driver.find_element(By.XPATH,
                                  "//button/span[. = 'Submit']")
    submit1.click()

    # 40. Click 'Yes2'
    yes2 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes2.click()

    # 41. Does 'Saved18' contain 'Saved'?
    saved18 = driver.find_element(By.XPATH,
                                  "//div[3]/div[. = 'Saved']")
    step_output = saved18.text
    assert step_output and ("Saved" in step_output)

    # 42. Click 'Create2'
    create2 = driver.find_element(By.XPATH,
                                  "//button[. = '\t\t\t\tCreate ']")
    create2.click()

    # 43. Click 'Work Order7'
    work_order7 = driver.find_element(By.XPATH,
                                      "//div[2]/div[1]/div[1]/div/ul//a[. = 'Work Order']")
    work_order7.click()

    # 44. Click 'Create'
    create = driver.find_element(By.XPATH,
                                 "//button[. = 'Create']")
    create.click()

    # 45. Click 'Save6'
    save6 = driver.find_element(By.XPATH,
                                "//div[4]//span[. = 'Save']")
    save6.click()

    # 46. Does 'Saved19' contain 'Saved'?
    saved19 = driver.find_element(By.XPATH,
                                  "//div[4]/div[. = 'Saved']")
    step_output = saved19.text
    assert step_output and ("Saved" in step_output)

    # 47. Click 'Submit4'
    submit4 = driver.find_element(By.XPATH,
                                  "//div[4]//span[. = 'Submit']")
    submit4.click()

    # 48. Click 'Yes4'
    yes4 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes4.click()

    # 49. Does 'Saved20' contain 'Saved'?
    saved20 = driver.find_element(By.XPATH,
                                  "//div[5]/div[. = 'Saved']")
    step_output = saved20.text
    assert step_output and ("Saved" in step_output)

    # 50. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 51. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

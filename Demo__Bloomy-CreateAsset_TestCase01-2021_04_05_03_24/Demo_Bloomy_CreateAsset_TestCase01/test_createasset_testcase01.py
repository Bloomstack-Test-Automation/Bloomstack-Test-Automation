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
    Test: CreateAsset_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 04/05/2021, 03:24:46
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="CreateAsset_TestCase01")
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

    # 8. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 9. Type 'Asset' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("Asset")

    # 10. Click 'New Asset1'
    new_asset1 = driver.find_element(By.XPATH,
                                     "//span[. = 'New Asset']")
    new_asset1.click()

    # 11. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/form/div[1]//input")
    input.click()

    # 12. Type 'vap' in 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/form/div[1]//input")
    input.send_keys("vap")

    # 13. Click 'VapeCo1'
    vapeco1 = driver.find_element(By.XPATH,
                                  "//li[. = 'VapeCo']")
    vapeco1.click()
    time.sleep(2)

    # 14. Click 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form/div[3]//input")
    input1.click()

    # 15. Type 'EPI Tester1' in 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form/div[3]//input")
    input1.send_keys("EPI Tester1")

    # 16. Click 'INPUT3'
    input3 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[2]/div[1]/div/div/input")
    input3.click()

    # 17. Click 'INPUT2'
    input2 = driver.find_element(By.XPATH,
                                 "//div[1]/form/div[4]//input")
    input2.click()

    # 18. Click 'LI'
    li = driver.find_element(By.XPATH,
                             "//div[2]/div[1]/div/div/ul/li[7]")
    li.click()

    # 19. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 20. Click 'INPUT4'
    input4 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[2]/form/div[5]//input")
    input4.click()

    # 21. Click 'svg'
    svg = driver.find_element(By.XPATH,
                              "//div[1]/nav/div[3]/*")
    svg.click()

    # 22. Click 'svg'
    svg = driver.find_element(By.XPATH,
                              "//div[1]/nav/div[3]/*")
    svg.click()

    # 23. Click '30'
    _30 = driver.find_element(By.XPATH,
                              "//div[32][. = '30']")
    _30.click()

    # 24. Click 'INPUT5'
    input5 = driver.find_element(By.XPATH,
                                 "//div[2]/form/div[8]//input")
    input5.click()

    # 25. Click 'MAT-PRE-2020-00128'
    mat_pre_2020_00128 = driver.find_element(By.XPATH,
                                             "//strong[. = 'MAT-PRE-2020-00128']")
    mat_pre_2020_00128.click()

    # 26. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 27. Does 'New Asset 11' contain 'New Asset 1'?
    new_asset_11 = driver.find_element(By.XPATH,
                                       "//div[. = 'New Asset 1']")
    step_output = new_asset_11.text
    assert step_output and ("New Asset 1" in step_output)

    # 28. Click 'Save'
    save = driver.find_element(By.XPATH,
                               "//span[. = 'Save']")
    save.click()

    # 29. Scroll window by ('0','-300')
    driver.execute_script("window.scrollBy(0,-300)")

    # 30. Does 'Saved' contain 'Saved'?
    saved = driver.find_element(By.XPATH,
                                "//div[. = 'Saved']")
    step_output = saved.text
    assert step_output and ("Saved" in step_output)

    # 31. Does 'Draft' contain 'Draft'?
    draft = driver.find_element(By.XPATH,
                                "//span/span[. = 'Draft']")
    step_output = draft.text
    assert step_output and ("Draft" in step_output)

    # 32. Click 'Submit'
    submit = driver.find_element(By.XPATH,
                                 "//span[. = 'Submit']")
    submit.click()

    # 33. Click 'Yes'
    yes = driver.find_element(By.XPATH,
                              "//button[. = 'Yes']")
    yes.click()

    # 34. Click 'Close'
    close = driver.find_element(By.XPATH,
                                "//span[. = 'Close']")
    close.click()

    # 35. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 36. Scroll window by ('0','-100')
    driver.execute_script("window.scrollBy(0,-100)")

    # 37. Click 'Submit1'
    submit1 = driver.find_element(By.XPATH,
                                  "//span[. = 'Submit']")
    submit1.click()

    # 38. Click 'Yes1'
    yes1 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes1.click()

    # 39. Scroll window by ('0','-84')
    driver.execute_script("window.scrollBy(0,-84)")

    # 40. Click 'DIV1'
    div1 = driver.find_element(By.XPATH,
                               "//div[7]/div[2]/div/div[2]")
    div1.click()

    # 41. Does 'Available for use date is required' contain 'Available for use date is required'?
    available_for_use_date_is_required = driver.find_element(By.XPATH,
                                                             "//div/div/div[2]/div/div[. = 'Available for use date is required']")
    step_output = available_for_use_date_is_required.text
    assert step_output and (
        "Available for use date is required" in step_output)

    # 42. Click 'Close1'
    close1 = driver.find_element(By.XPATH,
                                 "//button[. = '\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\tClose\n\t\t\t\t\t\t\t\t']")
    close1.click()

    # 43. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 44. Scroll window by ('0','400')
    driver.execute_script("window.scrollBy(0,400)")

    # 45. Click 'I'
    i = driver.find_element(By.XPATH,
                            "//a[2]/i")
    i.click()

    # 46. Scroll window by ('0','128')
    driver.execute_script("window.scrollBy(0,128)")

    # 47. Scroll window by ('0','-600')
    driver.execute_script("window.scrollBy(0,-600)")

    # 48. Click 'INPUT6'
    input6 = driver.find_element(By.XPATH,
                                 "//div[4]/div/div[1]/form/div[2]//input")
    input6.click()

    # 49. Click 'INPUT6'
    input6 = driver.find_element(By.XPATH,
                                 "//div[4]/div/div[1]/form/div[2]//input")
    input6.click()

    # 50. Click 'svg1'
    svg1 = driver.find_element(By.XPATH,
                               "//div[2]/nav/div[3]/*")
    svg1.click()

    # 51. Click 'svg1'
    svg1 = driver.find_element(By.XPATH,
                               "//div[2]/nav/div[3]/*")
    svg1.click()

    # 52. Click 'svg1'
    svg1 = driver.find_element(By.XPATH,
                               "//div[2]/nav/div[3]/*")
    svg1.click()

    # 53. Click '10'
    _10 = driver.find_element(By.XPATH,
                              "//div[2]/div//div[. = '10']")
    _10.click()

    # 54. Click 'Save1'
    save1 = driver.find_element(By.XPATH,
                                "//button[. = 'Save']")
    save1.click()

    # 55. Scroll window by ('0','-828')
    driver.execute_script("window.scrollBy(0,-828)")

    # 56. Does 'Saved1' contain 'Saved'?
    saved1 = driver.find_element(By.XPATH,
                                 "//div[2]/div[. = 'Saved']")
    step_output = saved1.text
    assert step_output and ("Saved" in step_output)

    # 57. Click 'Submit1'
    submit1 = driver.find_element(By.XPATH,
                                  "//span[. = 'Submit']")
    submit1.click()

    # 58. Click 'Yes1'
    yes1 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes1.click()

    # 59. Does 'Saved2' contain 'Saved'?
    saved2 = driver.find_element(By.XPATH,
                                 "//div[3]/div[. = 'Saved']")
    step_output = saved2.text
    assert step_output and ("Saved" in step_output)

    # 60. Does 'Submitted' contain 'Submitted'?
    submitted = driver.find_element(By.XPATH,
                                    "//span/span[. = 'Submitted']")
    step_output = submitted.text
    assert step_output and ("Submitted" in step_output)

    # 61. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 62. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

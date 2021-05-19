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
    Test: CreateAssetMovement_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 04/06/2021, 03:31:34
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="CreateAssetMovement_TestCase01")
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

    # 9. Type 'new asset' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("new asset")

    # 10. Click 'New Asset Movement1'
    new_asset_movement1 = driver.find_element(By.XPATH,
                                              "//span[. = 'New Asset Movement']")
    new_asset_movement1.click()

    # 11. Does 'New Asset Movement 1' contain 'New Asset Movement 1'?
    new_asset_movement_1 = driver.find_element(By.XPATH,
                                               "//div[. = 'New Asset Movement 1']")
    step_output = new_asset_movement_1.text
    assert step_output and ("New Asset Movement 1" in step_output)

    # 12. Click 'INPUT18'
    input18 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/div/div/input")
    input18.click()

    # 13. Type 'vap' in 'INPUT18'
    input18 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/div/div/input")
    input18.send_keys("vap")

    # 14. Click 'VapeCo2'
    vapeco2 = driver.find_element(By.XPATH,
                                  "//p[. = 'VapeCo']")
    vapeco2.click()

    # 15. Click 'INPUT19'
    input19 = driver.find_element(By.XPATH,
                                  "//form/div/div/div[2]/div/input")
    input19.click()

    # 16. Click 'svg3'
    svg3 = driver.find_element(By.XPATH,
                               "//div[3]/*[name()='svg']")
    svg3.click()

    # 17. Click 'svg3'
    svg3 = driver.find_element(By.XPATH,
                               "//div[3]/*[name()='svg']")
    svg3.click()

    # 18. Click '26'
    _26 = driver.find_element(By.XPATH,
                              "//div[. = '26']")
    _26.click()

    # 19. Click 'SELECT1'
    select1 = driver.find_element(By.XPATH,
                                  "//div[2]/div/select")
    select1.click()

    # 20. Select the 'Transfer' option in 'SELECT1'
    select1 = driver.find_element(By.XPATH,
                                  "//div[2]/div/select")
    Select(select1).select_by_value("Transfer")

    # 21. Click 'SELECT1'
    select1 = driver.find_element(By.XPATH,
                                  "//div[2]/div/select")
    select1.click()

    # 22. Click 'DIV4'
    div4 = driver.find_element(By.XPATH,
                               "//form/div/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div4.click()

    # 23. Click 'Assets2'
    assets2 = driver.find_element(By.XPATH,
                                  "//a[. = 'Assets']")
    assets2.click()

    # 24. Click 'Asset2'
    asset2 = driver.find_element(By.XPATH,
                                 "//div/a[. = 'Asset']")
    asset2.click()
    time.sleep(2)

    # 25. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//button[. = 'New']")
    new.click()

    # 26. Click 'INPUT20'
    input20 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[3]//input")
    input20.click()

    # 27. Type 'Rahul Tester' in 'INPUT20'
    input20 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[3]//input")
    input20.send_keys("Rahul Tester1")

    # 28. Click 'INPUT21'
    input21 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[2]/div/div[2]/div[1]/div//input")
    input21.click()

    # 29. Click 'india4'
    india4 = driver.find_element(By.XPATH,
                                 "//p[. = 'india']")
    india4.click()

    # 30. Click 'INPUT22'
    input22 = driver.find_element(By.XPATH,
                                  "//div[1]/form/div[4]//input")
    input22.click()

    # 31. Click 'P4'
    p4 = driver.find_element(By.XPATH,
                             "//div[2]/div[1]/div/div/ul/li[7]//p")
    p4.click()

    # 32. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 33. Click 'INPUT23'
    input23 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/form/div[5]//input")
    input23.click()

    # 34. Click 'svg1'
    svg1 = driver.find_element(By.XPATH,
                               "//div[2]/nav/div[3]/*")
    svg1.click()

    # 35. Click 'svg1'
    svg1 = driver.find_element(By.XPATH,
                               "//div[2]/nav/div[3]/*")
    svg1.click()

    # 36. Click 'svg1'
    svg1 = driver.find_element(By.XPATH,
                               "//div[2]/nav/div[3]/*")
    svg1.click()

    # 37. Click '16'
    _16 = driver.find_element(By.XPATH,
                              "//div[2]/div//div[. = '16']")
    _16.click()

    # 38. Click 'INPUT24'
    input24 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[8]//input")
    input24.click()

    # 39. Click 'MAT-PRE-2020-00128'
    mat_pre_2020_00128 = driver.find_element(By.XPATH,
                                             "//strong[. = 'MAT-PRE-2020-00128']")
    mat_pre_2020_00128.click()

    # 40. Does 'New Asset 13' contain 'New Asset 1'?
    new_asset_13 = driver.find_element(By.XPATH,
                                       "//div[. = 'New Asset 1']")
    step_output = new_asset_13.text
    assert step_output and ("New Asset 1" in step_output)

    # 41. Click 'Save3'
    save3 = driver.find_element(By.XPATH,
                                "//div[5]//span[. = 'Save']")
    save3.click()

    # 42. Scroll window by ('0','-200')
    driver.execute_script("window.scrollBy(0,-200)")

    # 43. Does 'Saved' contain 'Saved'?
    saved = driver.find_element(By.XPATH,
                                "//div[. = 'Saved']")
    step_output = saved.text
    assert step_output and ("Saved" in step_output)

    # 44. Does 'Draft1' contain 'Draft'?
    draft1 = driver.find_element(By.XPATH,
                                 "//span/span[. = 'Draft']")
    step_output = draft1.text
    assert step_output and ("Draft" in step_output)

    # 45. Click 'Submit3'
    submit3 = driver.find_element(By.XPATH,
                                  "//button/span[. = 'Submit']")
    submit3.click()

    # 46. Click 'Yes'
    yes = driver.find_element(By.XPATH,
                              "//button[. = 'Yes']")
    yes.click()

    # 47. Does 'Available for use date is required' contain 'Available for use date is required'?
    available_for_use_date_is_required = driver.find_element(By.XPATH,
                                                             "//div/div/div[2]/div/div[. = 'Available for use date is required']")
    step_output = available_for_use_date_is_required.text
    assert step_output and (
        "Available for use date is required" in step_output)

    # 48. Click 'Close'
    close = driver.find_element(By.XPATH,
                                "//span[. = 'Close']")
    close.click()

    # 49. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 50. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 51. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 52. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 53. Click 'INPUT25'
    input25 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[1]/form/div[2]//input")
    input25.click()

    # 54. Click 'svg4'
    svg4 = driver.find_element(By.XPATH,
                               "//div[3]/nav/div[3]/*")
    svg4.click()

    # 55. Click 'svg4'
    svg4 = driver.find_element(By.XPATH,
                               "//div[3]/nav/div[3]/*")
    svg4.click()

    # 56. Click '24'
    _24 = driver.find_element(By.XPATH,
                              "//div[3]//div[. = '24']")
    _24.click()

    # 57. Click 'Save3'
    save3 = driver.find_element(By.XPATH,
                                "//div[5]//span[. = 'Save']")
    save3.click()

    # 58. Scroll window by ('0','-700')
    driver.execute_script("window.scrollBy(0,-700)")

    # 59. Does 'Saved1' contain 'Saved'?
    saved1 = driver.find_element(By.XPATH,
                                 "//div[2]/div[. = 'Saved']")
    step_output = saved1.text
    assert step_output and ("Saved" in step_output)

    # 60. Click 'Submit3'
    submit3 = driver.find_element(By.XPATH,
                                  "//button/span[. = 'Submit']")
    submit3.click()

    # 61. Click 'Yes4'
    yes4 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes4.click()

    # 62. Does 'Saved4' contain 'Saved'?
    saved4 = driver.find_element(By.XPATH,
                                 "//div[3]/div[. = 'Saved']")
    step_output = saved4.text
    assert step_output and ("Saved" in step_output)

    # 63. Click 'I1'
    i1 = driver.find_element(By.XPATH,
                             "//div[2]/div/div/button/i")
    i1.click()

    # 64. Click 'SELECT2'
    select2 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]//select")
    select2.click()

    # 65. Select the 'Transfer' option in 'SELECT2'
    select2 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]//select")
    Select(select2).select_by_value("Transfer")

    # 66. Click 'SELECT2'
    select2 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]//select")
    select2.click()

    # 67. Click 'INPUT26'
    input26 = driver.find_element(By.XPATH,
                                  "//div[2]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[2]/div/div[2]//input")
    input26.click()

    # 68. Click '303'
    _303 = driver.find_element(By.XPATH,
                               "//div[1]/div[1]/div/div/div[32][. = '30']")
    _303.click()

    # 69. Scroll window by ('0','21')
    driver.execute_script("window.scrollBy(0,21)")

    # 70. Click 'DIV6'
    div6 = driver.find_element(By.XPATH,
                               "//div[2]/div[2]/div[1]/div/div/div[5]")
    div6.click()

    # 71. Click 'india5'
    india5 = driver.find_element(By.XPATH,
                                 "//div[1]/div/div/div/ul//p[. = 'india']")
    india5.click()

    # 72. Click 'From Employee'
    from_employee = driver.find_element(By.XPATH,
                                        "//input[@placeholder = 'From Employee']")
    from_employee.click()

    # 73. Click 'Save4'
    save4 = driver.find_element(By.XPATH,
                                "//span[. = 'Save']")
    save4.click()

    # 74. Scroll window by ('0','-21')
    driver.execute_script("window.scrollBy(0,-21)")

    # 75. Does 'Saved5' contain 'Saved'?
    saved5 = driver.find_element(By.XPATH,
                                 "//div[4]/div[. = 'Saved']")
    step_output = saved5.text
    assert step_output and ("Saved" in step_output)

    # 76. Does 'Asset Movement' contain 'Asset Movement'?
    asset_movement = driver.find_element(By.XPATH,
                                         "//li/a[. = 'Asset Movement']")
    step_output = asset_movement.text
    assert step_output and ("Asset Movement" in step_output)

    # 77. Click 'Submit4'
    submit4 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]//span[. = 'Submit']")
    submit4.click()

    # 78. Click 'Yes1'
    yes1 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes1.click()

    # 79. Does 'DIV7' contain '[NONE]'?
    div7 = driver.find_element(By.XPATH,
                               "//div[5]/div/div[5]")
    step_output = div7.text
    assert step_output and ("" in step_output)

    # 80. Does 'Submitted1' contain 'Submitted'?
    submitted1 = driver.find_element(By.XPATH,
                                     "//div[2]/div[1]/div/div/div[1]/h1/div[2]/span/span[. = 'Submitted']")
    step_output = submitted1.text
    assert step_output and ("Submitted" in step_output)

    # 81. Click 'R
    # 		           Settings'
    r_settings = driver.find_element(By.XPATH,
                                     "//a[. = '     \n\t\t\t\n\t\t\t\tR\n\t\t           Settings     ']")
    r_settings.click()

    # 82. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()
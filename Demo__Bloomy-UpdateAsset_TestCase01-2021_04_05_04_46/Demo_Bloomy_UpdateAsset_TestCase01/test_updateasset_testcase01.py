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
    Test: UpdateAsset_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 04/05/2021, 04:46:46
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="UpdateAsset_TestCase01")
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

    # 10. Click 'New Asset3'
    new_asset3 = driver.find_element(By.XPATH,
                                     "//span[. = 'New Asset']")
    new_asset3.click()

    # 11. Does 'New Asset 11' contain 'New Asset 1'?
    new_asset_11 = driver.find_element(By.XPATH,
                                       "//div[. = 'New Asset 1']")
    step_output = new_asset_11.text
    assert step_output and ("New Asset 1" in step_output)

    # 12. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/form/div[1]//input")
    input.click()

    # 13. Type 'vap' in 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/form/div[1]//input")
    input.send_keys("vap")

    # 14. Click 'VapeCo2'
    vapeco2 = driver.find_element(By.XPATH,
                                  "//p[. = 'VapeCo']")
    vapeco2.click()

    # 15. Click 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form/div[3]//input")
    input1.click()

    # 16. Type 'Updated' in 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form/div[3]//input")
    input1.send_keys("Updated")

    # 17. Click 'INPUT3'
    input3 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[2]/div[1]/div/div/input")
    input3.click()

    # 18. Click 'india'
    india = driver.find_element(By.XPATH,
                                "//strong[. = 'india']")
    india.click()

    # 19. Click 'INPUT2'
    input2 = driver.find_element(By.XPATH,
                                 "//div[1]/form/div[4]//input")
    input2.click()

    # 20. Click 'P2'
    p2 = driver.find_element(By.XPATH,
                             "//div/div/div/ul/li[7]//p")
    p2.click()

    # 21. Click 'INPUT4'
    input4 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[2]/form/div[5]//input")
    input4.click()

    # 22. Click 'svg'
    svg = driver.find_element(By.XPATH,
                              "//div[1]/nav/div[3]/*")
    svg.click()

    # 23. Click 'svg'
    svg = driver.find_element(By.XPATH,
                              "//div[1]/nav/div[3]/*")
    svg.click()

    # 24. Click '30'
    _30 = driver.find_element(By.XPATH,
                              "//div[32][. = '30']")
    _30.click()

    # 25. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 26. Click 'INPUT5'
    input5 = driver.find_element(By.XPATH,
                                 "//div[2]/form/div[8]//input")
    input5.click()

    # 27. Click 'MAT-PRE-2020-00128'
    mat_pre_2020_00128 = driver.find_element(By.XPATH,
                                             "//strong[. = 'MAT-PRE-2020-00128']")
    mat_pre_2020_00128.click()

    # 28. Click 'Save1'
    save1 = driver.find_element(By.XPATH,
                                "//button[. = 'Save']")
    save1.click()

    # 29. Scroll window by ('0','-200')
    driver.execute_script("window.scrollBy(0,-200)")

    # 30. Does 'Saved3' contain 'Saved'?
    saved3 = driver.find_element(By.XPATH,
                                 "//div[. = 'Saved']")
    step_output = saved3.text
    assert step_output and ("Saved" in step_output)

    # 31. Click 'Asset'
    asset = driver.find_element(By.XPATH,
                                "//li[2]/a[. = 'Asset']")
    asset.click()

    # 32. Does 'Asset1' contain 'Asset'?
    asset1 = driver.find_element(By.XPATH,
                                 "//div[. = 'Asset']")
    step_output = asset1.text
    assert step_output and ("Asset" in step_output)

    # 33. Click 'INPUT7'
    input7 = driver.find_element(By.XPATH,
                                 "//div[2]/div[2]/div[1]/div[1]/div/input")
    input7.click()

    # 34. Click 'SPAN'
    span = driver.find_element(By.XPATH,
                               "//div[3]/div[1]/div/div/div[2]/div[2]/button/span[1]")
    span.click()

    # 35. Click 'Edit'
    edit = driver.find_element(By.XPATH,
                               "//a[. = '\n\t\t\t\tEdit']")
    edit.click()

    # 36. Click 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select.click()

    # 37. Select the 'Asset Name' option in 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    Select(select).select_by_value("Asset Name")

    # 38. Click 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select.click()

    # 39. Click 'INPUT16'
    input16 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//input")
    input16.click()

    # 40. Type 'Updated01' in 'INPUT16'
    input16 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//input")
    input16.send_keys("Updated01")

    # 41. Click 'Update'
    update = driver.find_element(By.XPATH,
                                 "//button[. = 'Update']")
    update.click()

    # 42. Does 'Updated successfully1' contain 'Updated successfully'?
    updated_successfully1 = driver.find_element(By.XPATH,
                                                "//div[. = 'Updated successfully']")
    step_output = updated_successfully1.text
    assert step_output and ("Updated successfully" in step_output)

    # 43. Does 'DIV2' contain '[NONE]'?
    div2 = driver.find_element(By.XPATH,
                               "//div[3]/div[2]/div[2]/div/div[1]/div[1]")
    step_output = div2.text
    assert step_output and ("" in step_output)

    # 44. Click 'R
    # 		           Settings'
    r_settings = driver.find_element(By.XPATH,
                                     "//a[. = '     \n\t\t\t\n\t\t\t\tR\n\t\t           Settings     ']")
    r_settings.click()

    # 45. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()
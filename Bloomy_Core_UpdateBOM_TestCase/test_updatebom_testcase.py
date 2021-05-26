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
    Test: UpdateBOM_TestCase
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/26/2021, 12:46:28
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="UpdateBOM_TestCase")
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
    ApplicationURL = "https://epitest-demo.bloomstack.io"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Does 'Login' contain 'Login'?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    step_output = login.text
    assert step_output and ("Login" in step_output)

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

    # 10. Type 'bom' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("bom")

    # 11. Click 'BOM List'
    bom_list = driver.find_element(By.XPATH,
                                   "//li[. = 'BOM List']")
    bom_list.click()

    # 12. Is 'BOM2' visible?
    bom2 = driver.find_element(By.XPATH,
                               "//div[. = 'BOM']")
    assert bom2.is_displayed()
    time.sleep(2)

    # 13. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 14. Click 'INPUT25'
    input25 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[2]//input")
    input25.click()

    # 15. Type 'EPI Update' in 'INPUT25'
    input25 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[2]//input")
    input25.send_keys("EPI Update")

    # 16. Click 'INPUT73'
    input73 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[3]//input")
    input73.click()

    # 17. Click 'VC-RM-FO-000112'
    vc_rm_fo_000112 = driver.find_element(By.XPATH,
                                          "//strong[. = 'VC-RM-FO-0001']")
    vc_rm_fo_000112.click()

    # 18. Click 'INPUT74'
    input74 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]/div[1]/div//input")
    input74.click()

    # 19. Type 'vap' in 'INPUT74'
    input74 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]/div[1]/div//input")
    input74.send_keys("vap")

    # 20. Click 'VapeCo8'
    vapeco8 = driver.find_element(By.XPATH,
                                  "//li[. = 'VapeCo']")
    vapeco8.click()

    # 21. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 22. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 23. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 24. Click 'DIV10'
    div10 = driver.find_element(By.XPATH,
                                "//div[3]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div10.click()

    # 25. Click 'VC-RM-FO-00014'
    vc_rm_fo_00014 = driver.find_element(By.XPATH,
                                         "//div[1]/div/div/div/ul//strong[. = 'VC-RM-FO-0001']")
    vc_rm_fo_00014.click()

    # 26. Does 'DIV48' contain '[NONE]'?
    div48 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div48.text
    assert step_output and ("" in step_output)

    # 27. Get text from 'Item Code1'
    # captured item not saved
    item_code1 = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Item Code']")
    step_output = item_code1.get_attribute("value")

    # 28. Click 'Save31'
    save31 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    save31.click()

    # 29. Scroll window by ('0','-600')
    driver.execute_script("window.scrollBy(0,-600)")

    # 30. Does 'Saved' contain 'Saved'?
    saved = driver.find_element(By.XPATH,
                                "//div[. = 'Saved']")
    step_output = saved.text
    assert step_output and ("Saved" in step_output)

    # 31. Does 'DIV48' contain '[NONE]'?
    div48 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div48.text
    assert step_output and ("" in step_output)

    # 32. Click 'BOM1'
    bom1 = driver.find_element(By.XPATH,
                               "//li/a[. = 'BOM']")
    bom1.click()
    time.sleep(2)

    # 33. Click 'INPUT107'
    input107 = driver.find_element(By.XPATH,
                                   "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script( "arguments[0].click();", input107 )

    # 34. Click 'SPAN16'
    span16 = driver.find_element(By.XPATH,
                                 "//div[2]/div[1]/div/div/div[2]/div[2]/button/span[1]")
    span16.click()

    # 35. Click 'Edit'
    edit = driver.find_element(By.XPATH,
                               "//a[. = '\n\t\t\t\tEdit']")
    edit.click()

    # 36. Click 'SELECT1'
    select1 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select1.click()

    # 37. Select the 'Currency' option in 'SELECT1'
    select1 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    Select(select1).select_by_value("Currency")

    # 38. Click 'SELECT1'
    select1 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select1.click()

    # 39. Click 'INPUT5'
    input5 = driver.find_element(By.XPATH,
                                 "//div[2]/div[1]/div/div[2]/div/div/div/form//input")
    input5.click()

    # 40. Click 'USD1'
    usd1 = driver.find_element(By.XPATH,
                               "//p[. = 'USD']")
    usd1.click()

    # 41. Click 'Update1'
    update1 = driver.find_element(By.XPATH,
                                  "//button[. = 'Update']")
    update1.click()

    # 42. Does 'Updated successfully1' contain 'Updated successfully'?
    updated_successfully1 = driver.find_element(By.XPATH,
                                                "//div[. = 'Updated successfully']")
    step_output = updated_successfully1.text
    assert step_output and ("Updated successfully" in step_output)

    # 43. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 44. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 45. Does 'Cannabis Vapour Pen' contain 'Cannabis Vapour Pen'?
    cannabis_vapour_pen = driver.find_element(By.XPATH,
                                              "//h1[1][. = 'Cannabis Vapour Pen']")
    step_output = cannabis_vapour_pen.text
    assert step_output and ("Cannabis Vapour Pen" in step_output)



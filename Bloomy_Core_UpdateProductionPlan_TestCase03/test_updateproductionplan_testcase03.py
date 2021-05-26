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
    Test: UpdateProductionPlan_TestCase03
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/26/2021, 10:32:44
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="UpdateProductionPlan_TestCase03")
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

    # 2. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

    # 3. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

    # 4. Click 'Login'
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    login.click()

    # 5. Click 'Email Address'
    email_address = driver.find_element(By.CSS_SELECTOR,
                                        "#login_email")
    email_address.click()

    # 6. Type 'testautomationuser@bloomstack.com' in 'Email Address'
    email_address = driver.find_element(By.CSS_SELECTOR,
                                        "#login_email")
    email_address.send_keys("testautomationuser@bloomstack.com")

    # 7. Click 'Password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#login_password")
    password.click()

    # 8. Type 'epi@123' in 'Password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#login_password")
    password.send_keys("epi@123")

    # 9. Click 'Login1'
    login1 = driver.find_element(By.XPATH,
                                 "//button[. = '\n\t\t\t\tLogin']")
    login1.click()

    # 10. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 11. Type 'production' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("production")

    # 12. Click 'Production Plan List2'
    production_plan_list2 = driver.find_element(By.XPATH,
                                                "//span[. = 'Production Plan List']")
    production_plan_list2.click()

    # 13. Does 'Production Plan6' contain 'Production Plan'?
    production_plan6 = driver.find_element(By.XPATH,
                                           "//div[. = 'Production Plan']")
    step_output = production_plan6.text
    assert step_output and ("Production Plan" in step_output)
    time.sleep(2)

    # 14. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 15. Does 'DIV48' contain '[NONE]'?
    div48 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div48.text
    assert step_output and ("" in step_output)

    # 16. Click 'INPUT84'
    input84 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form//input")
    input84.click()

    # 17. Type 'vap' in 'INPUT84'
    input84 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form//input")
    input84.send_keys("vap")

    # 18. Click 'VapeCo21'
    vapeco21 = driver.find_element(By.XPATH,
                                   "//p[. = 'VapeCo']")
    vapeco21.click()

    # 19. Get text from 'INPUT84'
    # captured company Name status Not saved
    input84 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form//input")
    step_output = input84.get_attribute("value")

    # 20. Click 'DIV107'
    div107 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[2]/div[2]/div//div[3]")
    div107.click()

    # 21. Click 'VC-RM-FO-00019'
    vc_rm_fo_00019 = driver.find_element(By.XPATH,
                                         "//strong[. = 'VC-RM-FO-0001']")
    vc_rm_fo_00019.click()

    # 22. Click 'Planned Qty'
    planned_qty = driver.find_element(By.XPATH,
                                      "//input[@placeholder = 'Planned Qty']")
    planned_qty.click()

    # 23. Type '1.00' in 'Planned Qty'
    planned_qty = driver.find_element(By.XPATH,
                                      "//input[@placeholder = 'Planned Qty']")
    planned_qty.send_keys("1.00")

    # 24. Click 'For Warehouse'
    for_warehouse = driver.find_element(By.XPATH,
                                        "//input[@placeholder = 'For Warehouse']")
    for_warehouse.click()

    # 25. Click 'Flow Kana - Ship to HF  - VC6'
    flow_kana_ship_to_hf_vc6 = driver.find_element(By.XPATH,
                                                   "//strong[. = 'Flow Kana - Ship to HF  - VC']")
    flow_kana_ship_to_hf_vc6.click()

    # 26. Click 'Save31'
    save31 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    save31.click()

    # 27. Does 'Saved10' contain 'Saved'?
    saved10 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved10.text
    assert step_output and ("Saved" in step_output)

    # 28. Does 'DIV48' contain '[NONE]'?
    div48 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div48.text
    assert step_output and ("" in step_output)

    # 29. Get text from 'INPUT84'
    # Captured Company name after status changed to draft
    input84 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form//input")
    step_output = input84.get_attribute("value")

    # 30. Click 'Production Plan2'
    production_plan2 = driver.find_element(By.XPATH,
                                           "//li[2]/a[. = 'Production Plan']")
    production_plan2.click()
    time.sleep(1)

    # 31. Click 'INPUT107'
    input107 = driver.find_element(By.XPATH,
                                   "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script( "arguments[0].click();", input107 )

    # 32. Click 'Actions4'
    actions4 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]//span[. = 'Actions']")
    actions4.click()

    # 33. Click 'Edit'
    edit = driver.find_element(By.XPATH,
                               "//a[. = '\n\t\t\t\tEdit']")
    edit.click()

    # 34. Click 'SELECT2'
    select2 = driver.find_element(By.XPATH,
                                  "//div[1]/div/div[2]/div/select")
    select2.click()

    # 35. Select the 'Customer' option in 'SELECT2'
    select2 = driver.find_element(By.XPATH,
                                  "//div[1]/div/div[2]/div/select")
    Select(select2).select_by_value("Customer")

    # 36. Click 'SELECT2'
    select2 = driver.find_element(By.XPATH,
                                  "//div[1]/div/div[2]/div/select")
    select2.click()

    # 37. Click 'INPUT12'
    input12 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//input")
    input12.click()

    # 38. Click 'P12'
    p12 = driver.find_element(By.XPATH,
                              "//div[2]/div/div[2]/div[1]/div/div/ul/li[1]//p")
    p12.click()

    # 39. Click 'Update1'
    update1 = driver.find_element(By.XPATH,
                                  "//button[. = 'Update']")
    update1.click()

    # 40. Does 'Updated successfully3' contain 'Updated successfully'?
    updated_successfully3 = driver.find_element(By.XPATH,
                                                "//div[. = 'Updated successfully']")
    step_output = updated_successfully3.text
    assert step_output and ("Updated successfully" in step_output)

    # 41. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 42. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 43. Does 'Login' contain 'Login'?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    step_output = login.text
    assert step_output and ("Login" in step_output)

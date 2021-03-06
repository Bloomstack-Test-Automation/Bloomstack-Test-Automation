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
    Test: UpdateWorkOrder_TestCase
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/27/2021, 04:30:20
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="UpdateWorkOrder_TestCase")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Generated By:Rahul."""
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

    # 10. Type 'BOM' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("BOM")

    # 11. Click 'BOM List1'
    bom_list1 = driver.find_element(By.XPATH,
                                    "//span[. = 'BOM List']")
    bom_list1.click()

    # 12. Does 'BOM2' contain 'BOM'?
    bom2 = driver.find_element(By.XPATH,
                               "//div[. = 'BOM']")
    step_output = bom2.text
    assert step_output and ("BOM" in step_output)
    time.sleep(2)

    # 13. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 14. Does 'DIV106' contain '[NONE]'?
    div106 = driver.find_element(By.XPATH,
                                 "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div106.text
    assert step_output and ("" in step_output)

    # 15. Click 'INPUT73'
    input73 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[3]//input")
    input73.click()

    # 16. Click 'P21'
    p21 = driver.find_element(By.XPATH,
                              "//div/div/div/ul/li[1]/a/p")
    p21.click()

    # 17. Click 'INPUT74'
    input74 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]/div[1]/div//input")
    input74.click()

    # 18. Type 'vap' in 'INPUT74'
    input74 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]/div[1]/div//input")
    input74.send_keys("vap")

    # 19. Click 'VapeCo3'
    vapeco3 = driver.find_element(By.XPATH,
                                  "//p[. = 'VapeCo']")
    vapeco3.click()

    # 20. Scroll window by ('0','400')
    driver.execute_script("window.scrollBy(0,400)")

    # 21. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 22. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 23. Click 'DIV10'
    div10 = driver.find_element(By.XPATH,
                                "//div[3]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div10.click()

    # 24. Click 'Finished Oil, Dry Goods, Extracted Ja...4'
    finished_oil_dry_goods_extracted_ja_4 = driver.find_element(By.XPATH,
                                                                "//div[1]/div/div/div/ul//span[. = 'Finished Oil, Dry Goods, Extracted Jack Herer Cannabis Oil']")
    finished_oil_dry_goods_extracted_ja_4.click()

    # 25. Get text from 'Item Code1'
    # Captured Item 1
    item_code1 = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Item Code']")
    step_output = item_code1.get_attribute("value")

    # 26. Click 'Save31'
    save31 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    save31.click()

    # 27. Scroll window by ('0','-600')
    driver.execute_script("window.scrollBy(0,-600)")

    # 28. Does 'Saved' contain 'Saved'?
    saved = driver.find_element(By.XPATH,
                                "//div[. = 'Saved']")
    step_output = saved.text
    assert step_output and ("Saved" in step_output)

    # 29. Does 'DIV48' contain '[NONE]'?
    div48 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div48.text
    assert step_output and ("" in step_output)

    # 30. Click 'Submit15'
    submit15 = driver.find_element(By.XPATH,
                                   "//button/span[. = 'Submit']")
    submit15.click()

    # 31. Click 'Yes'
    yes = driver.find_element(By.XPATH,
                              "//button[. = 'Yes']")
    yes.click()

    # 32. Does 'Saved76' contain 'Saved'?
    saved76 = driver.find_element(By.XPATH,
                                  "//div[2]/div[. = 'Saved']")
    step_output = saved76.text
    assert step_output and ("Saved" in step_output)

    # 33. Does 'DIV48' contain '[NONE]'?
    div48 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div48.text
    assert step_output and ("" in step_output)

    # 34. Click 'Create8'
    create8 = driver.find_element(By.XPATH,
                                  "//button[. = '\t\t\t\tCreate ']")
    create8.click()

    # 35. Click 'Work Order8'
    work_order8 = driver.find_element(By.XPATH,
                                      "//div[2]/div[1]/div[1]/div/ul//a[. = 'Work Order']")
    work_order8.click()

    # 36. Click 'Create'
    create = driver.find_element(By.XPATH,
                                 "//button[. = 'Create']")
    create.click()

    # 37. Does 'DIV108' contain '[NONE]'?
    div108 = driver.find_element(By.XPATH,
                                 "//div[4]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div108.text
    assert step_output and ("" in step_output)

    # 38. Click 'Save'
    save = driver.find_element(By.XPATH,
                               "//span[. = 'Save']")
    save.click()

    # 39. Does 'Saved36' contain 'Saved'?
    saved36 = driver.find_element(By.XPATH,
                                  "//div[3]/div[. = 'Saved']")
    step_output = saved36.text
    assert step_output and ("Saved" in step_output)

    # 40. Does 'DIV25' contain '[NONE]'?
    div25 = driver.find_element(By.XPATH,
                                "//div[4]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div25.text
    assert step_output and ("" in step_output)

    # 41. Click 'Work Order4'
    work_order4 = driver.find_element(By.XPATH,
                                      "//li[2]/a[. = 'Work Order']")
    driver.execute_script( "arguments[0].click();", work_order4 )
    time.sleep(1)


    # 42. Click 'INPUT9'
    input9 = driver.find_element(By.XPATH,
                                 "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script( "arguments[0].click();", input9 )

    # 43. Click 'Actions2'
    actions2 = driver.find_element(By.XPATH,
                                   "//div[5]//button[. = '               Actions                            ']")
    actions2.click()

    # 44. Click 'Edit1'
    edit1 = driver.find_element(By.XPATH,
                                "//div[5]//a[. = '\n\t\t\t\tEdit']")
    edit1.click()

    # 45. Click 'SELECT18'
    select18 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select18.click()

    # 46. Select the 'Series' option in 'SELECT18'
    select18 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    Select(select18).select_by_value("Series")

    # 47. Click 'SELECT18'
    select18 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select18.click()

    # 48. Click 'Update'
    update = driver.find_element(By.XPATH,
                                 "//button[. = 'Update']")
    update.click()

    # 49. Does 'Updated successfully8' contain 'Updated successfully'?
    updated_successfully8 = driver.find_element(By.XPATH,
                                                "//div[. = 'Updated successfully']")
    step_output = updated_successfully8.text
    assert step_output and ("Updated successfully" in step_output)

    # 50. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 51. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 52. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

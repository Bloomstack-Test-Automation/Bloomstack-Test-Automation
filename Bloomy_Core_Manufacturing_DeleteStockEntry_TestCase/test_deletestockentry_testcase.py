import time

from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Bloomy_Core
    Package: TestProject.Generated.Tests.BloomyCore
    Test: DeleteStockEntry_TestCase
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/27/2021, 13:17:09
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="DeleteStockEntry_TestCase")
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
    ApplicationURL = "https://epitest-demo.bloomstack.io/"

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

    # 10. Type 'stock' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("stock")

    # 11. Click 'Stock Entry List2'
    stock_entry_list2 = driver.find_element(By.XPATH,
                                            "//p[. = 'Stock Entry List']")
    stock_entry_list2.click()

    # 12. Does 'Stock Entry4' contain 'Stock Entry'?
    stock_entry4 = driver.find_element(By.XPATH,
                                       "//div[. = 'Stock Entry']")
    step_output = stock_entry4.text
    assert step_output and ("Stock Entry" in step_output)
    time.sleep(2)

    # 13. Click 'New1'
    new1 = driver.find_element(By.XPATH,
                               "//span[. = 'New']")
    new1.click()

    # 14. Is 'DIV4' visible?
    div4 = driver.find_element(By.XPATH,
                               "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    assert div4.is_displayed()

    # 15. Click 'INPUT91'
    input91 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[3]//input")
    input91.click()

    # 16. Click 'Material Receipt2'
    material_receipt2 = driver.find_element(By.XPATH,
                                            "//p[. = 'Material Receipt']")
    material_receipt2.click()

    # 17. Click 'INPUT92'
    input92 = driver.find_element(By.XPATH,
                                  "//div[6]/div/div[2]//input")
    input92.click()

    # 18. Type 'vap' in 'INPUT92'
    input92 = driver.find_element(By.XPATH,
                                  "//div[6]/div/div[2]//input")
    input92.send_keys("vap")

    # 19. Click 'VapeCo6'
    vapeco6 = driver.find_element(By.XPATH,
                                  "//li[. = 'VapeCo']")
    vapeco6.click()

    # 20. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 21. Click 'DIV29'
    div29 = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div29.click()

    # 22. Click 'Flow Kana - Ship to HF  - VC'
    flow_kana_ship_to_hf_vc = driver.find_element(By.XPATH,
                                                  "//strong[. = 'Flow Kana - Ship to HF  - VC']")
    flow_kana_ship_to_hf_vc.click()

    # 23. Click 'Target Warehouse'
    target_warehouse = driver.find_element(By.XPATH,
                                           "//input[@placeholder = 'Target Warehouse']")
    target_warehouse.click()

    # 24. Click 'Work In Progress - VC6'
    work_in_progress_vc6 = driver.find_element(By.XPATH,
                                               "//div[3]/div[1]/div/div/div/ul/li[. = 'Work In Progress - VC']")
    work_in_progress_vc6.click()

    # 25. Click 'Qty'
    qty = driver.find_element(By.XPATH,
                              "//input[@placeholder = 'Qty']")
    qty.click()

    # 26. Type '1.00' in 'Qty'
    qty = driver.find_element(By.XPATH,
                              "//input[@placeholder = 'Qty']")
    qty.send_keys("1.00")

    # 27. Click 'Item Code2'
    item_code2 = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Item Code']")
    item_code2.click()

    # 28. Click 'Finished Oil, Dry Goods, Extracted Ja...3'
    finished_oil_dry_goods_extracted_ja_3 = driver.find_element(By.XPATH,
                                                                "//span[. = 'Finished Oil, Dry Goods, Extracted Jack Herer Cannabis Oil']")
    finished_oil_dry_goods_extracted_ja_3.click()
    time.sleep(2)

    # 29. Click 'Save8'
    save8 = driver.find_element(By.XPATH,
                                "//span[. = 'Save']")
    driver.execute_script("arguments[0].click();", save8)

    # 30. Scroll window by ('0','-300')
    driver.execute_script("window.scrollBy(0,-300)")

    # 31. Does 'Saved11' contain 'Saved'?
    saved11 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved11.text
    assert step_output and ("Saved" in step_output)

    # 32. Does 'Draft3' contain 'Draft'?
    draft3 = driver.find_element(By.XPATH,
                                 "//div/span[. = 'Draft']")
    step_output = draft3.text
    assert step_output and ("Draft" in step_output)

    # 33. Does 'DIV4' contain '[NONE]'?
    div4 = driver.find_element(By.XPATH,
                               "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div4.text
    assert step_output and ("" in step_output)

    # 34. Click 'Stock Entry3'
    stock_entry3 = driver.find_element(By.XPATH,
                                       "//li[2]/a[. = 'Stock Entry']")
    stock_entry3.click()
    time.sleep(2)

    # 35. Click 'INPUT83'
    input83 = driver.find_element(By.XPATH,
                                  "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script("arguments[0].click();", input83)

    # 36. Click 'Actions7'
    actions7 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]//span[. = 'Actions']")
    actions7.click()

    # 37. Click 'Delete2'
    delete2 = driver.find_element(By.XPATH,
                                  "//a[. = '\n\t\t\t\tDelete']")
    delete2.click()

    # 38. Does 'Delete 1 items permanently?' contain 'Delete 1 items permanently?'?
    delete_1_items_permanently_question_mark_ = driver.find_element(By.XPATH,
                                                                    "//p[. = 'Delete 1 items permanently?']")
    step_output = delete_1_items_permanently_question_mark_.text
    assert step_output and ("Delete 1 items permanently?" in step_output)

    # 39. Click 'Yes1'
    yes1 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes1.click()

    # 40. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 41. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 42. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

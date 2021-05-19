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
    Test: CreateStockEntry_TestCase02
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/24/2021, 03:51:34
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="CreateStockEntry_TestCase02")
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

    # 8. Click 'Stock5'
    stock5 = driver.find_element(By.XPATH,
                                 "//div[. = '\n                Stock\n              ']")
    stock5.click()

    # 9. Does 'Stock1' contain 'Stock'?
    stock1 = driver.find_element(By.XPATH,
                                 "//div[. = 'Stock']")
    step_output = stock1.text
    assert step_output and ("Stock" in step_output)

    # 10. Click 'Stock Entry'
    stock_entry = driver.find_element(By.XPATH,
                                      "//div/a[. = 'Stock Entry']")
    stock_entry.click()

    # 11. Does 'Stock Entry1' contain 'Stock Entry'?
    stock_entry1 = driver.find_element(By.XPATH,
                                       "//div[. = 'Stock Entry']")
    step_output = stock_entry1.text
    assert step_output and ("Stock Entry" in step_output)
    time.sleep(2)

    # 12. Click 'New1'
    new1 = driver.find_element(By.XPATH,
                               "//span[. = 'New']")
    new1.click()

    # 13. Does 'New Stock Entry 1' contain 'New Stock Entry 1'?
    new_stock_entry_1 = driver.find_element(By.XPATH,
                                            "//div[. = 'New Stock Entry 1']")
    step_output = new_stock_entry_1.text
    assert step_output and ("New Stock Entry 1" in step_output)

    # 14. Click 'INPUT47'
    input47 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[3]//input")
    input47.click()

    # 15. Click 'Material Issue1'
    material_issue1 = driver.find_element(By.XPATH,
                                          "//p[. = 'Material Issue']")
    material_issue1.click()

    # 16. Click 'INPUT48'
    input48 = driver.find_element(By.XPATH,
                                  "//div[6]/div/div[2]//input")
    input48.click()

    # 17. Type 'vap' in 'INPUT48'
    input48 = driver.find_element(By.XPATH,
                                  "//div[6]/div/div[2]//input")
    input48.send_keys("vap")

    # 18. Click 'VapeCo6'
    vapeco6 = driver.find_element(By.XPATH,
                                  "//li[. = 'VapeCo']")
    vapeco6.click()

    # 19. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 20. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 21. Click 'DIV20'
    div20 = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div20.click()

    # 22. Click 'Flow Kana - Ship to HF  - VC'
    flow_kana_ship_to_hf_vc = driver.find_element(By.XPATH,
                                                  "//strong[. = 'Flow Kana - Ship to HF  - VC']")
    flow_kana_ship_to_hf_vc.click()

    # 23. Click 'Target Warehouse'
    target_warehouse = driver.find_element(By.XPATH,
                                           "//input[@placeholder = 'Target Warehouse']")
    target_warehouse.click()

    # 24. Click 'DT warehouse - VC4'
    dt_warehouse_vc4 = driver.find_element(By.XPATH,
                                           "//div[3]/div[1]/div/div/div/ul/li[. = 'DT warehouse - VC']")
    dt_warehouse_vc4.click()

    # 25. Click 'Item Code2'
    item_code2 = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Item Code']")
    item_code2.click()

    # 26. Click 'Qty'
    qty = driver.find_element(By.XPATH,
                              "//input[@placeholder = 'Qty']")
    qty.click()

    # 27. Type '10.00' in 'Qty'
    qty = driver.find_element(By.XPATH,
                              "//input[@placeholder = 'Qty']")
    qty.send_keys("10.00")

    # 28. Click 'Item Code2'
    item_code2 = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Item Code']")
    item_code2.click()

    # 29. Click 'VC-RM-FO-00012'
    vc_rm_fo_00012 = driver.find_element(By.XPATH,
                                         "//strong[. = 'VC-RM-FO-0001']")
    vc_rm_fo_00012.click()
    time.sleep(3)

    # 30. Click 'Save1'
    save1 = driver.find_element(By.XPATH,
                                "//span[. = 'Save']")
    save1.click()

    # 31. Scroll window by ('0','-300')
    driver.execute_script("window.scrollBy(0,-300)")

    # 32. Does 'Saved12' contain 'Saved'?
    saved12 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved12.text
    assert step_output and ("Saved" in step_output)

    # 33. Does 'Draft' contain 'Draft'?
    draft = driver.find_element(By.XPATH,
                                "//span/span[. = 'Draft']")
    step_output = draft.text
    assert step_output and ("Draft" in step_output)

    # 34. Click 'Submit'
    submit = driver.find_element(By.XPATH,
                                 "//button/span[. = 'Submit']")
    submit.click()

    # 35. Click 'Yes1'
    yes1 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes1.click()

    # 36. Does 'Saved13' contain 'Saved'?
    saved13 = driver.find_element(By.XPATH,
                                  "//div[2]/div[. = 'Saved']")
    step_output = saved13.text
    assert step_output and ("Saved" in step_output)

    # 37. Does 'Submitted' contain 'Submitted'?
    submitted = driver.find_element(By.XPATH,
                                    "//span/span[. = 'Submitted']")
    step_output = submitted.text
    assert step_output and ("Submitted" in step_output)

    # 38. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 39. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

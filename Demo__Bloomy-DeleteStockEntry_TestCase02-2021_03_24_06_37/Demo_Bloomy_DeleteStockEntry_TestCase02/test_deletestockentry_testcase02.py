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
    Test: DeleteStockEntry_TestCase02
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/24/2021, 06:37:43
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="DeleteStockEntry_TestCase02")
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
    GridValue = "Does 20 of 586 Generic Web Element contain \"20 of 586\" ?"

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

    # 15. Click 'Material Issue2'
    material_issue2 = driver.find_element(By.XPATH,
                                          "//p[. = 'Material Issue']")
    material_issue2.click()

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

    # 19. Scroll window by ('0','400')
    driver.execute_script("window.scrollBy(0,400)")

    # 20. Click 'DIV20'
    div20 = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div20.click()

    # 21. Click 'DT warehouse - VC5'
    dt_warehouse_vc5 = driver.find_element(By.XPATH,
                                           "//li[. = 'DT warehouse - VC']")
    dt_warehouse_vc5.click()

    # 22. Click 'Target Warehouse'
    target_warehouse = driver.find_element(By.XPATH,
                                           "//input[@placeholder = 'Target Warehouse']")
    target_warehouse.click()

    # 23. Click 'Work In Progress - VC5'
    work_in_progress_vc5 = driver.find_element(By.XPATH,
                                               "//div[3]/div[1]/div/div/div/ul//strong[. = 'Work In Progress - VC']")
    work_in_progress_vc5.click()

    # 24. Click 'Qty'
    qty = driver.find_element(By.XPATH,
                              "//input[@placeholder = 'Qty']")
    qty.click()

    # 25. Type '10.00' in 'Qty'
    qty = driver.find_element(By.XPATH,
                              "//input[@placeholder = 'Qty']")
    qty.send_keys("10.00")

    # 26. Click 'Item Code2'
    item_code2 = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Item Code']")
    item_code2.click()

    # 27. Click 'Finished Oil, Dry Goods, Extracted Ja...1'
    finished_oil_dry_goods_extracted_ja_1 = driver.find_element(By.XPATH,
                                                                "//span[. = 'Finished Oil, Dry Goods, Extracted Jack Herer Cannabis Oil']")
    finished_oil_dry_goods_extracted_ja_1.click()

    # 28. Click 'Save'
    save = driver.find_element(By.XPATH,
                               "//button[. = 'Save']")
    save.click()

    # 29. Scroll window by ('0','-400')
    driver.execute_script("window.scrollBy(0,-400)")

    # 30. Does 'Saved12' contain 'Saved'?
    saved12 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved12.text
    assert step_output and ("Saved" in step_output)

    # 31. Click 'Stock Entry3'
    stock_entry3 = driver.find_element(By.XPATH,
                                       "//li[2]/a[. = 'Stock Entry']")
    stock_entry3.click()

    # 32. Click 'INPUT10'
    input10 = driver.find_element(By.XPATH,
                                  "//div[2]/div[2]/div[1]/div[1]/div/input")
    input10.click()

    # 33. Click 'SPAN6'
    span6 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[2]/div[2]/button/span/span[2]")
    span6.click()

    # 34. Click 'Delete2'
    delete2 = driver.find_element(By.XPATH,
                                  "//a[. = '\n\t\t\t\tDelete']")
    delete2.click()

    # 35. Click 'Yes1'
    yes1 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes1.click()

    # 36. Does '20 of 586' contain '20 of 586'?
    if float(f'{GridValue}') <= float("Does 20 of 586 Generic Web Element contain \"20 of 586\" ?"):
        _20_of_586 = driver.find_element(By.XPATH,
                                         "//span/span[. = '20 of 586']")
        step_output = _20_of_586.text
        assert step_output and ("20 of 586" in step_output)

    # 37. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 38. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

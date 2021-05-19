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
    Test: CreateProductionPlan_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/12/2021, 07:34:43
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="CreateProductionPlan_TestCase01")
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

    # 1. Run LoginTest
    test_main.test_main(driver)

    # 2. Click 'Manufacturing'
    manufacturing = driver.find_element(By.XPATH,
                                        "//div[. = '\n                Manufacturing\n              ']")
    manufacturing.click()

    # 3. Does 'Manufacturing1' contain 'Manufacturing'?
    manufacturing1 = driver.find_element(By.XPATH,
                                         "//div[. = 'Manufacturing']")
    step_output = manufacturing1.text
    assert step_output and ("Manufacturing" in step_output)

    # 4. Click 'Production Plan'
    production_plan = driver.find_element(By.XPATH,
                                          "//div/a[. = 'Production Plan']")
    production_plan.click()

    # 5. Does 'Production Plan3' contain 'Production Plan'?
    production_plan3 = driver.find_element(By.XPATH,
                                           "//div[. = 'Production Plan']")
    step_output = production_plan3.text
    assert step_output and ("Production Plan" in step_output)
    time.sleep(3)

    # 6. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 7. Click 'INPUT7'
    input7 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form//input")
    input7.click()

    # 8. Type 'extra' in 'INPUT7'
    input7 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form//input")
    input7.send_keys("extra")

    # 9. Click 'Extrapreneurs India Pvt Ltd4'
    extrapreneurs_india_pvt_ltd4 = driver.find_element(By.XPATH,
                                                       "//li[. = 'Extrapreneurs India Pvt Ltd']")
    extrapreneurs_india_pvt_ltd4.click()

    # 10. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 11. Click 'DIV2'
    div2 = driver.find_element(By.XPATH,
                               "//div[2]/div/div[2]/div[2]/div//div[3]")
    div2.click()

    # 12. Type 'pi' in 'Item Code2'
    item_code2 = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Item Code']")
    item_code2.send_keys("pi")

    # 13. Click 'P6'
    p6 = driver.find_element(By.XPATH,
                             "//div[1]/div/div/div/ul/li[1]/a/p[1]")
    p6.click()

    # 14. Click 'Planned Qty'
    planned_qty = driver.find_element(By.XPATH,
                                      "//input[@placeholder = 'Planned Qty']")
    planned_qty.click()

    # 15. Type '1.00' in 'Planned Qty'
    planned_qty = driver.find_element(By.XPATH,
                                      "//input[@placeholder = 'Planned Qty']")
    planned_qty.send_keys("1.00")

    # 16. Click 'For Warehouse'
    for_warehouse = driver.find_element(By.XPATH,
                                        "//input[@placeholder = 'For Warehouse']")
    for_warehouse.click()

    # 17. Click 'EPI-Warehouse2 - EIPL'
    epi_warehouse2_eipl = driver.find_element(By.XPATH,
                                              "//strong[. = 'EPI-Warehouse2 - EIPL']")
    epi_warehouse2_eipl.click()

    # 18. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 19. Scroll window by ('0','-200')
    driver.execute_script("window.scrollBy(0,-200)")

    # 20. Click 'Save1'
    save1 = driver.find_element(By.XPATH,
                                "//button[. = 'Save']")
    save1.click()

    # 21. Scroll window by ('0','-100')
    driver.execute_script("window.scrollBy(0,-100)")

    # 22. Does 'Saved10' contain 'Saved'?
    saved10 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved10.text
    assert step_output and ("Saved" in step_output)

    # 23. Click 'Submit'
    submit = driver.find_element(By.XPATH,
                                 "//button/span[. = 'Submit']")
    submit.click()

    # 24. Click 'Yes'
    yes = driver.find_element(By.XPATH,
                              "//button[. = 'Yes']")
    yes.click()

    # 25. Does 'Saved11' contain 'Saved'?
    saved11 = driver.find_element(By.XPATH,
                                  "//div[2]/div[. = 'Saved']")
    step_output = saved11.text
    assert step_output and ("Saved" in step_output)

    # 26. Run LogoutTest
    test_main.test_main(driver)
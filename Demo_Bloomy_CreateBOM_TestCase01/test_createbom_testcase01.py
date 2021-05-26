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
    Test: CreateBOM_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/11/2021, 04:44:57
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="CreateBOM_TestCase01")
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
    email_address.send_keys("testautomationuser@bloomstack.com")

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

    # 8. Click 'Manufacturing'
    manufacturing = driver.find_element(By.XPATH,
                                        "//div[. = '\n                Manufacturing\n              ']")
    manufacturing.click()

    # 9. Does 'Manufacturing1' contain 'Manufacturing'?
    manufacturing1 = driver.find_element(By.XPATH,
                                         "//div[. = 'Manufacturing']")
    step_output = manufacturing1.text
    assert step_output and ("Manufacturing" in step_output)

    # 10. Click 'Bill of Materials'
    bill_of_materials = driver.find_element(By.XPATH,
                                            "//div/a[. = 'Bill of Materials']")
    bill_of_materials.click()

    # 11. Does 'BOM' contain 'BOM'?
    bom = driver.find_element(By.XPATH,
                              "//div[. = 'BOM']")
    step_output = bom.text
    assert step_output and ("BOM" in step_output)
    time.sleep(3)

    # 12. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()
    time.sleep(2)

    # 13. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/div/div[1]/form/div[3]//input")
    input.click()

    # 14. Type 'epi' in 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/div/div[1]/form/div[3]//input")
    input.send_keys("epi")


    # 15. Click 'P2'
    p2 = driver.find_element(By.XPATH,
                             "//li[9]//p")
    p2.click()

    # 16. Click 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//div[4]/div/div[2]/div[1]/div/div/input")
    input1.click()

    # 17. Type 'extra' in 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//div[4]/div/div[2]/div[1]/div/div/input")
    input1.send_keys("extra")

    # 18. Click 'Extrapreneurs India Pvt Ltd'
    extrapreneurs_india_pvt_ltd = driver.find_element(By.XPATH,
                                                      "//strong[. = 'Extrapreneurs India Pvt Ltd']")
    extrapreneurs_india_pvt_ltd.click()

    # 19. Click 'INPUT2'
    input2 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form/div[2]//input")
    input2.click()

    # 20. Type 'EPI Test Data' in 'INPUT2'
    input2 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form/div[2]//input")
    input2.send_keys("EPI Test Data")

    # 21. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/div/div[1]/form/div[3]//input")
    input.click()

    # 22. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 23. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 24. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 25. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 26. Click 'DIV1'
    div1 = driver.find_element(By.XPATH,
                               "//div[3]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div1.click()

    # 27. Type 'epi' in 'Item Code'
    item_code = driver.find_element(By.XPATH,
                                    "//input[@placeholder = 'Item Code']")
    item_code.send_keys("epi")
    time.sleep(2)

    # 28. Click 'P3'
    p3 = driver.find_element(By.XPATH,
                             "//div[1]/div/div/div/ul/li[2]//p")
    p3.click()
    time.sleep(2)

    # 29. Click 'Save'
    save = driver.find_element(By.XPATH,
                               "//span[. = 'Save']")
    save.click()

    # 30. Scroll window by ('0','-700')
    driver.execute_script("window.scrollBy(0,-700)")

    # 31. Does 'Saved2' contain 'Saved'?
    saved2 = driver.find_element(By.XPATH,
                                 "//div[. = 'Saved']")
    step_output = saved2.text
    assert step_output and ("Saved" in step_output)

    # 32. Click 'Submit'
    submit = driver.find_element(By.XPATH,
                                 "//button/span[. = 'Submit']")
    submit.click()

    # 33. Click 'Yes'
    yes = driver.find_element(By.XPATH,
                              "//button[. = 'Yes']")
    yes.click()

    # 34. Does 'Saved3' contain 'Saved'?
    saved3 = driver.find_element(By.XPATH,
                                 "//div[7]/div[. = 'Saved']")
    step_output = saved3.text
    assert step_output and ("Saved" in step_output)

    # 33. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 34. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

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
    Test: DeleteBOM_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/11/2021, 07:50:59
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="DeleteBOM_TestCase01")
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
    time.sleep(3)

    # 13. Click 'INPUT2'
    input2 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form/div[2]//input")
    input2.click()

    # 14. Type 'EPI Delete' in 'INPUT2'
    input2 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form/div[2]//input")
    input2.send_keys("EPI Delete")

    # 15. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/div/div[1]/form/div[3]//input")
    input.click()

    # 16. Type 'epi' in 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/div/div[1]/form/div[3]//input")
    input.send_keys("epi")

    # 17. Click 'LI'
    li = driver.find_element(By.XPATH,
                             "//div[2]/div[1]/div/div/ul/li[3]")
    li.click()

    # 18. Click 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//div[4]/div/div[2]/div[1]/div/div/input")
    input1.click()

    # 19. Type 'extra' in 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//div[4]/div/div[2]/div[1]/div/div/input")
    input1.send_keys("extra")

    # 20. Click 'Extrapreneurs India Pvt Ltd2'
    extrapreneurs_india_pvt_ltd2 = driver.find_element(By.XPATH,
                                                       "//li[. = 'Extrapreneurs India Pvt Ltd']")
    extrapreneurs_india_pvt_ltd2.click()

    # 21. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 22. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 23. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 24. Click 'DIV1'
    div1 = driver.find_element(By.XPATH,
                               "//div[3]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div1.click()

    # 25. Type 'epi' in 'Item Code1'
    item_code1 = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Item Code']")
    item_code1.send_keys("epi")

    # 26. Click 'P3'
    p3 = driver.find_element(By.XPATH,
                             "//div[1]/div/div/div/ul/li[2]//p")
    p3.click()
    time.sleep(3)

    # 27. Click 'Save'
    save = driver.find_element(By.XPATH,
                               "//span[. = 'Save']")
    save.click()
    time.sleep(3)

    # 28. Scroll window by ('0','-800')
    driver.execute_script("window.scrollBy(0,-800)")

    # 29. Does 'Saved7' contain 'Saved'?
    saved7 = driver.find_element(By.XPATH,
                                 "//div[. = 'Saved']")
    step_output = saved7.text
    assert step_output and ("Saved" in step_output)

    # 30. Click 'BOM1'
    bom1 = driver.find_element(By.XPATH,
                               "//li/a[. = 'BOM']")
    bom1.click()
    time.sleep(2)

    # 31. Click 'INPUT3'
    input3 = driver.find_element(By.XPATH,
                                 "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script("arguments[0].click();", input3)


    # 32. Click 'SPAN1'
    span1 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[2]/div[2]/button/span/span[2]")
    span1.click()
    time.sleep( 3 )

    # 33. Click 'Delete'
    delete = driver.find_element(By.XPATH,
                                 "//a[. = '\n\t\t\t\tDelete']")
    delete.click()

    # 34. Click 'Yes'
    yes = driver.find_element(By.XPATH,
                              "//button[. = 'Yes']")
    yes.click()

    # 33. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 34. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()



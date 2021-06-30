from addons.random_data_generator import RandomDataGenerator
from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
from subtests import test_login
from subtests import test_logout
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Bloomy_Core
    Package: TestProject.Generated.Tests.BloomyCore
    Test: SalesPartner_TestCase
    Generated by: Meenal Kardale (meenal.kardale@extrapreneurs-india.com)
    Generated on 06/30/2021, 10:48:08
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="3J0RNM_48lLt_KM5Ab6s6A_HZzddmktVs_HhX77AjTM",
                              project_name="Bloomy_Core",
                              job_name="SalesPartner_TestCase")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """1) Go to Selling and click on sales partner.

    2) Enter sales partner  name, commision rate and add item group3) Click on save.
    """
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io/"
    ExpectedSalesPartnerName = ""
    username = ""
    pwd = ""
    Randomsalespartner = ""

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Login to the Application
    test_login.test_main(driver)

    # 3. Click 'Selling'
    selling = driver.find_element(By.XPATH,
                                  "//a[. = '\n                Selling\n              ']")
    selling.click()

    # 4. Click 'Sales Partner'
    sales_partner = driver.find_element(By.XPATH,
                                        "//a[. = 'Sales Partner']")
    sales_partner.click()

    # 5. Does 'Sales Partner1' contain 'Sales Partner'?
    sales_partner1 = driver.find_element(By.XPATH,
                                         "//div[. = 'Sales Partner']")
    step_output = sales_partner1.text
    assert step_output and ("Sales Partner" in step_output)

    # 6. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//button[. = 'New']")
    new.click()

    # 7. Click 'INPUT119'
    input119 = driver.find_element(By.XPATH,
                                   "//div[1]/form/div[2]/div/div[2]/div/input")
    input119.click()

    # 8. Generate random name
    step_output = driver.addons().execute(
        RandomDataGenerator.generatename(
        ))
    Randomsalespartner = step_output

    # 9. Type '{Randomsalespartner}' in 'INPUT119'
    input119 = driver.find_element(By.XPATH,
                                   "//div[1]/form/div[2]/div/div[2]/div/input")
    input119.send_keys(f'{Randomsalespartner}')

    # 10. Get text from 'INPUT119'
    input119 = driver.find_element(By.XPATH,
                                   "//div[1]/form/div[2]/div/div[2]/div/input")
    step_output = input119.get_attribute("value")
    ExpectedSalesPartnerName = step_output

    # 11. Click 'INPUT120'
    input120 = driver.find_element(By.XPATH,
                                   "//div[2]/div/div[2]/form//input")
    input120.click()

    # 12. Type '100.00' in 'INPUT120'
    input120 = driver.find_element(By.XPATH,
                                   "//div[2]/div/div[2]/form//input")
    input120.send_keys("100.00")

    # 13. Click 'INPUT121'
    input121 = driver.find_element(By.XPATH,
                                   "//form/div[3]//input")
    input121.click()

    # 14. Type 'agen' in 'INPUT121'
    input121 = driver.find_element(By.XPATH,
                                   "//form/div[3]//input")
    input121.send_keys("agen")

    # 15. Click 'Agent'
    agent = driver.find_element(By.XPATH,
                                "//li[. = 'Agent']")
    agent.click()

    # 16. Click 'INPUT111'
    input111 = driver.find_element(By.XPATH,
                                   "//div[4]/div/div[2]/div[1]/div/div/input")
    input111.click()

    # 17. Clear 'Clear' contents
    clear = driver.find_element(By.XPATH,
                                "//div[4]/div/div[2]/div[1]/div/div/input")
    clear.clear()

    # 18. Type 'los' in 'INPUT111'
    input111 = driver.find_element(By.XPATH,
                                   "//div[4]/div/div[2]/div[1]/div/div/input")
    input111.send_keys("los")

    # 19. Click 'P14'
    p14 = driver.find_element(By.XPATH,
                              "//div[4]/div/div[2]/div[1]/div/div/ul/li[1]//p")
    p14.click()

    # 20. Click 'Add Row1'
    add_row1 = driver.find_element(By.XPATH,
                                   "//button[. = '\n\t\t\t\t\t\t\tAdd Row']")
    add_row1.click()

    # 21. Click 'DIV43'
    div43 = driver.find_element(By.XPATH,
                                "//div[2]/div[2]/div[1]/div/div/div[6]")
    div43.click()

    # 22. Type ' test' in 'Target Distribution'
    target_distribution = driver.find_element(By.XPATH,
                                              "//input[@placeholder = 'Target Distribution']")
    target_distribution.send_keys(" test")

    # 23. Click 'testdis'
    testdis = driver.find_element(By.XPATH,
                                  "//div[6]/div[1]/div/div/div/ul/li[1]")
    testdis.click()

    # 24. Does 'New Sales Partner 1' contain 'New Sales Partner 1'?
    new_sales_partner_1 = driver.find_element(By.XPATH,
                                              "//div[. = 'New Sales Partner 1']")
    step_output = new_sales_partner_1.text
    assert step_output and ("New Sales Partner 1" in step_output)

    # 25. Does 'Not Saved' contain 'Not Saved'?
    not_saved = driver.find_element(By.XPATH,
                                    "//span/span[. = 'Not Saved']")
    step_output = not_saved.text
    assert step_output and ("Not Saved" in step_output)

    # 26. Click 'clicksabutton'
    clicksabutton = driver.find_element(By.XPATH,
                                        "//button[. = 'Save']")
    clicksabutton.click()

    # 27. Does 'Saved7' contain 'Saved'?
    saved7 = driver.find_element(By.XPATH,
                                 "//div[. = 'Saved']")
    step_output = saved7.text
    assert step_output and ("Saved" in step_output)

    # 28. Click 'clicksabutton'
    clicksabutton = driver.find_element(By.XPATH,
                                        "//button[. = 'Save']")
    clicksabutton.click()

    # 29. Click 'Sales Partner2'
    sales_partner2 = driver.find_element(By.XPATH,
                                         "//li/a[. = 'Sales Partner']")
    sales_partner2.click()

    # 30. Get text from 'getsalespartner'
    getsalespartner = driver.find_element(By.XPATH,
                                          "//div[2]/div[1]/div[1]/div[1]/span/a")
    step_output = getsalespartner.get_attribute("value")

    # 31. Logout from the application
    test_logout.test_main(driver)

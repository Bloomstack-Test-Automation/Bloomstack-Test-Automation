import time

from selenium.common.exceptions import NoSuchElementException
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
    Test: CreateItemPrice_TestCase1
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/28/2021, 06:32:05
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="CreateItemPrice_TestCase1")
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

    # 10. Type 'itemprice' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("itemprice")

    # 11. Click 'Item Price List'
    item_price_list = driver.find_element(By.XPATH,
                                          "//p[. = 'Item Price List']")
    item_price_list.click()

    # 12. Does 'Item Price1' contain 'Item Price'?
    item_price1 = driver.find_element(By.XPATH,
                                      "//div[. = 'Item Price']")
    step_output = item_price1.text
    assert step_output and ("Item Price" in step_output)
    time.sleep(2)

    # 13. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    time.sleep(2)
    new.click()

    # 14. Click 'INPUT85'
    input85 = driver.find_element(By.XPATH,
                                  "//form/div[1]/div/div//input")
    input85.click()

    # 15. Click 'EPI-Chocolate'
    epi_chocolate = driver.find_element(By.XPATH,
                                        "//p[. = 'EPI-Chocolate']")
    epi_chocolate.click()

    # 16. Click 'INPUT35'
    input35 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/div/div/input")
    input35.click()

    # 17. Click 'P61'
    p61 = driver.find_element(By.XPATH,
                              "//div[2]/div/div[2]/div[1]/div/div/ul/li[1]//p")
    p61.click()

    # 18. Click 'INPUT15'
    input15 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]//input")
    input15.click()

    # 19. Type '89.00' in 'INPUT15'
    input15 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]//input")
    input15.send_keys("156")
    time.sleep(2)



    #Close
   # close4 = driver.find_element(By.XPATH, "//div[2]/div/div//button[. = '\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\tClose\n\t\t\t\t\t\t\t\t']")
    #time.sleep(2)
    #close4.click()


    # 20. Click 'Save6'
    save6 = driver.find_element(By.XPATH,"//button[. = 'Save']")
    time.sleep(2)
    save6.click()
    time.sleep(2)

    try:
        eleme = driver.find_element(By.XPATH, "//div[2]/div/div//button[. = '\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\tClose\n\t\t\t\t\t\t\t\t']")
        if eleme.is_displayed() and eleme.is_enabled():
            eleme.click()  # this will click the element if it is there
            #print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
    except NoSuchElementException:
           print("No such Element")
       #else:
        #   element = driver.find_element(By.XPATH,
          #                          "//span[. = '      Settings']")
         #  element.click()

# 21. Click 'Settings2'
    settings2 = driver.find_element(By.XPATH,
                                    "//span[. = '      Settings']")
    time.sleep(2)
    settings2.click()

    # 22. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 23. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

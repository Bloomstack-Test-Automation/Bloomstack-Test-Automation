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
    Test: DeleteDeliveryNote_TestCase
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/26/2021, 09:05:41
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="DeleteDeliveryNote_TestCase")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Generated By: Rahul."""
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

    # 5. Type 'rahul.prakash@extrapreneursindia.com' in 'Email Address'
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

    # 10. Type 'delivery' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("delivery")

    # 11. Click 'Delivery Note List'
    delivery_note_list = driver.find_element(By.XPATH,
                                             "//span[. = 'Delivery Note List']")
    delivery_note_list.click()

    # 12. Does 'Delivery Note6' contain 'Delivery Note'?
    delivery_note6 = driver.find_element(By.XPATH,
                                         "//div[. = 'Delivery Note']")
    step_output = delivery_note6.text
    assert step_output and ("Delivery Note" in step_output)
    time.sleep(2)

    # 13. Click 'New1'
    new1 = driver.find_element(By.XPATH,
                               "//span[. = 'New']")
    new1.click()

    # 14. Does 'DIV4' contain '[NONE]'?
    div4 = driver.find_element(By.XPATH,
                               "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div4.text
    assert step_output and ("" in step_output)

    # 15. Click 'INPUT79'
    input79 = driver.find_element(By.XPATH,
                                  "//div[3]/div[2]/div[2]/form/div[2]//input")
    input79.click()

    # 16. Type 'vap' in 'INPUT79'
    input79 = driver.find_element(By.XPATH,
                                  "//div[3]/div[2]/div[2]/form/div[2]//input")
    input79.send_keys("vap")

    # 17. Click 'VapeCo'
    vapeco = driver.find_element(By.XPATH,
                                 "//strong[. = 'VapeCo']")
    vapeco.click()

    # 18. Click 'INPUT80'
    input80 = driver.find_element(By.XPATH,
                                  "//div[3]/div[2]/div[1]/form//input")
    input80.click()

    # 19. Click 'P12'
    p12 = driver.find_element(By.XPATH,
                              "//div[3]/div/div[2]/div[1]/div/div/ul/li[1]//p")
    p12.click()

    # 20. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 21. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 22. Click 'DIV24'
    div24 = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div24.click()

    # 23. Click 'Finished Oil, Dry Goods, Extracted Ja...'
    finished_oil_dry_goods_extracted_ja_ = driver.find_element(By.XPATH,
                                                               "//span[. = 'Finished Oil, Dry Goods, Extracted Jack Herer Cannabis Oil']")
    finished_oil_dry_goods_extracted_ja_.click()

    # 24. Scroll window by ('0','-100')
    driver.execute_script("window.scrollBy(0,-100)")

    # 25. Click 'Insert'
    insert = driver.find_element(By.XPATH,
                                 "//button[. = 'Insert']")
    insert.click()

    # 26. Scroll window by ('0','-400')
    driver.execute_script("window.scrollBy(0,-400)")

    # 27. Get text from 'INPUT79'
    # Captured Company Name
    input79 = driver.find_element(By.XPATH,
                                  "//div[3]/div[2]/div[2]/form/div[2]//input")
    step_output = input79.get_attribute("value")

    # 28. Click 'Save8'
    save8 = driver.find_element(By.XPATH,
                                "//span[. = 'Save']")
    save8.click()

    # 29. Scroll window by ('0','-100')
    driver.execute_script("window.scrollBy(0,-100)")

    # 30. Click 'Close'
    close = driver.find_element(By.XPATH,
                                "//div[2]/div/div//span[. = 'Close']")
    close.click()

    # 31. Does 'Saved' contain 'Saved'?
    saved = driver.find_element(By.XPATH,
                                "//div[. = 'Saved']")
    step_output = saved.text
    assert step_output and ("Saved" in step_output)

    # 32. Does 'DIV4' contain '[NONE]'?
    div4 = driver.find_element(By.XPATH,
                               "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div4.text
    assert step_output and ("" in step_output)

    # 33. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 34. Get text from 'INPUT79'
    # Captured Company Name After status changed to draft
    input79 = driver.find_element(By.XPATH,
                                  "//div[3]/div[2]/div[2]/form/div[2]//input")
    step_output = input79.get_attribute("value")

    # 35. Click 'Delivery Note3'
    delivery_note3 = driver.find_element(By.XPATH,
                                         "//div[1]/ul//a[. = 'Delivery Note']")
    delivery_note3.click()

    # 36. Scroll window by ('0','-100')
    driver.execute_script("window.scrollBy(0,-100)")

    # 37. Scroll window by ('0','-100')
    driver.execute_script("window.scrollBy(0,-100)")

    # 38. Click 'INPUT81'
    input81 = driver.find_element(By.XPATH,
                                  "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script( "arguments[0].click();", input81)

    # 39. Click 'Actions6'
    actions6 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]//button[. = '               Actions                            ']")
    actions6.click()

    # 40. Click 'Delete1'
    delete1 = driver.find_element(By.XPATH,
                                  "//a[. = '\n\t\t\t\tDelete']")
    delete1.click()

    # 41. Does 'Delete 1 items permanently?' contain 'Delete 1 items permanently?'?
    delete_1_items_permanently_question_mark_ = driver.find_element(By.XPATH,
                                                                    "//p[. = 'Delete 1 items permanently?']")
    step_output = delete_1_items_permanently_question_mark_.text
    assert step_output and ("Delete 1 items permanently?" in step_output)

    # 42. Click 'Yes'
    yes = driver.find_element(By.XPATH,
                              "//button[. = 'Yes']")
    yes.click()

    # 43. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 44. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 45. Does 'Login' contain 'Login'?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    step_output = login.text
    assert step_output and ("Login" in step_output)

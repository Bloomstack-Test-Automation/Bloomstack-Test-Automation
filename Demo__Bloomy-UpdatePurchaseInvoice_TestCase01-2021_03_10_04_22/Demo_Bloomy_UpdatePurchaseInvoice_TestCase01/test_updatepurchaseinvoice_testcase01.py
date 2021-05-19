from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Demo_ Bloomy
    Package: TestProject.Generated.Tests.DemoBloomy
    Test: UpdatePurchaseInvoice_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/10/2021, 04:22:48
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="UpdatePurchaseInvoice_TestCase01")
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

    # 8. Click 'Purchasing'
    purchasing = driver.find_element(By.XPATH,
                                     "//div[. = '\n                Purchasing\n              ']")
    purchasing.click()

    # 9. Does 'Purchasing1' contain 'Purchasing'?
    purchasing1 = driver.find_element(By.XPATH,
                                      "//div[. = 'Purchasing']")
    step_output = purchasing1.text
    assert step_output and ("Purchasing" in step_output)

    # 10. Click 'Purchase Invoice'
    purchase_invoice = driver.find_element(By.XPATH,
                                           "//div/a[. = 'Purchase Invoice']")
    purchase_invoice.click()

    # 11. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 12. Click 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form//select")
    select.click()

    # 13. Select the 'ACC-PINV-.YYYY.-' option in 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form//select")
    Select(select).select_by_value("ACC-PINV-.YYYY.-")

    # 14. Click 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/div/div[1]/form//select")
    select.click()

    # 15. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/div/div[1]/form/div[4]//input")
    input.click()

    # 16. Type 'epi' in 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/div/div[1]/form/div[4]//input")
    input.send_keys("epi")

    # 17. Click 'P42'
    p42 = driver.find_element(By.XPATH,
                              "//li[4]//p")
    p42.click()

    # 18. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 19. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 20. Click 'DIV1'
    div1 = driver.find_element(By.XPATH,
                               "//div[3]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div1.click()

    # 21. Type 'epi' in 'Item1'
    item1 = driver.find_element(By.XPATH,
                                "//input[@placeholder = 'Item']")
    item1.send_keys("epi")

    # 22. Click 'EG-EPI-11'
    eg_epi_11 = driver.find_element(By.XPATH,
                                    "//strong[. = 'EG-EPI-11']")
    eg_epi_11.click()

    # 23. Click 'Save'
    save = driver.find_element(By.XPATH,
                               "//span[. = 'Save']")
    save.click()

    # 24. Scroll window by ('0','-500')
    driver.execute_script("window.scrollBy(0,-500)")

    # 25. Does 'Saved9' contain 'Saved'?
    saved9 = driver.find_element(By.XPATH,
                                 "//div[. = 'Saved']")
    step_output = saved9.text
    assert step_output and ("Saved" in step_output)

    # 26. Click 'Purchase Invoice2'
    purchase_invoice2 = driver.find_element(By.XPATH,
                                            "//li[2]/a[. = 'Purchase Invoice']")
    purchase_invoice2.click()

    # 27. Click 'INPUT38'
    input38 = driver.find_element(By.XPATH,
                                  "//div[2]/div[2]/div[1]/div[1]/div/input")
    input38.click()

    # 28. Click 'SPAN1'
    span1 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[2]/div[2]/button/span[1]")
    span1.click()

    # 29. Click 'Edit'
    edit = driver.find_element(By.XPATH,
                               "//a[. = '\n\t\t\t\tEdit']")
    edit.click()

    # 30. Click 'SELECT14'
    select14 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form/div[1]//select")
    select14.click()

    # 31. Select the 'Price List' option in 'SELECT14'
    select14 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form/div[1]//select")
    Select(select14).select_by_value("Price List")

    # 32. Click 'SELECT14'
    select14 = driver.find_element(By.XPATH,
                                   "//div[2]/div[1]/div/div[2]/div/div/div/form/div[1]//select")
    select14.click()

    # 33. Click 'INPUT44'
    input44 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form//input")
    input44.click()

    # 34. Click 'P36'
    p36 = driver.find_element(By.XPATH,
                              "//div[2]/div/div[2]/div[1]/div/div/ul/li[1]//p")
    p36.click()

    # 35. Click 'Update'
    update = driver.find_element(By.XPATH,
                                 "//button[. = 'Update']")
    update.click()

    # 36. Does 'Updated successfully1' contain 'Updated successfully'?
    updated_successfully1 = driver.find_element(By.XPATH,
                                                "//div[. = 'Updated successfully']")
    step_output = updated_successfully1.text
    assert step_output and ("Updated successfully" in step_output)

    # 37. Click 'EPI-Supplier12'
    epi_supplier12 = driver.find_element(By.XPATH,
                                         "//div[2]/div[1]/div[1]//a[. = '\n\t\t\t\tEPI-Supplier1\n\t\t\t\t']")
    epi_supplier12.click()

    # 38. Click 'u1'
    u1 = driver.find_element(By.XPATH,
                             "//button//span[. = 'u']")
    u1.click()

    # 39. Click 'Yes5'
    yes5 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes5.click()

    # 40. Does 'Purchase Invoice has been submitted s...' contain 'Purchase Invoice has been submitted successfully'?
    purchase_invoice_has_been_submitted_s_ = driver.find_element(By.XPATH,
                                                                 "//div[. = 'Purchase Invoice has been submitted successfully']")
    step_output = purchase_invoice_has_been_submitted_s_.text
    assert step_output and (
        "Purchase Invoice has been submitted successfully" in step_output)

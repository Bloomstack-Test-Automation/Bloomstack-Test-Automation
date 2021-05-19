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
    Test: DeleteDeliveryNote_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/18/2021, 05:27:08
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="DeleteDeliveryNote_TestCase01")
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
    Grid = "Does 20 of 446 span contain \"20 of 446\" ?"

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

    # 8. Click 'Stock'
    stock = driver.find_element(By.XPATH,
                                "//div[. = '\n                Stock\n              ']")
    stock.click()

    # 9. Does 'Stock1' contain 'Stock'?
    stock1 = driver.find_element(By.XPATH,
                                 "//div[. = 'Stock']")
    step_output = stock1.text
    assert step_output and ("Stock" in step_output)

    # 10. Click 'Delivery Note'
    delivery_note = driver.find_element(By.XPATH,
                                        "//div/a[. = 'Delivery Note']")
    delivery_note.click()

    # 11. Does 'Delivery Note1' contain 'Delivery Note'?
    delivery_note1 = driver.find_element(By.XPATH,
                                         "//div[. = 'Delivery Note']")
    step_output = delivery_note1.text
    assert step_output and ("Delivery Note" in step_output)

    # 12. Click 'New1'
    new1 = driver.find_element(By.XPATH,
                               "//span[. = 'New']")
    new1.click()

    # 13. Does 'DIV1' contain '[NONE]'?
    div1 = driver.find_element(By.XPATH,
                               "//div[4]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div1.text
    assert step_output and ("" in step_output)

    # 14. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/form/div[2]/div/div[2]/div[1]/div//input")
    input.click()

    # 15. Type 'vap' in 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/form/div[2]/div/div[2]/div[1]/div//input")
    input.send_keys("vap")

    # 16. Click 'VapeCo'
    vapeco = driver.find_element(By.XPATH,
                                 "//strong[. = 'VapeCo']")
    vapeco.click()

    # 17. Click 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//div[3]/div[2]/div[1]/form//input")
    input1.click()

    # 18. Click 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//div[3]/div[2]/div[1]/form//input")
    input1.click()

    # 19. Click 'P'
    p = driver.find_element(By.XPATH,
                            "//div[3]/div/div[2]/div[1]/div/div/ul/li[1]//p")
    p.click()

    # 20. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 21. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 22. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 23. Click 'DIV'
    div = driver.find_element(By.XPATH,
                              "//div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div.click()

    # 24. Click 'Finished Oil, Dry Goods, Extracted Ja...'
    finished_oil_dry_goods_extracted_ja_ = driver.find_element(By.XPATH,
                                                               "//span[. = 'Finished Oil, Dry Goods, Extracted Jack Herer Cannabis Oil']")
    finished_oil_dry_goods_extracted_ja_.click()

    # 25. Does 'Select Batch Numbers' contain 'Select Batch Numbers'?
    select_batch_numbers = driver.find_element(By.XPATH,
                                               "//h4[. = 'Select Batch Numbers']")
    step_output = select_batch_numbers.text
    assert step_output and ("Select Batch Numbers" in step_output)

    # 26. Click 'Insert'
    insert = driver.find_element(By.XPATH,
                                 "//button[. = 'Insert']")
    insert.click()

    # 27. Click 'Save1'
    save1 = driver.find_element(By.XPATH,
                                "//span[. = 'Save']")
    save1.click()

    # 28. Scroll window by ('0','-600')
    driver.execute_script("window.scrollBy(0,-600)")

    # 29. Click 'Close'
    close = driver.find_element(By.XPATH,
                                "//div[2]/div/div//span[. = 'Close']")
    close.click()

    # 30. Does 'Saved' contain 'Saved'?
    saved = driver.find_element(By.XPATH,
                                "//div[. = 'Saved']")
    step_output = saved.text
    assert step_output and ("Saved" in step_output)

    # 31. Does 'DIV1' contain '[NONE]'?
    div1 = driver.find_element(By.XPATH,
                               "//div[4]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div1.text
    assert step_output and ("" in step_output)

    # 32. Click 'Delivery Note3'
    delivery_note3 = driver.find_element(By.XPATH,
                                         "//div[1]/ul//a[. = 'Delivery Note']")
    delivery_note3.click()

    # 33. Click 'INPUT6'
    input6 = driver.find_element(By.XPATH,
                                 "//div[2]/div[2]/div[1]/div[1]/div/input")
    input6.click()

    # 34. Click 'Actions1'
    actions1 = driver.find_element(By.XPATH,
                                   "//div[3]//button[. = '               Actions                            ']")
    actions1.click()

    # 35. Click 'Delete1'
    delete1 = driver.find_element(By.XPATH,
                                  "//a[. = '\n\t\t\t\tDelete']")
    delete1.click()

    # 36. Click 'Yes'
    yes = driver.find_element(By.XPATH,
                              "//button[. = 'Yes']")
    yes.click()

    # 37. Does '20 of 446' contain '20 of 446'?
    if float(f'{Grid}') <= float("Does 20 of 446 span contain \"20 of 446\" ?"):
        _20_of_446 = driver.find_element(By.XPATH,
                                         "//span/span[. = '20 of 446']")
        step_output = _20_of_446.text
        assert step_output and ("20 of 446" in step_output)

    # 38. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 39. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()
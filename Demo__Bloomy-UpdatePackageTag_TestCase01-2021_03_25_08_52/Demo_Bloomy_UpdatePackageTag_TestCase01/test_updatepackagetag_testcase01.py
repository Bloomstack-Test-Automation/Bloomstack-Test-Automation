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
    Test: UpdatePackageTag_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/25/2021, 08:52:26
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="UpdatePackageTag_TestCase01")
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

    # 10. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 11. Type 'package' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("package")

    # 12. Click 'New Package Tag'
    new_package_tag = driver.find_element(By.XPATH,
                                          "//li[. = 'New Package Tag']")
    new_package_tag.click()

    # 13. Click 'INPUT59'
    input59 = driver.find_element(By.XPATH,
                                  "//div[1]/div/div[2]/div[1]/div/div/input")
    input59.click()

    # 14. Type 'extra' in 'INPUT59'
    input59 = driver.find_element(By.XPATH,
                                  "//div[1]/div/div[2]/div[1]/div/div/input")
    input59.send_keys("extra")

    # 15. Click 'Extrapreneurs India Pvt Ltd'
    extrapreneurs_india_pvt_ltd = driver.find_element(By.XPATH,
                                                      "//strong[. = 'Extrapreneurs India Pvt Ltd']")
    extrapreneurs_india_pvt_ltd.click()

    # 16. Click 'INPUT60'
    input60 = driver.find_element(By.XPATH,
                                  "//div[2]/div/input")
    input60.click()

    # 17. Type 'Epi Update' in 'INPUT60'
    input60 = driver.find_element(By.XPATH,
                                  "//div[2]/div/input")
    input60.send_keys("Epi Update")

    # 18. Click 'INPUT62'
    input62 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]//input")
    input62.click()

    # 19. Type 'd' in 'INPUT62'
    input62 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]//input")
    input62.send_keys("d")

    # 20. Click 'INPUT60'
    input60 = driver.find_element(By.XPATH,
                                  "//div[2]/div/input")
    input60.click()

    # 21. Type 'Epi Updated' in 'INPUT60'
    input60 = driver.find_element(By.XPATH,
                                  "//div[2]/div/input")
    input60.send_keys("Epi Updated")

    # 22. Click 'INPUT62'
    input62 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]//input")
    input62.click()

    # 23. Click 'VC-RM-FO-00014'
    vc_rm_fo_00014 = driver.find_element(By.XPATH,
                                         "//strong[. = 'VC-RM-FO-0001']")
    vc_rm_fo_00014.click()

    # 24. Click 'Save2'
    save2 = driver.find_element(By.XPATH,
                                "//button[. = 'Save']")
    save2.click()

    # 25. Click 'Package Tag'
    package_tag = driver.find_element(By.XPATH,
                                      "//a[. = 'Package Tag']")
    package_tag.click()

    # 26. Click 'INPUT17'
    input17 = driver.find_element(By.XPATH,
                                  "//div[2]/div[2]/div[1]/div[1]/div/input")
    input17.click()

    # 27. Click 'Actions3'
    actions3 = driver.find_element(By.XPATH,
                                   "//div[4]//button[. = '               Actions                            ']")
    actions3.click()

    # 28. Click 'Edit1'
    edit1 = driver.find_element(By.XPATH,
                                "//a[. = '\n\t\t\t\tEdit']")
    edit1.click()

    # 29. Click 'Field'
    field = driver.find_element(By.XPATH,
                                "//div[. = '\t\t\t\t\t\tField\t\t\t\t\t']")
    field.click()

    # 30. Does 'Edit3' contain 'Edit'?
    edit3 = driver.find_element(By.XPATH,
                                "//h4[. = 'Edit']")
    step_output = edit3.text
    assert step_output and ("Edit" in step_output)

    # 31. Click 'SELECT9'
    select9 = driver.find_element(By.XPATH,
                                  "//div[2]/div/select")
    select9.click()

    # 32. Select the 'Item Code' option in 'SELECT9'
    select9 = driver.find_element(By.XPATH,
                                  "//div[2]/div/select")
    Select(select9).select_by_value("Item Code")

    # 33. Click 'SELECT9'
    select9 = driver.find_element(By.XPATH,
                                  "//div[2]/div/select")
    select9.click()

    # 34. Click 'INPUT64'
    input64 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div/div[2]/div[1]/div//input")
    input64.click()

    # 35. Click 'VC-SP-CO-STD-0001'
    vc_sp_co_std_0001 = driver.find_element(By.XPATH,
                                            "//div[2]/div/div[2]//strong[. = 'VC-SP-CO-STD-0001']")
    vc_sp_co_std_0001.click()

    # 36. Click 'Update'
    update = driver.find_element(By.XPATH,
                                 "//button[. = 'Update']")
    update.click()

    # 37. Does 'Updated successfully8' contain 'Updated successfully'?
    updated_successfully8 = driver.find_element(By.XPATH,
                                                "//div[. = 'Updated successfully']")
    step_output = updated_successfully8.text
    assert step_output and ("Updated successfully" in step_output)

    # 38. Click 'Epi Updated'
    epi_updated = driver.find_element(By.XPATH,
                                      "//a[. = '\n\t\t\t\tEpi Updated\n\t\t\t\t']")
    epi_updated.click()

    # 39. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 40. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 41. Does 'INPUT65' contain '[NONE]'?
    input65 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[1]/form//input")
    step_output = input65.text
    assert step_output and ("" in step_output)

    # 42. Click 'Save8'
    save8 = driver.find_element(By.XPATH,
                                "//span[. = 'Save']")
    save8.click()

    # 43. Scroll window by ('0','-400')
    driver.execute_script("window.scrollBy(0,-400)")

    # 44. Does 'Saved14' contain 'Saved'?
    saved14 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved14.text
    assert step_output and ("Saved" in step_output)

    # 45. Click 'R
    # 		           Settings'
    r_settings = driver.find_element(By.XPATH,
                                     "//a[. = '     \n\t\t\t\n\t\t\t\tR\n\t\t           Settings     ']")
    r_settings.click()

    # 46. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

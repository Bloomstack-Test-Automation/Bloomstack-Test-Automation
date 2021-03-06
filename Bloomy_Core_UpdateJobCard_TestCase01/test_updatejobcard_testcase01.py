import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Bloomy_Core
    Package: TestProject.Generated.Tests.BloomyCore
    Test: UpdateJobCard_TestCase01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/28/2021, 11:42:37
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="UpdateJobCard_TestCase01")
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
    ApplicationURL = "https://epitest-demo.bloomstack.io"

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

    # 10. Type 'job card' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("job card")

    # 11. Click 'Job Card List2'
    job_card_list2 = driver.find_element(By.XPATH,
                                         "//p[. = 'Job Card List']")
    job_card_list2.click()

    # 12. Does 'Job Card16' contain 'Job Card'?
    job_card16 = driver.find_element(By.XPATH,
                                     "//div[. = 'Job Card']")
    step_output = job_card16.text
    assert step_output and ("Job Card" in step_output)
    time.sleep(2)

    # 13. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 14. Click 'INPUT114'
    input114 = driver.find_element(By.XPATH,
                                   "//div[2]/div/div[2]/div[1]/div/div/input")
    input114.click()

    # 15. Click 'MFG-WO-2019-00050'
    mfg_wo_2019_00050 = driver.find_element(By.XPATH,
                                            "//p[. = 'MFG-WO-2019-00050']")
    mfg_wo_2019_00050.click()

    # 16. Click 'INPUT115'
    input115 = driver.find_element(By.XPATH,
                                   "//form/div[3]//input")
    input115.click()

    # 17. Click 'Assembly Station4'
    assembly_station4 = driver.find_element(By.XPATH,
                                            "//p[. = 'Assembly Station']")
    assembly_station4.click()

    # 18. Click 'INPUT116'
    input116 = driver.find_element(By.XPATH,
                                   "//div[4]/div/div[2]//input")
    input116.click()

    # 19. Click 'Filtration'
    filtration = driver.find_element(By.XPATH,
                                     "//li[20]//p[. = 'Filtration']")
    filtration.click()

    # 20. Click 'INPUT117'
    input117 = driver.find_element(By.XPATH,
                                   "//div[5]/div/div[2]//input")
    input117.click()

    # 21. Type 'vap' in 'INPUT117'
    input117 = driver.find_element(By.XPATH,
                                   "//div[5]/div/div[2]//input")
    input117.send_keys("vap")

    # 22. Click 'VapeCo30'
    vapeco30 = driver.find_element(By.XPATH,
                                   "//p[. = 'VapeCo']")
    vapeco30.click()

    # 23. Click 'INPUT118'
    input118 = driver.find_element(By.XPATH,
                                   "//div[6]/div/div[2]//input")
    input118.click()

    # 24. Click 'Flow Kana - Ship to HF  - VC1'
    flow_kana_ship_to_hf_vc1 = driver.find_element(By.XPATH,
                                                   "//strong[. = 'Flow Kana - Ship to HF  - VC']")
    flow_kana_ship_to_hf_vc1.click()

    # 25. Click 'Edit in full page'
    edit_in_full_page = driver.find_element(By.XPATH,
                                            "//button[. = 'Edit in full page']")
    edit_in_full_page.click()

    # 26. Does 'DIV48' contain '[NONE]'?
    div48 = driver.find_element(By.XPATH,
                                "//div[3]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div48.text
    assert step_output and ("" in step_output)

    # 27. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 28. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 29. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 30. Click 'Add Row12'
    add_row12 = driver.find_element( By.XPATH,
                                     "//div[4]//button[. = '\n\t\t\t\t\t\t\tAdd Row']" )
    add_row12.click()

    # 31. Click 'DIV109'
    div109 = driver.find_element( By.XPATH,
                                  "//form/div/div/div[2]/div[2]/div[1]/div/div/div[2]" )
    div109.click()

    # 32. Scroll window by ('0','-100')
    driver.execute_script( "window.scrollBy(0,-100)" )

    # 33. Click 'svg5'
    svg5 = driver.find_element( By.XPATH,
                                "//div[2]/nav/div[3]/*" )
    svg5.click()

    # 34. Click '3014'
    _3014 = driver.find_element( By.XPATH,
                                 "//div[32][. = '30']" )
    _3014.click()

    # 35. Click 'To Time1'
    to_time1 = driver.find_element( By.XPATH,
                                    "//input[@placeholder = 'To Time']" )
    to_time1.click()

    # 36. Click 'svg6'
    svg6 = driver.find_element( By.XPATH,
                                "//div[3]/nav/div[3]/*" )
    svg6.click()

    # 37. Click '3015'
    _3015 = driver.find_element( By.XPATH,
                                 "//div[3]//div[32][. = '30']" )
    _3015.click()

    # 40. Click 'Save31'
    save31 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    save31.click()

    # 41. Scroll window by ('0','-500')
    driver.execute_script("window.scrollBy(0,-500)")

    # 42. Does 'Saved17' contain 'Saved'?
    saved17 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved17.text
    assert step_output and ("Saved" in step_output)

    # 43. Click 'Job Card17'
    job_card17 = driver.find_element(By.XPATH,
                                     "//a[. = 'Job Card']")
    job_card17.click()
    time.sleep(1)

    # 44. Click 'INPUT107'
    input107 = driver.find_element(By.XPATH,
                                   "(//input[@class='level-item list-row-checkbox hidden-xs'])[1]")
    driver.execute_script( "arguments[0].click();", input107)

    # 45. Click 'SPAN16'
    span16 = driver.find_element(By.XPATH,
                                 "//div[2]/div[1]/div/div/div[2]/div[2]/button/span[1]")
    span16.click()

    # 46. Click 'Edit'
    edit = driver.find_element(By.XPATH,
                               "//a[. = '\n\t\t\t\tEdit']")
    edit.click()

    # 47. Click 'SELECT20'
    select20 = driver.find_element(By.XPATH,
                                   "//div[2]/div/div[2]/div[1]/div//select")
    select20.click()

    # 48. Select the 'Company' option in 'SELECT20'
    select20 = driver.find_element(By.XPATH,
                                   "//div[2]/div/div[2]/div[1]/div//select")
    Select(select20).select_by_value("Company")

    # 49. Click 'SELECT20'
    select20 = driver.find_element(By.XPATH,
                                   "//div[2]/div/div[2]/div[1]/div//select")
    select20.click()

    # 50. Click 'INPUT119'
    input119 = driver.find_element(By.XPATH,
                                   "//div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/form//input")
    input119.click()

    # 51. Click 'Bloom India1'
    bloom_india1 = driver.find_element(By.XPATH,
                                       "//p[. = 'Bloom India']")
    bloom_india1.click()

    # 52. Click 'Update'
    update = driver.find_element(By.XPATH,
                                 "//button[. = 'Update']")
    update.click()

    # 53. Does 'Updated successfully11' contain 'Updated successfully'?
    updated_successfully11 = driver.find_element(By.XPATH,
                                                 "//div[. = 'Updated successfully']")
    step_output = updated_successfully11.text
    assert step_output and ("Updated successfully" in step_output)

    # 54. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 55. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

    # 56. Is 'Login' visible?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    assert login.is_displayed()

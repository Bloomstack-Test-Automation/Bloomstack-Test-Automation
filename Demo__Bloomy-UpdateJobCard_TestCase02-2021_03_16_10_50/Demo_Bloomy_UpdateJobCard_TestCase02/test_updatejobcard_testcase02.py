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
    Test: UpdateJobCard_TestCase02
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 03/16/2021, 10:50:50
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Demo_ Bloomy",
                              job_name="UpdateJobCard_TestCase02")
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

    # 2. Does 'Login' contain 'Login'?
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    step_output = login.text
    assert step_output and ("Login" in step_output)

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
    email_address.send_keys("rahul.prakash@extrapreneursindia.com")

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

    # 10. Type 'item' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("item")

    # 11. Click 'New Item3'
    new_item3 = driver.find_element(By.XPATH,
                                    "//span[. = 'New Item']")
    new_item3.click()

    # 12. Click 'INPUT22'
    input22 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]//input")
    input22.click()

    # 13. Type 'Item Update01' in 'INPUT22'
    input22 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]//input")
    input22.send_keys("Item Update01")

    # 14. Click 'INPUT22'
    input22 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[2]//input")
    input22.click()

    # 15. Click 'INPUT23'
    input23 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]//input")
    input23.click()

    # 16. Type 'Item Update01' in 'INPUT23'
    input23 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]//input")
    input23.send_keys("Item Update01")

    # 17. Click 'INPUT24'
    input24 = driver.find_element(By.XPATH,
                                  "//div[5]//input")
    input24.click()

    # 18. Click 'All Item Groups1'
    all_item_groups1 = driver.find_element(By.XPATH,
                                           "//strong[. = 'All Item Groups']")
    all_item_groups1.click()

    # 19. Click 'Save4'
    save4 = driver.find_element(By.XPATH,
                                "//button[. = 'Save']")
    save4.click()

    # 20. Click 'Save11'
    save11 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    save11.click()

    # 21. Does 'Saved16' contain 'Saved'?
    saved16 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved16.text
    assert step_output and ("Saved" in step_output)

    # 22. Does 'Item Update01' contain 'Item Update01'?
    item_update01 = driver.find_element(By.XPATH,
                                        "//h1//div[. = 'Item Update01']")
    step_output = item_update01.text
    assert step_output and ("Item Update01" in step_output)

    # 23. Click 'I5'
    i5 = driver.find_element(By.XPATH,
                             "//div[1]/div[1]/div[1]/button/i")
    i5.click()

    # 24. Does 'New BOM 11' contain 'New BOM 1'?
    new_bom_11 = driver.find_element(By.XPATH,
                                     "//div[. = 'New BOM 1']")
    step_output = new_bom_11.text
    assert step_output and ("New BOM 1" in step_output)

    # 25. Click 'INPUT26'
    input26 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[4]//input")
    input26.click()

    # 26. Type 'va' in 'INPUT26'
    input26 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/form/div[4]//input")
    input26.send_keys("va")

    # 27. Click 'VapeCo11'
    vapeco11 = driver.find_element(By.XPATH,
                                   "//li[. = 'VapeCo']")
    vapeco11.click()

    # 28. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 29. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 30. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 31. Click 'Add Row'
    add_row = driver.find_element(By.XPATH,
                                  "//div[6]//button[. = '\n\t\t\t\t\t\t\tAdd Row']")
    add_row.click()

    # 32. Click 'DIV10'
    div10 = driver.find_element(By.XPATH,
                                "//div[3]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div10.click()

    # 33. Click 'VC-RM-FO-0001'
    vc_rm_fo_0001 = driver.find_element(By.XPATH,
                                        "//strong[. = 'VC-RM-FO-0001']")
    vc_rm_fo_0001.click()

    # 34. Click 'Save10'
    save10 = driver.find_element(By.XPATH,
                                 "//div[3]//span[. = 'Save']")
    save10.click()

    # 35. Scroll window by ('0','-700')
    driver.execute_script("window.scrollBy(0,-700)")

    # 36. Does 'Saved13' contain 'Saved'?
    saved13 = driver.find_element(By.XPATH,
                                  "//div[3]/div[. = 'Saved']")
    step_output = saved13.text
    assert step_output and ("Saved" in step_output)

    # 37. Click 'Submit2'
    submit2 = driver.find_element(By.XPATH,
                                  "//span[. = 'Submit']")
    submit2.click()

    # 38. Click 'Yes2'
    yes2 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes2.click()

    # 39. Does 'Saved21' contain 'Saved'?
    saved21 = driver.find_element(By.XPATH,
                                  "//div[4]/div[. = 'Saved']")
    step_output = saved21.text
    assert step_output and ("Saved" in step_output)

    # 40. Click 'SPAN3'
    span3 = driver.find_element(By.XPATH,
                                "//div[3]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]//span")
    span3.click()

    # 41. Click 'Work Order5'
    work_order5 = driver.find_element(By.XPATH,
                                      "//div[2]/div[1]/div[1]/div/ul//a[. = 'Work Order']")
    work_order5.click()

    # 42. Click 'Create4'
    create4 = driver.find_element(By.XPATH,
                                  "//button[. = 'Create']")
    create4.click()

    # 43. Click 'Save6'
    save6 = driver.find_element(By.XPATH,
                                "//div[4]//span[. = 'Save']")
    save6.click()

    # 44. Does 'Saved26' contain 'Saved'?
    saved26 = driver.find_element(By.XPATH,
                                  "//div[5]/div[. = 'Saved']")
    step_output = saved26.text
    assert step_output and ("Saved" in step_output)

    # 45. Click 'Submit4'
    submit4 = driver.find_element(By.XPATH,
                                  "//div[4]//span[. = 'Submit']")
    submit4.click()

    # 46. Click 'Yes4'
    yes4 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes4.click()

    # 47. Does 'Not Started' contain 'Not Started'?
    not_started = driver.find_element(By.XPATH,
                                      "//span/span[. = 'Not Started']")
    step_output = not_started.text
    assert step_output and ("Not Started" in step_output)

    # 48. Click 'Job Card'
    job_card = driver.find_element(By.XPATH,
                                   "//div[2]/a[. = 'Job Card']")
    job_card.click()

    # 49. Does 'Job Card1' contain 'Job Card'?
    job_card1 = driver.find_element(By.XPATH,
                                    "//div[. = 'Job Card']")
    step_output = job_card1.text
    assert step_output and ("Job Card" in step_output)

    # 50. Click 'New5'
    new5 = driver.find_element(By.XPATH,
                               "//span[. = 'New']")
    new5.click()

    # 51. Click 'INPUT36'
    input36 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div[1]/div[2]/div/div/div/form/div[3]/div/div[2]/div[1]/div//input")
    input36.click()

    # 52. Click 'Packing Station2'
    packing_station2 = driver.find_element(By.XPATH,
                                           "//li[. = 'Packing Station']")
    packing_station2.click()

    # 53. Click 'INPUT37'
    input37 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div[1]/div[2]/div/div/div/form/div[4]/div/div[2]/div[1]/div//input")
    input37.click()

    # 54. Click 'EPI-Wakad'
    epi_wakad = driver.find_element(By.XPATH,
                                    "//li[1]//p[. = 'EPI-Wakad']")
    epi_wakad.click()

    # 55. Click 'INPUT38'
    input38 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/form/div[5]//input")
    input38.click()

    # 56. Type 'va' in 'INPUT38'
    input38 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/form/div[5]//input")
    input38.send_keys("va")

    # 57. Click 'VapeCo5'
    vapeco5 = driver.find_element(By.XPATH,
                                  "//div[5]//li[. = 'VapeCo']")
    vapeco5.click()

    # 58. Click 'INPUT39'
    input39 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/form/div[6]//input")
    input39.click()

    # 59. Click 'Non Stock Accounts Warehouse - BTPL'
    non_stock_accounts_warehouse_btpl = driver.find_element(By.XPATH,
                                                            "//strong[. = 'Non Stock Accounts Warehouse - BTPL']")
    non_stock_accounts_warehouse_btpl.click()

    # 60. Click 'Save13'
    save13 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div//button[3][. = 'Save']")
    save13.click()

    # 61. Click 'Submit6'
    submit6 = driver.find_element(By.XPATH,
                                  "//button[3][. = 'Submit']")
    submit6.click()

    # 62. Click 'PO-JOB00357'
    po_job00357 = driver.find_element(By.XPATH,
                                      "//a[. = 'PO-JOB00357']")
    po_job00357.click()

    # 63. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 64. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 65. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")

    # 66. Click 'DIV22'
    div22 = driver.find_element(By.XPATH,
                                "//div[4]/div[2]/div/form/div/div/div[3]")
    div22.click()

    # 67. Click 'Add Row2'
    add_row2 = driver.find_element(By.XPATH,
                                   "//div[4]/div[2]/div/form//button[. = '\n\t\t\t\t\t\t\tAdd Row']")
    add_row2.click()

    # 68. Click 'DIV16'
    div16 = driver.find_element(By.XPATH,
                                "//div[4]/div[2]/div/form/div/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div16.click()

    # 69. Click '302'
    _302 = driver.find_element(By.XPATH,
                               "//div[5]//div[. = '30']")
    _302.click()

    # 70. Click 'To Time'
    to_time = driver.find_element(By.XPATH,
                                  "//input[@placeholder = 'To Time']")
    to_time.click()

    # 71. Click '314'
    _314 = driver.find_element(By.XPATH,
                               "//div[6]/div[1]//div[32][. = '31']")
    _314.click()

    # 72. Click 'Save2'
    save2 = driver.find_element(By.XPATH,
                                "//div[6]//span[. = 'Save']")
    save2.click()

    # 73. Scroll window by ('0','-800')
    driver.execute_script("window.scrollBy(0,-800)")

    # 74. Does 'Saved30' contain 'Saved'?
    saved30 = driver.find_element(By.XPATH,
                                  "//div[7]/div[. = 'Saved']")
    step_output = saved30.text
    assert step_output and ("Saved" in step_output)

    # 75. Does 'Draft3' contain 'Draft'?
    draft3 = driver.find_element(By.XPATH,
                                 "//span/span[. = 'Draft']")
    step_output = draft3.text
    assert step_output and ("Draft" in step_output)

    # 76. Click 'Job Card4'
    job_card4 = driver.find_element(By.XPATH,
                                    "//li/a[. = 'Job Card']")
    job_card4.click()

    # 77. Click 'DIV23'
    div23 = driver.find_element(By.XPATH,
                                "//div[3]/div[2]/div[2]/div[1]/div[1]/div[1]")
    div23.click()

    # 78. Click 'Job Card4'
    job_card4 = driver.find_element(By.XPATH,
                                    "//li/a[. = 'Job Card']")
    job_card4.click()

    # 79. Click 'INPUT46'
    input46 = driver.find_element(By.XPATH,
                                  "//div[2]/div[2]/div[1]/div[1]/div/input")
    input46.click()

    # 80. Click 'DIV24'
    div24 = driver.find_element(By.XPATH,
                                "//div[3]/div[2]/div[1]/div[3]/div[2]")
    div24.click()

    # 81. Click 'SPAN2'
    span2 = driver.find_element(By.XPATH,
                                "//div[5]/div[1]/div/div/div[2]/div[2]/button/span[1]")
    span2.click()

    # 82. Click 'Edit'
    edit = driver.find_element(By.XPATH,
                               "//a[. = '\n\t\t\t\tEdit']")
    edit.click()

    # 83. Click 'SELECT9'
    select9 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select9.click()

    # 84. Select the 'Workstation' option in 'SELECT9'
    select9 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/form//select")
    Select(select9).select_by_value("Workstation")

    # 85. Click 'SELECT9'
    select9 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/form//select")
    select9.click()

    # 86. Click 'INPUT47'
    input47 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/form//input")
    input47.click()

    # 87. Click 'Assembly Station'
    assembly_station = driver.find_element(By.XPATH,
                                           "//div[2]/div/div[2]//strong[. = 'Assembly Station']")
    assembly_station.click()

    # 88. Click 'Update'
    update = driver.find_element(By.XPATH,
                                 "//button[. = 'Update']")
    update.click()

    # 89. Does 'Updated successfully6' contain 'Updated successfully'?
    updated_successfully6 = driver.find_element(By.XPATH,
                                                "//div[. = 'Updated successfully']")
    step_output = updated_successfully6.text
    assert step_output and ("Updated successfully" in step_output)

    # 90. Click 'EPI-Wakad1'
    epi_wakad1 = driver.find_element(By.XPATH,
                                     "//a[. = '\n\t\t\t\tEPI-Wakad\n\t\t\t\t']")
    epi_wakad1.click()

    # 91. Click 'Submit7'
    submit7 = driver.find_element(By.XPATH,
                                  "//div[6]//span[. = 'Submit']")
    submit7.click()

    # 92. Click 'Yes4'
    yes4 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes4.click()

    # 93. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 94. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

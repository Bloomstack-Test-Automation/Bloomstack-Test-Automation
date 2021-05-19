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
    Test: E2EWF_Manufacturing_Work order creation from Sales Order_01
    Generated by: Rahul Prakash (rahulprakash0862@gmail.com)
    Generated on 05/19/2021, 11:26:36
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="5o-UXmLZug6gaKmDcoeI6tT7NM19XyG1qnolFybLul4",
                              project_name="Bloomy_Core",
                              job_name="E2EWF_Manufacturing_Work order creation from Sales Order_01")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """1. Go to the sales order.

    2. create new SO, select customer, select items( Make sure item should have defauld BOM), qty and Delivery date.3.Save and submit the sales order.4. Hit on + button of work order on sales order dashboard or hit on the create button on select work order.5. Pop up window will appear and hit on create.6. Sytem will create work order based on the item in the Sales order.7. go to the work Order.( Sales Order referance number will appear in work order).6.Save and Submit.7.Job card will be created based on operation.8. Start the work order.9. Create stock entry \"Material Transfer for Manufacture\", select the package tag if item is cannabis item and select batch.10. save and submit.11. Go back to work order.12. Open the job card.13. Select employee.14. start the job card.15. complete the job card.16  submit.17. Repet same action 13, 14,15,16 if there are more then one job card.18. Go back to the work order.19. hit on the \"Finish\" button to finish the work order.20. it will redirect you to on stock entry \"Manufacture\".21. selec packag tag and batch for the finished items.22. Save and Submit..
    """
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Does 'Cannabis Vapour Pen' contain 'Cannabis Vapour Pen'?
    cannabis_vapour_pen = driver.find_element(By.XPATH,
                                              "//h1[1][. = 'Cannabis Vapour Pen']")
    step_output = cannabis_vapour_pen.text
    assert step_output and ("Cannabis Vapour Pen" in step_output)

    # 3. Click 'Login'
    login = driver.find_element(By.XPATH,
                                "//a[. = 'Login']")
    login.click()

    # 4. Does 'Login2' contain 'Login'?
    login2 = driver.find_element(By.XPATH,
                                 "//span[. = 'Login']")
    step_output = login2.text
    assert step_output and ("Login" in step_output)

    # 5. Click 'Email Address'
    email_address = driver.find_element(By.CSS_SELECTOR,
                                        "#login_email")
    email_address.click()

    # 6. Type 'rahul.prakash@extrapreneursindia.com' in 'Email Address'
    email_address = driver.find_element(By.CSS_SELECTOR,
                                        "#login_email")
    email_address.send_keys("rahul.prakash@extrapreneursindia.com")

    # 7. Click 'Password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#login_password")
    password.click()

    # 8. Type 'epi@123' in 'Password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#login_password")
    password.send_keys("epi@123")

    # 9. Click 'Login1'
    login1 = driver.find_element(By.XPATH,
                                 "//button[. = '\n\t\t\t\tLogin']")
    login1.click()

    # 10. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 11. Type 'sales' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("sales")

    # 12. Click 'Sales Order List1'
    sales_order_list1 = driver.find_element(By.XPATH,
                                            "//span[. = 'Sales Order List']")
    sales_order_list1.click()

    # 13. Does 'Sales Order1' contain 'Sales Order'?
    sales_order1 = driver.find_element(By.XPATH,
                                       "//div[. = 'Sales Order']")
    step_output = sales_order1.text
    assert step_output and ("Sales Order" in step_output)

    # 14. Click 'New'
    new = driver.find_element(By.XPATH,
                              "//span[. = 'New']")
    new.click()

    # 15. Does 'New Sales Order 11' contain 'New Sales Order 1'?
    new_sales_order_11 = driver.find_element(By.XPATH,
                                             "//div[. = 'New Sales Order 1']")
    step_output = new_sales_order_11.text
    assert step_output and ("New Sales Order 1" in step_output)

    # 16. Click 'INPUT77'
    input77 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[3]//input")
    input77.click()

    # 17. Click 'P22'
    p22 = driver.find_element(By.XPATH,
                              "//div/div/div/ul/li[1]/a/p")
    p22.click()

    # 18. Click 'INPUT78'
    input78 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]/div/input")
    input78.click()

    # 19. Click 'path1'
    path1 = driver.find_element(By.XPATH,
                                "//div[3]/nav/div[3]//*[name()='path']")
    path1.click()

    # 20. Click 'svg3'
    svg3 = driver.find_element(By.XPATH,
                               "//div[3]/nav/div[3]/*")
    svg3.click()

    # 21. Click '3012'
    _3012 = driver.find_element(By.XPATH,
                                "//div[32][. = '30']")
    _3012.click()

    # 22. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 23. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 24. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 25. Click 'DIV67'
    div67 = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div67.click()

    # 26. Click 'P23'
    p23 = driver.find_element(By.XPATH,
                              "//div[1]/div/div/div/ul/li[1]/a/p")
    p23.click()

    # 27. Click 'Save31'
    save31 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    save31.click()

    # 28. Scroll window by ('0','-500')
    driver.execute_script("window.scrollBy(0,-500)")

    # 29. Click 'Close10'
    close10 = driver.find_element(By.XPATH,
                                  "//button/span[. = 'Close']")
    close10.click()

    # 30. Does 'Saved10' contain 'Saved'?
    saved10 = driver.find_element(By.XPATH,
                                  "//div[. = 'Saved']")
    step_output = saved10.text
    assert step_output and ("Saved" in step_output)

    # 31. Click 'Submit15'
    submit15 = driver.find_element(By.XPATH,
                                   "//button/span[. = 'Submit']")
    submit15.click()

    # 32. Click 'Yes1'
    yes1 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes1.click()

    # 33. Click 'Close13'
    close13 = driver.find_element(By.XPATH,
                                  "//button/span[. = 'Close']")
    close13.click()

    # 34. Does 'Sales Order has been submitted succes...1' contain 'Sales Order has been submitted successfully'?
    sales_order_has_been_submitted_succes_1 = driver.find_element(By.XPATH,
                                                                  "//div[. = 'Sales Order has been submitted successfully']")
    step_output = sales_order_has_been_submitted_succes_1.text
    assert step_output and (
        "Sales Order has been submitted successfully" in step_output)

    # 35. Click 'SPAN8'
    span8 = driver.find_element(By.XPATH,
                                "//div[1]/div[1]/button/span")
    span8.click()

    # 36. Click 'Work Order12'
    work_order12 = driver.find_element(By.XPATH,
                                       "//div[1]/ul//a[. = 'Work Order']")
    work_order12.click()

    # 37. Click 'Create'
    create = driver.find_element(By.XPATH,
                                 "//button[. = 'Create']")
    create.click()

    # 38. Does 'DIV50' contain '[NONE]'?
    div50 = driver.find_element(By.XPATH,
                                "//div[6]/div[2]/div/div[1]/div/div[1]")
    step_output = div50.text
    assert step_output and ("" in step_output)

    # 39. Click 'MFG-WO-2021-00282'
    mfg_wo_2021_00282 = driver.find_element(By.XPATH,
                                            "//a[. = 'MFG-WO-2021-00282']")
    mfg_wo_2021_00282.click()

    # 40. Does 'Not Saved' contain 'Not Saved'?
    not_saved = driver.find_element(By.XPATH,
                                    "//span/span[. = 'Not Saved']")
    step_output = not_saved.text
    assert step_output and ("Not Saved" in step_output)

    # 41. Click 'Save1'
    save1 = driver.find_element(By.XPATH,
                                "//button[. = 'Save']")
    save1.click()

    # 42. Does 'Saved21' contain 'Saved'?
    saved21 = driver.find_element(By.XPATH,
                                  "//div[4]/div[. = 'Saved']")
    step_output = saved21.text
    assert step_output and ("Saved" in step_output)

    # 43. Click 'Submit4'
    submit4 = driver.find_element(By.XPATH,
                                  "//div[4]//span[. = 'Submit']")
    submit4.click()

    # 44. Click 'Yes3'
    yes3 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes3.click()

    # 45. Click 'Close11'
    close11 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div[1]/div/div[2]/div/button/span[. = 'Close']")
    close11.click()

    # 46. Does 'Saved22' contain 'Saved'?
    saved22 = driver.find_element(By.XPATH,
                                  "//div[5]/div[. = 'Saved']")
    step_output = saved22.text
    assert step_output and ("Saved" in step_output)

    # 47. Click 'Start7'
    start7 = driver.find_element(By.XPATH,
                                 "//button[. = 'Start']")
    start7.click()

    # 48. Does 'DIV69' contain '[NONE]'?
    div69 = driver.find_element(By.XPATH,
                                "//div[11]/div[2]/div/div[1]/div/div[1]")
    step_output = div69.text
    assert step_output and ("" in step_output)

    # 49. Click 'Create5'
    create5 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div//button[. = 'Create']")
    create5.click()

    # 50. Does 'New Stock Entry 12' contain 'New Stock Entry 1'?
    new_stock_entry_12 = driver.find_element(By.XPATH,
                                             "//div[. = 'New Stock Entry 1']")
    step_output = new_stock_entry_12.text
    assert step_output and ("New Stock Entry 1" in step_output)

    # 51. Click 'Save29'
    save29 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    save29.click()

    # 52. Does 'Saved29' contain 'Saved'?
    saved29 = driver.find_element(By.XPATH,
                                  "//div[6]/div[. = 'Saved']")
    step_output = saved29.text
    assert step_output and ("Saved" in step_output)

    # 53. Does 'DIV37' contain '[NONE]'?
    div37 = driver.find_element(By.XPATH,
                                "//div[5]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div37.text
    assert step_output and ("" in step_output)

    # 54. Click 'Submit8'
    submit8 = driver.find_element(By.XPATH,
                                  "//div[5]//span[. = 'Submit']")
    submit8.click()

    # 55. Click 'Yes4'
    yes4 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes4.click()

    # 56. Does 'Saved30' contain 'Saved'?
    saved30 = driver.find_element(By.XPATH,
                                  "//div[7]/div[. = 'Saved']")
    step_output = saved30.text
    assert step_output and ("Saved" in step_output)

    # 57. Does 'Submitted1' contain 'Submitted'?
    submitted1 = driver.find_element(By.XPATH,
                                     "//span/span[. = 'Submitted']")
    step_output = submitted1.text
    assert step_output and ("Submitted" in step_output)

    # 58. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 59. Click 'MFG-WO-2021-002821'
    mfg_wo_2021_002821 = driver.find_element(By.XPATH,
                                             "//a[. = '\n\t\t\t\tMFG-WO-2021-00282']")
    mfg_wo_2021_002821.click()

    # 60. Scroll window by ('0','-100')
    driver.execute_script("window.scrollBy(0,-100)")

    # 61. Does 'In Process1' contain 'In Process'?
    in_process1 = driver.find_element(By.XPATH,
                                      "//span/span[. = 'In Process']")
    step_output = in_process1.text
    assert step_output and ("In Process" in step_output)

    # 62. Click 'Job Card9'
    job_card9 = driver.find_element(By.XPATH,
                                    "//a[. = 'Job Card']")
    job_card9.click()

    # 63. Does 'Job Card3' contain 'Job Card'?
    job_card3 = driver.find_element(By.XPATH,
                                    "//div[. = 'Job Card']")
    step_output = job_card3.text
    assert step_output and ("Job Card" in step_output)

    # 64. Click 'EPI Wakad9'
    epi_wakad9 = driver.find_element(By.XPATH,
                                     "//a[. = '\n\t\t\t\tEPI Wakad\n\t\t\t\t']")
    epi_wakad9.click()

    # 65. Does 'DIV46' contain '[NONE]'?
    div46 = driver.find_element(By.XPATH,
                                "//div[7]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div46.text
    assert step_output and ("" in step_output)

    # 66. Click 'Start1'
    start1 = driver.find_element(By.XPATH,
                                 "//button[. = 'Start']")
    start1.click()

    # 67. Does 'DIV90' contain '[NONE]'?
    div90 = driver.find_element(By.XPATH,
                                "//div[13]/div[2]/div/div[1]/div/div[1]")
    step_output = div90.text
    assert step_output and ("" in step_output)

    # 68. Click 'INPUT81'
    input81 = driver.find_element(By.XPATH,
                                  "//div[2]/div[1]/div/div[2]/div/div/div/form/div/div/div[2]/div[1]/div/div/input")
    input81.click()

    # 69. Click 'HR-EMP-000698'
    hr_emp_000698 = driver.find_element(By.XPATH,
                                        "//p[. = 'HR-EMP-00069']")
    hr_emp_000698.click()

    # 70. Click 'Start9'
    start9 = driver.find_element(By.XPATH,
                                 "//button[3][. = 'Start']")
    start9.click()

    # 71. Does 'Saved31' contain 'Saved'?
    saved31 = driver.find_element(By.XPATH,
                                  "//div[8]/div[. = 'Saved']")
    step_output = saved31.text
    assert step_output and ("Saved" in step_output)

    # 72. Click 'Complete4'
    complete4 = driver.find_element(By.XPATH,
                                    "//button[. = 'Complete']")
    complete4.click()

    # 73. Click 'Complete1'
    complete1 = driver.find_element(By.XPATH,
                                    "//button[3][. = 'Complete']")
    complete1.click()

    # 74. Does 'Saved65' contain 'Saved'?
    saved65 = driver.find_element(By.XPATH,
                                  "//div[9]/div[. = 'Saved']")
    step_output = saved65.text
    assert step_output and ("Saved" in step_output)

    # 75. Click 'Submit9'
    submit9 = driver.find_element(By.XPATH,
                                  "//div[7]//span[. = 'Submit']")
    submit9.click()

    # 76. Click 'Yes4'
    yes4 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes4.click()

    # 77. Does 'Saved66' contain 'Saved'?
    saved66 = driver.find_element(By.XPATH,
                                  "//div[10]/div[. = 'Saved']")
    step_output = saved66.text
    assert step_output and ("Saved" in step_output)

    # 78. Does 'DIV46' contain '[NONE]'?
    div46 = driver.find_element(By.XPATH,
                                "//div[7]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div46.text
    assert step_output and ("" in step_output)

    # 79. Click 'MFG-WO-2021-002822'
    mfg_wo_2021_002822 = driver.find_element(By.XPATH,
                                             "//div[3]/div/div[2]//a[. = '\n\t\t\t\tMFG-WO-2021-00282']")
    mfg_wo_2021_002822.click()

    # 80. Click 'Finish2'
    finish2 = driver.find_element(By.XPATH,
                                  "//button[. = 'Finish']")
    finish2.click()

    # 81. Click 'Create5'
    create5 = driver.find_element(By.XPATH,
                                  "//div[2]/div/div//button[. = 'Create']")
    create5.click()

    # 82. Does 'New Stock Entry 2' contain 'New Stock Entry 2'?
    new_stock_entry_2 = driver.find_element(By.XPATH,
                                            "//div[. = 'New Stock Entry 2']")
    step_output = new_stock_entry_2.text
    assert step_output and ("New Stock Entry 2" in step_output)

    # 83. Click 'Save32'
    save32 = driver.find_element(By.XPATH,
                                 "//span[. = 'Save']")
    save32.click()

    # 84. Does 'Saved33' contain 'Saved'?
    saved33 = driver.find_element(By.XPATH,
                                  "//div[11]/div[. = 'Saved']")
    step_output = saved33.text
    assert step_output and ("Saved" in step_output)

    # 85. Click 'Submit23'
    submit23 = driver.find_element(By.XPATH,
                                   "//div[5]//button[. = 'Submit']")
    submit23.click()

    # 86. Click 'Yes4'
    yes4 = driver.find_element(By.XPATH,
                               "//div[2]/div/div//button[. = 'Yes']")
    yes4.click()

    # 87. Does 'Saved68' contain 'Saved'?
    saved68 = driver.find_element(By.XPATH,
                                  "//div[12]/div[. = 'Saved']")
    step_output = saved68.text
    assert step_output and ("Saved" in step_output)

    # 88. Does 'DIV37' contain '[NONE]'?
    div37 = driver.find_element(By.XPATH,
                                "//div[5]/div[1]/div/div/div[1]/h1/div[2]")
    step_output = div37.text
    assert step_output and ("" in step_output)

    # 89. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//span[. = '      Settings']")
    settings.click()

    # 90. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//a[. = '       Logout']")
    logout.click()

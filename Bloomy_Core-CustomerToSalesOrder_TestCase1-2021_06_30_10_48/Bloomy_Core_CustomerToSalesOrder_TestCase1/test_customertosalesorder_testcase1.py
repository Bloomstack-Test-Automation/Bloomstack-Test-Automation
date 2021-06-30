from addons.generate_date_time_current_future_or_past_ import GenerateDateTimeCurrentFutureOrPast
from addons.random_data_generator import RandomDataGenerator
from addons.string_utils import StringUtils
from distutils.util import strtobool
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    Test: CustomerToSalesOrder_TestCase1
    Generated by: Meenal Kardale (meenal.kardale@extrapreneurs-india.com)
    Generated on 06/30/2021, 10:48:39
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="3J0RNM_48lLt_KM5Ab6s6A_HZzddmktVs_HhX77AjTM",
                              project_name="Bloomy_Core",
                              job_name="CustomerToSalesOrder_TestCase1")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """1. Go to the Customer Doctype.(Desk >> Selling>> Customer) or Type Customer in Search bar.

    2. Open Customer.3. On Customer Dashboard in Order section click on Sales Order\"\" +\"\" sign.4. Select Company and Requested Delivery Date in Sales Order5. In Item Table hit on Add Row and Add item and Enter Qty and Rate,Add Delivery Warehouse6. Save and Submit..
    """
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io/"
    ActualCustnm = ""
    username = ""
    pwd = ""
    randomcustnm = ""
    ExpectedCustNm = ""
    FutureDt = ""
    ActualCustNmOnSaleOrderScreen = ""
    ActualCustNmOnSalesOrderTitle = ""

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Login to the Application
    test_login.test_main(driver)

    # 3. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 4. Type 'customer ' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("customer ")

    # 5. Click 'Customer List'
    customer_list = driver.find_element(By.XPATH,
                                        "//li[. = 'Customer List']")
    customer_list.click()

    # 6. Does 'Customer2' contain 'Customer'?
    customer2 = driver.find_element(By.XPATH,
                                    "//div[. = 'Customer']")
    step_output = customer2.text
    assert step_output and ("Customer" in step_output)

    # 7. Click 'New4'
    new4 = driver.find_element(By.XPATH,
                               "//button[. = 'New']")
    new4.click()

    # 8. Click 'Edit in full page'
    edit_in_full_page = driver.find_element(By.XPATH,
                                            "//button[. = 'Edit in full page']")
    edit_in_full_page.click()

    # 9. Click 'INPUT101'
    input101 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div[2]/div[1]/form/div[3]//input")
    input101.click()

    # 10. Generate random name
    step_output = driver.addons().execute(
        RandomDataGenerator.generatename(
        ))
    randomcustnm = step_output

    # 11. Type '{randomcustnm}' in 'INPUT101'
    input101 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div[2]/div[1]/form/div[3]//input")
    input101.send_keys(f'{randomcustnm}')

    # 12. Does 'cust' contain '[NONE]'?
    # Does New Customer 1 Div contain "New Customer 1" ?
    cust = driver.find_element(By.XPATH,
                               "//div[. = 'New Customer 1']")
    step_output = cust.text
    assert step_output and ("" in step_output)

    # 13. Does 'stat' contain '[NONE]'?
    # Does Not Saved2 span contain "Not Saved" ?
    stat = driver.find_element(By.XPATH,
                               "//span/span[. = 'Not Saved']")
    step_output = stat.text
    assert step_output and ("" in step_output)

    # 14. Get text from 'gettext Get text from INPUT101 Textbox'
    # Get text from INPUT101 Textbox
    gettext_get_text_from_input101_textbox = driver.find_element(By.XPATH,
                                                                 "//div[3]/div/div/div[2]/div[3]/div[2]/div[1]/form/div[3]//input")
    step_output = gettext_get_text_from_input101_textbox.get_attribute("value")
    ExpectedCustNm = step_output

    # 15. Click 'SELECT13'
    select13 = driver.find_element(By.XPATH,
                                   "//div[5]//select")
    select13.click()

    # 16. Select the 'Corporation' option in 'SELECT13'
    select13 = driver.find_element(By.XPATH,
                                   "//div[5]//select")
    Select(select13).select_by_value("Corporation")

    # 17. Click 'SELECT13'
    select13 = driver.find_element(By.XPATH,
                                   "//div[5]//select")
    select13.click()

    # 18. Click 'INPUT102'
    input102 = driver.find_element(By.XPATH,
                                   "//div[3]/div[2]/div[2]/form/div[2]/div/div[2]/div[1]/div//input")
    input102.click()

    # 19. Clear 'cleartext1' contents
    # clear 1
    cleartext1 = driver.find_element(By.XPATH,
                                     "//div[3]/div[2]/div[2]/form/div[2]/div/div[2]/div[1]/div//input")
    cleartext1.clear()

    # 20. Type 'cor' in 'INPUT102'
    input102 = driver.find_element(By.XPATH,
                                   "//div[3]/div[2]/div[2]/form/div[2]/div/div[2]/div[1]/div//input")
    input102.send_keys("cor")

    # 21. Click 'Corporate'
    corporate = driver.find_element(By.XPATH,
                                    "//li[. = 'Corporate']")
    corporate.click()

    # 22. Click 'INPUT103'
    input103 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div[2]/div[2]/form/div[3]//input")
    input103.click()

    # 23. Clear 'clear1' contents
    # clear 2
    clear1 = driver.find_element(By.XPATH,
                                 "//div[3]/div/div/div[2]/div[3]/div[2]/div[2]/form/div[3]//input")
    clear1.clear()

    # 24. Type 'los' in 'INPUT103'
    input103 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div[2]/div[2]/form/div[3]//input")
    input103.send_keys("los")

    # 25. Click 'LI15'
    li15 = driver.find_element(By.XPATH,
                               "//div[3]/div/div[2]/div[1]/div/div/ul/li[1]")
    li15.click()

    # 26. Click 'Save13'
    save13 = driver.find_element(By.XPATH,
                                 "//button[2][. = 'Save']")
    save13.click()

    # 27. Get text from 'customernm'
    customernm = driver.find_element(By.XPATH,
                                     "//h1//div[. = 'test11']")
    step_output = customernm.get_attribute("value")
    ActualCustnm = step_output

    # 28. Compares '{ExpectedCustNm}' with '{ActualCustnm}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedCustNm}',
            secondString=f'{ActualCustnm}',
            ignoreCase=False,
            expectedResult=0))

    # 29. Does 'Enabled2' contain 'Enabled'?
    enabled2 = driver.find_element(By.XPATH,
                                   "//span/span[. = 'Enabled']")
    step_output = enabled2.text
    assert step_output and ("Enabled" in step_output)

    # 30. Click 'I5'
    i5 = driver.find_element(By.XPATH,
                             "//div[5]/div/div/div[1]/div[2]/div[1]//i")
    i5.click()

    # 31. Click 'test123'
    test123 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[3]/div/div[2]/form/div[2]//input")
    test123.click()

    # 32. Type 'vap' in 'test123'
    test123 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[3]/div/div[2]/form/div[2]//input")
    test123.send_keys("vap")

    # 33. Click 'VapeCo14'
    vapeco14 = driver.find_element(By.XPATH,
                                   "//li[. = 'VapeCo']")
    vapeco14.click()

    # 34. Click 'INPUT105'
    input105 = driver.find_element(By.XPATH,
                                   "//div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[3]/div/div[2]/form/div[4]//input")
    input105.click()

    # 35. Positive values for future and negative for past dates
    step_output = driver.addons().execute(
        GenerateDateTimeCurrentFutureOrPast.futurepastaction(
            days=5,
            months=0,
            years=0,
            hours=0,
            minutes=0,
            format="dd"))
    FutureDt = step_output

    # 36. Click '3012'
    _3012 = driver.find_element(By.XPATH,
                                f'//div[5]/div[1]/div/div/div[. = {FutureDt}]')
    _3012.click()

    # 37. Click 'Add Row6'
    add_row6 = driver.find_element(By.XPATH,
                                   "//div[7]//button[. = '\n\t\t\t\t\t\t\tAdd Row']")
    add_row6.click()

    # 38. Click 'DIV44'
    div44 = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div44.click()

    # 39. Type '[NONE]' in 'Item Code'
    item_code = driver.find_element(By.XPATH,
                                    "//input[@placeholder = 'Item Code']")
    item_code.send_keys(" ")

    # 40. Click 'LI16'
    li16 = driver.find_element(By.XPATH,
                               "//div[2]/div[1]/div/div/div[2]/div[1]/div//li[1]")
    li16.click()

    # 41. Click 'SPAN13'
    span13 = driver.find_element(By.XPATH,
                                 "//div[6]/a/span")
    span13.click()

    # 42. Click 'DIV45'
    div45 = driver.find_element(By.XPATH,
                                "//body/div[1]/div/div[5]/div")
    div45.click()

    # 43. Does 'New Sales Order 11' contain 'New Sales Order 1'?
    new_sales_order_11 = driver.find_element(By.XPATH,
                                             "//div[. = 'New Sales Order 1']")
    step_output = new_sales_order_11.text
    assert step_output and ("New Sales Order 1" in step_output)

    # 44. Does 'Not Saved1' contain 'Not Saved'?
    not_saved1 = driver.find_element(By.XPATH,
                                     "//span/span[. = 'Not Saved']")
    step_output = not_saved1.text
    assert step_output and ("Not Saved" in step_output)

    # 45. Click 'Save23'
    save23 = driver.find_element(By.XPATH,
                                 "//div[4]//button[2][. = 'Save']")
    save23.click()

    # 46. Click 'Close4'
    close4 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div//button[. = '\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\tClose\n\t\t\t\t\t\t\t\t']")
    close4.click()

    # 47. Get text from 'ActualCustNmOnSalesOrder'
    actualcustnmonsalesorder = driver.find_element(By.XPATH,
                                                   "//div[. = 'test - 5']")
    step_output = actualcustnmonsalesorder.get_attribute("value")
    ActualCustNmOnSalesOrderTitle = step_output

    # 48. Get text from 'input451'
    input451 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div[1]/form/div[3]/div/div[2]/div[1]/div//input")
    step_output = input451.get_attribute("value")
    ActualCustNmOnSaleOrderScreen = step_output

    # 49. Compares '{ExpectedCustNm}' with '{ActualCustNmOnSalesOrderTitle}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedCustNm}',
            secondString=f'{ActualCustNmOnSalesOrderTitle}',
            ignoreCase=False,
            expectedResult=0))

    # 50. Compares '{ExpectedCustNm}' with '{ActualCustNmOnSaleOrderScreen}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedCustNm}',
            secondString=f'{ActualCustNmOnSaleOrderScreen}',
            ignoreCase=False,
            expectedResult=0))

    # 51. Does 'draftstat' contain '[NONE]'?
    draftstat = driver.find_element(By.XPATH,
                                    "//span/span[. = 'Draft']")
    step_output = draftstat.text
    assert step_output and ("" in step_output)

    # 52. Click 'Submit4'
    submit4 = driver.find_element(By.XPATH,
                                  "//button[. = 'Submit']")
    submit4.click()

    # 53. Click 'Yes5'
    yes5 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes5.click()

    # 54. Click 'Close4'
    close4 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div//button[. = '\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\tClose\n\t\t\t\t\t\t\t\t']")
    close4.click()

    # 55. Is 'Sales Order1 has been submitted succes...1' present?
    sales_order1_has_been_submitted_succes_1 = driver.find_element(By.XPATH,
                                                                   "//div[. = 'Sales Order has been submitted successfully']")

    # 56. Does 'To Deliver and Bill11' contain '[NONE]'?
    to_deliver_and_bill11 = driver.find_element(By.XPATH,
                                                "//span/span[. = 'To Deliver and Bill']")
    step_output = to_deliver_and_bill11.text
    assert step_output and ("" in step_output)

    # 57. Logout from the application
    test_logout.test_main(driver)
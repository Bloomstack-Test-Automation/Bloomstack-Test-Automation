from addons.generate_date_time_current_future_or_past_ import GenerateDateTimeCurrentFutureOrPast
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
    Test: SalesOrder_Staus(Re-Open)_TestCase
    Generated by: Meenal Kardale (meenal.kardale@extrapreneurs-india.com)
    Generated on 06/30/2021, 10:49:16
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="3J0RNM_48lLt_KM5Ab6s6A_HZzddmktVs_HhX77AjTM",
                              project_name="Bloomy_Core",
                              job_name="SalesOrder_Staus(Re-Open)_TestCase")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """1.Go to the Sales Order Doctype.(Desk >> Selling >> Sales Order) or Type sales Order on search bar.

    2.Open Sales Order 3.Click on Submit4. Click on Status as Re-open5. Verify status next to sales order name (status should be To deliver and Bill).
    """
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io/"
    ActualCustomerName = ""
    ExpectedCustomer = ""
    ExpectedOrderType = ""
    ActualCustNmOnSave = ""
    ActualCustOnSubmit = ""
    ActualStatus = ""
    username = ""
    pwd = ""
    ExpectedCompany = ""
    ExpectedItem = ""
    ExpectedQTY = ""
    ExpectedAMT = ""
    ExpectedRate = ""
    ActualCustNameOnSubmit = ""
    ActualOrderType = ""
    ActualCompany = ""
    ActualExpDeliDate = ""
    ActualItem = ""
    ActualQTY = ""
    ActualRate = ""
    ActualAmt = ""
    RandomDate = ""
    ExpectedDeliDate = ""

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Login to the Application
    test_login.test_main(driver)

    # 3. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 4. Type 'sales order ' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("sales order ")

    # 5. Click 'Sales Order List'
    sales_order_list = driver.find_element(By.XPATH,
                                           "//li[. = 'Sales Order List']")
    sales_order_list.click()

    # 6. Does 'Sales Order2' contain 'Sales Order'?
    sales_order2 = driver.find_element(By.XPATH,
                                       "//div[. = 'Sales Order']")
    step_output = sales_order2.text
    assert step_output and ("Sales Order" in step_output)

    # 7. Click 'New4'
    new4 = driver.find_element(By.XPATH,
                               "//button[. = 'New']")
    new4.click()

    # 8. Does 'New Sales Order 126' contain '[NONE]'?
    # Does New Sales Order 125 Div contain "New Sales Order 1" ?
    new_sales_order_126 = driver.find_element(By.XPATH,
                                              "//div[. = 'New Sales Order 1']")
    step_output = new_sales_order_126.text
    assert step_output and ("" in step_output)

    # 9. Does 'status1' contain '[NONE]'?
    # Does stat1 span contain "Not Saved" ?
    status1 = driver.find_element(By.XPATH,
                                  "//span/span[. = 'Not Saved']")
    step_output = status1.text
    assert step_output and ("" in step_output)

    # 10. Click 'INPUT55'
    input55 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[3]//input")
    input55.click()

    # 11. Type 'good tree' in 'INPUT55'
    input55 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[3]//input")
    input55.send_keys("good tree")

    # 12. Click 'LI7'
    li7 = driver.find_element(By.XPATH,
                              "//div[3]/div/div[2]/div[1]/div/div/ul/li[1]")
    li7.click()

    # 13. Get text from 'Good Tree Holdings, LLC'
    good_tree_holdings_llc = driver.find_element(By.XPATH,
                                                 "//div[. = 'Good Tree Holdings, LLC ']")
    step_output = good_tree_holdings_llc.get_attribute("value")
    ActualCustomerName = step_output

    # 14. Get text from 'INPUT55'
    input55 = driver.find_element(By.XPATH,
                                  "//div[3]/div/div[1]/form/div[3]//input")
    step_output = input55.get_attribute("value")
    ExpectedCustomer = step_output

    # 15. Compares '{ExpectedCustomer}' with '{ActualCustomerName}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedCustomer}',
            secondString=f'{ActualCustomerName}',
            ignoreCase=False,
            expectedResult=0))

    # 16. Click 'SELECT19'
    select19 = driver.find_element(By.XPATH,
                                   "//div[5]//select")
    select19.click()

    # 17. Select the 'Consignment' option in 'SELECT19'
    select19 = driver.find_element(By.XPATH,
                                   "//div[5]//select")
    Select(select19).select_by_value("Consignment")

    # 18. Click 'SELECT19'
    select19 = driver.find_element(By.XPATH,
                                   "//div[5]//select")
    select19.click()

    '''
    # (STEP DISABLED)
    # 19. Get text from 'SELECT19'
    select19 = driver.find_element(By.XPATH,
    "//div[5]//select")
    step_output = select19.get_attribute("value")
    ExpectedOrderType = step_output
    '''

    # 20. Get text from 'INPUT1271'
    input1271 = driver.find_element(By.XPATH,
                                    "//div[3]/div/div[2]/form/div[2]//input")
    step_output = input1271.get_attribute("value")
    ExpectedCompany = step_output

    # 21. Click 'INPUT60'
    input60 = driver.find_element(By.XPATH,
                                  "//div[4]/div/div[2]/div/input")
    input60.click()

    # 22. Positive values for future and negative for past dates
    step_output = driver.addons().execute(
        GenerateDateTimeCurrentFutureOrPast.futurepastaction(
            days=5,
            months=0,
            years=0,
            hours=0,
            minutes=0,
            format="dd"))
    RandomDate = step_output

    # 23. Click '3011'
    _3011 = driver.find_element(By.XPATH,
                                f'//div[3]//div[. = {RandomDate}]')
    _3011.click()

    # 24. Click 'DIV25'
    div25 = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div25.click()

    # 25. Get text from 'input7868'
    input7868 = driver.find_element(By.XPATH,
                                    "//div[4]/div/div[2]/div/input")
    step_output = input7868.get_attribute("value")
    ExpectedDeliDate = step_output

    # 26. Type '[NONE]' in 'Item Code'
    item_code = driver.find_element(By.XPATH,
                                    "//input[@placeholder = 'Item Code']")
    item_code.send_keys(" ")

    # 27. Click 'LI6'
    li6 = driver.find_element(By.XPATH,
                              "//div[2]/div[1]/div/div/div[2]/div[1]/div//li[1]")
    li6.click()

    # 28. Get text from 'item code123'
    item_code123 = driver.find_element(By.XPATH,
                                       "//input[@placeholder = 'Item Code']")
    step_output = item_code123.get_attribute("value")
    ExpectedItem = step_output

    # 29. Get text from 'QTY12'
    qty12 = driver.find_element(By.XPATH,
                                "//input[@placeholder = 'Quantity']")
    step_output = qty12.get_attribute("value")
    ExpectedQTY = step_output

    # 30. Get text from 'Rate (USD)212'
    rate_usd_212 = driver.find_element(By.XPATH,
                                       "//input[@placeholder = 'Rate (USD)']")
    step_output = rate_usd_212.get_attribute("value")
    ExpectedRate = step_output

    # 31. Get text from 'Amount (USD)123'
    amount_usd_123 = driver.find_element(By.XPATH,
                                         "//input[@placeholder = 'Amount (USD)']")
    step_output = amount_usd_123.get_attribute("value")
    ExpectedAMT = step_output

    # 32. Click 'clicksabutton'
    clicksabutton = driver.find_element(By.XPATH,
                                        "//button[. = 'Save']")
    clicksabutton.click()

    # 33. Get text from 'Good Tree Holdings, LLC1'
    good_tree_holdings_llc1 = driver.find_element(By.XPATH,
                                                  "//div[. = 'Good Tree Holdings, LLC']")
    step_output = good_tree_holdings_llc1.get_attribute("value")
    ActualCustNmOnSave = step_output

    # 34. Compares '{ExpectedCustomer}' with '{ActualCustNmOnSave}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedCustomer}',
            secondString=f'{ActualCustNmOnSave}',
            ignoreCase=False,
            expectedResult=0))

    # 35. Does 'Draft' contain 'Draft'?
    draft = driver.find_element(By.XPATH,
                                "//span/span[. = 'Draft']")
    step_output = draft.text
    assert step_output and ("Draft" in step_output)

    # 36. Click 'Submit8'
    submit8 = driver.find_element(By.XPATH,
                                  "//button[. = 'Submit']")
    submit8.click()

    # 37. Click 'Yes1'
    yes1 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes1.click()

    # 38. Does 'sale112' contain '[NONE]'?
    sale112 = driver.find_element(By.XPATH,
                                  "//div[. = 'Sales Order has been submitted successfully']")
    step_output = sale112.text
    assert step_output and ("" in step_output)

    # 39. Does 'To Deliver and Bill2' contain 'To Deliver and Bill'?
    to_deliver_and_bill2 = driver.find_element(By.XPATH,
                                               "//span/span[. = 'To Deliver and Bill']")
    step_output = to_deliver_and_bill2.text
    assert step_output and ("To Deliver and Bill" in step_output)

    # 40. Get text from 'Good Tree Holdings, LLC1'
    good_tree_holdings_llc1 = driver.find_element(By.XPATH,
                                                  "//div[. = 'Good Tree Holdings, LLC']")
    step_output = good_tree_holdings_llc1.get_attribute("value")
    ActualCustOnSubmit = step_output

    # 41. Get text from 'custnamw'
    custnamw = driver.find_element(By.XPATH,
                                   "//div[. = 'Good Tree Holdings, LLC ']")
    step_output = custnamw.get_attribute("value")
    ActualCustNameOnSubmit = step_output

    # 42. Get text from 'custnmactual'
    custnmactual = driver.find_element(By.XPATH,
                                       "//div[3]/div/div[1]/form/div[5]/div/div/div[2]")
    step_output = custnmactual.get_attribute("value")
    ActualOrderType = step_output

    # 43. Get text from 'comp12'
    comp12 = driver.find_element(By.XPATH,
                                 "//div[3]/div/div[2]/form/div[2]/div/div/div[2]")
    step_output = comp12.get_attribute("value")
    ActualCompany = step_output

    # 44. Get text from 'input7868'
    input7868 = driver.find_element(By.XPATH,
                                    "//div[4]/div/div[2]/div/input")
    step_output = input7868.get_attribute("value")
    ActualExpDeliDate = step_output

    # 45. Get text from 'DIV50'
    div50 = driver.find_element(By.XPATH,
                                "//div[7]/div/div/form/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]")
    step_output = div50.get_attribute("value")
    ActualItem = step_output

    # 46. Get text from 'DIV53'
    div53 = driver.find_element(By.XPATH,
                                "//div[7]/div/div/form/div[2]/div/div[2]/div[2]//div[3]")
    step_output = div53.get_attribute("value")
    ActualQTY = step_output

    # 47. Get text from 'DIV54'
    div54 = driver.find_element(By.XPATH,
                                "//div[7]/div/div/form/div[2]/div/div[2]/div[2]//div[4]")
    step_output = div54.get_attribute("value")
    ActualRate = step_output

    # 48. Get text from 'DIV56'
    div56 = driver.find_element(By.XPATH,
                                "//div[7]/div/div/form/div[2]/div/div[2]/div[2]//div[5]")
    step_output = div56.get_attribute("value")
    ActualAmt = step_output

    # 49. Compares '{ExpectedCustomer}' with '{ActualCustOnSubmit}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedCustomer}',
            secondString=f'{ActualCustOnSubmit}',
            ignoreCase=False,
            expectedResult=0))

    # 50. Compares '{ExpectedCustomer}' with '{ActualCustNameOnSubmit}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedCustomer}',
            secondString=f'{ActualCustNameOnSubmit}',
            ignoreCase=False,
            expectedResult=0))

    # 51. Compares 'Consignment' with '{ActualOrderType}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString="Consignment",
            secondString=f'{ActualOrderType}',
            ignoreCase=False,
            expectedResult=0))

    # 52. Compares '{ExpectedCompany}' with '{ActualCompany}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedCompany}',
            secondString=f'{ActualCompany}',
            ignoreCase=False,
            expectedResult=0))

    # 53. Compares '{ExpectedDeliDate}' with '{ActualExpDeliDate}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedDeliDate}',
            secondString=f'{ActualExpDeliDate}',
            ignoreCase=False,
            expectedResult=0))

    '''
    # (STEP DISABLED)
    # 54. Compares '{ExpectedItem}' with '{ActualItem}'
    step_output = driver.addons().execute(
    StringUtils.comparetwostrings(
    firstString = f'{ExpectedItem}',
    secondString = f'{ActualItem}',
    ignoreCase = bool(strtobool(EPI TestItem: )),
    expectedResult = 0))
    assert "f'{ExpectedItem}'" in step_output.result

    '''

    '''
    # (STEP DISABLED)
    # 55. Compares '{ExpectedQTY}' with '{ActualQTY}'
    step_output = driver.addons().execute(
    StringUtils.comparetwostrings(
    firstString = f'{ExpectedQTY}',
    secondString = f'{ActualQTY}',
    ignoreCase = bool(strtobool(.00)),
    expectedResult = 0))
    assert "f'{ExpectedQTY}'" in step_output.result

    '''

    '''
    # (STEP DISABLED)
    # 56. Compares '{ExpectedRate}' with '{ActualRate}'
    step_output = driver.addons().execute(
    StringUtils.comparetwostrings(
    firstString = f'{ExpectedRate}',
    secondString = f'{ActualRate}',
    ignoreCase = bool(strtobool($)),
    expectedResult = 0))
    assert "f'{ExpectedRate}'" in step_output.result

    '''

    '''
    # (STEP DISABLED)
    # 57. Compares '{ExpectedAMT}' with '{ActualAmt}'
    step_output = driver.addons().execute(
    StringUtils.comparetwostrings(
    firstString = f'{ExpectedAMT}',
    secondString = f'{ActualAmt}',
    ignoreCase = bool(strtobool($)),
    expectedResult = 0))
    '''

    # 58. Click 'Status'
    status = driver.find_element(By.XPATH,
                                 "//button[. = '\t\t\t\tStatus ']")
    status.click()

    # 59. Click 'clos'
    clos = driver.find_element(By.XPATH,
                               "//a[. = 'Close']")
    clos.click()

    # 60. Get text from 'cls123'
    cls123 = driver.find_element(By.XPATH,
                                 "//span/span[. = 'Closed']")
    step_output = cls123.get_attribute("value")

    # 61. Click 'but'
    but = driver.find_element(By.XPATH,
                              "//button[. = '\t\t\t\tStatus ']")
    but.click()

    # 62. Click 'closed123'
    closed123 = driver.find_element(By.XPATH,
                                    "//a[. = 'Close']")
    closed123.click()

    # 63. Get text from 'stat12344'
    # get text from status
    stat12344 = driver.find_element(By.XPATH,
                                    "//span/span[. = 'Closed']")
    step_output = stat12344.get_attribute("value")
    ActualStatus = step_output

    # 64. Compares 'To Deliver and Bill' with '{ActualStatus}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString="To Deliver and Bill",
            secondString=f'{ActualStatus}',
            ignoreCase=False,
            expectedResult=0))

    # 65. Logout from the application
    test_logout.test_main(driver)
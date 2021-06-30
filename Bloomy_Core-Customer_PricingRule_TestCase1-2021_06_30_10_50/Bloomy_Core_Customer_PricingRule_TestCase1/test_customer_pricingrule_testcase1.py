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
    Test: Customer_PricingRule_TestCase1
    Generated by: Meenal Kardale (meenal.kardale@extrapreneurs-india.com)
    Generated on 06/30/2021, 10:50:19
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="3J0RNM_48lLt_KM5Ab6s6A_HZzddmktVs_HhX77AjTM",
                              project_name="Bloomy_Core",
                              job_name="Customer_PricingRule_TestCase1")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """1. Go to the Customer Doctype.(Desk >> Selling>> Customer) or Type Customer in Search bar.

    2. Open Customer.3. On Customer Dashboard , click on create -> pricing rule4. Enter title and select apply on as Item Code5. Add item code6. Select Selling Checkbox7. Select Min Qty, Max Qty, Min Amt and Max Amt8. Select Valid from , Valid upto and company9. Select rate or discount as discount amount and enter discount amount5. Save and Submit.
    """
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io/"
    ActualFullName = ""
    ActualTitle = ""
    username = ""
    pwd = ""
    RandomCustNm = ""
    ExpectedFullNm = ""
    RandomTitle = ""
    RandomValidTo = ""
    ExpectedTitle = ""

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Login to the Application
    test_login.test_main(driver)

    # 3. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 4. Type 'customer' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("customer")

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

    # 9. Click 'getcust1'
    getcust1 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div[2]/div[1]/form/div[3]//input")
    getcust1.click()

    # 10. Generate random name
    step_output = driver.addons().execute(
        RandomDataGenerator.generatename(
        ))
    RandomCustNm = step_output

    # 11. Type '{RandomCustNm}' in 'getcust1'
    getcust1 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div[2]/div[1]/form/div[3]//input")
    getcust1.send_keys(f'{RandomCustNm}')

    # 12. Get text from 'getcustfullnm'
    # get text entered customer full name
    getcustfullnm = driver.find_element(By.XPATH,
                                        "//div[3]/div/div/div[2]/div[3]/div[2]/div[1]/form/div[3]//input")
    step_output = getcustfullnm.get_attribute("value")
    ExpectedFullNm = step_output

    # 13. Does 'cust' contain 'New Customer 1'?
    cust = driver.find_element(By.XPATH,
                               "//div[. = 'New Customer 1']")
    step_output = cust.text
    assert step_output and ("New Customer 1" in step_output)

    # 14. Does 'status1' contain 'Not Saved'?
    status1 = driver.find_element(By.XPATH,
                                  "//span/span[. = 'Not Saved']")
    step_output = status1.text
    assert step_output and ("Not Saved" in step_output)

    # 15. Click 'save344'
    save344 = driver.find_element(By.XPATH,
                                  "//button[2][. = 'Save']")
    save344.click()

    # 16. Click 'save234'
    # click on save button
    save234 = driver.find_element(By.XPATH,
                                  "//button[2][. = 'Save']")
    save234.click()

    # 17. Get text from 'Full nametest'
    full_nametest = driver.find_element(By.XPATH,
                                        "//h1//div[. = 'Full nametest']")
    step_output = full_nametest.get_attribute("value")
    ActualFullName = step_output

    # 18. Compares '{ExpectedFullNm}' with '{ActualFullName}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedFullNm}',
            secondString=f'{ActualFullName}',
            ignoreCase=False,
            expectedResult=0))

    # 19. Does 'Enabled2' contain 'Enabled'?
    enabled2 = driver.find_element(By.XPATH,
                                   "//span/span[. = 'Enabled']")
    step_output = enabled2.text
    assert step_output and ("Enabled" in step_output)

    # 20. Click 'crt'
    crt = driver.find_element(By.XPATH,
                              "//button[. = '\t\t\t\tCreate ']")
    crt.click()

    # 21. Click 'Pricing Rule'
    pricing_rule = driver.find_element(By.XPATH,
                                       "//li[1]/a[. = 'Pricing Rule']")
    pricing_rule.click()

    # 22. Does 'New Pricing Rule 1' contain 'New Pricing Rule 1'?
    new_pricing_rule_1 = driver.find_element(By.XPATH,
                                             "//div[. = 'New Pricing Rule 1']")
    step_output = new_pricing_rule_1.text
    assert step_output and ("New Pricing Rule 1" in step_output)

    # 23. Click 'INPUT137'
    input137 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div/div[1]/form/div[1]//input")
    input137.click()

    # 24. Generate random word
    step_output = driver.addons().execute(
        RandomDataGenerator.generateword(
        ))
    RandomTitle = step_output

    # 25. Type '{RandomTitle}' in 'INPUT137'
    input137 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div/div[1]/form/div[1]//input")
    input137.send_keys(f'{RandomTitle}')

    # 26. Get text from 'gettitle'
    # get text entered title in pricing rule screen
    gettitle = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div/div[1]/form/div[1]//input")
    step_output = gettitle.get_attribute("value")
    ExpectedTitle = step_output

    # 27. Click 'SELECT24'
    select24 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div[2]/div/select")
    select24.click()

    # 28. Click 'SELECT24'
    select24 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div[2]/div/select")
    select24.click()

    # 29. Click 'Add Row12'
    add_row12 = driver.find_element(By.XPATH,
                                    "//div[2]/form/div[2]//button[. = '\n\t\t\t\t\t\t\tAdd Row']")
    add_row12.click()

    # 30. Click 'DIV69'
    div69 = driver.find_element(By.XPATH,
                                "//div[2]/div/div[2]/div[2]/div//div[3]")
    div69.click()

    # 31. Type '[NONE]' in 'item code123'
    item_code123 = driver.find_element(By.XPATH,
                                       "//input[@placeholder = 'Item Code']")
    item_code123.send_keys(" ")

    # 32. Click 'LI21'
    li21 = driver.find_element(By.XPATH,
                               "//div[2]/div[1]/div/div/div[2]/div[1]/div//li[1]")
    li21.click()

    # 33. Click 'UOM'
    uom = driver.find_element(By.XPATH,
                              "//input[@placeholder = 'UOM']")
    uom.click()

    # 34. Type '[NONE]' in 'UOM'
    uom = driver.find_element(By.XPATH,
                              "//input[@placeholder = 'UOM']")
    uom.send_keys(" ")

    # 35. Click 'Gram'
    gram = driver.find_element(By.XPATH,
                               "//p[. = 'Nos']")
    gram.click()

    # 36. Click 'INPUT138'
    input138 = driver.find_element(By.XPATH,
                                   "//div[5]/div[2]/div[1]/form/div[1]/div/label//input")
    input138.click()

    # 37. Click 'INPUT138'
    input138 = driver.find_element(By.XPATH,
                                   "//div[5]/div[2]/div[1]/form/div[1]/div/label//input")
    input138.click()

    # 38. Click 'INPUT139'
    input139 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[1]/form/div[1]/div/div[2]/div/input")
    input139.click()

    # 39. Click 'INPUT139'
    input139 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[1]/form/div[1]/div/div[2]/div/input")
    input139.click()

    # 40. Click 'INPUT139'
    input139 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[1]/form/div[1]/div/div[2]/div/input")
    input139.click()

    # 41. Clear 'minqty123' contents
    # clear value from min qty
    minqty123 = driver.find_element(By.XPATH,
                                    "//div[6]/div[2]/div[1]/form/div[1]/div/div[2]/div/input")
    minqty123.clear()

    # 42. Type '10.00' in 'INPUT139'
    input139 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[1]/form/div[1]/div/div[2]/div/input")
    input139.send_keys("10.00")

    # 43. Click 'INPUT140'
    input140 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[1]/form/div[2]//input")
    input140.click()

    # 44. Clear 'INPUT140' contents
    input140 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[1]/form/div[2]//input")
    input140.clear()

    # 45. Type '100.00' in 'INPUT140'
    input140 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[1]/form/div[2]//input")
    input140.send_keys("100.00")

    # 46. Click 'INPUT141'
    input141 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[2]/form/div[1]//input")
    input141.click()

    # 47. Clear 'INPUT141' contents
    input141 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[2]/form/div[1]//input")
    input141.clear()

    # 48. Type '20.00' in 'INPUT141'
    input141 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[2]/form/div[1]//input")
    input141.send_keys("20.00")

    # 49. Click 'INPUT142'
    input142 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[2]/form/div[2]//input")
    input142.click()

    # 50. Clear 'INPUT142' contents
    input142 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[2]/form/div[2]//input")
    input142.clear()

    # 51. Type '200.00' in 'INPUT142'
    input142 = driver.find_element(By.XPATH,
                                   "//div[6]/div[2]/div[2]/form/div[2]//input")
    input142.send_keys("200.00")

    # 52. Click 'INPUT143'
    input143 = driver.find_element(By.XPATH,
                                   "//div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[7]/div[2]/div[1]/form/div[2]//input")
    input143.click()

    '''
    # (STEP DISABLED)
    # 53. Positive values for future and negative for past dates
    step_output = driver.addons().execute(
    GenerateDateTimeCurrentFutureOrPast.futurepastaction(
    days = 1,
    months = 0,
    years = 0,
    hours = 0,
    minutes = 0,
    format = "dd"))
    RandomValidTo = step_output
    '''

    # 54. Click '3019'
    _3019 = driver.find_element(By.XPATH,
                                "//div[5]/div[1]/div/div/div[32][. = '30']")
    _3019.click()

    # 55. Click 'INPUT144'
    input144 = driver.find_element(By.XPATH,
                                   "//div[7]/div[2]/div[2]/form/div[1]//input")
    input144.click()

    # 56. Type 'vap' in 'INPUT144'
    input144 = driver.find_element(By.XPATH,
                                   "//div[7]/div[2]/div[2]/form/div[1]//input")
    input144.send_keys("vap")

    # 57. Click 'VapeCo18'
    vapeco18 = driver.find_element(By.XPATH,
                                   "//li[. = 'VapeCo']")
    vapeco18.click()

    # 58. Click 'SELECT25'
    select25 = driver.find_element(By.XPATH,
                                   "//div[9]/div[2]/div[1]/form/div[1]//select")
    select25.click()

    # 59. Select the 'Discount Amount' option in 'SELECT25'
    select25 = driver.find_element(By.XPATH,
                                   "//div[9]/div[2]/div[1]/form/div[1]//select")
    Select(select25).select_by_value("Discount Amount")

    # 60. Click 'SELECT25'
    select25 = driver.find_element(By.XPATH,
                                   "//div[9]/div[2]/div[1]/form/div[1]//select")
    select25.click()

    # 61. Click 'INPUT145'
    input145 = driver.find_element(By.XPATH,
                                   "//div[2]/form/div[3]/div/div[2]/div/input")
    input145.click()

    # 62. Clear 'INPUT145' contents
    input145 = driver.find_element(By.XPATH,
                                   "//div[2]/form/div[3]/div/div[2]/div/input")
    input145.clear()

    # 63. Type '5.00' in 'INPUT145'
    input145 = driver.find_element(By.XPATH,
                                   "//div[2]/form/div[3]/div/div[2]/div/input")
    input145.send_keys("5.00")

    # 64. Does 'Not Saved11' contain 'Not Saved'?
    not_saved11 = driver.find_element(By.XPATH,
                                      "//span/span[. = 'Not Saved']")
    step_output = not_saved11.text
    assert step_output and ("Not Saved" in step_output)

    # 65. Click 'Save23'
    save23 = driver.find_element(By.XPATH,
                                 "//div[4]//button[2][. = 'Save']")
    save23.click()

    # 66. Click 'Save23'
    save23 = driver.find_element(By.XPATH,
                                 "//div[4]//button[2][. = 'Save']")
    save23.click()

    # 67. Get text from 'Title'
    title = driver.find_element(By.XPATH,
                                "//h1//div[. = 'Title']")
    step_output = title.get_attribute("value")
    ActualTitle = step_output

    # 68. Compares '{ExpectedTitle}' with '{ActualTitle}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedTitle}',
            secondString=f'{ActualTitle}',
            ignoreCase=False,
            expectedResult=0))

    # 69. Click 'Save23'
    save23 = driver.find_element(By.XPATH,
                                 "//div[4]//button[2][. = 'Save']")
    save23.click()

    # 70. Does 'Saved9' contain 'Saved'?
    saved9 = driver.find_element(By.XPATH,
                                 "//div[4]/div[. = 'Saved']")
    step_output = saved9.text
    assert step_output and ("Saved" in step_output)

    # 71. Logout from the application
    test_logout.test_main(driver)

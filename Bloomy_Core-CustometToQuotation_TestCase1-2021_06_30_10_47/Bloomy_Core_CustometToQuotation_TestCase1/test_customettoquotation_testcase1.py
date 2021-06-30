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
    Test: CustometToQuotation_TestCase1
    Generated by: Meenal Kardale (meenal.kardale@extrapreneurs-india.com)
    Generated on 06/30/2021, 10:47:32
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="3J0RNM_48lLt_KM5Ab6s6A_HZzddmktVs_HhX77AjTM",
                              project_name="Bloomy_Core",
                              job_name="CustometToQuotation_TestCase1")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """1. Go to the customer doctype.(Desk>> Selling>>Customer) or Type \"customer in search bar\".

    2. Open Customer.3.Click on + Sign with quotation on customer doctype.  It will redirect you to on Quotation doctype.4. Customer name will be fetched from the customer 5. Select company.6. Select Requested Delivery Date.7. Select \"\" Valid Till date\"\"should be future date.8. Add items and Qty.9. Save and Submit.
    """
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io/"
    ExpectedFullName = ""
    ActualFullName = ""
    username = ""
    pwd = ""
    RandomCustFullName = ""
    ActualcustnameonCustomerpage = ""
    Actualcustnmtwo = ""
    actualcustnm1 = ""
    daydelidate = ""
    dayvalidtill = ""

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

    # 9. Click 'INPUT101'
    input101 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div[2]/div[1]/form/div[3]//input")
    input101.click()

    # 10. Generate random name
    step_output = driver.addons().execute(
        RandomDataGenerator.generatename(
        ))
    RandomCustFullName = step_output

    # 11. Type '{RandomCustFullName}' in 'INPUT101'
    input101 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div[2]/div[1]/form/div[3]//input")
    input101.send_keys(f'{RandomCustFullName}')

    # 12. Get text from 'INPUT101'
    input101 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div[2]/div[1]/form/div[3]//input")
    step_output = input101.get_attribute("value")
    ExpectedFullName = step_output

    # 13. Does 'New Customer 1' contain 'New Customer 1'?
    new_customer_1 = driver.find_element(By.XPATH,
                                         "//div[. = 'New Customer 1']")
    step_output = new_customer_1.text
    assert step_output and ("New Customer 1" in step_output)

    # 14. Does 'Not Saved2' contain 'Not Saved'?
    not_saved2 = driver.find_element(By.XPATH,
                                     "//span/span[. = 'Not Saved']")
    step_output = not_saved2.text
    assert step_output and ("Not Saved" in step_output)

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

    # 19. Clear 'clearcustgroup' contents
    clearcustgroup = driver.find_element(By.XPATH,
                                         "//div[3]/div[2]/div[2]/form/div[2]/div/div[2]/div[1]/div//input")
    clearcustgroup.clear()

    # 20. Click 'click23'
    click23 = driver.find_element(By.XPATH,
                                  "//div[3]/div[2]/div[2]/form/div[2]/div/div[2]/div[1]/div//input")
    click23.click()

    # 21. Click 'Self'
    self = driver.find_element(By.XPATH,
                               "//li[. = 'Self']")
    self.click()

    # 22. Click 'INPUT103'
    input103 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div[2]/div[2]/form/div[3]//input")
    input103.click()

    # 23. Clear 'cleartext12' contents
    cleartext12 = driver.find_element(By.XPATH,
                                      "//div[3]/div/div/div[2]/div[3]/div[2]/div[2]/form/div[3]//input")
    cleartext12.clear()

    # 24. Click 'click456'
    click456 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div/div[2]/div[3]/div[2]/div[2]/form/div[3]//input")
    click456.click()

    # 25. Click 'LI11'
    li11 = driver.find_element(By.XPATH,
                               "//div[3]/div/div[2]/div[1]/div/div/ul/li[2]")
    li11.click()

    # 26. Click 'Save13'
    save13 = driver.find_element(By.XPATH,
                                 "//button[2][. = 'Save']")
    save13.click()

    # 27. Get text from 'testnmm'
    testnmm = driver.find_element(By.XPATH,
                                  "//h1//div[. = 'testnmm']")
    step_output = testnmm.get_attribute("value")
    ActualFullName = step_output

    # 28. Does 'Enabled2' contain 'Enabled'?
    enabled2 = driver.find_element(By.XPATH,
                                   "//span/span[. = 'Enabled']")
    step_output = enabled2.text
    assert step_output and ("Enabled" in step_output)

    # 29. Click '1'
    _1 = driver.find_element(By.XPATH,
                             "//div[1]/div[2]/button[. = '        ']")
    _1.click()

    # 30. Click 'INPUT104'
    input104 = driver.find_element(By.XPATH,
                                   "//div[3]/div/div[1]/form/div[4]//input")
    input104.click()

    # 31. Get text from 'custnametwo'
    custnametwo = driver.find_element(By.XPATH,
                                      "//div[3]/div/div[1]/form/div[4]//input")
    step_output = custnametwo.get_attribute("value")
    Actualcustnmtwo = step_output

    # 32. Click 'testnmm1'
    testnmm1 = driver.find_element(By.XPATH,
                                   "//div[5]//div[. = 'testnmm']")
    testnmm1.click()

    # 33. Get text from 'customername'
    customername = driver.find_element(By.XPATH,
                                       "//div[5]//div[. = 'testnmm']")
    step_output = customername.get_attribute("value")
    ActualcustnameonCustomerpage = step_output

    # 34. Click 'INPUT78'
    input78 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[3]/div/div[2]/form/div[2]//input")
    input78.click()

    # 35. Type 'vap' in 'INPUT78'
    input78 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[3]/div/div[2]/form/div[2]//input")
    input78.send_keys("vap")

    # 36. Click 'VapeCo10'
    vapeco10 = driver.find_element(By.XPATH,
                                   "//li[. = 'VapeCo']")
    vapeco10.click()

    # 37. Click 'INPUT105'
    input105 = driver.find_element(By.XPATH,
                                   "//div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[3]/div/div[2]/form/div[4]//input")
    input105.click()

    # 38. Positive values for future and negative for past dates
    step_output = driver.addons().execute(
        GenerateDateTimeCurrentFutureOrPast.futurepastaction(
            days=5,
            months=0,
            years=0,
            hours=0,
            minutes=0,
            format="dd"))
    daydelidate = step_output

    # 39. Click '304'
    _304 = driver.find_element(By.XPATH,
                               f'//div[5]/div[1]/div/div/div[. = {daydelidate}]')
    _304.click()

    # 40. Click 'INPUT106'
    input106 = driver.find_element(By.XPATH,
                                   "//div[5]/div/div[2]/div/input")
    input106.click()

    # 41. Positive values for future and negative for past dates
    step_output = driver.addons().execute(
        GenerateDateTimeCurrentFutureOrPast.futurepastaction(
            days=5,
            months=0,
            years=0,
            hours=0,
            minutes=0,
            format="dd"))
    dayvalidtill = step_output

    # 42. Click '312'
    _312 = driver.find_element(By.XPATH,
                               f'//div[. = {dayvalidtill}]')
    _312.click()

    # 43. Click 'Add Row8'
    add_row8 = driver.find_element(By.XPATH,
                                   "//div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]//button[. = '\n\t\t\t\t\t\t\tAdd Row']")
    add_row8.click()

    # 44. Click 'DIV27'
    div27 = driver.find_element(By.XPATH,
                                "//form/div/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div27.click()

    # 45. Type '[NONE]' in 'Item Code'
    item_code = driver.find_element(By.XPATH,
                                    "//input[@placeholder = 'Item Code']")
    item_code.send_keys(" ")

    # 46. Click 'P9'
    p9 = driver.find_element(By.XPATH,
                             "//div[1]/div/div/div/ul/li[1]/a/p")
    p9.click()

    # 47. Compares '{ExpectedFullName}' with '{ActualFullName}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedFullName}',
            secondString=f'{ActualFullName}',
            ignoreCase=False,
            expectedResult=0))

    # 48. Compares '{ExpectedFullName}' with '{ActualcustnameonCustomerpage}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedFullName}',
            secondString=f'{ActualcustnameonCustomerpage}',
            ignoreCase=False,
            expectedResult=0))

    # 49. Compares '{ExpectedFullName}' with '{Actualcustnmtwo}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedFullName}',
            secondString=f'{Actualcustnmtwo}',
            ignoreCase=False,
            expectedResult=0))

    # 50. Click 'Save23'
    save23 = driver.find_element(By.XPATH,
                                 "//div[4]//button[2][. = 'Save']")
    save23.click()

    # 51. Click 'Close3'
    close3 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div//span[. = 'Close']")
    close3.click()

    # 52. Does 'Draft1' contain 'Draft'?
    draft1 = driver.find_element(By.XPATH,
                                 "//span/span[. = 'Draft']")
    step_output = draft1.text
    assert step_output and ("Draft" in step_output)

    # 53. Click 'Submit4'
    submit4 = driver.find_element(By.XPATH,
                                  "//button[. = 'Submit']")
    submit4.click()

    # 54. Click 'Yes1'
    yes1 = driver.find_element(By.XPATH,
                               "//button[. = 'Yes']")
    yes1.click()

    # 55. Click 'Close3'
    close3 = driver.find_element(By.XPATH,
                                 "//div[2]/div/div//span[. = 'Close']")
    close3.click()

    # 56. Does 'Open' contain 'Open'?
    open = driver.find_element(By.XPATH,
                               "//span/span[. = 'Open']")
    step_output = open.text
    assert step_output and ("Open" in step_output)

    # 57. Logout from the application
    test_logout.test_main(driver)
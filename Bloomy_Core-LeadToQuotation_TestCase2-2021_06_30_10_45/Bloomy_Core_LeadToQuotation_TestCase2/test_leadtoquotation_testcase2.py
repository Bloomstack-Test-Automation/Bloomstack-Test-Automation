from addons.generate_date_time_current_future_or_past_ import GenerateDateTimeCurrentFutureOrPast
from addons.random_data_generator import RandomDataGenerator
from addons.string_utils import StringUtils
from distutils.util import strtobool
from selenium.webdriver.common.by import By
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
    Test: LeadToQuotation_TestCase2
    Generated by: Meenal Kardale (meenal.kardale@extrapreneurs-india.com)
    Generated on 06/30/2021, 10:45:18
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="3J0RNM_48lLt_KM5Ab6s6A_HZzddmktVs_HhX77AjTM",
                              project_name="Bloomy_Core",
                              job_name="LeadToQuotation_TestCase2")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """1. Go to the lead doctype.(Desk>> CRM>>Lead) or Type \"Lead in search bar\".

     2.Open Lead. 3.Click on the \"\"+\"\" sign with Quotation on Lead Dashboard.  It will redirect you to on Quotation doctype. 4 Lead ID and customer name will be fetched from the lead .address and contact will fetch from Lead doctype 5.Select company. 6.Select Requested Delivery Date. 7. Select \"\" Valid Till date\"\"should be future date. 8.Add items and Qty and Rate. 9. Add Cover tax, coupon code and payment term 10.Save and Submit.
    """
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://epitest-demo.bloomstack.io/"
    ExpectedLeadNm = ""
    ExpectedLeadMobile = ""
    ActualLeadNm = ""
    ExpectedLeadID = ""
    ActualLeadNmQuotation = ""
    username = ""
    pwd = ""
    ActualLeadIDQuotation = ""
    ActualLeadNameQuotation = ""
    ActualMobileNoQuotation = ""
    RandomLeadName = ""
    DeliveryDateFuture = ""
    ValidTillDateFuture = ""

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Login to the Application
    test_login.test_main(driver)

    # 3. Click 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.click()

    # 4. Type 'lead li' in 'Search or type a command (Ctrl + G)'
    search_or_type_a_command_ctrl_g_ = driver.find_element(By.CSS_SELECTOR,
                                                           "#navbar-search")
    search_or_type_a_command_ctrl_g_.send_keys("lead li")

    # 5. Click 'Lead List'
    lead_list = driver.find_element(By.XPATH,
                                    "//li[. = 'Lead List']")
    lead_list.click()

    # 6. Does 'Lead7' contain 'Lead'?
    lead7 = driver.find_element(By.XPATH,
                                "//div[. = 'Lead']")
    step_output = lead7.text
    assert step_output and ("Lead" in step_output)

    # 7. Click 'New4'
    new4 = driver.find_element(By.XPATH,
                               "//button[. = 'New']")
    new4.click()

    # 8. Does 'Not Saved' contain 'Not Saved'?
    not_saved = driver.find_element(By.XPATH,
                                    "//span/span[. = 'Not Saved']")
    step_output = not_saved.text
    assert step_output and ("Not Saved" in step_output)

    # 9. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 10. Click 'INPUT64'
    input64 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[1]/form/div[2]//input")
    input64.click()

    # 11. Generate random name
    step_output = driver.addons().execute(
        RandomDataGenerator.generatename(
        ))
    RandomLeadName = step_output

    # 12. Type '{RandomLeadName}' in 'INPUT64'
    input64 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[1]/form/div[2]//input")
    input64.send_keys(f'{RandomLeadName}')

    # 13. Get text from 'INPUT64'
    input64 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[1]/form/div[2]//input")
    step_output = input64.get_attribute("value")
    ExpectedLeadNm = step_output

    # 14. Click 'INPUT67'
    input67 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[1]//input")
    input67.click()

    # 15. Type 'Address Test' in 'INPUT67'
    input67 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[1]//input")
    input67.send_keys("Address Test")

    # 16. Click 'INPUT68'
    input68 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[2]//input")
    input68.click()

    # 17. Type 'Address 1' in 'INPUT68'
    input68 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[2]//input")
    input68.send_keys("Address 1")

    # 18. Click 'INPUT69'
    input69 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[3]//input")
    input69.click()

    # 19. Type 'Address 2' in 'INPUT69'
    input69 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[3]//input")
    input69.send_keys("Address 2")

    # 20. Click 'INPUT70'
    input70 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[4]//input")
    input70.click()

    # 21. Type 'mumbai' in 'INPUT70'
    input70 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[4]//input")
    input70.send_keys("mumbai")

    # 22. Click 'INPUT71'
    input71 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[5]//input")
    input71.click()

    # 23. Type 'india' in 'INPUT71'
    input71 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[1]/form/div[5]//input")
    input71.send_keys("india")

    # 24. Click 'INPUT72'
    input72 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[2]/form/div[1]//input")
    input72.click()

    # 25. Type 'maharastra' in 'INPUT72'
    input72 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[2]/form/div[1]//input")
    input72.send_keys("maharastra")

    # 26. Click 'INPUT73'
    input73 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[2]/form/div[2]//input")
    input73.click()

    # 27. Clear 'CountryList' contents
    countrylist = driver.find_element(By.XPATH,
                                      "//div[7]/div[2]/div[2]/form/div[2]//input")
    countrylist.clear()

    # 28. Type 'indi' in 'INPUT73'
    input73 = driver.find_element(By.XPATH,
                                  "//div[7]/div[2]/div[2]/form/div[2]//input")
    input73.send_keys("indi")

    # 29. Click 'India'
    india = driver.find_element(By.XPATH,
                                "//li[. = 'India']")
    india.click()

    # 30. Click 'INPUT74'
    input74 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[3]/div/div[2]/div/input")
    input74.click()

    # 31. Type '40066' in 'INPUT74'
    input74 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[3]/div/div[2]/div/input")
    input74.send_keys("40066")

    # 32. Click 'INPUT75'
    input75 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[1]//input")
    input75.click()

    # 33. Type '1234567898' in 'INPUT75'
    input75 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[1]//input")
    input75.send_keys("1234567898")

    # 34. Click 'INPUT76'
    input76 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[2]//input")
    input76.click()

    # 35. Type '9876543234' in 'INPUT76'
    input76 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[2]//input")
    input76.send_keys("9876543234")

    # 36. Get text from 'INPUT76'
    input76 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[2]//input")
    step_output = input76.get_attribute("value")
    ExpectedLeadMobile = step_output

    # 37. Click 'INPUT77'
    input77 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[3]//input")
    input77.click()

    # 38. Type '4455' in 'INPUT77'
    input77 = driver.find_element(By.XPATH,
                                  "//div[8]/div[2]/div/form/div[3]//input")
    input77.send_keys("4455")

    # 39. Click 'SaveButton'
    savebutton = driver.find_element(By.XPATH,
                                     "//button[. = 'Save']")
    savebutton.click()

    '''
    # (STEP DISABLED)
    # 40. Click 'Save123'
    save123 = driver.find_element(By.XPATH,
    "//button[. = 'Save']")
    save123.click()
    '''

    # 41. Get text from 'Person Test'
    person_test = driver.find_element(By.XPATH,
                                      "//h1//div[. = 'Person Test']")
    step_output = person_test.get_attribute("value")
    ActualLeadNm = step_output

    # 42. Does 'Lead8' contain 'Lead'?
    lead8 = driver.find_element(By.XPATH,
                                "//span/span[. = 'Lead']")
    step_output = lead8.text
    assert step_output and ("Lead" in step_output)

    # 43. Get text from 'CRM-LEAD-2021-00355'
    crm_lead_2021_00355 = driver.find_element(By.XPATH,
                                              "//h6[. = 'CRM-LEAD-2021-00355']")
    step_output = crm_lead_2021_00355.get_attribute("value")
    ExpectedLeadID = step_output

    # 44. Click 'I2'
    i2 = driver.find_element(By.XPATH,
                             "//div[5]/div/div/div/div/div[2]//i")
    i2.click()

    # 45. Click 'INPUT78'
    input78 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[3]/div/div[2]/form/div[2]//input")
    input78.click()

    # 46. Type 'vap' in 'INPUT78'
    input78 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[3]/div/div[2]/form/div[2]//input")
    input78.send_keys("vap")

    # 47. Click 'VapeCo8'
    vapeco8 = driver.find_element(By.XPATH,
                                  "//li[. = 'VapeCo']")
    vapeco8.click()

    # 48. Click 'INPUT90'
    input90 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[4]/div/div[2]/div/input")
    input90.click()

    # 49. Positive values for future and negative for past dates
    step_output = driver.addons().execute(
        GenerateDateTimeCurrentFutureOrPast.futurepastaction(
            days=5,
            months=0,
            years=0,
            hours=0,
            minutes=0,
            format="dd"))
    DeliveryDateFuture = step_output

    # 50. Click '302'
    _302 = driver.find_element(By.XPATH,
                               f'//div[5]//div[. = {DeliveryDateFuture}]')
    _302.click()

    # 51. Click 'INPUT91'
    input91 = driver.find_element(By.XPATH,
                                  "//div[2]/form/div[5]/div/div[2]/div/input")
    input91.click()

    # 52. Positive values for future and negative for past dates
    step_output = driver.addons().execute(
        GenerateDateTimeCurrentFutureOrPast.futurepastaction(
            days=10,
            months=0,
            years=0,
            hours=0,
            minutes=0,
            format="dd"))
    ValidTillDateFuture = step_output

    # 53. Click '303'
    _303 = driver.find_element(By.XPATH,
                               f'//div[. = {ValidTillDateFuture}]')
    _303.click()

    # 54. Click 'SPAN7'
    span7 = driver.find_element(By.XPATH,
                                "//div[4]/div[1]/span")
    span7.click()

    # 55. Click 'contactspan12'
    contactspan12 = driver.find_element(By.XPATH,
                                        "//div[4]/div/span")
    contactspan12.click()

    # 56. Get text from 'GetMobileNoQuotation1'
    getmobilenoquotation1 = driver.find_element(By.XPATH,
                                                "//div[2]/div[1]/form/div[5]/div/div/div[2]")
    step_output = getmobilenoquotation1.get_attribute("value")
    ActualMobileNoQuotation = step_output

    # 57. Click 'Add Row'
    add_row = driver.find_element(By.XPATH,
                                  "//div[6]//button[. = '\n\t\t\t\t\t\t\tAdd Row']")
    add_row.click()

    # 58. Click 'DIV30'
    div30 = driver.find_element(By.XPATH,
                                "//form/div/div/div[2]/div[2]/div[1]/div/div/div[2]")
    div30.click()

    # 59. Click 'VC-RM-FO-00011'
    vc_rm_fo_00011 = driver.find_element(By.XPATH,
                                         "//strong[. = 'VC-RM-FO-0001']")
    vc_rm_fo_00011.click()

    # 60. Click 'INPUT79'
    input79 = driver.find_element(By.XPATH,
                                  "//div[4]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[9]/div[2]/div[1]//input")
    input79.click()

    # 61. Click 'Use tax'
    use_tax = driver.find_element(By.XPATH,
                                  "//p[. = 'Use tax']")
    use_tax.click()

    # 62. Click 'INPUT82'
    input82 = driver.find_element(By.XPATH,
                                  "//div[10]/div/div/form/div[1]//input")
    input82.click()

    # 63. Click 'US ST 6% - VC1'
    us_st_6_vc1 = driver.find_element(By.XPATH,
                                      "//li[. = 'US ST 6% - VC']")
    us_st_6_vc1.click()

    # 64. Click 'INPUT80'
    input80 = driver.find_element(By.XPATH,
                                  "//div[10]/div/div/form/div[2]//input")
    input80.click()

    # 65. Click 'INPUT92'
    input92 = driver.find_element(By.XPATH,
                                  "//div[15]/div[2]/div/form/div[1]//input")
    input92.click()

    # 66. Click 'Net 14'
    net_14 = driver.find_element(By.XPATH,
                                 "//li[. = 'Net 14']")
    net_14.click()

    # 67. Click 'SPAN8'
    span8 = driver.find_element(By.XPATH,
                                "//div[13]/div/span")
    span8.click()

    # 68. Click 'INPUT83'
    input83 = driver.find_element(By.XPATH,
                                  "//div[13]/div[2]/div[1]/form/div[1]//input")
    input83.click()

    # 69. Click 'INPUT83'
    input83 = driver.find_element(By.XPATH,
                                  "//div[13]/div[2]/div[1]/form/div[1]//input")
    input83.click()

    # 70. Type '[NONE]' in 'INPUT83'
    input83 = driver.find_element(By.XPATH,
                                  "//div[13]/div[2]/div[1]/form/div[1]//input")
    input83.send_keys(" ")

    # 71. Click 'EPI_Coupon@011'
    epi_coupon_011 = driver.find_element(By.XPATH,
                                         "//li[. = 'EPI_Coupon@01']")
    epi_coupon_011.click()

    # 72. Get text from 'GetLeadIDQuotation'
    # LeadIDQuotation
    getleadidquotation = driver.find_element(By.XPATH,
                                             "//div[1]/form/div[4]/div/div[2]/div[1]/div//input")
    step_output = getleadidquotation.get_attribute("value")
    ActualLeadIDQuotation = step_output

    # 73. Get text from 'GetCustNameQuotation'
    # CustomerNameQuotation
    getcustnamequotation = driver.find_element(By.XPATH,
                                               "//div[3]/div/div[1]/form/div[5]/div/div/div[2]")
    step_output = getcustnamequotation.get_attribute("value")
    ActualLeadNameQuotation = step_output

    # 74. Does 'Not Saved1' contain 'Not Saved'?
    not_saved1 = driver.find_element(By.XPATH,
                                     "//span/span[. = 'Not Saved']")
    step_output = not_saved1.text
    assert step_output and ("Not Saved" in step_output)

    # 75. Click 'Save19'
    save19 = driver.find_element(By.XPATH,
                                 "//div[4]//button[. = 'Save']")
    save19.click()

    # 76. Get text from 'Person Test1'
    person_test1 = driver.find_element(By.XPATH,
                                       "//div[4]/div[1]/div/div//div[. = 'Person Test']")
    step_output = person_test1.get_attribute("value")
    ActualLeadNmQuotation = step_output

    # 77. Does 'Draft1' contain 'Draft'?
    draft1 = driver.find_element(By.XPATH,
                                 "//span/span[. = 'Draft']")
    step_output = draft1.text
    assert step_output and ("Draft" in step_output)

    # 78. Compares '{ExpectedLeadNm}' with '{ActualLeadNm}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedLeadNm}',
            secondString=f'{ActualLeadNm}',
            ignoreCase=False,
            expectedResult=0))

    # 79. Compares '{ExpectedLeadNm}' with '{ActualLeadNmQuotation}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedLeadNm}',
            secondString=f'{ActualLeadNmQuotation}',
            ignoreCase=False,
            expectedResult=0))

    # 80. Compares '{ExpectedLeadID}' with '{ActualLeadIDQuotation}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedLeadID}',
            secondString=f'{ActualLeadIDQuotation}',
            ignoreCase=False,
            expectedResult=0))

    # 81. Compares '{ExpectedLeadNm}' with '{ActualLeadNameQuotation}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedLeadNm}',
            secondString=f'{ActualLeadNameQuotation}',
            ignoreCase=False,
            expectedResult=0))

    # 82. Compares '{ExpectedLeadMobile}' with '{ActualMobileNoQuotation}'
    step_output = driver.addons().execute(
        StringUtils.comparetwostrings(
            firstString=f'{ExpectedLeadMobile}',
            secondString=f'{ActualMobileNoQuotation}',
            ignoreCase=False,
            expectedResult=0))

    # 83. Click 'Submit9'
    submit9 = driver.find_element(By.XPATH,
                                  "//button[. = 'Submit']")
    submit9.click()

    # 84. Click 'Yes'
    yes = driver.find_element(By.XPATH,
                              "//button[. = 'Yes']")
    yes.click()

    # 85. Is 'Quotation has been submitted successf...1' present?
    quotation_has_been_submitted_successf_1 = driver.find_element(By.XPATH,
                                                                  "//div[. = 'Quotation has been submitted successfully']")

    # 86. Does 'Open' contain 'Open'?
    open = driver.find_element(By.XPATH,
                               "//span/span[. = 'Open']")
    step_output = open.text
    assert step_output and ("Open" in step_output)

    # 87. Logout from the application
    test_logout.test_main(driver)
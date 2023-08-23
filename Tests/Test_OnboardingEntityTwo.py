import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass
from pageObjects.OnboardingEntityPage import OnboardingEntityPage


#Validating if inavlid GST error is received #PASS
class TestTwo(BaseClass):
    def test_onboardingEntity2(self):
        #login page
        log = self.getLogger()
        self.driver.find_element(By.ID, "mat-tab-label-0-1").click()
        self.driver.find_element(By.ID, "mat-input-1").send_keys("pisesumeet99@gmail.com")
        self.driver.find_element(By.ID, "mat-input-2").send_keys("123456")
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        #Invalid GST
        onboardPage = OnboardingEntityPage(self.driver)
        onboardPage.Onboardicon().click()
        onboardPage.OnboardEntity().click()
        GSTNumber = onboardPage.gst()
        GSTNumber.send_keys("12345678")
        log.info("GST Number")
        GSTNumber.send_keys(Keys.ENTER)
        GST = onboardPage.InvalidGST().text
        log.info("invalid GST")
        assert "Invalid GSTIN Number" in GST

#Validating typo in the error is received #FAIL
class TestThree(BaseClass):

    def test_onboardingEntity3(self):
        #login page
        log = self.getLogger()
        self.driver.find_element(By.ID, "mat-tab-label-0-1").click()
        self.driver.find_element(By.ID, "mat-input-1").send_keys("pisesumeet99@gmail.com")
        self.driver.find_element(By.ID, "mat-input-2").send_keys("123456")
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        #Invalid GST
        onboardPage = OnboardingEntityPage(self.driver)
        onboardPage.Onboardicon().click()
        onboardPage.OnboardEntity().click()
        GSTNumber = onboardPage.gst()
        GSTNumber.send_keys("12345678")
        GSTNumber.send_keys(Keys.ENTER)
        GST = onboardPage.InvalidGST().text
        print(GST)
        assert "Invalid GST IN Number" == GST
        log.info("Expected = Invalid GSTIN Number")


#Validating form submittion by just entering valid GST number #FAIL
class TestFour(BaseClass):

    def test_onboardingEntity4(self):
        #login page
        log = self.getLogger()
        self.driver.find_element(By.ID, "mat-tab-label-0-1").click()
        self.driver.find_element(By.ID, "mat-input-1").send_keys("pisesumeet99@gmail.com")
        self.driver.find_element(By.ID, "mat-input-2").send_keys("123456")
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()

        onboardPage = OnboardingEntityPage(self.driver)
        onboardPage.Onboardicon().click()
        onboardPage.OnboardEntity().click()
        GSTNumber = onboardPage.gst()
        GSTNumber.send_keys("27AAACT2727Q1ZW")
        log.info("Enter all the Credentials marked with Asterisk*")
        onboardPage.Submit().click()

#Validating if the checkbox is selected #FAIL
class TestFive(BaseClass):
    def test_onboardingEntity5(self):
        #login page
        log = self.getLogger()
        self.driver.find_element(By.ID, "mat-tab-label-0-1").click()
        self.driver.find_element(By.ID, "mat-input-1").send_keys("pisesumeet99@gmail.com")
        self.driver.find_element(By.ID, "mat-input-2").send_keys("123456")
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()

        onboardPage = OnboardingEntityPage(self.driver)
        onboardPage.Onboardicon().click()
        onboardPage.OnboardEntity().click()
        onboardPage.gst().send_keys("27AAACT2727Q1ZW")
        onboardPage.gstButton().click()
        checkbox= onboardPage.CorporateType()
        #checkbox.click()
        assert checkbox.is_selected()
        log.info("Checkbox is not selected")

#Validating if the checkbox is selected #PASS
class TestSix(BaseClass):
    def test_onboardingEntity6(self):
        #login page
        log = self.getLogger()
        self.driver.find_element(By.ID, "mat-tab-label-0-1").click()
        self.driver.find_element(By.ID, "mat-input-1").send_keys("pisesumeet99@gmail.com")
        self.driver.find_element(By.ID, "mat-input-2").send_keys("123456")
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()

        onboardPage = OnboardingEntityPage(self.driver)
        onboardPage.Onboardicon().click()
        onboardPage.OnboardEntity().click()
        onboardPage.gst().send_keys("27AAACT2727Q1ZW")
        onboardPage.gstButton().click()
        checkbox= onboardPage.CorporateType()
        checkbox.click()
        assert checkbox.is_selected()
        log.info("checkbox selected")

#Validating to click on submit button by keeping all fields empty #FAIL
class TestSeven(BaseClass):
    def test_onboardingEntity7(self):
        #login page
        log = self.getLogger()
        self.driver.find_element(By.ID, "mat-tab-label-0-1").click()
        self.driver.find_element(By.ID, "mat-input-1").send_keys("pisesumeet99@gmail.com")
        self.driver.find_element(By.ID, "mat-input-2").send_keys("123456")
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()

        onboardPage = OnboardingEntityPage(self.driver)
        onboardPage.Onboardicon().click()
        onboardPage.OnboardEntity().click()
        onboardPage.Submit().click()
        log.info("Enter all the fields marked with asterisk*")

#Entering all the fields but with invalid GST number and trying to submit
class TestEight(BaseClass):
    def test_onboardingEntity8(self):
        #login page
        log = self.getLogger()
        self.driver.find_element(By.ID, "mat-tab-label-0-1").click()
        self.driver.find_element(By.ID, "mat-input-1").send_keys("pisesumeet99@gmail.com")
        self.driver.find_element(By.ID, "mat-input-2").send_keys("123456")
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()

        #Entity details
        onboardPage = OnboardingEntityPage(self.driver)
        onboardPage.Onboardicon().click()
        onboardPage.OnboardEntity().click()
        onboardPage.gst().send_keys("123456789")
        onboardPage.gstButton().click()
        NatureOfBusiness = Select(onboardPage.natureofBusiness())
        NatureOfBusiness.select_by_visible_text("Manufacturing")


        # Incorporation date
        onboardPage.IncorportaionDate().click()
        onboardPage.MonthandYear1().click()
        onboardPage.PreviousYear1().click()
        onboardPage.SelectYear1().click()
        onboardPage.SelectMonth1().click()
        onboardPage.SelectDay1().click()

        wait = WebDriverWait(self.driver, 5)
        onboardPage.CorporateType().click()
        wait.until(expected_conditions.element_to_be_clickable((onboardPage.CorporateType())))
        onboardPage.Corporatelogo().send_keys("C://Users\pissumee\Pictures/logos/2017-logo-Tata-Motors.jpg")
        onboardPage.IconLogo().send_keys("C://Users\pissumee\Pictures/logos/2017-logo-Tata-Motors.jpg")

        CreditRating = Select(onboardPage.CreditID())
        CreditRating.select_by_index(1)
        AnnualTurnover = Select(onboardPage.AnnualTurnover())
        AnnualTurnover.select_by_index(1)

        #Business Commencement date
        time.sleep(1)
        onboardPage.CommencementDate().click()
        onboardPage.MonthandYear2().click()
        onboardPage.PreviousYear2().click()
        onboardPage.SelectYear2().click()
        onboardPage.SelectMonth2().click()
        onboardPage.SelectDay2().click()
        onboardPage.EntityCode().send_keys("1234")
        onboardPage.ApprovedLimit().send_keys("10000000")
        onboardPage.LoanAccountNo().send_keys("1234567890")
        onboardPage.EntityLimit().click()

        #address Information
        onboardPage.ContactPerson().send_keys("abc")
        onboardPage.ContactPhone().send_keys("9123456789")
        onboardPage.ContactEmail().send_keys("abc@gmail.com")

        # Authorised Personal Information
        Individualtype = Select(onboardPage.IndividualType())
        Individualtype.select_by_value("director")
        Applicanttype = Select(onboardPage.ApplicantType())
        Applicanttype.select_by_value("guarantor")
        relationship = Select(onboardPage.Relationship())
        relationship.select_by_visible_text("Other")

        time.sleep(2)
        onboardPage.AuthorizationChkBox().click()
        Title = Select(onboardPage.ApplicantTitle())
        Title.select_by_value("MR")
        onboardPage.ApplicantFirstname().send_keys("abc")
        onboardPage.ApplicantLastName().send_keys("xyz")
        onboardPage.ApplicantAadhar().send_keys("abc xyz")
        Gender = Select(onboardPage.ApplicantGender())
        Gender.select_by_value("1: Male")
        onboardPage.ApplicantEmail().send_keys("abc@gmail.com")
        onboardPage.ApplicantMobile().send_keys("9123456789")

        # date of birth
        onboardPage.Birthdate().click()
        onboardPage.MonthandYear3().click()
        onboardPage.PreviousYear3().click()
        onboardPage.SelectYear3().click()
        onboardPage.SelectMonth3().click()
        onboardPage.SelectDay3().click()

        onboardPage.PanNumber().send_keys("ABCDE1234F")
        onboardPage.DinNumber().send_keys("12345")
        onboardPage.Qualification()
        Qualification = Select(onboardPage.Qualification())
        Qualification.select_by_value("32")
        Religion = Select(onboardPage.Religion())
        Religion.select_by_value("HINDU")
        OwnershipOffice = Select(onboardPage.OfficeOwnership())
        OwnershipOffice.select_by_value("49")
        OwnershipResidense = Select(onboardPage.ResidenceOwnership())
        OwnershipResidense.select_by_value("49")
        onboardPage.AnnualIncome().send_keys("1000000")
        onboardPage.MotherName().send_keys("def")
        onboardPage.FatherName().send_keys("ghi")
        Maritalstatus = Select(onboardPage.MaritailStatus())
        Maritalstatus.select_by_value("SINGLE")
        time.sleep(1)
        onboardPage.Submit().click()












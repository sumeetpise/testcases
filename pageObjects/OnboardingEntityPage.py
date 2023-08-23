from selenium.webdriver.common.by import By


class OnboardingEntityPage:
    def __init__(self,driver):
        self.driver = driver


    Onboardingicon = (By.XPATH, "(//img[@alt='dashboard icon'])[4]")
    OnboardingEntity = (By.XPATH, "//a[text()='Onboarding Entity']")
    gstNumber = (By.XPATH, "//input[@placeholder='GSTIN']")
    gstBtn = (By.ID, "gstDetailBtn")
    # invalid GST
    invalidgst = (By.XPATH, "//div[text()='Invalid GSTIN Number']")
    businessName = (By.XPATH, "//input[@formcontrolname='entity_name']")
    business = (By.ID, "entitytype")
    datepicker1 = (By.XPATH, "(//*[name()='svg'][@class='mat-datepicker-toggle-default-icon ng-star-inserted'])[1]")
    mnthandyr1 = (By.XPATH, "//button[@aria-label='Choose month and year']/span[1]")
    previousYr1 = (By.XPATH, "//button[@aria-label='Previous 24 years']")
    Year1 = (By.XPATH, "//td[@aria-label='1985']")
    Month1 = (By.XPATH, "//td[@aria-label='Sat Jun 01 1985']")
    Day1 = (By.XPATH, "//td[@aria-label='Tue Jun 04 1985']")
    corporatetyp = (By.XPATH, "//input[@formcontrolname='is_msme']")
    logo = (By.XPATH, "//input[@formcontrolname='entityLogo']")
    Icon = (By.XPATH, "//input[@formcontrolname='entityIcon']")
    crdtID = (By.ID, "credit_id")
    Turnover = (By.XPATH, "//select[@formcontrolname='annual_turnover']")
    datepicker2 = (By.XPATH, "(//*[name()='svg'][@class='mat-datepicker-toggle-default-icon ng-star-inserted'])[2]")
    mnthandyr2 = (By.XPATH, "//button[@aria-label='Choose month and year']/span[1]")
    previousYr2 = (By.XPATH, "//button[@aria-label='Previous 24 years']")
    Year2 = (By.XPATH, "//td[@aria-label='1985']")
    Month2 = (By.XPATH, "//td[@aria-label='Sat Jun 01 1985']")
    Day2 = (By.XPATH, "//td[@aria-label='Tue Jun 04 1985']")
    Entitycde = (By.XPATH, "//input[@placeholder='Entity Code']")
    approvedLmt = (By.XPATH, "//input[@placeholder='Approved Limit']")
    loanAccntNo = (By.XPATH, "//input[@placeholder='Loan Account No']")
    entitylimit = (By.XPATH, "//input[@formcontrolname='entity_level_limit']")
    contactprsn = (By.XPATH, "//input[@placeholder='Contact Person']")
    contactphne = (By.XPATH, "//input[@formcontrolname='contact_person_phone']")
    contacteml = (By.XPATH, "//input[@placeholder='Contact Person Email']")
    individualtyp = (By.ID, "apType")
    applicanttyp = (By.ID, "applicant_type")
    relationshiptyp = (By.ID, "relationship_with_applicant")
    authorizedcheckbox = (By.XPATH, "//input[@formcontrolname='is_authorized']")
    aptitle = (By.XPATH, "//select[@formcontrolname='title']")
    apfirstname = (By.ID, "apFirstname")
    aplastname = (By.ID, "apLastname")
    apaadharname = (By.ID, "apaadhar_name")
    apgender = (By.XPATH, "//select[@formcontrolname='gender']")
    apemail = (By.ID, "apEmail")
    apmobileno = (By.ID, "mobile")
    datepicker3 = (By.XPATH, "(//*[name()='svg'][@class='mat-datepicker-toggle-default-icon ng-star-inserted'])[3]")
    mnthandyr3 = (By.XPATH, "//button[@aria-label='Choose month and year']/span[1]")
    previousYr3 = (By.XPATH, "//button[@aria-label='Previous 24 years']")
    Year3 = (By.XPATH, "//td[@aria-label='1997']")
    Month3 = (By.XPATH, "//td[@aria-label='Fri Aug 01 1997']")
    Day3 = (By.XPATH, "//td[@aria-label='Thu Aug 14 1997']")
    panNo = (By.XPATH, "//input[@name='PAN']")
    dinNo = (By.XPATH, "//input[@formcontrolname='din']")
    qualificatn = (By.ID, "Quali_id")
    religion = (By.XPATH, "//select[@formcontrolname='religion']")
    officeOwnrshp = (By.XPATH, "//select[@formcontrolname='ownership_office']")
    residenceOwnrshp = (By.XPATH, "//select[@formcontrolname='ownership_residence']")

    incomeAnnual = (By.XPATH, "//input[@placeholder='Income Per Annum']")
    motherNme = (By.XPATH, "//input[@placeholder='Mother Name']")
    fatherNme = (By.XPATH, "//input[@placeholder='Father Name']")
    maritialstats = (By.ID, "marital_status")
    submit = (By.XPATH, "//button[text()='Submit']")


    def Onboardicon(self):
        return self.driver.find_element(*OnboardingEntityPage.Onboardingicon)

    def OnboardEntity(self):
        return self.driver.find_element(*OnboardingEntityPage.OnboardingEntity)

    def gst(self):
        return self.driver.find_element(*OnboardingEntityPage.gstNumber)

    def InvalidGST(self):
        return self.driver.find_element(*OnboardingEntityPage.invalidgst)

    def gstButton(self):
        return self.driver.find_element(*OnboardingEntityPage.gstBtn)

    def BusinessName(self):
        return self.driver.find_element(*OnboardingEntityPage.businessName)

    def natureofBusiness(self):
        return self.driver.find_element(*OnboardingEntityPage.business)

    def IncorportaionDate(self):
        return self.driver.find_element(*OnboardingEntityPage.datepicker1)

    def MonthandYear1(self):
        return self.driver.find_element(*OnboardingEntityPage.mnthandyr1)

    def PreviousYear1(self):
        return self.driver.find_element(*OnboardingEntityPage.previousYr1)

    def SelectYear1(self):
        return self.driver.find_element(*OnboardingEntityPage.Year1)

    def SelectMonth1(self):
        return self.driver.find_element(*OnboardingEntityPage.Month1)

    def SelectDay1(self):
        return self.driver.find_element(*OnboardingEntityPage.Day1)

    def CorporateType(self):
        return self.driver.find_element(*OnboardingEntityPage.corporatetyp)

    def Corporatelogo(self):
        return self.driver.find_element(*OnboardingEntityPage.logo)

    def IconLogo(self):
        return self.driver.find_element(*OnboardingEntityPage.Icon)

    def CreditID(self):
        return self.driver.find_element(*OnboardingEntityPage.crdtID)

    def AnnualTurnover(self):
        return self.driver.find_element(*OnboardingEntityPage.Turnover)

    def CommencementDate(self):
        return self.driver.find_element(*OnboardingEntityPage.datepicker2)

    def MonthandYear2(self):
        return self.driver.find_element(*OnboardingEntityPage.mnthandyr2)

    def PreviousYear2(self):
        return self.driver.find_element(*OnboardingEntityPage.previousYr2)

    def SelectYear2(self):
        return self.driver.find_element(*OnboardingEntityPage.Year2)

    def SelectMonth2(self):
        return self.driver.find_element(*OnboardingEntityPage.Month2)

    def SelectDay2(self):
        return self.driver.find_element(*OnboardingEntityPage.Day2)

    def EntityCode(self):
        return self.driver.find_element(*OnboardingEntityPage.Entitycde)

    def ApprovedLimit(self):
        return self.driver.find_element(*OnboardingEntityPage.approvedLmt)

    def LoanAccountNo(self):
        return self.driver.find_element(*OnboardingEntityPage.loanAccntNo)

    def EntityLimit(self):
        return self.driver.find_element(*OnboardingEntityPage.entitylimit)

    def ContactPerson(self):
        return self.driver.find_element(*OnboardingEntityPage.contactprsn)

    def ContactPhone(self):
        return self.driver.find_element(*OnboardingEntityPage.contactphne)

    def ContactEmail(self):
        return self.driver.find_element(*OnboardingEntityPage.contacteml)

    def IndividualType(self):
        return self.driver.find_element(*OnboardingEntityPage.individualtyp)

    def ApplicantType(self):
        return self.driver.find_element(*OnboardingEntityPage.applicanttyp)

    def Relationship(self):
        return self.driver.find_element(*OnboardingEntityPage.relationshiptyp)

    def AuthorizationChkBox(self):
        return self.driver.find_element(*OnboardingEntityPage.authorizedcheckbox)

    def ApplicantTitle(self):
        return self.driver.find_element(*OnboardingEntityPage.aptitle)

    def ApplicantFirstname(self):
        return self.driver.find_element(*OnboardingEntityPage.apfirstname)

    def ApplicantLastName(self):
        return self.driver.find_element(*OnboardingEntityPage.aplastname)

    def ApplicantAadhar(self):
        return self.driver.find_element(*OnboardingEntityPage.apaadharname)

    def ApplicantGender(self):
        return self.driver.find_element(*OnboardingEntityPage.apgender)

    def ApplicantEmail(self):
        return self.driver.find_element(*OnboardingEntityPage.apemail)

    def ApplicantMobile(self):
        return self.driver.find_element(*OnboardingEntityPage.apmobileno)

    def Birthdate(self):
        return self.driver.find_element(*OnboardingEntityPage.datepicker3)

    def MonthandYear3(self):
        return self.driver.find_element(*OnboardingEntityPage.mnthandyr3)

    def PreviousYear3(self):
        return self.driver.find_element(*OnboardingEntityPage.previousYr3)

    def SelectYear3(self):
        return self.driver.find_element(*OnboardingEntityPage.Year3)

    def SelectMonth3(self):
        return self.driver.find_element(*OnboardingEntityPage.Month3)

    def SelectDay3(self):
        return self.driver.find_element(*OnboardingEntityPage.Day3)

    def PanNumber(self):
        return self.driver.find_element(*OnboardingEntityPage.panNo)

    def DinNumber(self):
        return self.driver.find_element(*OnboardingEntityPage.dinNo)

    def Qualification(self):
        return self.driver.find_element(*OnboardingEntityPage.qualificatn)

    def Religion(self):
        return self.driver.find_element(*OnboardingEntityPage.religion)

    def OfficeOwnership(self):
        return self.driver.find_element(*OnboardingEntityPage.officeOwnrshp)

    def ResidenceOwnership(self):
        return self.driver.find_element(*OnboardingEntityPage.residenceOwnrshp)

    def AnnualIncome(self):
        return self.driver.find_element(*OnboardingEntityPage.incomeAnnual)

    def MotherName(self):
        return self.driver.find_element(*OnboardingEntityPage.motherNme)

    def FatherName(self):
        return self.driver.find_element(*OnboardingEntityPage.fatherNme)

    def MaritailStatus(self):
        return self.driver.find_element(*OnboardingEntityPage.maritialstats)

    def Submit(self):
        return self.driver.find_element(*OnboardingEntityPage.submit)











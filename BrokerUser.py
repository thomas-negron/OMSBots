from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from settings import CLIENT_ID, LOGIN_ID, STRING
import pandas as pd
from selenium.webdriver.firefox.options import Options

def addBroker(entity, city, state, zip):
    # Click 'Add Organization' button
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_btnAddOrg_input"]').click()
    time.sleep(1)

    # Enter company name
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_tboNameRAD"]').send_keys(entity)
    time.sleep(1)

    # Enter city
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_ucOAddress_cbCity_Input"]').send_keys(city)
    time.sleep(2)
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_ucOAddress_lbState"]').click()
    time.sleep(2)

    # Find state
    myDriver.find_element(By.XPATH,
                          '//*[@id="ctl00__MainContent_uc_oms_cctr_ucOAddress_ddlState"]/span/span[2]').click()
    time.sleep(1)
    myDriver.find_element(By.XPATH, "//li[contains(.,'" + state + "')]").click()
    time.sleep(1)

    # Enter zipcode
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_ucOAddress_tbZIP"]').send_keys(zip)
    time.sleep(1)

    # Click dropdown button
    myDriver.find_element(By.XPATH,
                          '// *[ @ id = "ctl00__MainContent_uc_oms_cctr_ddOrgTypeCodeRAD"] / span / span[2]').click()
    time.sleep(1)

    # Click 'Broker'
    myDriver.find_element(By.XPATH,
                          '//*[@id="ctl00__MainContent_uc_oms_cctr_ddOrgTypeCodeRAD_DropDown"]/div/ul/li[4]').click()
    time.sleep(1)

    # Click save
    myDriver.find_element(By.XPATH, '// *[ @ id = "ctl00__MainContent_uc_oms_cctr_cmdOrgSaveRAD_input"]').click()
    time.sleep(2)

    # Click 'Customer Center' menu button
    myDriver.find_element(By.XPATH, '// *[ @ id = "ctl00_ucLeftMenu_rptMainMenu_ctl08_lbLeftMenuItem"]').click()
    time.sleep(1)


def addPerson(fname, lname, email, city, state, zip, recordType):
    # Click 'Add Person' button
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_btnAddPer_input"]').click()
    time.sleep(1)

    # Enter first name
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_tbpfnameRAD"]').send_keys(fname)
    time.sleep(1)

    # Enter last name
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_tbplnameRAD"]').send_keys(lname)
    time.sleep(1)

    # Enter email
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_tbpemailRAD"]').send_keys(email)
    time.sleep(1)

    # Enter city
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_ucPAddress_cbCity_Input"]').send_keys(city)
    time.sleep(2)
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_ucPAddress_lbState"]').click()
    time.sleep(2)

    # Find state
    myDriver.find_element(By.XPATH,
                          '//*[@id="ctl00__MainContent_uc_oms_cctr_ucPAddress_ddlState"]/span/span[2]').click()
    time.sleep(1)
    myDriver.find_element(By.XPATH, "//li[contains(.,'" + state + "')]").click()
    time.sleep(1)

    # Enter zipcode
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_ucPAddress_tbZIP"]').send_keys(zip)
    time.sleep(1)

    # Choose Person type
    myDriver.find_element(By.XPATH,
                          '// *[ @ id = "ctl00__MainContent_uc_oms_cctr_ddPertypeCodeRAD"] / span / span[2]').click()
    time.sleep(1)
    myDriver.find_element(By.XPATH,
                          '//*[@id="ctl00__MainContent_uc_oms_cctr_ddPertypeCodeRAD_DropDown"]/div/ul/li[4]').click()
    time.sleep(1)

    # Click save
    myDriver.find_element(By.XPATH, '// *[ @ id = "ctl00__MainContent_uc_oms_cctr_cmdPerSaveRAD_input"]').click()
    time.sleep(1)

    # Click 'Relationships'
    myDriver.find_element(By.XPATH, '// *[ @ id = "ctl00__MainContent_mnuDataTabs"] / ul / li[6] / a / span').click()
    time.sleep(1)

    # Click 'Add'
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_cmdRelationAdd_input"]').click()
    time.sleep(1)

    # Enter 'Relation to'
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_rcbRelationTOCOMBO_Input"]').send_keys(
        entity)
    time.sleep(4)
    myDriver.find_element(By.XPATH,
                          "//li[contains(.,'(O) " + entity + " " + city + " " + state + " " + zip + "')]").click()
    time.sleep(2)

    # Choose Relation type
    myDriver.find_element(By.XPATH,
                          '// *[ @ id = "ctl00__MainContent_uc_oms_cctr_ddlrelationtype"] / span / span[2]').click()
    time.sleep(2)
    myDriver.find_element(By.XPATH,
                          '// *[ @ id = "ctl00__MainContent_uc_oms_cctr_ddlrelationtype_DropDown"] / div / ul / li[9]').click()
    time.sleep(2)

    # Click save
    myDriver.find_element(By.XPATH, '//*[@id="ctl00__MainContent_uc_oms_cctr_cmdRelationSave_input"]').click()
    time.sleep(1)

    # Click 'Customer Center' menu button
    myDriver.find_element(By.XPATH, '// *[ @ id = "ctl00_ucLeftMenu_rptMainMenu_ctl08_lbLeftMenuItem"]').click()
    time.sleep(1)


# Set driver to use Firefox
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#myDriver = webdriver.Firefox(executable_path="/home/OMSBots/geckodriver.exe")
options = Options();
options.binary_location = r"C:home/OMSBots/firefox.exe"
myDriver = webdriver.Firefox(options=options, executable_path="C:home/OMSBots/geckodriver.exe")

firefox_options = webdriver.FirefoxOptions()
myDriver = webdriver.Remote(
    command_executor='http://10.116.0.2:4444',
    options=firefox_options
)
myDriver.get("http://www.google.com")

myDriver.maximize_window()

# Enter Client ID
myDriver.find_element(By.XPATH, '//*[@id="TanentID"]').send_keys(CLIENT_ID)
time.sleep(1)

# Enter Login ID
myDriver.find_element(By.XPATH, '//*[@id="LoginID"]').send_keys(LOGIN_ID)
time.sleep(1)

# Enter password
myDriver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(STRING)
time.sleep(1)

# Click login button
myDriver.find_element(By.XPATH, '/html/body/div/main/div/div/form/div[7]/div/button[1]').click()
time.sleep(1)

# Click 'Customer Center' b menu button
myDriver.find_element(By.XPATH, '//*[@id="ctl00_ucLeftMenu_rptMainMenu_ctl08_lbLeftMenuItem"]').click()
time.sleep(1)

df = pd.DataFrame(pd.read_csv(
    '/Users/richardthomas/Downloads/Broker Data Upload Sheet Scrubbed 2-11-22 lab_to_include_CyberBrokers.csv'))

for index, row in df.head(17).iterrows():
    entity = row['entityname']
    city = row['physicalcity']
    state = row['physicalstate']
    zip = str(row['physicalzip'])
    email = row['email']
    recordType = row['record_type']
    fname = row['first_name']
    lname = row['last_name']
    orgCode = row['organization_type_code']
    peopleCode = row['People_type_code']
    linkBroker = row['Link Broker and contact']

    if recordType == "O":
        addBroker(entity, city, state, zip[0:5])
    else:
        addPerson(fname, lname, email, city, state, zip[0:5], recordType)

myDriver.quit()

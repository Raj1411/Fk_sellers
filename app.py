import streamlit as st
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
import gspread
from oauth2client.service_account import ServiceAccountCredentials




st.title('Flipkart Sellers Check')
# chromedriver_autoinstaller.install()

# option=webdriver.ChromeOptions()
# option.add_argument('--headless')
# option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# option.add_argument('--disable-gpu')
# option.add_argument('--no-sandbox')
# option.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), options=option)

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
# s=Service("/home/appuser/.conda/bin/geckodriver")

# s=Service(geckodriver_autoinstaller.install())
# driver = webdriver.Firefox(service=s,options=firefoxOptions)


headers1 = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}



scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

txt_input = st.text_input("Enter list of all Flipkart FSN's: ")

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument("disable-gpu")


link = 'https://www.flipkart.com/sellers?pid='

x=1
if txt_input:
    txt_input = txt_input.split(" ")
    for i in txt_input:
        a = driver = webdriver.Firefox(executable_path="/home/appuser/.conda/bin/geckodriver",options=firefoxOptions)
        a.get(link+i,)
        sleep(1)
        a= driver = webdriver.Firefox(executable_path="/home/appuser/.conda/bin/geckodriver",options=firefoxOptions)
        a.get(link+str(i))
        b= a.page_source
        if b.find('SRASRAretail'):
            c = 'SRASRAretail Available'
            gc = gspread.service_account(filename="./creds.json")
            sh = gc.open("BSR Ref")
            ws = sh.worksheet("Sheet3")
            ws.update_cell(x, 1, c)

        else:
            c = 'SRASRAretail Not Available'
            gc = gspread.service_account(filename="./creds.json")
            sh = gc.open("BSR Ref")
            ws = sh.worksheet("Sheet3")
            ws.update_cell(x, 1, c)
        a.quit()

        x=x+1

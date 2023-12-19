from selenium import webdriver
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service


def find_ks_data(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    )

    service = Service('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
    service.start()


    driver = webdriver.Remote(service.service_url)
    driver.get(url)

    page_source = driver.page_source
    driver.quit()

    print('Finished Reading Website Data')

    # get the goodies 
    soup = BeautifulSoup(page_source, "html.parser")
    pledge_amount = soup.find('span', class_='ksr-green-500').get_text()
    backers = soup.find(class_='count').get_text()
    days_to_go = soup.find(class_='block type-16 type-28-md bold dark-grey-500').get_text()

    pledge_amount= int((pledge_amount.split(' ')[1]).replace(',',''))
    
    print(f"Pledge Amount: {pledge_amount}")
    print(f"Backers: {backers}")
    print(f"Days to Go: {days_to_go}")
    return pledge_amount, backers, days_to_go


    
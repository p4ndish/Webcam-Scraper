import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path = 'PATH' #    <------ your chrome driver path

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(path)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
}

req = requests.get('https://www.insecam.org/en/bycountry/US/', headers = headers)

for page in range(2, 5): #by changing the last value upto 623 u can get a list of urls for us country
    req = requests.get('https://www.insecam.org/en/bycountry/US/?page=' + str(page), headers = headers)

    

    soup = BeautifulSoup(req.text, 'html.parser')

    try:
        div = soup.find_all('div', class_='thumbnail-item__preview')

        for divs in div:
            img = divs.find('img', class_='thumbnail-item__img img-responsive')
            url = img.attrs['src']
            parse = urlparse(url)
            mainurl = parse.scheme + '://' + parse.netloc
            print(mainurl)
            s = mainurl + '\n'
            file = open('ips.txt', 'a')
            
            file.write(mainurl + '\n')
            file.close()
            driver.execute_script(f'window.open("{mainurl}", "_blank");')
    except Exception as identifier:
        pass
    

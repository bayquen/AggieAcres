from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

min_price_filter = 2000
max_price_filter = 2500

min_bed_filter = 1
max_bed_filter = 2

def scrape_apartments_website():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    # service = Service(executable_path="/Users/ethann/Desktop/hackdavis24/chromedriver")
    # driver = webdriver.Chrome(service=service)
    driver.get("https://www.apartments.com/davis-ca/")
    titles = driver.find_elements(By.CLASS_NAME, "property-address")
    prices = driver.find_elements(By.CLASS_NAME, "property-pricing")
    beds = driver.find_elements(By.CLASS_NAME, "property-beds")
    links = driver.find_elements(By.CLASS_NAME, "property-link")
    for title, price, bed in zip(titles, prices, beds):
        price_range = price.text.replace(",", "").replace("$", "").split(" - ")
        bed_text = bed.text.replace(" Beds", "")
        bed_range = bed_text.split("-")
        try:
            if len(price_range) == 2:
                min_price = float(price_range[0])
                max_price = float(price_range[1])
                price_value = (min_price + max_price) / 2
            else:
                price_value = float(price_range[0])
        except ValueError:
            price_value = None
            
        try:
            if bed_text.lower() == "studio":
                perfect_bed = None  
            else:
                if len(bed_range) == 2:
                    min_bed = float(bed_range[0])
                    max_bed = float(bed_range[1])
                    perfect_bed = (min_bed + max_bed) / 2
                else:
                    perfect_bed = float(bed_text)
        except ValueError:
            perfect_bed = None
            
        if price_value is not None and perfect_bed is not None:
            if (min_price_filter is None or min_price_filter <= price_value) and (max_price_filter is None or price_value <= max_price_filter) \
                    and (min_bed_filter is None or min_bed_filter <= perfect_bed) and (max_bed_filter is None or perfect_bed <= max_bed_filter):
                print("Address:", title.text)
                print("Price:", price.text)
                print("Beds:", bed.text)
                print()   
    
    driver.quit()
def scrape_other_website():
    service = Service(executable_path="/Users/ethann/Desktop/hackdavis24/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.trulia.com/for_rent/Davis,CA/")
    titles = driver.find_elements(By.CLASS_NAME, "property-address")
    prices = driver.find_elements(By.CLASS_NAME, "property-pricing")
    beds = driver.find_elements(By.CLASS_NAME, "property-beds")
    links = driver.find_elements(By.CLASS_NAME, "property-link")
    for title, price, bed in zip(titles, prices, beds):
        price_range = price.text.replace(",", "").replace("$", "").replace("/mo", "").split(" - ")
        bed_text = bed.text.replace("bd", "")
        bed_range = bed_text.split("-")
        try:
            if len(price_range) == 2:
                min_price = float(price_range[0])
                max_price = float(price_range[1])
                price_value = (min_price + max_price) / 2
            else:
                price_value = float(price_range[0])
        except ValueError:
            price_value = None
            
        try:
            if bed_text.lower() == "studio":
                perfect_bed = None  
            else:
                if len(bed_range) == 2:
                    min_bed = float(bed_range[0])
                    max_bed = float(bed_range[1])
                    perfect_bed = (min_bed + max_bed) / 2
                else:
                    perfect_bed = float(bed_text)
        except ValueError:
            perfect_bed = None
            
        if price_value is not None and perfect_bed is not None:
            if (min_price_filter is None or min_price_filter <= price_value) and (max_price_filter is None or price_value <= max_price_filter) \
                    and (min_bed_filter is None or min_bed_filter <= perfect_bed) and (max_bed_filter is None or perfect_bed <= max_bed_filter):
                print("Address:", title.text)
                print("Price:", price.text)
                print("Beds:", bed.text)
                print()   
    

    driver.quit()
    



if __name__ == "__main__":
    scrape_apartments_website()
    # scrape_other_website()
    

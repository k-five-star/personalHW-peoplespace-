from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv

# tickers
ticker = ['XLC', 'XLY', 'XLP', 'XLE', 'XLF', 'XLV', 'XLI', 'XLB', 'XLRE', 'XLK', 'XLU']
# XLC : communication services
# XLY : consumer discretionary
# XLP : consumer staples
# XLE : energy
# XLF : financials
# XLV : health care
# XLI : industrials
# XLB : materials
# XLRE : real estate
# XLK : technology
# XLU : utilities

stock_data = []

for stock in ticker:
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enables headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Specify the path to chromedriver using Service
    service = Service(executable_path='chromedriver.exe')


    # Initialize the browser with these options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    URL = f"https://finance.yahoo.com/quote/{stock}/history?period1=1579219200&period2=1705449600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
    # Open the target URL
    driver.get(URL)

    # Wait for the page to load
    time.sleep(10)

    # Extract data
    rows = driver.find_elements(By.CSS_SELECTOR, 'tr.BdT')

    for row in rows:
        # Extract each column data
        cols = row.find_elements(By.TAG_NAME, 'span')
        if len(cols) >= 6:
            date = cols[0].text
            open_price = cols[1].text
            high = cols[2].text
            low = cols[3].text
            close = cols[4].text
            volume = cols[5].text
            stock_data.append([stock, date, open_price, high, low, close, volume])

    # Close the browser
    driver.quit()

# Write to CSV
with open('stock_data.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    writer.writerows(stock_data)

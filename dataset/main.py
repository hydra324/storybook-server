import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
import logging
import pickle

# Set up logging
logging.basicConfig(level=logging.DEBUG,filename='dataset.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


# URL of the website you want to scrape
home_page = "https://www.letsreadasia.org/category/5728283396145152"
language_suffix = "?bookLang=4846240843956224"

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set up the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Send a GET request to the website
driver.get(home_page)
time.sleep(5)  # Adjust the sleep duration as needed

image_dict = []

# Find all divs with class name "AllBooksGrid_book_image"
book_container = driver.find_elements(By.XPATH, "//div[contains(@class, 'AllBooksGrid_book_image')]")

# Click on each div
for index in range(len(book_container)):
    logging.info(f"Scraping book {index+1}")
    allbooks = driver.find_elements(By.XPATH, "//div[contains(@class, 'AllBooksGrid_book_image')]")
    #click on indexth book
    allbooks[index].click()
    time.sleep(5)  # Adjust the sleep duration as needed
    # Click on the "Read" button
    read_button = driver.find_element(By.XPATH, "//button[contains(@class, 'BookDetailModel_btn')]")
    read_button.click()
    # Wait for the page to load
    time.sleep(5)  # Adjust the sleep duration as needed
    # Extract source and alt text of images with class name "bookreading_image"
    images = driver.find_elements(By.XPATH, "//img[contains(@class, 'bookreading_image')]")
    
    for image in images:
        src = image.get_attribute("src")
        alt = image.get_attribute("alt")
        image_dict.append([src,alt])

    # Log the image dictionary
    logging.info(image_dict)

    driver.get(home_page)
    time.sleep(5)  # Adjust the sleep duration as needed

# Save the image dictionary to a pickle file
with open('/home/akhil/Documents/storybook-server/dataset/image_dict.pickle', 'wb') as file:
    pickle.dump(image_dict, file)

# Close the Chrome driver
driver.quit()
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

# List of URLs to scrape
urls = [
        "https://odb.org/2024/07/20"
]

# Set up WebDriver
driver = webdriver.Chrome()

try:
    # Create a folder to store images if it doesn't exist
    image_folder = "images"
    os.makedirs(image_folder, exist_ok=True)

    # Loop through each URL
    for url in urls:
        print(f"Scraping URL: {url}")
        
        try:
            # Open the URL
            driver.get(url)

            # Wait until the 'sticky-parent' element is present
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "sticky-parent"))
            )

            # Extract the date part from the URL
            date_part = url.split("/")[-1]  # Example: '24'
            month_part = url.split("/")[-2]  # Example: '11'
            year_part = url.split("/")[-3]  # Example: '2024'

            # Format the file name for the image
            image_name = f"{year_part}_{month_part}_{date_part}.jpg"
            image_path = os.path.join(image_folder, image_name)

            # Locate the image with class 'today-img'
            try:
                image_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "today-img"))
                )
                image_url = image_element.get_attribute("src")  # Get the image URL
                
                # Download and save the image
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(image_path, "wb") as img_file:
                        img_file.write(response.content)
                    print(f"Image saved to {image_path}")
                else:
                    print(f"Failed to download image from {image_url}")
            except TimeoutException:
                print(f"Image with class 'today-img' not found on {url}")

        except TimeoutException:
            print(f"Timeout while waiting for sticky-parent on {url}. Skipping.")

finally:
    # Close the browser
    driver.quit()

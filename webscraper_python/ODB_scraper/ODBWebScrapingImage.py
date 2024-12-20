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
        "https://odb.org/2024/01/01",
        "https://odb.org/2024/01/02",
        "https://odb.org/2024/01/03",
        "https://odb.org/2024/01/04",
        "https://odb.org/2024/01/05",
        "https://odb.org/2024/01/06",
        "https://odb.org/2024/01/07",
        "https://odb.org/2024/01/08",
        "https://odb.org/2024/01/09",
        "https://odb.org/2024/01/10",
        "https://odb.org/2024/01/11",
        "https://odb.org/2024/01/12",
        "https://odb.org/2024/01/13",
        "https://odb.org/2024/01/14",
        "https://odb.org/2024/01/15",
        "https://odb.org/2024/01/16",
        "https://odb.org/2024/01/17",
        "https://odb.org/2024/01/18",
        "https://odb.org/2024/01/19",
        "https://odb.org/2024/01/20",
        "https://odb.org/2024/01/21",
        "https://odb.org/2024/01/22",
        "https://odb.org/2024/01/23",
        "https://odb.org/2024/01/24",
        "https://odb.org/2024/01/25",
        "https://odb.org/2024/01/26",
        "https://odb.org/2024/01/27",
        "https://odb.org/2024/01/28",
        "https://odb.org/2024/01/29",
        "https://odb.org/2024/01/30",
        "https://odb.org/2024/01/31",
        "https://odb.org/2024/02/01",
        "https://odb.org/2024/02/02",
        "https://odb.org/2024/02/03",
        "https://odb.org/2024/02/04",
        "https://odb.org/2024/02/05",
        "https://odb.org/2024/02/06",
        "https://odb.org/2024/02/07",
        "https://odb.org/2024/02/08",
        "https://odb.org/2024/02/09",
        "https://odb.org/2024/02/10",
        "https://odb.org/2024/02/11",
        "https://odb.org/2024/02/12",
        "https://odb.org/2024/02/13",
        "https://odb.org/2024/02/14",
        "https://odb.org/2024/02/15",
        "https://odb.org/2024/02/16",
        "https://odb.org/2024/02/17",
        "https://odb.org/2024/02/18",
        "https://odb.org/2024/02/19",
        "https://odb.org/2024/02/20",
        "https://odb.org/2024/02/21",
        "https://odb.org/2024/02/22",
        "https://odb.org/2024/02/23",
        "https://odb.org/2024/02/24",
        "https://odb.org/2024/02/25",
        "https://odb.org/2024/02/26",
        "https://odb.org/2024/02/27",
        "https://odb.org/2024/02/28",
        "https://odb.org/2024/02/29",
        "https://odb.org/2024/03/01",
        "https://odb.org/2024/03/02",
        "https://odb.org/2024/03/03",
        "https://odb.org/2024/03/04",
        "https://odb.org/2024/03/05",
        "https://odb.org/2024/03/06",
        "https://odb.org/2024/03/07",
        "https://odb.org/2024/03/08",
        "https://odb.org/2024/03/09",
        "https://odb.org/2024/03/10",
        "https://odb.org/2024/03/11",
        "https://odb.org/2024/03/12",
        "https://odb.org/2024/03/13",
        "https://odb.org/2024/03/14",
        "https://odb.org/2024/03/15",
        "https://odb.org/2024/03/16",
        "https://odb.org/2024/03/17",
        "https://odb.org/2024/03/18",
        "https://odb.org/2024/03/19",
        "https://odb.org/2024/03/20",
        "https://odb.org/2024/03/21",
        "https://odb.org/2024/03/22",
        "https://odb.org/2024/03/23",
        "https://odb.org/2024/03/24",
        "https://odb.org/2024/03/25",
        "https://odb.org/2024/03/26",
        "https://odb.org/2024/03/27",
        "https://odb.org/2024/03/28",
        "https://odb.org/2024/03/29",
        "https://odb.org/2024/03/30",
        "https://odb.org/2024/03/31",
        "https://odb.org/2024/04/01",
        "https://odb.org/2024/04/02",
        "https://odb.org/2024/04/03",
        "https://odb.org/2024/04/04",
        "https://odb.org/2024/04/05",
        "https://odb.org/2024/04/06",
        "https://odb.org/2024/04/07",
        "https://odb.org/2024/04/08",
        "https://odb.org/2024/04/09",
        "https://odb.org/2024/04/10",
        "https://odb.org/2024/04/11",
        "https://odb.org/2024/04/12",
        "https://odb.org/2024/04/13",
        "https://odb.org/2024/04/14",
        "https://odb.org/2024/04/15",
        "https://odb.org/2024/04/16",
        "https://odb.org/2024/04/17",
        "https://odb.org/2024/04/18",
        "https://odb.org/2024/04/19",
        "https://odb.org/2024/04/20",
        "https://odb.org/2024/04/21",
        "https://odb.org/2024/04/22",
        "https://odb.org/2024/04/23",
        "https://odb.org/2024/04/24",
        "https://odb.org/2024/04/25",
        "https://odb.org/2024/04/26",
        "https://odb.org/2024/04/27",
        "https://odb.org/2024/04/28",
        "https://odb.org/2024/04/29",
        "https://odb.org/2024/04/30",
        "https://odb.org/2024/05/01",
        "https://odb.org/2024/05/02",
        "https://odb.org/2024/05/03",
        "https://odb.org/2024/05/04",
        "https://odb.org/2024/05/05",
        "https://odb.org/2024/05/06",
        "https://odb.org/2024/05/07",
        "https://odb.org/2024/05/08",
        "https://odb.org/2024/05/09",
        "https://odb.org/2024/05/10",
        "https://odb.org/2024/05/11",
        "https://odb.org/2024/05/12",
        "https://odb.org/2024/05/13",
        "https://odb.org/2024/05/14",
        "https://odb.org/2024/05/15",
        "https://odb.org/2024/05/16",
        "https://odb.org/2024/05/17",
        "https://odb.org/2024/05/18",
        "https://odb.org/2024/05/19",
        "https://odb.org/2024/05/20",
        "https://odb.org/2024/05/21",
        "https://odb.org/2024/05/22",
        "https://odb.org/2024/05/23",
        "https://odb.org/2024/05/24",
        "https://odb.org/2024/05/25",
        "https://odb.org/2024/05/26",
        "https://odb.org/2024/05/27",
        "https://odb.org/2024/05/28",
        "https://odb.org/2024/05/29",
        "https://odb.org/2024/05/30",
        "https://odb.org/2024/05/31",
        "https://odb.org/2024/06/01",
        "https://odb.org/2024/06/02",
        "https://odb.org/2024/06/03",
        "https://odb.org/2024/06/04",
        "https://odb.org/2024/06/05",
        "https://odb.org/2024/06/06",
        "https://odb.org/2024/06/07",
        "https://odb.org/2024/06/08",
        "https://odb.org/2024/06/09",
        "https://odb.org/2024/06/10",
        "https://odb.org/2024/06/11",
        "https://odb.org/2024/06/12",
        "https://odb.org/2024/06/13",
        "https://odb.org/2024/06/14",
        "https://odb.org/2024/06/15",
        "https://odb.org/2024/06/16",
        "https://odb.org/2024/06/17",
        "https://odb.org/2024/06/18",
        "https://odb.org/2024/06/19",
        "https://odb.org/2024/06/20",
        "https://odb.org/2024/06/21",
        "https://odb.org/2024/06/22",
        "https://odb.org/2024/06/23",
        "https://odb.org/2024/06/24",
        "https://odb.org/2024/06/25",
        "https://odb.org/2024/06/26",
        "https://odb.org/2024/06/27",
        "https://odb.org/2024/06/28",
        "https://odb.org/2024/06/29",
        "https://odb.org/2024/06/30",
        "https://odb.org/2024/07/01",
        "https://odb.org/2024/07/02",
        "https://odb.org/2024/07/03",
        "https://odb.org/2024/07/04",
        "https://odb.org/2024/07/05",
        "https://odb.org/2024/07/06",
        "https://odb.org/2024/07/07",
        "https://odb.org/2024/07/08",
        "https://odb.org/2024/07/09",
        "https://odb.org/2024/07/10",
        "https://odb.org/2024/07/11",
        "https://odb.org/2024/07/12",
        "https://odb.org/2024/07/13",
        "https://odb.org/2024/07/14",
        "https://odb.org/2024/07/15",
        "https://odb.org/2024/07/16",
        "https://odb.org/2024/07/17",
        "https://odb.org/2024/07/18",
        "https://odb.org/2024/07/19",
        "https://odb.org/2024/07/20",
        "https://odb.org/2024/07/21",
        "https://odb.org/2024/07/22",
        "https://odb.org/2024/07/23",
        "https://odb.org/2024/07/24",
        "https://odb.org/2024/07/25",
        "https://odb.org/2024/07/26",
        "https://odb.org/2024/07/27",
        "https://odb.org/2024/07/28",
        "https://odb.org/2024/07/29",
        "https://odb.org/2024/07/30",
        "https://odb.org/2024/07/31",
        "https://odb.org/2024/08/01",
        "https://odb.org/2024/08/02",
        "https://odb.org/2024/08/03",
        "https://odb.org/2024/08/04",
        "https://odb.org/2024/08/05",
        "https://odb.org/2024/08/06",
        "https://odb.org/2024/08/07",
        "https://odb.org/2024/08/08",
        "https://odb.org/2024/08/09",
        "https://odb.org/2024/08/10",
        "https://odb.org/2024/08/11",
        "https://odb.org/2024/08/12",
        "https://odb.org/2024/08/13",
        "https://odb.org/2024/08/14",
        "https://odb.org/2024/08/15",
        "https://odb.org/2024/08/16",
        "https://odb.org/2024/08/17",
        "https://odb.org/2024/08/18",
        "https://odb.org/2024/08/19",
        "https://odb.org/2024/08/20",
        "https://odb.org/2024/08/21",
        "https://odb.org/2024/08/22",
        "https://odb.org/2024/08/23",
        "https://odb.org/2024/08/24",
        "https://odb.org/2024/08/25",
        "https://odb.org/2024/08/26",
        "https://odb.org/2024/08/27",
        "https://odb.org/2024/08/28",
        "https://odb.org/2024/08/29",
        "https://odb.org/2024/08/30",
        "https://odb.org/2024/08/31",
        "https://odb.org/2024/09/01",
        "https://odb.org/2024/09/02",
        "https://odb.org/2024/09/03",
        "https://odb.org/2024/09/04",
        "https://odb.org/2024/09/05",
        "https://odb.org/2024/09/06",
        "https://odb.org/2024/09/07",
        "https://odb.org/2024/09/08",
        "https://odb.org/2024/09/09",
        "https://odb.org/2024/09/10",
        "https://odb.org/2024/09/11",
        "https://odb.org/2024/09/12",
        "https://odb.org/2024/09/13",
        "https://odb.org/2024/09/14",
        "https://odb.org/2024/09/15",
        "https://odb.org/2024/09/16",
        "https://odb.org/2024/09/17",
        "https://odb.org/2024/09/18",
        "https://odb.org/2024/09/19",
        "https://odb.org/2024/09/20",
        "https://odb.org/2024/09/21",
        "https://odb.org/2024/09/22",
        "https://odb.org/2024/09/23",
        "https://odb.org/2024/09/24",
        "https://odb.org/2024/09/25",
        "https://odb.org/2024/09/26",
        "https://odb.org/2024/09/27",
        "https://odb.org/2024/09/28",
        "https://odb.org/2024/09/29",
        "https://odb.org/2024/09/30",
        "https://odb.org/2024/10/01",
        "https://odb.org/2024/10/02",
        "https://odb.org/2024/10/03",
        "https://odb.org/2024/10/04",
        "https://odb.org/2024/10/05",
        "https://odb.org/2024/10/06",
        "https://odb.org/2024/10/07",
        "https://odb.org/2024/10/08",
        "https://odb.org/2024/10/09",
        "https://odb.org/2024/10/10",
        "https://odb.org/2024/10/11",
        "https://odb.org/2024/10/12",
        "https://odb.org/2024/10/13",
        "https://odb.org/2024/10/14",
        "https://odb.org/2024/10/15",
        "https://odb.org/2024/10/16",
        "https://odb.org/2024/10/17",
        "https://odb.org/2024/10/18",
        "https://odb.org/2024/10/19",
        "https://odb.org/2024/10/20",
        "https://odb.org/2024/10/21",
        "https://odb.org/2024/10/22",
        "https://odb.org/2024/10/23",
        "https://odb.org/2024/10/24",
        "https://odb.org/2024/10/25",
        "https://odb.org/2024/10/26",
        "https://odb.org/2024/10/27",
        "https://odb.org/2024/10/28",
        "https://odb.org/2024/10/29",
        "https://odb.org/2024/10/30",
        "https://odb.org/2024/10/31",
        "https://odb.org/2024/11/01",
        "https://odb.org/2024/11/02",
        "https://odb.org/2024/11/03",
        "https://odb.org/2024/11/04",
        "https://odb.org/2024/11/05",
        "https://odb.org/2024/11/06",
        "https://odb.org/2024/11/07",
        "https://odb.org/2024/11/08",
        "https://odb.org/2024/11/09",
        "https://odb.org/2024/11/10",
        "https://odb.org/2024/11/11",
        "https://odb.org/2024/11/12",
        "https://odb.org/2024/11/13",
        "https://odb.org/2024/11/14",
        "https://odb.org/2024/11/15",
        "https://odb.org/2024/11/16",
        "https://odb.org/2024/11/17",
        "https://odb.org/2024/11/18",
        "https://odb.org/2024/11/19",
        "https://odb.org/2024/11/20",
        "https://odb.org/2024/11/21",
        "https://odb.org/2024/11/22",
        "https://odb.org/2024/11/23",
        "https://odb.org/2024/11/24",
        "https://odb.org/2024/11/25",
        "https://odb.org/2024/11/26",
        "https://odb.org/2024/11/27",
        "https://odb.org/2024/11/28",
        "https://odb.org/2024/11/29",
        "https://odb.org/2024/11/30",
        "https://odb.org/2024/12/01",
        "https://odb.org/2024/12/02",
        "https://odb.org/2024/12/03",
        "https://odb.org/2024/12/04",
        "https://odb.org/2024/12/05",
        "https://odb.org/2024/12/06",
        "https://odb.org/2024/12/07",
        "https://odb.org/2024/12/08",
        "https://odb.org/2024/12/09",
        "https://odb.org/2024/12/10",
        "https://odb.org/2024/12/11",
        "https://odb.org/2024/12/12",
        "https://odb.org/2024/12/13",
        "https://odb.org/2024/12/14",
        "https://odb.org/2024/12/15",
        "https://odb.org/2024/12/16",
        "https://odb.org/2024/12/17",
        "https://odb.org/2024/12/18",
        "https://odb.org/2024/12/19",
        "https://odb.org/2024/12/20",
        "https://odb.org/2024/12/21",
        "https://odb.org/2024/12/22",
        "https://odb.org/2024/12/23",
        "https://odb.org/2024/12/24",
        "https://odb.org/2024/12/25",
        "https://odb.org/2024/12/26",
        "https://odb.org/2024/12/27",
        "https://odb.org/2024/12/28",
        "https://odb.org/2024/12/29",
        "https://odb.org/2024/12/30",
        "https://odb.org/2024/12/31"
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

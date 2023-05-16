'''

Download links for lecture recordings from canvas, and save them to a CSV file

CSV File Format:
Lecture Name, Date, Link

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import json
import re

import time
import csv

link_to_canvas = "https://umich.instructure.com/courses/200"

time_to_wait = 10 # Increase this number if the page takes longer to load (internet connection is slow)

def main():

    driver = webdriver.Chrome() # You must have chrome to run this script

    driver.get(link_to_canvas)
    
    # Allow user to log into canvas 
    input("Please log in manually in the browser window and then navigate to page with all lecture recording links. Ensure the webpage has loaded completely. Press enter to continue...")

    driver.switch_to.frame(driver.find_element(By.ID, "tool_content"))

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    # Exract all links
    script = soup.find_all('script')[7]
    
    recordings = re.search(r'var recordings = (.*?);', script.string)

    if recordings:
        # Parse the JSON string into a Python object
        json_obj = json.loads(recordings.group(1))

        # Print out all titles
        data = []

        for recording in json_obj:
            print(f"Retrieving {recording['title']}")

            title = recording['title']
            date = recording['date']
            link = recording['url']

            # append "https://leccap.engin.umich.edu" to the link
            link = "https://leccap.engin.umich.edu" + link

            driver.get(link)
            time.sleep(time_to_wait)

            html_lec = driver.page_source
        
            soup_lec = BeautifulSoup(html_lec, 'html.parser')
            div = soup_lec.find('div', {'class': 'video', 'id': 'tempid'})

            video = div.find('video')

            if video is not None:
                src = video.get('src')  # Get the 'src' attribute of the video

                # remove 2 // from the beginning of the link
                src = src[2:]

                src = "https://" + src

                data.append({"Lecture Name" : title, "Date" : date, "Link" : src})

            else:
                print("Video tag not found. Could be due to page not loading completely. Increase time_to_wait variable and try again.")
            

        # # Save it as a JSON file
        # with open('recordings.json', 'w') as f:
        #     json.dump(json_obj, f)

    # Save data to CSV file

    # Specify the field names (column names) for the CSV file
    fieldnames = ["Lecture Name", "Date", "Link"]

    # Write the data to a CSV file
    with open('lectures.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write the header (field names)
        writer.writerows(data)  # Write the data
        driver.quit()




if __name__ == "__main__":
    main()
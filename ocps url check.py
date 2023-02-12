import requests
from bs4 import BeautifulSoup
import os

def send_notification(title, message):
   os.system(f'osascript -e \'display notification "{message}" with title "{title}"\'')

# URL of the webpage to scrape
url = "https://www.ocps.net/departments/student_enrollment/transfers"

# Send a GET request to retrieve the source code of the webpage
response = requests.get(url)

# Parse the source code using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# URL to search for on the webpage
link = soup.find("a", href="/UserFiles/Servers/Server_54619/File/Departments/Student Enrollment/Controlled Open Enrollment Capacity/COET 2023-24/COET List 2023-24 02 08 23.pdf")

if link:
    print("Link has not changed")
    send_notification("OCPS Check", "The link has not changed.")
else:
    print("The link has changed!!")
    send_notification("OCPS Check", "The link has changed! Check website!")
# Import dependencies
from bs4 import BeautifulSoup
import requests
import time
import smtplib

# Initialize email info
gmail_from_address = 'your_gmail_account@gmail.com'
gmail_password = 'yOuRgmAIlPasSwoRd'
receiving_email = 'receiving_email@email.com'


# Retrieves information from tvinna.is
def get_jobs_from_list():
    try:
        response = requests.get("http://www.tvinna.is/")
        content = response.content
        parser = BeautifulSoup(content, 'html.parser')
        job_list = parser.find_all("section", class_="job-listing")[0].select("ul")[0].select("li")
        title = []
        company = []
        for item in job_list:
            title.append(item.select("h2")[0].text)
            company.append(item.select("p")[0].text)
        return title, company
    except Exception:
        print("URL error")

# Sends email from gmail_from_address to receiving_email
def send_email(message):
    fromaddr = gmail_from_address
    toaddrs  = receiving_email
    msg = "\r\n".join([
      "From: " + gmail_from_address,
      "To: "+ receiving_email,
      "Subject: New Jobs at tvinna.is!",
      "",
      message
      ])
    username = gmail_from_address
    password = gmail_password
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

# Initializes the old job list
old_title, old_company = get_jobs_from_list()

# Tester
# Remove the following comments to check if it works
#old_title = old_title[1:len(old_title)-1]
#old_company = old_company[1:len(old_title)-1]

# Checks for new jobs on the list every 5 minutes
while True:
    new_title, new_company = get_jobs_from_list()
    for i, item in enumerate(new_title):
        if item not in old_title:
            print("Change")
            message = "Job title: " + new_title[i].encode('utf-8') + "\n" + "Company: "+ new_company[i].encode('utf-8') +  "\n www.tvinna.is "
            send_email(message)

    old_title = new_title
    old_company = new_company
    time.sleep(600)

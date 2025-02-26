import requests
from bs4 import BeautifulSoup

# URL of the job listings page
url = "https://careers.google.com/jobs/results/"

# Send a GET request to the page
response = requests.get(url)

# Parse the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all job listings in the <ul> tag with class 'spHGqe'
job_listings = soup.find_all('li', class_='lLd3Je')

# Loop through each job listing and extract data
for job in job_listings:
    # Extract the job title
    title = job.find('h3', class_='QJPWVe')
    job_title = title.get_text() if title else 'No title found'

    # Extract the company name
    company = job.find('span', class_='RP7SMd')
    company_name = company.get_text() if company else 'No company found'

    # Extract the job location
    location = job.find('span', class_='r0wTof')
    job_location = location.get_text() if location else 'No location found'

    # Extract the job link
    link_tag = job.find('a', class_='WpHeLc')
    job_link = "https://careers.google.com/" + link_tag['href'] if link_tag else 'No link found'

    # Print the details
    print(f"Job Title: {job_title}")
    print(f"Company: {company_name}")
    print(f"Location: {job_location}")
    print(f"Link: {job_link}")
    print('---' * 10)

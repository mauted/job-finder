import sqlite3
import requests
from bs4 import BeautifulSoup

# Connect to the correct database
conn = sqlite3.connect('job_finder.db')  # Use job_finder.db instead of companies.db
cursor = conn.cursor()

# Fetch company names and careers page URLs from the companies table
cursor.execute("SELECT name, career_page_url FROM companies")
companies = cursor.fetchall()

# Loop through each company to scrape their career page
for company_name, careers_url in companies:
    # Send a GET request to the company's careers page
    response = requests.get(careers_url)
    
    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find job listings (adjust the selectors as needed for each website)
    job_listings = soup.find_all('li', class_='lLd3Je')  # Example selector, adjust accordingly
    
    # Loop through each job listing and extract data
    for job in job_listings:
        # Extract the job title
        title = job.find('h3', class_='QJPWVe')
        job_title = title.get_text() if title else 'No title found'
        
        # Extract the company name (if needed)
        company = job.find('span', class_='RP7SMd')
        company_name = company.get_text() if company else 'No company found'
        
        # Extract the job location
        location = job.find('span', class_='r0wTof')
        job_location = location.get_text() if location else 'No location found'
        
        # Print or store the job details
        print(f"Job Title: {job_title}")
        print(f"Company: {company_name}")
        print(f"Location: {job_location}")
        print('---' * 10)

# Close the database connection
conn.close()
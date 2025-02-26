import requests
from bs4 import BeautifulSoup
from database import insert_job
import warnings

# Suppress SSL warnings (optional, only for testing)
# warnings.filterwarnings('ignore', category=InsecureRequestWarning)

def scrape_jobs(company_url):
    try:
        # Setting allow_redirects=False to debug redirects
        response = requests.get(company_url, verify=False, allow_redirects=True)  # Change to True if needed
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Replace with your scraping logic for extracting jobs
        job_listings = soup.find_all('div', class_='job_listing')

        for job_listing in job_listings:
            job = {
                'title': job_listing.find('h2').text,
                'location': job_listing.find('span', class_='location').text,
                'company': 'Company Name',  # You can set this dynamically
                'description': job_listing.find('p', class_='description').text,
                'url': job_listing.find('a')['href']
            }
            insert_job(job)

    except requests.exceptions.TooManyRedirects:
        print(f"Too many redirects while trying to access {company_url}. Please check the URL or the site configuration.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
scrape_jobs('https://www.google.com/about/careers/applications/jobs/results/')

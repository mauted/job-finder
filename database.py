import sqlite3

# Function to create the database and the necessary table if they don't exist
def create_db():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()

    # Create jobs table (if not already created)
    c.execute('''CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    location TEXT,
                    company TEXT,
                    description TEXT,
                    url TEXT)''')

    conn.commit()
    conn.close()

# Function to insert a new job into the database
def insert_job(title, location, company, description, url):
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()

    # Insert the job record into the jobs table
    c.execute('''INSERT INTO jobs (title, location, company, description, url)
                 VALUES (?, ?, ?, ?, ?)''', (title, location, company, description, url))

    conn.commit()
    conn.close()

# Function to retrieve jobs from the database based on filter criteria (role and company)
def get_jobs(role=None, company=None):
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()

    # Construct the query based on filter criteria
    query = 'SELECT * FROM jobs WHERE 1=1'
    params = []

    if role:
        query += ' AND title LIKE ?'
        params.append(f'%{role}%')

    if company:
        query += ' AND company LIKE ?'
        params.append(f'%{company}%')

    c.execute(query, params)
    jobs = c.fetchall()

    conn.close()

    # Return job listings as a list of dictionaries
    return [{'title': job[1], 'location': job[2], 'company': job[3], 'description': job[4], 'url': job[5]} for job in jobs]

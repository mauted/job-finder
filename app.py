from flask import Flask, request, render_template
from database import create_db, get_jobs  # Import database-related functions
from scheduler import start_scheduler  # Import the scheduler function

app = Flask(__name__)

# Initialize the database and create the necessary tables
create_db()

# Start the background job scheduler to scrape jobs periodically
start_scheduler()

@app.route('/')
def home():
    return render_template('index.html')  # Render home page (if you have one)

@app.route('/filter')
def filter_jobs():
    # Get filtering parameters from query string
    role = request.args.get('role')
    company = request.args.get('company')

    # You can add more filtering criteria as needed (e.g., keywords)
    filtered_jobs = get_jobs(role=role, company=company)

    # Render filtered job listings in the template
    return render_template('jobs.html', jobs=filtered_jobs)

if __name__ == "__main__":
    app.run(debug=True)

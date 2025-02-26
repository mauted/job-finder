
import sqlite3

def add_company(name, career_page_url):
    conn = sqlite3.connect("job_finder.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO companies (name, career_page_url) VALUES (?, ?)", (name, career_page_url))
        conn.commit()
        print(f"Added {name} to the database.")
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

    conn.close()

# Example usage
if __name__ == "__main__":
    company_name = input("Enter company name: ")
    career_url = input("Enter career page URL: ")
    add_company(company_name, career_url)

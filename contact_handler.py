import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('gaushala_data.db')
    c = conn.cursor()
    
    # Create contacts table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            message TEXT NOT NULL,
            submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def save_contact(name, phone, email, message):
    conn = sqlite3.connect('gaushala_data.db')
    c = conn.cursor()
    
    c.execute('''
        INSERT INTO contacts (name, phone, email, message)
        VALUES (?, ?, ?, ?)
    ''', (name, phone, email, message))
    
    conn.commit()
    conn.close()
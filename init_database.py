#!/usr/bin/env python

"""
This script creates or recreates a sameple database and table 

"""

import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


# Delete database table if it already exists 
# and then recreate a blank table for testing.
try:
    cursor.execute("SELECT * FROM items")
except sqlite3.Error:
    print("Table does not exist, creating...")
    cursor.execute('''CREATE TABLE items (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     equipment_type text,
                     model text,
                     serial_number text,
                     calibration_due_date text,
                     status text,
                     description text)''')
    cursor.commit()

else:
    print("Table exists, deleting...")
    cursor.execute("DROP TABLE IF EXISTS items")
    conn.commit()
    print("Recreating table")
    cursor.execute('''CREATE TABLE items (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     equipment_type text,
                     model text,
                     serial_number text,
                     calibration_due_date text,
                     status text,
                     description text)''')
    conn.commit()



# Sample items
items = [
    {
        'equipment_type': 'Calibrator',
        'model': 'CM-34',
        'serial_number': '123456',
        'calibration_due_date': '2022-01-01',
        'status': 'Calibrated',
        'description': 'Temperature calibrator'
    },
    {
        'equipment_type': 'Multimeter',
        'model': 'MM-22',
        'serial_number': '789012',
        'calibration_due_date': '2022-03-01',
        'status': 'Calibration overdue',
        'description': 'Digital multimeter'
    }
]

# insert the sample items into the database
for item in items:
    cursor.execute('''INSERT INTO items (equipment_type, model, serial_number, calibration_due_date, status, description)
                      VALUES (?, ?, ?, ?, ?, ?)''', (item['equipment_type'], item['model'], item['serial_number'], item['calibration_due_date'], item['status'], item['description']))

conn.commit()
cursor.close()
conn.close()


def list_items():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM items''')
    items = cursor.fetchall()
    print(items)
    conn.close()
    #return render_template('items.html', items=items)


if __name__ == '__main__':
    list_items()



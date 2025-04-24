import sys
sys.dont_write_bytecode = True

import json
import sqlite3
import os

from pathlib import Path

db_path = Path("D:/python/projects/garden-series-2/garden/garden.sqlite")

file_path_plants = os.path.join(os.path.dirname(__file__), 'plants.json')

try:
    with open(file_path_plants, 'r', encoding='utf-8') as f:
        plants = json.load(f)
except FileNotFoundError:
    plants = []  # Default value
except json.JSONDecodeError:
    plants = []  # Handle corrupt file


conn = sqlite3.connect(db_path)
cursor = conn.cursor()

for item in plants:
    cursor.execute('''INSERT INTO plants (name, 
                   category, 
                   code, 
                   intro, 
                   thumbnail, 
                   location, 
                   display, 
                   status, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                 (
                    item['name'], 
                    item['category'], 
                    item['code'], 
                    item['intro'],
                    item['thumbnail'],
                    item['location'],
                    item['display'],
                    item['status'],
                    item['timestamp']
                  ))
 
conn.commit()
conn.close()

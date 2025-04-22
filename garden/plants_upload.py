import sys
sys.dont_write_bytecode = True

import json
import sqlite3
import os

from pathlib import Path

db_path = Path("D:/python/projects/garden-series-2/garden/garden.sqlite")

# def inspect_database(db_path):
#     print(f"\n=== Инспекция базы данных {db_path} ===")
#     print(f"Размер файла: {db_path.stat().st_size} байт")
    
#     try:
#         conn = sqlite3.connect(f"file:{db_path}?mode=rw", uri=True)
#         cursor = conn.cursor()
        
#         # 1. Проверка всех таблиц (включая скрытые)
#         cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
#         tables = cursor.fetchall()
#         print(f"\nВсе таблицы ({len(tables)}):")
#         for table in tables:
#             print(f"- {table[0]}")
            
#             # 2. Проверка структуры каждой таблицы
#             cursor.execute(f"PRAGMA table_info({table[0]})")
#             columns = cursor.fetchall()
#             print(f"  Колонки ({len(columns)}):")
#             for col in columns:
#                 print(f"  {col[1]} ({col[2]})")
        
#         # 3. Проверка временных таблиц
#         cursor.execute("SELECT name FROM sqlite_temp_master WHERE type='table'")
#         temp_tables = cursor.fetchall()
#         if temp_tables:
#             print("\nВременные таблицы:")
#             for table in temp_tables:
#                 print(f"- {table[0]}")
        
#         # 4. Проверка индексов
#         cursor.execute("SELECT name FROM sqlite_master WHERE type='index'")
#         indexes = cursor.fetchall()
#         if indexes:
#             print("\nИндексы:")
#             for idx in indexes:
#                 print(f"- {idx[0]}")
        
#         conn.close()
#         return True
        
#     except sqlite3.Error as e:
#         print(f"\nОшибка доступа к базе: {e}")
#         return False

# inspect_database(db_path)


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

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.db import connection

# Create the items_item table manually
with connection.cursor() as cursor:
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items_item (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        description TEXT NOT NULL,
        created_at DATETIME NOT NULL
    )
    ''')
    
print("Table created successfully!")
import sqlite3

conn = sqlite3.connect("db/finance_manager.db")
cursor = conn.cursor()
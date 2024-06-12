from __init__ import conn, cursor

class Income:
    def __init__(self, source, date, amount, category_id, id=None):
        self.id = id
        self.source = source
        self.date = date
        self.amount = amount
        self.category_id = category_id

    def __repr__(self):
        return f"<Income(id={self.id}, source={self.source}, date={self.date}, amount={self.amount}, category_id={self.category_id})>"

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS incomes (
            id INTEGER PRIMARY KEY,
            source TEXT NOT NULL,
            date DATE NOT NULL,
            amount FLOAT,
            category_id INTEGER,
            FOREIGN KEY(category_id) REFERENCES categories(id)
        )
        """
        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = "INSERT INTO incomes (source, date, amount, category_id) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (self.source, self.date, self.amount, self.category_id))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM incomes"
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM incomes WHERE id = ?"
        cursor.execute(sql, (id,))
        return cursor.fetchone()

    def delete(self):
        sql = "DELETE FROM incomes WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()


# Ensure the table exists
Income.create_table()


incomes_data = [
    ("Salary", "2024-06-01", 2500.0, 3),  # Assuming 'Income' category has id 3
    ("Freelance", "2024-05-28", 1200.0, 3),  # Assuming 'Income' category has id 3
    # Add more incomes as needed
]

for data in incomes_data:
    income = Income(*data)
    income.save()

print("Incomes table populated.")        

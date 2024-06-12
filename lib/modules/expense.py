from __init__ import conn, cursor

class Expense:
    def __init__(self, description, date, amount, category_id, id=None):
        self.id = id
        self.description = description
        self.date = date
        self.amount = amount
        self.category_id = category_id

    def __repr__(self):
        return f"<Expense(id={self.id}, description={self.description}, date={self.date}, amount={self.amount}, category_id={self.category_id})>"

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL,
            date DATE NOT NULL,
            amount FLOAT,
            category_id INTEGER,
            FOREIGN KEY(category_id) REFERENCES categories(id)
        )
        """
        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = "INSERT INTO expenses (description, date, amount, category_id) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (self.description, self.date, self.amount, self.category_id))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM expenses"
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM expenses WHERE id = ?"
        cursor.execute(sql, (id,))
        return cursor.fetchone()

    def delete(self):
        sql = "DELETE FROM expenses WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()

# Ensure the table exists
Expense.create_table()


expenses_data = [
    ("Book purchase", "2024-06-12", 20.5, 1),  # Assuming 'Books' category has id 1
    ("Groceries", "2024-06-11", 35.75, 4),    # Assuming 'Food' category has id 4
    ("Rent", "2024-06-13", 27000.70, 6),
    ("Electricity-Bill", "2024-07-17", 500.4, 5),
    # Add more expenses as needed
]

for data in expenses_data:
    expense = Expense(*data)
    expense.save()

print("Expenses table populated.")
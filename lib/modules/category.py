from __init__ import conn, cursor

class Category:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """
        print("Creating categories table...")
        cursor.execute(sql)
        conn.commit()
        print("Categories table created.")

    def save(self):

        if Category.find_by_name(self.name):
            print(f"Category {self.name} already exists.")
            return

            
        sql = "INSERT INTO categories (name) VALUES (?)"
        cursor.execute(sql, (self.name,))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM categories"
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM categories WHERE id = ?"
        cursor.execute(sql, (id,))
        return cursor.fetchone()
    
    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM categories WHERE name = ?"
        cursor.execute(sql, (name,))
        return cursor.fetchone()


    def delete(self):
        sql = "DELETE FROM categories WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()

Category.create_table()

# Populate categories with sample data
categories_data = [
    "Books",
    "Electronics",
    "Clothing",
    "Food",
    ""
]

for name in categories_data:
    category = Category(name)
    category.save()

print("Categories table populated.")

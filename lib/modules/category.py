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
        cursor.execute(sql)
        conn.commit()

    def save(self):
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

    def delete(self):
        sql = "DELETE FROM categories WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()

import sqlite3


class SQL():
    """Class for conections with database SQLite."""
    def __init__(self):
        self.conn = sqlite3.connect("database.db", check_same_thread=False)
        self.cursor = self.conn.cursor()


    def create_table(self):
        """Method for create table."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id CHAR(36) NOT NULL UNIQUE,
            first_name VARCHAR(255) NOT NULL,
            last_name  VARCHAR(255) NOT NULL,
            age INTEGER NOT NULL,
            document CHAR(11) PRIMARY KEY,
            web_site VARCHAR(100) NOT NULL DEFAULT '-',
            comments TEXT DEFAULT '-',
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.conn.commit()


    def users_database(self, only_documents:bool = True):
        """Return all users exists in database."""
        self.create_table()
        selector = 'document' if only_documents else '*'
        users = self.cursor.execute(f'SELECT {selector} FROM users').fetchall()
        return tuple(user[0] for user in users) if only_documents else users


    def insert_database(self, inserts:str):
        """Insert a row into user's table."""
        self.cursor.execute(f"""
                INSERT INTO users (id, first_name, last_name, age, document, web_site, comments, created_at)
                    VALUES {inserts[:-1]};
            """
        )
  
        self.conn.commit()
        self.cursor.close()


    def delete_all_users(self):
        """Delete all users."""
        self.create_table()
        try:
            self.cursor.execute('DELETE FROM users')
            self.conn.commit()
        except Exception as error:
            print(error)
        self.cursor.close()
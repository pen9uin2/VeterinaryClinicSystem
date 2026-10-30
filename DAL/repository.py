from DAL.connection import get_connection

class OwnerRepository:
    @staticmethod
    def add_owner(first_name, last_name, phone, email):
        conn = get_connection()
        conn.execute("INSERT INTO owners (first_name, last_name, phone, email) VALUES (?, ?, ?, ?)",
                     (first_name, last_name, phone, email))
        conn.commit()
        conn.close()
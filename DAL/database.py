from DAL.connection import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Создание всех таблиц
    tables = [
        '''CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL, last_name TEXT NOT NULL, phone TEXT, email TEXT)''',
            
        '''CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, species TEXT, breed TEXT, birth_date TEXT, owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES owners(id))''',
            
        '''CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL, specialization TEXT, position TEXT)''',
            
        '''CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, price REAL NOT NULL, description TEXT)''',
            
        '''CREATE TABLE IF NOT EXISTS medications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, unit_price REAL NOT NULL, stock_quantity INTEGER DEFAULT 0)''',
            
        '''CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL, time TEXT NOT NULL, status TEXT DEFAULT 'Запланирован',
            pet_id INTEGER, doctor_id INTEGER,
            FOREIGN KEY (pet_id) REFERENCES pets(id), FOREIGN KEY (doctor_id) REFERENCES employees(id))''',
            
        '''CREATE TABLE IF NOT EXISTS appointment_services (
            appointment_id INTEGER, service_id INTEGER, final_price REAL,
            FOREIGN KEY (appointment_id) REFERENCES appointments(id), FOREIGN KEY (service_id) REFERENCES services(id))''',
            
        '''CREATE TABLE IF NOT EXISTS appointment_medications (
            appointment_id INTEGER, medication_id INTEGER, quantity INTEGER, dosage TEXT,
            FOREIGN KEY (appointment_id) REFERENCES appointments(id), FOREIGN KEY (medication_id) REFERENCES medications(id))'''
    ]
    
    for table in tables:
        cursor.execute(table)
        
    conn.commit()
    conn.close()
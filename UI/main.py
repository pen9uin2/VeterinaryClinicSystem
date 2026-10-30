import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from DAL.database import init_db
from UI.interface import start_app

def main():
    print("Инициализация базы данных...")
    init_db()
    start_app()

if __name__ == "__main__":
    main()
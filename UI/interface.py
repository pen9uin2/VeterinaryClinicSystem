from BLL.services import OwnerService

def start_app():
    while True:
        print("\n=== Ветеринарная клиника ===")
        print("1. Добавить владельца")
        print("2. Выход")
        choice = input("Выбор: ")
        
        if choice == '1':
            fname = input("Имя: ")
            lname = input("Фамилия: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            OwnerService.register(fname, lname, phone, email)
            print("Готово!")
        elif choice == '2':
            break
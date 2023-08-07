transactions = []
user_amount = 0


def show_menu():
    print("1. Пополнить баланс")
    print("2. Снять деньги")
    print("3. Показать историю операций")
    print("4. Ваш баланс средст")
    print("5. Выйти")


def deposit(amount):
    transactions.append(f"Пополнение: {amount} руб.")
    print(f"Баланс увеличен на {amount} руб.")


def withdraw(amount):
    if amount <= get_balance():
        transactions.append(f"Снятие: {amount} руб.")
        print(f"Снято {amount} руб.")
    else:
        print("Недостаточно средств")


def get_balance():
    global user_amount
    return user_amount


def show_transactions():
    if transactions:
        print("История операций:")
        for transaction in transactions:
            print(transaction)
    else:
        print("Нет операций")


def execute_choice(choice):
    global user_amount
    if choice == '1':
        amount = int(input("Введите сумму для пополнения: "))
        deposit(amount)
        user_amount += amount
    elif choice == '2':
        amount = int(input("Введите сумму для снятия: "))
        withdraw(amount)
        user_amount -= amount
    elif choice == '3':
        show_transactions()
    elif choice == '4':
        print(f"Ваш Баланс {get_balance()} руб. ")
    elif choice == '5':
        print("До свидания!")
        return False
    else:
        print("Неверный выбор")

    return True


def main():
    running = True
    while running:
        show_menu()
        choice = input("Выберите пункт меню: ")
        running = execute_choice(choice)


if __name__ == "__main__":
    main()

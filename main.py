# Класс User: базовый класс для обычных сотрудников
class User:
    def __init__(self, user_id, name, access_level='user'):
        """
        Инициализирует новый экземпляр пользователя.

        :param user_id: Уникальный идентификатор пользователя
        :param name: Имя пользователя
        :param access_level: Уровень доступа пользователя (по умолчанию 'user')
        """
        self.__id = user_id             # Приватный атрибут ID
        self.__name = name              # Приватный атрибут имени
        self.__access_level = access_level  # Приватный атрибут уровня доступа

    # Метод для получения ID пользователя
    def get_id(self):
        """
        Возвращает ID пользователя.
        """
        return self.__id

    # Метод для установки нового ID пользователя
    def set_id(self, user_id):
        """
        Устанавливает новый ID пользователя.

        :param user_id: Новый уникальный идентификатор
        """
        self.__id = user_id

    # Метод для получения имени пользователя
    def get_name(self):
        """
        Возвращает имя пользователя.
        """
        return self.__name

    # Метод для установки нового имени пользователя
    def set_name(self, name):
        """
        Устанавливает новое имя пользователя.

        :param name: Новое имя
        """
        self.__name = name

    # Метод для получения уровня доступа пользователя
    def get_access_level(self):
        """
        Возвращает уровень доступа пользователя.
        """
        return self.__access_level

    # Метод для установки нового уровня доступа пользователя
    def set_access_level(self, access_level):
        """
        Устанавливает новый уровень доступа пользователя.

        :param access_level: Новый уровень доступа (например, 'user')
        """
        self.__access_level = access_level

    # Метод для представления объекта в виде строки (для удобства)
    def __str__(self):
        return f"User[ID={self.__id}, Name={self.__name}, Access Level={self.__access_level}]"


# Класс Admin: наследуется от User и добавляет функциональность администратора
class Admin(User):
    def __init__(self, user_id, name, access_level='admin'):
        """
        Инициализирует новый экземпляр администратора.

        :param user_id: Уникальный идентификатор администратора
        :param name: Имя администратора
        :param access_level: Уровень доступа администратора (по умолчанию 'admin')
        """
        super().__init__(user_id, name, access_level)  # Вызов конструктора базового класса

    # Метод для добавления пользователя в систему
    def add_user(self, user_list, user):
        """
        Добавляет нового пользователя в список пользователей.

        :param user_list: Список текущих пользователей
        :param user: Экземпляр класса User, которого нужно добавить
        """
        # Проверяем, не существует ли уже пользователь с таким ID
        for existing_user in user_list:
            if existing_user.get_id() == user.get_id():
                print(f"Пользователь с ID {user.get_id()} уже существует.")
                return
        user_list.append(user)  # Добавляем пользователя в список
        print(f"Пользователь {user.get_name()} добавлен успешно.")

    # Метод для удаления пользователя из системы по ID
    def remove_user(self, user_list, user_id):
        """
        Удаляет пользователя из списка пользователей по его ID.

        :param user_list: Список текущих пользователей
        :param user_id: ID пользователя, которого нужно удалить
        """
        for user in user_list:
            if user.get_id() == user_id:
                user_list.remove(user)  # Удаляем пользователя из списка
                print(f"Пользователь с ID {user_id} удален успешно.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    # Переопределение метода представления объекта в виде строки
    def __str__(self):
        return f"Admin[ID={self.get_id()}, Name={self.get_name()}, Access Level={self.get_access_level()}]"


# Пример использования системы управления учетными записями

# Создаем список для хранения пользователей
users = []

# Создаем администратора
admin = Admin(user_id=1, name='Иван Иванов')

# Добавляем администратора в список пользователей
users.append(admin)

# Администратор добавляет обычных пользователей
user1 = User(user_id=2, name='Мария Петрова')
admin.add_user(users, user1)

user2 = User(user_id=3, name='Алексей Смирнов')
admin.add_user(users, user2)

# Пытаемся добавить пользователя с существующим ID
user_duplicate = User(user_id=2, name='Сергей Кузнецов')
admin.add_user(users, user_duplicate)

# Выводим всех пользователей
print("\nСписок пользователей:")
for user in users:
    print(user)

# Администратор удаляет пользователя
admin.remove_user(users, user_id=2)

# Пытаемся удалить несуществующего пользователя
admin.remove_user(users, user_id=4)

# Выводим обновленный список пользователей
print("\nОбновленный список пользователей:")
for user in users:
    print(user)

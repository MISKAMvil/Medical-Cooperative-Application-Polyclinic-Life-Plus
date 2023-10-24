from flask_login import current_user

# Политики доступа к ресурсам
# Класс имеет в себе набор методов, каждый из которых отвечает за определенные действия
class UsersPolicy:
    def __init__(self, record):
		# Передаем запись из БД, над которой будут производиться действия
        self.record = record

    # def create_book(self):
    #     return current_user.is_admin()

    # def delete_book(self):
    #     return current_user.is_admin()

    # def show_book(self):
    #     return True
    
    # def edit_book(self):
    #     return current_user.is_admin() or current_user.is_moderator()
    
    # def add_review(self):
    #     return.is_a
    
    # def user_dashboard(self):
    #     return not (current_user.is_admin() or current_user.is_moderator())
    
    # def moderator_dashboard(self):
    #     return current_user.is_moderator()

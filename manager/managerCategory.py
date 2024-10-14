from core.models.category import Category
from core.models.db_helper import db_helper
import os


class ManagerCategory:
    def __init__(self):
        self.db_helper = db_helper
        self.running: bool = True

    def create_category(
            self,
    ) -> None:
        while self.running:
            os.system('cls')
            print("----КЕРУВАННЯ КАТЕГОРІЯМИ----")
            print("-----------------------------------------------------------")
            print("1 - Вивести список категорій")
            print("-----------------------------------------------------------")
            print("2 - Додати категорію")
            print("-----------------------------------------------------------")
            print("3 - Видалити категорію")
            print("-----------------------------------------------------------")
            print("0 - Назад")
            print("-----------------------------------------------------------")
            action: int = int(input())
            match action:
                case 1:
                    with db_helper.get_db() as db:
                        categories = db.query(Category).all()
                        for category in categories:
                            print(f"ID: {category.id}, Назва: {category.category_name}")
                        input(("Нажміть будь-яку клавішу для продовження:"))
                case 2:
                    category_name: str = str(input("Введіть назву нової категорії:"))
                    with db_helper.get_db() as db:
                        new_category = Category(category_name=category_name)
                        db.add(new_category)
                        db.commit()
                        print("Категорія створена")
                        input(("Нажміть будь-яку клавішу для продовження:"))

                case 3:
                    with db_helper.get_db() as db:
                        categories = db.query(Category).all()
                        for category in categories:
                            print(f"ID: {category.id}, Назва: {category.category_name}")

                        category = db.query(Category).filter(Category.id == int(input("Введіть ID категрії:"))).first()
                        if category:
                            db.delete(category)
                            db.commit()
                            print("Категорія видалена")
                        input(("Нажміть будь-яку клавішу для продовження:"))

                case 0:
                    self.running = False

from core.models.category import Category
from core.models.db_helper import db_helper
import os

from core.models.products import Products


class ManageProducts:
    def __init__(self):
        self.db_helper = db_helper
        self.running: bool = True

    def create_products(
            self,
    ) -> None:
        while self.running:
            os.system('cls')
            print("----КЕРУВАННЯ ТОВАРОМ----")
            print("-----------------------------------------------------------")
            print("1 - Вивести список товару")
            print("-----------------------------------------------------------")
            print("2 - Додати товар")
            print("-----------------------------------------------------------")
            print("3 - Видалити товар")
            print("-----------------------------------------------------------")
            print("0 - Назад")
            print("-----------------------------------------------------------")

            action: int = int(input())
            match action:
                case 1:
                    with db_helper.get_db() as db:
                        products = db.query(Products).all()
                        for product in products:
                            print(f"ID: {product.id}, Назва: {product.name}")
                        input(("Нажміть будь-яку клавішу для продовження:"))
                case 2:
                    with db_helper.get_db() as db:
                        name = str(input("Введіть назву товару:"))
                        sale = int(input("Введіть ціну товару:"))
                        description = str(input("Введіть опис товару:"))
                        count = str(input("Введіть кількість товару:"))
                        categories = db.query(Category).all()
                        for category in categories:
                            print(f"ID: {category.id}, Назва: {category.category_name}")
                        category_id = str(input("Введіть ID категорії (для добавлення товару):"))
                        new_category = Products(
                            name=name,
                            sale=sale,
                            description=description,
                            count=count,
                            category_id=category_id,
                        )
                        db.add(new_category)
                        db.commit()
                        print("Товар додано")
                        input(("Нажміть будь-яку клавішу для продовження:"))

                case 3:
                    with db_helper.get_db() as db:
                        products = db.query(Products).all()
                        for product in products:
                            print(f"ID: {product.id}, Назва: {product.name}")
                        product = db.query(Products).filter(Products.id == int(input("Введіть ID продукта:"))).first()
                        if product:
                            db.delete(product)
                            db.commit()
                            print("Категорія видалена")
                        input(("Нажміть будь-яку клавішу для продовження:"))

                case 0:
                    self.running = False

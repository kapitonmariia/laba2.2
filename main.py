import os
from core.models.category import Category
from core.models.products import Products

from manager.managerCategory import ManagerCategory
from manager.managerProducts import ManageProducts
from manager.managerSearch import ManagerSearch

running: bool = True

if __name__ == '__main__':
    while running:
        os.system('cls')
        print("------Виберіть опцію------")
        print("-----------------------------------------------------------")
        print("1 - Пошук товару")
        print("-----------------------------------------------------------")
        print("2 - Пошук по категорії")
        print("-----------------------------------------------------------")
        print("3 - Керування товаром")
        print("-----------------------------------------------------------")
        print("4 - Керування категоріями")
        print("-----------------------------------------------------------")
        print("0 - Вихід")
        print("-----------------------------------------------------------")
        action: int = int(input())
        match action:
            case 1:
                ManagerSearch().search_product()
            case 2:
                ManagerSearch().search_category()
            case 3:
                ManageProducts().create_products()
            case 4:
                ManagerCategory().create_category()
            case 0:
                running = False

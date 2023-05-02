#Ради избежания использования глобальных переменных во втором задании, принял решение реализовать задание через класс CookBookAPP.
class CookBookAPP:
    def __init__(self, file_name):
        self.cook_book = self.generateCookBook(file_name)
    #больше для контроля, чем для задания
    def __str__(self):
        output = ''
        for key, values in self.cook_book.items():
            output += f'{key}:\n'
            for value in values:
                output += f'{value["ingredient_name"]} | {value["quantity"]} | {value["measure"]}\n'
        return output
    # ЗАДАНИЕ 1
    def generateCookBook(self, file_name):
        cook_book = {}
        with open(file_name, 'r', encoding='utf-8') as f:
            for line in f:
                dish_name = line.strip()
                cook_book[dish_name] = []
                number_of_ingredient = int(f.readline().strip())
                for _ in range(number_of_ingredient):
                    ingredient_name, quantity, measure = f.readline().split(' | ')
                    cook_book[dish_name].append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()})
                cook_book
                f.readline()
        return cook_book
    # ЗАДАНИЕ 2        
    def get_shop_list_by_dishes(self, dishes, person_count):
        shop_list = {}
        for dish in dishes:
            if not dish in self.cook_book.keys(): return f'Блюда {dish} нет в книге!'
            for ingredient in self.cook_book[dish]: # Наверное было бы понятнее через if-else... но что-то там про легкие пути.
                shop_list[ingredient['ingredient_name']] =  {'measure' : ingredient['measure'],\
                                                             'quantity' : (ingredient['quantity'] * person_count) + shop_list.get(ingredient['ingredient_name'], 0)}

        return shop_list
            
cook_book = CookBookAPP('recipes.txt')
print(cook_book)
print("----------------------------------------------")
shop_list = cook_book.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 20)
print(shop_list)
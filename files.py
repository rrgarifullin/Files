from pprint import pprint
from dec import log


@log('logs/perfomance.log')
def open_file():
    cook_book = {}
    quantity = 0
    recipes_book = []
    recipes_book.append([])
    with open('recipe.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if len(line) != 0:
                recipes_book[quantity].append(line)
            else:
                recipes_book.append([])
                quantity += 1
    for dish in recipes_book:
        cook_book.update({dish[0]: []})
        for ingredients in range(2, len(dish)):
            recipe = dish[ingredients].split(' | ')
            ingred_dict = {'ingredient_name': recipe[0], 'quantity': int(recipe[1]), 'measure': recipe[2]}
            cook_book[dish[0]].append(ingred_dict)
    return cook_book


@log('logs/perfomance_2.log')
def get_shop_list_by_dishes(cook_book, dishes, person_count):
    dishes_book = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in dishes_book:
                dishes_book.update({ingredient['ingredient_name']: {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}})
            else:
                dishes_book[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return dishes, dishes_book


def main():
    cook_book = open_file()
    print('Книга рецептов: ')
    pprint(cook_book)
    dishes, dishes_book = get_shop_list_by_dishes(cook_book, ['Омлет', 'Запеченный картофель'], 2)
    print(f'\nКоличество ингредиентов для блюд: {dishes}:\n')
    pprint(dishes_book)


main()
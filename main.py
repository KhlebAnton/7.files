import re

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def parse_recipe(content):
    recipes = content.split('\n\n')
    cook_book = {}
    for recipe in recipes:
        name = re.match(r'^(.+)\n', recipe).group(1)
        ingredients = re.findall(r'(.*?)\s*\|\s*(\d+)\s*\|\s*(\S+)', recipe)
        
        cook_book[name] = [{'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]} for ingredient in ingredients]
    return cook_book


file_path = 'recipes.txt'
content = read_file(file_path)
cook_book = parse_recipe(content)
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity']}
            else:
                if ingredient['measure'] == shop_list[ingredient['ingredient_name']]['measure']:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
                else:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity']}
    for key in shop_list:
        shop_list[key]['quantity'] *= person_count
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

def sort_files_to_one(files, result_filename):
    sequence = {}
    for element in files:
        with open(element,'rt', encoding='utf-8') as file:
            f = file.readlines()
        sequence[len(f)] = element
    sorted_sequence = sorted(sequence.items())
    with open(result_filename, 'wt', encoding='utf-8') as file:
        for element in sorted_sequence:
            file.write(str(element[1])+'\n')
            file.write(str(element[0])+'\n')
            with open(str(element[1]),'rt', encoding='utf-8') as f:
                lines = f.readlines()
            for l in lines:
                file.write(l)
            file.write('\n')
            
files = ['sorted/1.txt', 'sorted/2.txt', 'sorted/3.txt']
result_filename = 'result.txt'
sort_files_to_one(files,result_filename)
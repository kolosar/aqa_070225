""" Задано дані (список списків) про багаж (кількість речей і загальна вага багажу) пасажирів. 
1. Скласти функцію, яка повертає тапл де міститься: 
    * кількість пасажирів, які мають більше двох речей; 
    * чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25 кг; 
    * число пасажирів, кількість речей яких перевершує середнє число речей всіх пасажирів.
2. Напишіть тести для перевірки роботу функції на різних вхідних даних.
# Алгоритм вирішення
1. Проведіь розрахунок кількості пасажирів з більше ніж 2 речами
2. Виконайте перевірку наявності пасажира з однією річчю вагою менше 25 кг
3. Проведіь обчислення середнього числа речей
4. З'ясуйте кількість пасажирів, які мають більше речей за середнє значення
"""

# Приклад вхідних даних
passengers = [
    {'number_of_items': 3, 'total_weight': 30},
    {'number_of_items': 2, 'total_weight': 20},
    {'number_of_items': 1, 'total_weight': 15},
    {'number_of_items': 4, 'total_weight': 40},
    {'number_of_items': 1, 'total_weight': 10},
    {'number_of_items': 5, 'total_weight': 50},
    {'number_of_items': 2, 'total_weight': 18},
    {'number_of_items': 3, 'total_weight': 35},
    {'number_of_items': 1, 'total_weight': 5},
    {'number_of_items': 4, 'total_weight': 45}
]

def check_passenger(passengers): 
    
    if len(passengers) == 0:
        msg = "Non-empty list expected" 
        raise ValueError(msg)
    count_more_then_two_items = 0 
    has_one_item_less_25 = False 
    count_above_avg = 0 
    total_items = 0
    
    for p in passengers:
        total_items += p['number_of_items']
        
    avg_items = total_items / len(passengers)   
    
    for p in passengers:
         print(f"Processing passenger with {p['number_of_items']} items and total weight {p['total_weight']}")
        
         if p['number_of_items'] > avg_items:
                print(f"Passenger has more than average items: {p['number_of_items']}")
                count_above_avg += 1

    print(f"Total passengers with items above average: {count_above_avg}")
    
    for p in passengers:
        if p['number_of_items'] > 2:
            count_more_then_two_items = +1
            
        if p['number_of_items'] == 1 and p['total_weight'] < 25:
            has_one_item_less_25 = True
    return count_more_then_two_items, has_one_item_less_25, count_above_avg

if __name__ == "__main__":
    a, b, c = check_passenger(passengers)
    print(f"Count of passengers with more than two items: {a}")
    print(f"Is there any passenger with 1 item and total weight < 25: {b}")
    print(f"Count of passengers with items above average: {c}")
    
    

    



        

        
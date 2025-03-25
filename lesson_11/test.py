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
import unittest

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
    
    assert len(passengers) > 0, "Non-empty list expected"

    count_more_than_two_items = 0
    has_one_item_less_25 = False
    count_above_avg = 0

    total_items = sum(p['number_of_items'] for p in passengers)
    avg_items = total_items / len(passengers)
    #print(f"Average number of items: {avg_items}")

    
    for p in passengers:
        num_items = p['number_of_items']
        weight = p['total_weight']

        print(f"Processing passenger: number_of_items={num_items}, total_weight={weight}")

        if num_items > avg_items:
            print(f"More than avg items: {num_items}")
            count_above_avg += 1

        if num_items > 2:
            count_more_than_two_items += 1

        if num_items == 1 and weight < 25:
            has_one_item_less_25 = True

    return count_more_than_two_items, has_one_item_less_25, count_above_avg

"""
if __name__ == "__main__":
    
    a, b, c = check_passenger(passengers)
    print(f"Count of passengers with more than two items: {a}")
    print(f"Is there any passenger with 1 item and total weight < 25: {b}")
    print(f"Count of passengers with items above average: {c}")

    
    try:
        a, b, c = check_passenger([])
    except (ValueError, AssertionError) as e:
        print(f"Error: {e}")"""
        
class TestCheckPassenger(unittest.TestCase):
    
    def test_positive(self):
        passengers = [
            {'number_of_items': 3, 'total_weight': 30},
            {'number_of_items': 1, 'total_weight': 10},
            {'number_of_items': 4, 'total_weight': 40},
            {'number_of_items': 1, 'total_weight': 15},
            {'number_of_items': 5, 'total_weight': 50}
        ]
        result = check_passenger(passengers)
        self.assertEqual(result, (3, True, 3))
        
    def test_all_passengers_above_avg(self):
        passengers = [
            {'number_of_items': 5, 'total_weight': 50},
            {'number_of_items': 6, 'total_weight': 60},
            {'number_of_items': 7, 'total_weight': 70},
        ]
        result = check_passenger(passengers)
        self.assertEqual(result, (3, False, 1))
        
    def test_all_passengers_one_item_heavy(self):
        passengers = [
            {'number_of_items': 1, 'total_weight': 30},
            {'number_of_items': 1, 'total_weight': 40},
            {'number_of_items': 1, 'total_weight': 50},
        ]
        result = check_passenger(passengers)
        self.assertEqual(result, (0, False, 0))
        
    def test_all_passengers_one_item_light(self):
        passengers = [
            {'number_of_items': 1, 'total_weight': 10},
            {'number_of_items': 1, 'total_weight': 5},
        ]
        result = check_passenger(passengers)
        self.assertEqual(result, (0, True, 0))
        
    def test_empty_list(self):
        with self.assertRaises(AssertionError):
            check_passenger([])
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
    

    
        
    
"""
Лабораторная работа №4: Найти сумму произведений из списка словарей

Выполнила: Гончар Юлия

Описание задачи:
Вы работаете над аналитической программой, которая обрабатывает данные в формате JSON.

[
    ...,
    {
        "score": 0.0009456152645028281,
        "weight": 1
    },
    ...
]

Вам поставлена задача реализовать функцию, которая прочитает JSON файл
и найдет сумму произведений двух значений в каждом словаре.
Значения для умножения находятся по ключам "score" и "weight".
Вам нужно вычислить произведение "score" * "weight" в каждом словаре
и найти сумму этих произведений.

Функция должна вернуть значение с плавающей запятой, округленное
до 3 знаков после запятой. В ответе распечатайте полученную сумму.

Тестовые данные нахдятся в файле data.json
[
    {"score": 0.1, "weight": 2},
    {"score": 0.2, "weight": 3},
    {"score": 0.3, "weight": 4}
]
"""

import json

def calculate_product_sum(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            # Используем генератор списков для вычисления произведений и sum для получения суммы
            result = round(sum(item["score"] * item["weight"] for item in data), 3)
            return result
    # Исключения для обработки ошибок и корректности открытия файла
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {filename}.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
filename = "data.json"
result = calculate_product_sum(filename)

if result is not None:
    print(f"Сумма произведений score * weight: {result}")
# Ответ: Сумма произведений score * weight: 2.0

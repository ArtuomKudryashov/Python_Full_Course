def encode(word):
    word = word.lower()
    res = ''

    for char in word:
        if word.count(char) == 1:
            res += '('
        else:
            res += ')'

    return res


def number(bus_stops):
    total_passengers = 0

    for stop in bus_stops:
        total_passengers += stop[0]  # Добавляем количество людей, вошедших в автобус на текущей остановке
        total_passengers -= stop[1]  # Вычитаем количество людей, вышедших из автобуса на текущей остановке

    return max(total_passengers, 0)  # Гарантируем, что количество пассажиров не будет отрицательным

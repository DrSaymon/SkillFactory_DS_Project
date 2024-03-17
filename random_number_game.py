import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    if number > 100 or number < 1:
        raise ValueError('Функция принимает только числа в диапазоне от 1 до 100')
    
    count = 0
    min_num = 0
    max_num = 100
    predict = None

    while number != predict:
        count += 1
        predict = round((min_num+max_num)/2)
        if predict > number:
            max_num = predict
        else:
            min_num = predict

    return count

score_game(game_core_v3)
import numpy as np

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
    min_num = 1
    max_num = 101
    predict = np.random.randint(min_num, max_num)

    while number != predict:
        count += 1
        if predict > number:
            max_num = predict
            predict = np.random.randint(min_num, max_num)
        elif predict < number:
            min_num = predict
            predict = np.random.randint(min_num, max_num)

    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

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

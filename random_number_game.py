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

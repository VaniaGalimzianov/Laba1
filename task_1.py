def binary_search(data, elem):
    low = 0
    high = len(data) - 1
    step_counter = 1
    message = 'Элемента нет в списке'
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == elem:
            return step_counter
        elif data[mid] > elem:
            high = mid - 1
        else:
            low = mid + 1
        step_counter += 1

while True:
    arr = sorted(map(int, input('Введите список чисел через пробел: ').split()))
    elem = int(input('Введите число для поиска: '))
    res = binary_search(arr, elem)
    if res:
        print(f"Элемент найден. Число шагов для поиска: {res}")
    else:
        print('Такого элемента нет в списке')
    
    ans = input('Хотите продолжить(да или нет)? ')
    if ans == 'нет':
        break
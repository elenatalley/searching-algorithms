def binary_search(lst, search_item):
    low = 0
    high = len(lst) - 1
    search_res = False

    while low <= high and not search_res:
        middle = (low + high) // 2
        guess = lst[middle]
        if guess == search_item:
            search_res = True
        if guess > search_item:
            high = middle - 1
        else:
            low = middle + 1
    return search_res


lst = [3, 5, 11, 12, 15, 23, 25, 34, 67, 86]
value = 67
result = binary_search(lst, value)
if result:
    print("Элемент найден!")
else:
    print("Элемент не найден.")




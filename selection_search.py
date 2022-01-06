def SelectionSort(A):
    for i in range(0, len(A) - 1):
        # Среди элементов A[i:] выбираем наименьший
        # Сохраняем его индекс в переменной min_idx
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        # Теперь поставим A[min_idx] на место A[i]
        A[i], A[min_idx] = A[min_idx], A[i]


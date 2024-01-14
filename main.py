import random
import timeit


# Генератор набору даних
def generate_dataset(length: int) -> list[int]:
    dataset = list(range(1, length + 1))
    random.shuffle(dataset)
    return dataset


# Сортування вбудовними в Пайтон методами sort() та sorted()
def timsort_sort(dataset):
    dataset.sort()
    return dataset


def timsort_sorted(dataset):
    return sorted(dataset)


# Сортування злиттям
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Сортування вставками
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def sorting_execution_measurement(length):
    print(f"Генеруємо набір даних з {length} елеметрів")
    dataset = generate_dataset(length)

    # Час виконання 'Timsort' -> sorted
    copy_dataset = dataset.copy()
    execution_time = timeit.timeit(lambda: timsort_sorted(copy_dataset), number=1)
    print(f"Час виконання 'Timsort -> sorted': {execution_time} секунд")

    # Час виконання 'Timsort' -> sort
    copy_dataset = dataset.copy()
    execution_time = timeit.timeit(lambda: timsort_sort(copy_dataset), number=1)
    print(f"Час виконання 'Timsort -> sort': {execution_time} секунд")

    # Час виконання сортування злиттям
    copy_dataset = dataset.copy()
    execution_time = timeit.timeit(lambda: merge_sort(copy_dataset), number=1)
    print(f"Час виконання 'merge': {execution_time} секунд")

    # Час виконання сортування вставкою
    copy_dataset = dataset.copy()
    execution_time = timeit.timeit(lambda: insertion_sort(copy_dataset), number=1)
    print(f"Час виконання 'insertion': {execution_time} секунд")


def main():
    sorting_execution_measurement(10)
    sorting_execution_measurement(100)
    sorting_execution_measurement(1000)
    sorting_execution_measurement(10000)
    sorting_execution_measurement(100000)


if __name__ == "__main__":
    main()

import random


def quick_sort(data, start_index, end_idx):
    if start_index < end_idx:
        q = partition(data, start_index, end_idx)
        quick_sort(data, start_index, q - 1)
        quick_sort(data, q + 1, end_idx)


def randomized_quick_sort(data, start_index, end_idx):
    if start_index < end_idx:
        q = randomized_partition(data, start_index, end_idx)
        randomized_quick_sort(data, start_index, q - 1)
        randomized_quick_sort(data, q + 1, end_idx)


def randomized_partition(data, start_index, end_idx):
    i = random.randint(start_index, end_idx)
    # Swap the random element with the first element
    data[start_index], data[i] = data[i], data[start_index]
    return partition(data, start_index, end_idx)


def partition(data, start_index, end_idx):
    x = data[start_index]  # Pivot
    i = start_index - 1
    for j in range(start_index + 1, end_idx + 1):
        if data[j] < x:
            i = i + 1
            data[i], data[j] = data[j], data[i]  # Swap elements
    # Place the pivot in the correct position
    data[i + 1], data[end_idx] = data[end_idx], data[i + 1]
    return i + 1


# Example usage
if __name__ == "__main__":
    data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    quick_sort(data, 0, len(data) - 1)
    print(data)

    n = [23, 5, 46, 3, 52, 12, 5, 6, 11, 3, 5, 6]
    randomized_quick_sort(n, 0, len(n) - 1)
    print(n)

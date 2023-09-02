import matplotlib.pyplot as plt
import random

data = [random.randint(1, 100) for _ in range(10)]

def visualize(data):
    plt.bar(range(len(data)), data)
    plt.show(block=False)
    plt.pause(0.7)
    plt.close()

def selection_sort_visualized(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        visualize(arr)

selection_sort_visualized(data)
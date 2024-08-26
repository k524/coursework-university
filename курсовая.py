import numpy as np
from scipy.stats import spearmanr
import tkinter as tk
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Ранговый коэффициент корреляции Спирмена")

first_label = tk.Label(root, text="Введите первый массив признаков через пробел(размеры массивов должны совпадать):")
first_entry = tk.Entry(root)

second_label = tk.Label(root, text="Введите второй массив признаков через пробел(размеры массивов должны совпадать):")
second_entry = tk.Entry(root)

def calculate_correlation():
    result_text.delete("1.0", tk.END)
    first = np.array(list(map(float, first_entry.get().split())))
    second = np.array(list(map(float, second_entry.get().split())))

    correlation, p_value = spearmanr(first, second)
    
    result_text.insert(tk.END, f"Ранговый коэффициент корреляции Спирмена: {correlation}\n")

    plt.plot(first, second, 'o')
    m, b = np.polyfit(first, second, 1)
    plt.plot(first, m*first + b)
    plt.xlabel("Первый массив признаков")
    plt.ylabel("Второй массив признаков")
    plt.title("Регрессионная прямая")
    plt.show()
    
calculate_button = tk.Button(root, text="Рассчитать", command=calculate_correlation)
result_text = tk.Text(root)

first_label.pack()
first_entry.pack()

second_label.pack()
second_entry.pack()

calculate_button.pack()
result_text.pack()

root.mainloop()

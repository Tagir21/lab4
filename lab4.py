import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

def my_rand1(n):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(1, 6))

    return rand_list

def my_rand2(n):
    res = random.sample([1, 2, 3, 4, 5, 6] * n, n)
    return res

def my_rand3(n):
    return [random.randrange(1, 7, 1) for i in range(n)]

def my_rand4(n):
    list = []
    for _ in range(n):
        list.append(random.randint(0, 6))

    return list

def my_rand_np1(n):
    return list(np.random.randint(low=1, high=7, size=n))

def count_rate(kub_data: list):
    kub_rate = {}
    for i in range(1, 7):
        if (i in kub_data):
            kub_rate[i] = kub_data.count(i)
        else:
            kub_rate[i] = 0

    return kub_rate


def create_dataframe(sorted_date: dict):
    df = pd.DataFrame(sorted_date, index=[0])
    df = df.T
    df = df.rename(columns={0: 'Частота'})
    df.insert(0, 'Количество выпаданий', range(1, 1 + len(df)))

    return df

def probability_solving(dataframe: pd.DataFrame):
    sum_rate = dataframe['Частота'].sum()
    probability = []
    for i in dataframe['Частота']:
        probability.append(i / sum_rate)
    dataframe['Вероятность'] = probability

    return dataframe

def stages(kube_rate, color):
    df = create_dataframe(kube_rate)
    df = probability_solving(df)
    df['Вероятность'].plot(kind='bar', legend=True, color=color)
    plt.show()

def calc_my_rand1():
    arr = [my_rand1(100), my_rand1(1000), my_rand1(10000), my_rand1(1000000)]
    color = 'blue'
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(count_rate(arr[i]))
    for i in range(len(arr)):
        stages(new_arr[i], color)

def calc_my_rand2():
    arr = [my_rand2(100), my_rand2(1000), my_rand2(10000), my_rand2(1000000)]
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(count_rate(arr[i]))
    color = 'green'
    for i in range(len(arr)):
        stages(new_arr[i], color)

def calc_my_rand3():
    arr = [my_rand3(100), my_rand3(1000), my_rand3(10000), my_rand3(1000000)]
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(count_rate(arr[i]))
    color = 'yellow'
    for i in range(len(arr)):
        stages(new_arr[i], color)

def calc_my_rand4():
    arr = [my_rand4(100), my_rand4(1000), my_rand4(10000), my_rand4(1000000)]
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(count_rate(arr[i]))
    color = 'red'
    for i in range(len(arr)):
        stages(new_arr[i], color)

def calc_my_rand_np():
    arr = [my_rand_np1(100), my_rand_np1(1000), my_rand_np1(10000), my_rand_np1(1000000)]
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(count_rate(arr[i]))
    color = 'purple'
    for i in range(len(arr)):
        stages(new_arr[i], color)

def main():
    calc_my_rand1()
    calc_my_rand2()
    calc_my_rand3()
    calc_my_rand4()
    calc_my_rand_np()

if __name__ == "__main__":
    main()
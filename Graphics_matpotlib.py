import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def Create_Graphics(history):
    paths = []
    categories = []
    for i in history:
        categories.append(i[2])
    categories = sorted(list(set(categories)))
    values = [0 for _ in range(len(categories))]
    for i in range(len(history)):
        values[categories.index(history[i][2])] += history[i][3]
    categories_index = [x for x in range(1, len(categories) + 1)]
    fig, ax = plt.subplots()
    color_rectangle = np.random.rand(7, 3)  # RGB
    bars = ax.bar(categories_index, values, color=color_rectangle)
    fig.set_figwidth(10)
    fig.set_figheight(6)
    ax.legend(bars, categories)
    plt.savefig(r'Graphics\0.png')
    image_path = r'Graphics\0.png'
    img = Image.open(image_path)
    new_image = img.resize((400, 240))
    new_image.save(r'Graphics\0.png')
    paths.append(r'Graphics\0.png')
    plt.close()
    if len(categories) > 1:
        for w in range(1, len(categories) + 1):
            dates = []
            prices = []
            for i in history:
                if i[2] == categories[w - 1]:
                    dates.append(i[1])
            dates = sorted(list(set(dates)))
            prices = [0 for _ in range(len(dates))]
            for i in range(len(history)):
                if history[i][2] == categories[w - 1]:
                    prices[dates.index(history[i][1])] += history[i][3]
            plt.figure(figsize=(8, 6))
            plt.plot(dates, prices, 'o-r')
            plt.savefig(f'Graphics\{w}.png')
            image_path = f'Graphics\{w}.png'
            img = Image.open(image_path)
            new_image = img.resize((800, 600))
            new_image.save(f'Graphics\{w}.png')
            paths.append(f'Graphics\{w}.png')
            plt.close()
    return (paths, categories)

# Create_Graphics([(0, '11.02.3221', 'dwerwer', 1231), (0, '01.01.2023', 'Зарплата и выплаты сотрудникам', 999),
#                  (0, '23.03.2014', 'Зарплата и выплаты сотрудникам', 5466),
#                  (0, '10.12.2006', 'Аренда и коммунальные услуги', 1234), (0, '12.10.2006', 'Я гнида', 4566),
#                  (0, '28.04.2006', 'Транспорт и доставка', 45646),
#                  (0, '01.01.2000', 'Зарплата и выплаты сотрудникам', 0),
#                  (0, '03.09.1990', 'Аренда и коммунальные услуги', 2345)])

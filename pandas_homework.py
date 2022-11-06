import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv', delimiter=',', encoding='utf-8')

# 1. Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел

men = df[df['Sex'] == 'male']
women = df[df['Sex'] == 'female']
q_men = len(men)
q_women = len(women)

print('Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел')
print(q_men, q_women)


# 2. Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров. Ответ приведите в процентах, округлив до двух знаков

survived_people = df[df['Survived'] == 1]
q_survived_people = len(survived_people)
all_passengers = len(df)

survived_part = (q_survived_people / all_passengers) * 100
die_part = 100 - survived_part

print('Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров. Ответ приведите в процентах, округлив до двух знаков')
print(round(survived_part, 2))

# 3. Какую долю пассажиры первого класса составляли среди всех пассажиров? Ответ приведите в процентах, округлив до двух знаков

class_1 = df[df['Pclass'] == 1]
q_passengers_class_1 = len(class_1)

class_1_part = (q_passengers_class_1 / all_passengers) * 100
class_2_3_part = 100 - class_1_part

print('Какую долю пассажиры первого класса составляли среди всех пассажиров? Ответ приведите в процентах, округлив до двух знаков')
print(round(class_1_part, 2))

# 4. Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров. В качестве ответа приведите два числа через пробел

age = round(df['Age'].mean(), 1)
mediana_age = df['Age'].median()

print('Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров. В качестве ответа приведите два числа через пробел')
print(age, mediana_age)

figure = plt.figure(layout='constrained')
ax1 = figure.add_subplot(2, 2, 1)
ax2 = figure.add_subplot(2, 2, 2)
ax3 = figure.add_subplot(2, 2, 3)

# Первый график

bar_labels = ['мужчины', 'женщины']
qwantity_sex = [q_men, q_women]
bar_color = ['blue', 'red']

ax1.bar(bar_labels, qwantity_sex, color = bar_color)
ax1.set_xlabel('Пол', fontsize=6)
ax1.set_ylabel('Количество пассажиров', fontsize=6)
ax1.set_title('Количество пассажиров в зависимости от пола', fontsize=9)

#Второй график

pie_labels = 'Выжившие', 'Погибшие'
pie_size = [survived_part, die_part]
pie_color = ['yellow', 'green']
explode = (0.1, 0)

ax2.pie(pie_size, explode=explode, labels=pie_labels, autopct='%1.1f%%',
        shadow=True, startangle=90, labeldistance=1.3, colors=pie_color)

ax2.set_title('Доля выживших пассажиров', fontsize=9)

#Третий график

pie_labels_2= '1 класс', '2-3 класс'
pie_size_2 = [class_1_part, class_2_3_part]
pie_color_2 = ['red', 'grey']
explode_2 = (0.1, 0)

ax3.pie(pie_size_2, explode=explode_2, labels=pie_labels_2, autopct='%1.1f%%',
        shadow=True, startangle=90, labeldistance=1.3, colors=pie_color_2)

ax3.set_title('Доля пассажиров 1-го класса', fontsize=9)

# Четвертый график






figure.show()
input()

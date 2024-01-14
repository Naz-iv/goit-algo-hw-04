## goit-algo-hw-04

# Набори даних:

Генеруємо список унікальних елементів заданої довжини.
Перемішуємо дані елементи для подальшого використання
під час оцінки ефективності алгоритмів сортування,
Розглядаємо 5 наборів даних з: 10, 1 000, 10 000, 100 000 елементів.
Використовуємо копію одного масиву даних для порівняння алгоритмів,
щоб коректно оцінити ефективність.

# Результати виконання:

| Алгоритм        | Часова складність | 10               | 100            | 1 000            | 10 000     | 10 000      | 
|-----------------|-------------------|------------------|----------------|------------------|------------|-------------|
| Timsort(sorted) | O(n log n)        | 2.0000006771e-06 | 6.70000736e-06 | 6.84999977e-05   | 0.00106710 | 0.0134785   |
| Timsort(sort)   | O(n log n)        | 1.199994585e-06  | 4.00000135e-06 | 5.4999996792e-05 | 0.0009758  | 0.013055    |
| Merge           | O(n log n)        | 1.449999399e-05  | 0.000141299999 | 0.001957600005   | 0.0246956  | 0.3027198   |
| Insertion       | O(n^2)            | 5.299996701e-06  | 0.000187099999 | 0.023313400001   | 2.2188797  | 226.8774536 |


# Висновок

За результатами замірів часу можна стверджувати, що найшвидший алгоритм серед порівнюваних є `Timsort`.
Найповільнішим є алгоритм `Insertion`, зі збільшенням розміру вибірки час виконнання суттєво збільшується, що підтверджує квадратичну складність алгоритму.

Таким чином можна підсумувати, що вбудований алгноритм сортування у `Python` є значно ефективнішим ніж сортування вставкою чи злиттям.

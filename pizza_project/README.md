# Pizza project

 Для работы в файле cli.py нужно установить пакет **click** в терминале: ```pip install click```

Для того чтобы вывести с его помощью меню пишем: ```python cli.py menu```

Получаем:

```- Margherita 🧀: tomato sauce, mozzarella, tomatoes```

```- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni```

```- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples```

------
Чтобы посмотреть на этапы приготовления нашей пиццы: ```python cli.py order peperoni --delivery```

Например, можем получить вывод такого типы (но время может быть другое)

```🔪 приготовили за 4 минут!```

```🛵 доставили за 9 минут!```

------
Переходим к тестированию нашего проекта.

Для запска тестовых функций в терпинале запускаем: ```python -m pytest -v testing.py```

Получем:
 
PS D:\pythonProject1> python -m pytest -v testing.py

=================================== test session starts===================================

platform win32 -- Python 3.10.7, pytest-7.4.3, pluggy-1.3.0 -- D:\python\python.exe

cachedir: .pytest_cache

rootdir: D:\pythonProject1

plugins: cov-4.1.0

=================================== 10 passed in 0.09s ===================================

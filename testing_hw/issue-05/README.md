# issue-05
Сначала устанавливаем плагин под названием *pytest-cov*, который позволит вам вызывать coverage.py от **pytest** с некоторыми дополнительными опциями pytest.
Поскольку coverage является одной из зависимостей *pytest-cov*, достаточно установить *pytest-cov* и он притянет за собой coverage.py:
```pip install pytest-cov```.

Далее хотим вывести отчет о базовом покрытии в терминале нам поможет это сделать команда: ```pytest --cov=what_is_year_now```.

Если вы снова запустите coverage.py с параметром --cov-report=html, будет создан отчет в формате HTML: ```pytest --cov=what_is_year_now --cov-report=html```.

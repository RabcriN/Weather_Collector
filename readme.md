### Описание
Проект **Weather Collector** собирает погодные данные, необходимые для управления мощностями Дата-центров в плане охлаждения и нагрузки.

1. Обращаемся к сторонней API для получения списка ТОП-50 городов мира по количеству населения.

2. Получаем и обрабатываем информацию от API https://openweathermap.org/

3. Сохраняем полученные данные в БД.

4. Повторяем процедуру спустя 1 час.


### Как запустить проект:
Клонировать репозиторий:
```
git clone https://github.com/RabcriN/weather_collector
```
Обновить pip: 
```
python -m pip install --upgrade pip
```
Установить зависимости:
```
python -m pip install -r requirements.txt
```
Запустить проект:
```
python main.py
```
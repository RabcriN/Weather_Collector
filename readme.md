### Описание
Проект **Weather Collector** собирает погодные данные, необходимые для управления мощностями Дата-центров в плане охлаждения и нагрузки.

1. Обращаемся к стороннему API для получения списка ТОП-50 городов мира по количеству населения.

2. Получаем и обрабатываем информацию от API https://openweathermap.org/

3. Сохраняем полученные данные в БД.

4. Повторяем процедуру спустя 1 час.


### Как запустить проект:
Клонировать репозиторий:
```
git clone https://github.com/RabcriN/Weather_Collector
```
Cоздать и активировать виртуальное окружение:
Команда для установки виртуального окружения (Mac/Linux):
```
python3 -m venv env
source venv/bin/activate
```
Команда для Windows должна быть такая:
```
python -m venv venv
source venv/Scripts/activate
```
Обновить pip:
```
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить проект:
```
python main.py
```

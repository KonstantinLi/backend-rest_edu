# RESTful web service (education)
> Власність студента **Ліненка Костянтина** групи *ІО-01 ФІОТ*

## Котроткий опис

Репозиторій створений в навчальних цілях для вивчення основних принципів створення RESTful додатків, використовуючи **Python Flask**.  

Проект використовує теги версій, що відображають етапи розробки застосунку на лабораторних роботах №1 та №2:
1. tag v1.0.0 - лаб1
2. tag v1.0.1 - лаб2
3. tag v1.0.2 - лаб3

## Лабораторна робота №1
Метою роботи є налаштування базового REST API та його деплой.

Реалізовані ендпоінти:
* Створення та видалення користувача 
* Створення та видалення категорії витрат
* Створення та видалення запису про витрати
* Отримання списку категорій
* Отримання списку записів по певному користувачу
* Отримання списку записів в категорії для певного користувача

### Домен
Застосунок задеплоєний на платформу https://www.heroku.com

Результуючий URL адрес: https://flask2022-2-restapi.herokuapp.com

## Запуск на локальній машині

Для початку необхідно клонувати проект у свою робочу директорію:

```
git clone https://github.com/KonstantinLi/backend-rest_edu.git
```

Далі запустити проект можна декількома способами.

#### Для користувачів IDE **PyCharm Pro**:
1. Додати нову конфігурацію `Flask server`
2. В секції `Configuration` в полі `Target type` обрати **Script path**
3. Прописати шлях до виконавчого модуля ***__init__.py*** пакету ***app*** `<your_directory>/app/__init__.py`
4. В полі `Application` прописати змінну об'єкта **Flask app** `app`
5. Обраний `Python interpreter` повинен бути версії **3.x**
6. Перевірити, що шлях в `Working directory` відповідає вашій робочій директорії

#### Виористовуючи **контейнер Docker**:
1. Завантажити Docker з офіційного сайту https://www.docker.com/
2. Знаходячись у робочій директорії, створити образ  проекту. Для цього необхідно прописати в консолі
```
  docker build -t flask_app:latest .
```
3. Збілдити та запустити контейнер за допомогою команд
```
  docker-compose build
  docker-compose up
```

## Лабораторна робота №2
На цьому етапі реалізується робота с базою даних SQlite. Для цього створюються entities, що є відображенням таблиць БД у об'єктно орієнтованій манері.

Для перевірки тіл запитів та респонсів використовуються об'екти Schema пакету marshmallow.

Також були застосовані Blueprint's для полегшення підтримки коду.

### Варіант додаткового завдання - **1**
Валюти:
1. Додаткова сутність Currency
2. Зв'язки між таблицями currency та users
3. Значення обраної користувачем валюти за замовчуванням - **Hryvnia**
4. Новий ендпоінт: GET /currency - вивід списка валют

## Лабораторна робота №3
Були створені нові ендпоінти реєстрації та авторизації користувачів. Вони виконуються на однаковому URI /users з параметрами **name** і **password**, але їх відмінність у значенні параметра **type**:
* "auth" - авторизація
* "registration" - реєстрація

Тепер для вже створених ендпоінтів, які повинні бути доступними лише для авторизованих користувачів, створений захист у вигляді декоратора @jwt_required(), який потребує **access token**, отримати який можна лише при успішній авторизації.

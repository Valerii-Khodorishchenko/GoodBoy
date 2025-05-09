# Good boy
Цель приложения дисциплинировать пользователей регулярно заниматься любимыми
делами отслеживая прогресс, внедряя систему самонаград и ограничений.
Пользователь сам выбирает награды, ценность действий на пути к развитию и
ограничения на отвлекающие от развития факторы.
Статистика дней до достижения цели, должна предвкушать ожидаемую награду за
вложенные усилия, что позволит увеличить темп прогресса в любимом занятии.
Ограничения мотивируют рационально распределять время.


## MVP
- Один локальный пользователь
- Создание занятий
- Создания дел(метрик для отслеживания) эквивалент балл или человеко\час
- Создание наград(количество баллов или человеко\часов которыми пользователь
оценивает свой вклад в развитие в любимом деле до получения вознаграждения).
- Накопив необходимое количество баллов пользователь может получить одну из
созданных для себя наград.
- Создание ограничений на занятия основными тайм киллирами (хочешь
прокрастинировать, заслужи). Может быть как положительным (накопил), так и 
отрицательным (взял у себя в займы).
- Отслеживание статистики достижения наград и наложенных ограничений.
- Статистика за месяц показывающая темп.

## Отложенные функции
- Планы достижения целей, TODO для отслеживания еще и мелких задач на пути к целям.
- Авторизация, профили, синхронизация, напоминания, приватизация информации профиля, друзья, соревнования, совместные кранчи, Геймификация, кастомизация профилей
- История активности по датам как мозайка коммитов в GitHub, Аналитика, графики прогресса,
- Юзер-френдли интерфейс с растягиванием перетаскиванием.


## Установка
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Valerii-Khodorishchenko/GoodBoy.git
cd goodboy
```
Создать и заполнить файл `.env` переменными окружения

```bash
touch .env
# Имя приложения (название директории с Flask-приложением)
echo "FLASK_APP=goodboy" >> .env
# Режим отладки: 1—включено, 0—выключено. Не используйте отладку в продакшене!
echo "FLASK_DEBUG=0" >> .env
# Конфигурация базы данных: создаст db.sqlite3 в папке ./instance
# Используйте любую базу данных, поддерживаемую Flask-SQLAlchemy
echo "DATABASE_URI=sqlite:///db.sqlite3" >> .env
# Генерация секретного ключа
echo "SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(32))')" >> .env
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```
## Запуск
<!-- ### Подготовка базы данных к запуску
Необходимо выполнить только при первом запуске, а также если были внесены 
изменения в модели проекта. Сама база данных будет создана по адресу `./instance/db/sqlite3`
```bash
flask db upgrade
```
Для того чтобы запустить сервис в первый и последующие разы используйте -->

```bash
flask run
```
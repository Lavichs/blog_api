# Blogging Platform API


![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-007ACC?style=for-the-badge&logo=fastapi&logoColor=white) 
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white) 
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) 
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-000000?style=for-the-badge&logo=docker&logoColor=white) 
![Уровень сложности: Простой](https://img.shields.io/badge/Уровень%20сложности-Простой-green.svg)


## Содержание

- [Описание](#описание)
- [Используемые_технологии](#используемые-технологии-и-навыки)
- [Функциональность](#функциональность)
- [Установка и запуск](#установка-и-запуск)
- [Установка и запуск в Docker](#установка-и-запуск-в-docker)
- [Структура проекта](#структура-проекта)
- [Заключение](#заключение)

## Описание

Это RESTful API для управления персональным блогом. API поддерживает основные операции CRUD (Создание, Чтение, Обновление и Удаление) для постов блога. Вы сможете добавлять, обновлять и удалять статьи, а также извлекать их список или отдельные статьи по их идентификатору.

## Уровень сложности

Легкий

## Используемые технологии и навыки

- CRUD для основных операций
- Работа с базами данных SQL
- Серверный RESTful API
- FastAPI (Python)
- Docker, docker-compose

## Функциональность

API поддерживает следующие эндпоинты:

- **GET /posts**: Возвращает список статей (с возможностью фильтрации по дате публикации и тегам).
- **GET /posts/{id}**: Возвращает отдельную статью по указанному идентификатору.
- **POST /posts**: Создает новую статью.
- **PUT /posts/{id}**: Обновляет статью по указанному идентификатору.
- **DELETE /posts/{id}**: Удаляет статью по указанному идентификатору.

## Установка и запуск

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/Lavichs/blog_api.git
    cd blog_api
    ```
   
2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

3. Создайте файл .env в корневой директории проекта по примеру в .env.sample

4. Создайте базу данных в postgresql
5. Выполните миграции базы данных:
    ```bash
    alembic upgrade head
    ```

6Для запуска приложения выполните следующую команду:
   ```bash
   uvicorn main:app --reload
   ```
   
API будет доступно по адресу http://localhost:8000.

## Установка и запуск в Docker

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/Lavichs/blog_api.git
    cd blog_api
    ```
   
2. Соберите и запустите проект с помощью docker-compose:
    ```bash
    docker-compose up --build
    ```

3. Выполните миграции базы данных:
    Войдите в контейнер приложения:
    ```bash
    docker-compose exec server bash
    ```
   Выполните миграции:
    ```bash
    alembic upgrade head
    ```
   
API будет доступно по адресу http://localhost:8000.

## Структура проекта
- `main.py`: Основной файл приложения, содержащий настройки и конфигурацию FastAPI.
- `config.py`: Файл конфигурации, который управляет настройками базы данных с помощью библиотеки Pydantic.
- `router.py`: Определяет маршруты для работы с постами блога.
- `database.py`: Содержит функции для управления таблицами базы данных.
- `schemas.py`: Содержит схемы и модели для валидации Pydantic.
- `repository.py`: Реализует паттерн репозиторий для сущности Посты.



## Заключение
Это простой учебный проект созданный в целях ознакомления в фреймворком FatAPI.





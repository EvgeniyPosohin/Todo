# Todo Project

Веб-приложение для управления задачами, построенное на Django. Позволяет пользователям создавать, редактировать и отслеживать свои задачи с поддержкой категорий, приоритетов и статусов.

## Возможности

- 🔐 Система аутентификации пользователей
- 📝 Создание, редактирование и удаление задач
- 📂 Организация задач по категориям
- 🎯 Установка приоритетов (низкий, средний, высокий)
- 📊 Отслеживание статуса задач (к выполнению, в процессе, выполнено)
- 🔍 Поиск и фильтрация задач
- 📅 Установка дат выполнения с отслеживанием просроченных задач
- 📱 Адаптивный интерфейс 

![интерфейс](https://github.com/EvgeniyPosohin/Todo/blob/main/todoproject/task/templates/image/task_list.png)
![интерфейс](https://github.com/EvgeniyPosohin/Todo/blob/main/todoproject/task/templates/image/new_task.png)

## Технологии

- **Backend**: Django 5.2.5
- **API**: Django REST Framework (DRF)
- **База данных**: SQLite (по умолчанию), поддержка PostgreSQL
- **Frontend**: HTML, CSS, Django Templates
- **Документация API**: Swagger/OpenAPI, ReDoc
- **Аутентификация API**: dj-rest-auth
- **Python**: 3.8+

## Установка и запуск

### Предварительные требования

- Python 3.8 или выше
- pip (менеджер пакетов Python)

### Шаги установки

1. **Клонируйте репозиторий**
   ```bash
   git clone <url-репозитория>
   cd todoproject
   ```

2. **Создайте виртуальное окружение**
   ```bash
   python -m venv .venv
   ```

3. **Активируйте виртуальное окружение**
   
   Windows:
   ```cmd
   .venv\Scripts\activate
   ```
   
   Linux/macOS:
   ```bash
   source .venv/bin/activate
   ```

4. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

5. **Выполните миграции базы данных**
   ```bash
   cd todoproject
   python manage.py migrate
   ```

6. **Создайте суперпользователя (опционально)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Запустите сервер разработки**
   ```bash
   python manage.py runserver
   ```

8. **Откройте приложение в браузере**
   
   - Веб-интерфейс: http://127.0.0.1:8000/
   - API документация (Swagger): http://127.0.0.1:8000/swagger/
   - API документация (ReDoc): http://127.0.0.1:8000/redoc/

## Структура проекта

```
todoproject/
├── todoproject/           # Основная директория Django проекта
│   ├── settings.py       # Настройки проекта
│   ├── urls.py          # Главные URL маршруты
│   └── wsgi.py          # WSGI конфигурация
├── task/                 # Приложение для управления задачами
│   ├── models.py        # Модели данных (Task, Category)
│   ├── views.py         # Представления
│   ├── forms.py         # Формы
│   ├── urls.py          # URL маршруты приложения
│   └── templates/       # HTML шаблоны
├── api/                  # REST API приложение
│   ├── views.py         # API представления (ViewSets)
│   ├── serializers.py   # Сериализаторы для API
│   ├── urls.py          # API маршруты
│   └── permissions.py   # Права доступа API
├── manage.py            # Утилита управления Django
├── requirements.txt     # Зависимости Python
└── README.md           # Документация проекта
```

## Модели данных

### Task (Задача)
- `title` - название задачи
- `description` - описание задачи
- `category` - категория задачи
- `status` - статус (к выполнению, в процессе, выполнено)
- `priority` - приоритет (низкий, средний, высокий)
- `date` - дата выполнения
- `owner` - владелец задачи
- `create_at` - дата создания
- `update_at` - дата последнего обновления

### Category (Категория)
- `name` - название категории
- `owner` - владелец категории

## Использование

### Веб-интерфейс

1. **Регистрация/Вход**: Создайте аккаунт или войдите в существующий
2. **Создание категорий**: Организуйте свои задачи по категориям
3. **Добавление задач**: Создавайте новые задачи с описанием, приоритетом и датой
4. **Управление задачами**: Редактируйте статус, приоритет и другие параметры
5. **Поиск и фильтрация**: Используйте фильтры для быстрого поиска нужных задач

## REST API

Проект предоставляет полнофункциональный REST API для интеграции с внешними приложениями и мобильными клиентами.

### Базовый URL
```
http://127.0.0.1:8000/api/v1/
```

### Аутентификация

API поддерживает несколько методов аутентификации:

1. **Session Authentication** - для веб-интерфейса
2. **Token Authentication** - для внешних приложений
3. **dj-rest-auth** - для регистрации и аутентификации через API

#### Получение токена
```bash
# Регистрация нового пользователя
POST /api/v1/dj-rest-auth/registration/
{
    "username": "newuser",
    "email": "user@example.com",
    "password1": "securepassword123",
    "password2": "securepassword123"
}

# Вход и получение токена
POST /api/v1/dj-rest-auth/login/
{
    "username": "newuser",
    "password": "securepassword123"
}
```

### Основные endpoints

#### Задачи (Tasks)
```bash
# Получить все задачи пользователя
GET /api/v1/tasks/

# Создать новую задачу
POST /api/v1/tasks/
{
    "title": "Новая задача",
    "description": "Описание задачи",
    "status": "todo",
    "priority": "medium",
    "date": "2024-12-31"
}

# Получить конкретную задачу
GET /api/v1/tasks/{id}/

# Обновить задачу
PUT /api/v1/tasks/{id}/
PATCH /api/v1/tasks/{id}/

# Удалить задачу
DELETE /api/v1/tasks/{id}/
```

#### Категории (Categories)
```bash
# Получить все категории пользователя
GET /api/v1/category/

# Создать новую категорию
POST /api/v1/category/
{
    "name": "Работа"
}

# Получить конкретную категорию
GET /api/v1/category/{id}/

# Обновить категорию
PUT /api/v1/category/{id}/
PATCH /api/v1/category/{id}/

# Удалить категорию
DELETE /api/v1/category/{id}/
```

#### Пользователи (Users)
```bash
# Получить список пользователей
GET /api/v1/users/

# Получить информацию о пользователе
GET /api/v1/users/{id}/
```

### Примеры использования API

#### Создание задачи с помощью curl
```bash
curl -X POST http://127.0.0.1:8000/api/v1/tasks/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Изучить Django REST Framework",
    "description": "Пройти документацию и создать тестовый проект",
    "status": "todo",
    "priority": "high",
    "date": "2024-12-31"
  }'
```

#### Получение задач с помощью JavaScript
```javascript
fetch('http://127.0.0.1:8000/api/v1/tasks/', {
  method: 'GET',
  headers: {
    'Authorization': 'Token YOUR_TOKEN_HERE',
    'Content-Type': 'application/json',
  },
})
.then(response => response.json())
.then(data => console.log(data));
```

### Документация API

- **Swagger UI**: http://127.0.0.1:8000/swagger/ - интерактивная документация с возможностью тестирования
- **ReDoc**: http://127.0.0.1:8000/redoc/ - альтернативный интерфейс документации

### Права доступа

API использует систему прав доступа:
- Пользователи могут просматривать и редактировать только свои задачи и категории
- Неаутентифицированные пользователи имеют доступ только на чтение к публичным данным
- Администраторы имеют полный доступ ко всем ресурсам

## Разработка

### Запуск тестов
```bash
# Запуск всех тестов
python manage.py test

# Запуск тестов только для API
python manage.py test api

# Запуск тестов с подробным выводом
python manage.py test --verbosity=2
```

### Тестирование API

Для тестирования API можно использовать различные инструменты:

#### Использование Django REST Framework Browsable API
Перейдите по адресу http://127.0.0.1:8000/api/v1/ для интерактивного тестирования

#### Использование Postman или Insomnia
Импортируйте коллекцию endpoints из Swagger документации

#### Использование httpie
```bash
# Установка httpie
pip install httpie

# Примеры запросов
http GET http://127.0.0.1:8000/api/v1/tasks/ "Authorization:Token YOUR_TOKEN"
http POST http://127.0.0.1:8000/api/v1/tasks/ title="Test Task" "Authorization:Token YOUR_TOKEN"
```

### Создание миграций
```bash
python manage.py makemigrations
python manage.py migrate
```

### Сбор статических файлов
```bash
python manage.py collectstatic
```

### Генерация OpenAPI схемы
```bash
python manage.py generateschema --file openapi-schema.yml
```

## Конфигурация для продакшена

Для развертывания в продакшене:

1. Установите `DEBUG = False` в settings.py
2. Настройте `ALLOWED_HOSTS`
3. Используйте PostgreSQL вместо SQLite
4. Настройте переменные окружения для секретных ключей
5. Настройте веб-сервер (nginx + gunicorn)
6. Настройте CORS для API (если требуется доступ с других доменов)
7. Настройте rate limiting для API endpoints
8. Используйте HTTPS для безопасной передачи токенов
9. Настройте мониторинг API endpoints

## Лицензия

Этот проект распространяется под лицензией MIT.

## Контакты

Если у вас есть вопросы или предложения, создайте issue в репозитории проекта.

# ПРОЕКТ "СВОЙ КРУГ"
## ПОЛНОЕ ТЕХНИЧЕСКОЕ ОПИСАНИЕ СИСТЕМЫ

**Версия:** 2.0  
**Дата:** Ноябрь 2025  
**Статус:** Pre-MVP разработка  

---

## СОДЕРЖАНИЕ

1. [EXECUTIVE SUMMARY](#executive-summary)
2. [БИЗНЕС-МОДЕЛЬ И МОНЕТИЗАЦИЯ](#бизнес-модель-и-монетизация)
3. [ТЕХНИЧЕСКАЯ АРХИТЕКТУРА](#техническая-архитектура)
4. [ДЕТАЛЬНОЕ ОПИСАНИЕ МОДУЛЕЙ](#детальное-описание-модулей)
5. [ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ](#функциональные-требования)
6. [СИСТЕМА ГЕЙМИФИКАЦИИ И СТАТУСОВ](#система-геймификации-и-статусов)
7. [СИСТЕМА МЕРОПРИЯТИЙ](#система-мероприятий)
8. [АНАЛИТИКА И МЕТРИКИ](#аналитика-и-метрики)
9. [БЕЗОПАСНОСТЬ И COMPLIANCE](#безопасность-и-compliance)
10. [ДОРОЖНАЯ КАРТА РАЗРАБОТКИ](#дорожная-карта-разработки)
11. [РИСКИ И МИТИГАЦИЯ](#риски-и-митигация)

---

## EXECUTIVE SUMMARY

### Концепция проекта
**"Свой Круг"** - цифровая экосистема женских премиальных бизнесов, объединяющая независимые компании в единое клубное пространство с общей системой лояльности, аналитики и социального взаимодействия.

### Философия
Не бонусная карта, а **закрытое женское сообщество**, где каждая покупка = вклад в общую атмосферу доверия и статус внутри клуба.

### Ключевые отличия от конкурентов
1. **Не агрегатор** - надстройка над существующими CRM без вмешательства
2. **Не маркетплейс** - закрытый клуб с отбором партнеров
3. **Не просто скидки** - геймификация + социальное влияние
4. **Женское сообщество** - эмоциональная привязка через мероприятия

### Текущий статус
- **5 подтвержденных партнеров** на старте
- **Цель:** 500 активных участниц за первые 6 месяцев
- **География:** Один город (пилот)
- **Команда:** Solo-разработка

---

## БИЗНЕС-МОДЕЛЬ И МОНЕТИЗАЦИЯ

### Модель монетизации (гибридная)

#### Вариант 1: Revenue Share от вовлеченных транзакций
```
Комиссия = 3-5% от суммы покупки, совершенной благодаря платформе

Что считается "вовлеченной транзакцией":
- Клиент пришел в бизнес B после активации промо-кода от бизнеса A
- Клиент использовал кросс-бонусы внутри экосистемы
- Клиент забронировал услугу через приложение
```

**Пример расчета:**
```
Клиентка купила в салоне Миндаль маникюр за 3000₽ 
→ пришла по промо из гастромаркета Лисичкино
→ платформа получает 3000₽ × 3% = 90₽

Среднемесячная выручка при 500 клиентах:
500 клиентов × 2 кросс-покупки/мес × 3500₽ средний чек × 3% = 105,000₽/мес
```

#### Вариант 2: Фиксированная абонентская плата бизнесов
```
Тариф "Участник": 15,000₽/мес
- Доступ к аналитике
- Участие в кросс-промо
- 1 мероприятие в квартал

Тариф "Партнер": 25,000₽/мес
- Всё из "Участник"
- API-интеграция
- Приоритет в рекомендациях
- Неограниченные мероприятия
```

#### Вариант 3: Премиум-подписка для клиенток
```
"Свой Круг Premium": 1990₽/мес для участниц
- Автоматический VIP-статус
- Повышенный кешбэк (10% вместо 5%)
- Бесплатный вход на закрытые мероприятия
- Priority booking
- Персональный консьерж
```

### Рекомендуемая стратегия на старте
**Гибридная модель:**
1. **Первые 6 месяцев:** 0% комиссии для партнеров (привлечение)
2. **С 7-го месяца:** Revenue Share 2% (мягкий вход)
3. **С 12-го месяца:** Запуск Premium-подписки для клиенток
4. **С 18-го месяца:** Полноценная модель (3-5% + подписки)

---

## ТЕХНИЧЕСКАЯ АРХИТЕКТУРА

### Общая схема системы

```
┌─────────────────────────────────────────────────────────────────┐
│                    КЛИЕНТСКИЕ ПРИЛОЖЕНИЯ                        │
│  ┌──────────────────┐  ┌──────────────────┐  ┌───────────────┐ │
│  │ iOS приложение   │  │ Android          │  │  Web-версия   │ │
│  │ (React Native)   │  │ приложение       │  │  (PWA)        │ │
│  └──────────────────┘  └──────────────────┘  └───────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              ↓ ↑ REST API / GraphQL
┌─────────────────────────────────────────────────────────────────┐
│                      API GATEWAY (Kong/Nginx)                    │
│                    - Rate Limiting                               │
│                    - Authentication (JWT)                        │
│                    - Load Balancing                              │
└─────────────────────────────────────────────────────────────────┘
                              ↓ ↑
┌─────────────────────────────────────────────────────────────────┐
│                     BACKEND МИКРОСЕРВИСЫ                         │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────────┐│
│  │ User Service │ │ Loyalty      │ │ Events Service          ││
│  │ (Профили,    │ │ Service      │ │ (Мероприятия,           ││
│  │  Аутентифик.)│ │ (Бонусы,     │ │  Голосования,           ││
│  │              │ │  Статусы)    │ │  Конструктор)           ││
│  └──────────────┘ └──────────────┘ └──────────────────────────┘│
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────────┐│
│  │ Transaction  │ │ Analytics    │ │ Notification Service    ││
│  │ Service      │ │ Service      │ │ (Push, Email, SMS)      ││
│  │ (Покупки,    │ │ (Метрики,    │ │                         ││
│  │  История)    │ │  Дашборды)   │ │                         ││
│  └──────────────┘ └──────────────┘ └──────────────────────────┘│
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────────┐│
│  │ Integration  │ │ Business     │ │ Referral Service        ││
│  │ Service      │ │ Admin        │ │ (Реферальная            ││
│  │ (API коннект)│ │ Service      │ │  программа)             ││
│  └──────────────┘ └──────────────┘ └──────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
                              ↓ ↑
┌─────────────────────────────────────────────────────────────────┐
│                         DATA LAYER                               │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────────┐│
│  │ PostgreSQL   │ │ ClickHouse   │ │ Redis                   ││
│  │ (Основные    │ │ (Аналитика,  │ │ (Кеш, Сессии,           ││
│  │  данные)     │ │  OLAP)       │ │  Очереди)               ││
│  └──────────────┘ └──────────────┘ └──────────────────────────┘│
│  ┌──────────────┐ ┌──────────────┐                             │
│  │ S3-storage   │ │ Elasticsearch│                             │
│  │ (Фото, файлы)│ │ (Полнотекст) │                             │
│  └──────────────┘ └──────────────┘                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓ ↑
┌─────────────────────────────────────────────────────────────────┐
│                  ВНЕШНИЕ ИНТЕГРАЦИИ                              │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────────┐│
│  │ 1С           │ │ Bitrix24     │ │ YCLIENTS                ││
│  │ (Skinerica,  │ │ (Skinerica)  │ │ (Миндаль)               ││
│  │  Лисичкино)  │ │              │ │                         ││
│  └──────────────┘ └──────────────┘ └──────────────────────────┘│
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────────┐│
│  │ AMO CRM      │ │ МИС Renovatio│ │ Iiko                    ││
│  │ (Стим Центр) │ │ (Миллениум)  │ │ (Лисичкино)             ││
│  └──────────────┘ └──────────────┘ └──────────────────────────┘│
│  ┌──────────────┐ ┌──────────────┐                             │
│  │ Платежи      │ │ SMS/Email    │                             │
│  │ (ЮKassa,     │ │ провайдеры   │                             │
│  │  CloudPaym.) │ │              │                             │
│  └──────────────┘ └──────────────┘                             │
└─────────────────────────────────────────────────────────────────┘
```

### Технологический стек

#### Frontend (Мобильное приложение)
```yaml
Framework: React Native 0.73+
State Management: Redux Toolkit + RTK Query
Navigation: React Navigation 6
UI Library: React Native Paper (кастомизированная под Tiffany-стиль)
QR/Barcode: react-native-vision-camera + react-native-qrcode-scanner
Offline Support: Redux Persist + AsyncStorage
Push Notifications: Firebase Cloud Messaging (FCM)
Analytics: Firebase Analytics + Amplitude
Crash Reporting: Sentry

Ключевые компоненты:
- QR-wallet (цифровая карта участника)
- Gamification Ring (кольцо прогресса статуса)
- Event Builder (конструктор мероприятий)
- Loyalty Dashboard (панель бонусов)
```

#### Backend
```yaml
Primary Language: Python 3.11+
Framework: FastAPI 0.104+
Task Queue: Celery + Redis
Background Jobs: APScheduler (для cron-задач)
API Documentation: OpenAPI 3.0 (Swagger UI)

Вспомогательные библиотеки:
- Pydantic v2 (валидация данных)
- SQLAlchemy 2.0 (ORM)
- Alembic (миграции БД)
- python-jose (JWT токены)
- passlib (хеширование паролей)
- httpx (async HTTP клиент для интеграций)
- pandas (аналитика)
```

#### Базы данных
```yaml
PostgreSQL 15:
  - Пользователи, профили
  - Транзакции, бонусы
  - Мероприятия, голосования
  - Бизнес-данные

ClickHouse 23:
  - Аналитические отчеты
  - Метрики поведения
  - Когортный анализ
  - RFM-сегментация

Redis 7:
  - Кеш API-ответов
  - Сессии пользователей
  - Очереди задач (Celery)
  - Rate limiting

Elasticsearch 8:
  - Полнотекстовый поиск по мероприятиям
  - Поиск клиентов для админки
```

#### Инфраструктура
```yaml
Контейнеризация: Docker + Docker Compose
Оркестрация (prod): Kubernetes (опционально на будущее)
CI/CD: GitHub Actions / GitLab CI
Мониторинг: 
  - Prometheus + Grafana (метрики)
  - Sentry (ошибки)
  - Uptimerobot (доступность)
Logging: ELK Stack (Elasticsearch, Logstash, Kibana)

Облачная платформа (РФ):
  - Yandex Cloud / VK Cloud / Selectel
  - S3-совместимое хранилище для файлов
  - Managed PostgreSQL + Redis
```

### Схема безопасности

```
┌─────────────────────────────────────────────────────┐
│              УРОВНИ БЕЗОПАСНОСТИ                    │
├─────────────────────────────────────────────────────┤
│ 1. Сетевой уровень                                  │
│    - Firewall (только порты 80, 443)                │
│    - DDoS protection (Cloudflare/Yandex)            │
│    - VPN для доступа к админке                      │
├─────────────────────────────────────────────────────┤
│ 2. Аутентификация                                   │
│    - JWT токены (access + refresh)                  │
│    - 2FA для бизнес-аккаунтов (TOTP)                │
│    - Биометрия (FaceID/TouchID) в приложении        │
├─────────────────────────────────────────────────────┤
│ 3. Авторизация (RBAC)                               │
│    - Роль: Клиент (Insider/VIP/Elite)               │
│    - Роль: Менеджер бизнеса                         │
│    - Роль: Владелец бизнеса                         │
│    - Роль: Суперадмин экосистемы                    │
├─────────────────────────────────────────────────────┤
│ 4. Шифрование данных                                │
│    - In Transit: TLS 1.3 (HTTPS only)               │
│    - At Rest: AES-256-GCM                           │
│    - ПДн: отдельное шифрование (envelope)           │
├─────────────────────────────────────────────────────┤
│ 5. Compliance (152-ФЗ, врачебная тайна)             │
│    - Хранение данных в РФ                           │
│    - Раздельное хранение ПДн и транзакций           │
│    - Логирование всех операций с ПДн                │
│    - Псевдонимизация для аналитики                  │
│    - Политика согласий (GDPR-like)                  │
└─────────────────────────────────────────────────────┘
```

---

## ДЕТАЛЬНОЕ ОПИСАНИЕ МОДУЛЕЙ

### МОДУЛЬ 1: МОБИЛЬНОЕ ПРИЛОЖЕНИЕ (Frontend)

#### 1.1 Архитектура приложения

```
src/
├── app/
│   ├── App.tsx                 # Точка входа
│   ├── navigation/             # Навигация
│   │   ├── RootNavigator.tsx
│   │   ├── AuthNavigator.tsx
│   │   └── MainTabNavigator.tsx
│   └── theme/                  # Tiffany-стиль
│       ├── colors.ts
│       ├── typography.ts
│       └── liquidGlass.ts
├── features/                   # Модули по функциям
│   ├── auth/
│   │   ├── screens/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── api/
│   ├── profile/
│   ├── loyalty/
│   ├── events/
│   ├── qr-wallet/
│   └── analytics/
├── shared/                     # Общие компоненты
│   ├── components/
│   ├── hooks/
│   ├── utils/
│   └── api/
└── store/                      # Redux store
    ├── slices/
    └── middleware/
```

#### 1.2 Экраны приложения

**1.2.1 Onboarding & Auth**
```typescript
// Экран приветствия (первый запуск)
WelcomeScreen:
  - Видео-презентация клуба (30 сек)
  - 3 слайда с преимуществами
  - Кнопка "Вступить в Свой Круг"

// Регистрация
RegistrationScreen:
  Поля:
  - Имя, фамилия
  - Телефон (с подтверждением SMS)
  - Email (опционально)
  - Дата рождения
  - Город
  - Согласие на обработку ПДн
  - Согласие на получение рассылок
  
  Фичи:
  - Автозаполнение из контактов (если есть доступ)
  - Валидация в реальном времени
  - Реферальный код (если пришла по приглашению)

// Вход
LoginScreen:
  - Вход по телефону + SMS-код
  - Вход по FaceID/TouchID (после первой настройки)
  - "Забыли пароль?" → восстановление
```

**1.2.2 Главный экран (Home)**
```typescript
HomeScreen:
  Header:
    - Аватар пользователя + уровень статуса
    - Кнопка уведомлений (badge с количеством)
    - Кнопка QR-кода (быстрый доступ)
  
  Секция 1: Кольцо прогресса (Gamification Ring)
    - Визуализация прогресса до следующего статуса
    - Процент выполнения: "78% до VIP"
    - Подсказка: "Осталось 2 категории и 8,500₽"
    - Анимация при достижении
  
  Секция 2: Активные бонусы и промо
    - Карусель текущих акций
    - Таймер сгорания (если есть ограничение)
    - Кнопка "Использовать" → навигация в бизнес
  
  Секция 3: Рекомендации
    - "Попробуйте новое" (AI-рекомендации на основе истории)
    - Пример: "Вы часто посещаете салон. Попробуйте косметологию!"
  
  Секция 4: Ближайшие мероприятия
    - Карточки событий с датами
    - Статус регистрации (зарегистрирован / есть места / waitlist)
  
  Bottom Navigation:
    - Главная (Домик)
    - Мероприятия (Календарь)
    - QR-кошелек (QR-код)
    - Бизнесы (Список партнеров)
    - Профиль (Аватар)
```

**1.2.3 QR-Кошелек**
```typescript
QRWalletScreen:
  Визуал:
    - Большой QR-код по центру
    - Уникальный ID участницы
    - Уровень статуса (бейдж: Insider/VIP/Elite)
    - Баланс бонусов (крупно)
  
  Функции:
    - Яркость экрана автоматически на 100% при открытии
    - Режим "Не гаснет" пока экран открыт
    - Поворот QR-кода для удобства сканирования
    - Apple Wallet / Google Pay интеграция (добавить карту в кошелек)
  
  История транзакций (внизу):
    - Последние 5 начислений/списаний
    - Кнопка "Показать всё" → TransactionHistoryScreen
```

**1.2.4 Профиль**
```typescript
ProfileScreen:
  Header:
    - Большой аватар (с возможностью редактирования)
    - Имя, фамилия
    - Статус (Insider/VIP/Elite) + бейдж
    - Уровень влияния (если Elite) - вес голоса
  
  Статистика:
    - Всего покупок: 42
    - Посещено категорий: 5 из 9
    - Накоплено бонусов: 12,450₽
    - Участие в мероприятиях: 8
  
  Секции:
    ├── История покупок
    ├── Мои бонусы и купоны
    ├── Реферальная программа
    │   └── "Пригласить подругу" → генерация ссылки
    ├── Настройки
    │   ├── Уведомления (push/email/sms)
    │   ├── Приватность
    │   ├── Безопасность (смена пароля, 2FA)
    │   └── Удалить аккаунт
    └── Помощь и FAQ
```

**1.2.5 Мероприятия (Events Hub)**
```typescript
EventsScreen:
  Фильтры:
    - Все / Предстоящие / Мои регистрации
    - По формату: Бесплатные / Платные / Закрытые (только Elite)
    - По дате: На этой неделе / В этом месяце
  
  Карточка мероприятия:
    - Фото-обложка
    - Название
    - Дата и время
    - Локация (бизнес-партнер)
    - Формат (вечер / мастер-класс / ужин)
    - Количество мест: "Осталось 5 из 20"
    - Кнопка "Зарегистрироваться" / "Вы зарегистрированы"
  
EventDetailScreen (детали мероприятия):
    - Полное описание
    - Программа
    - Спикеры (если есть)
    - Что взять с собой
    - Отзывы участников прошлых событий
    - Галерея фото с прошлых мероприятий
    - Кнопка "Поделиться с подругой"
    - Календарь: "Добавить в Google Calendar / iCal"
```

**1.2.6 Конструктор мероприятий (только для VIP/Elite)**
```typescript
EventBuilderScreen:
  Доступ: 
    - VIP: может предлагать идеи (голосование без веса)
    - Elite: полный доступ + приоритет + вес голоса
  
  Шаги:
    Шаг 1: Тип мероприятия
      - Вечер с вином
      - Мастер-класс
      - Спортивное событие
      - Благотворительность
      - Networking
      - Custom (свой вариант)
    
    Шаг 2: Детали
      - Название
      - Описание
      - Желаемая дата (опционально)
      - Локация (выбор из партнеров)
      - Бюджет на человека
      - Максимум участников
    
    Шаг 3: Программа
      - Добавить пункты программы
      - Прикрепить фото/видео для визуализации
    
    Шаг 4: Публикация
      - Отправить на голосование
      - Видимость: Все / Только VIP+ / Только Elite
  
  После публикации:
    - Мероприятие попадает в раздел "На голосовании"
    - Участницы голосуют (вес голоса зависит от статуса)
    - Топ-3 идеи месяца реализуются организаторами
```

**1.2.7 Бизнесы (Каталог партнеров)**
```typescript
BusinessesScreen:
  Категории:
    - Красота (салон, косметология)
    - Здоровье (стоматология, клиника)
    - Еда (гастромаркет)
    - Дом (текстиль, флористика, оптика)
    - Услуги (юристы)
  
  Карточка бизнеса:
    - Логотип
    - Название
    - Категория
    - Рейтинг (на основе отзывов участниц)
    - Текущие акции (если есть)
    - Кнопка "Подробнее"
  
BusinessDetailScreen:
    - Описание
    - Услуги и цены
    - Фотогалерея
    - Отзывы участниц клуба
    - Контакты и адрес
    - Часы работы
    - Кнопка "Записаться" (deep link в их систему записи)
    - Кнопка "Построить маршрут" (Google Maps / Yandex Maps)
```

---

### МОДУЛЬ 2: BACKEND МИКРОСЕРВИСЫ

#### 2.1 User Service (Сервис пользователей)

**Ответственность:**
- Регистрация, аутентификация, авторизация
- Управление профилями
- JWT токены
- Роли и разрешения

**API Endpoints:**

```python
# Регистрация
POST /api/v1/auth/register
Request:
{
  "phone": "+79991234567",
  "first_name": "Анна",
  "last_name": "Смирнова",
  "email": "anna@example.com",
  "birth_date": "1990-05-15",
  "city": "Москва",
  "referral_code": "MARIA123" // опционально
}
Response:
{
  "user_id": "uuid",
  "access_token": "jwt...",
  "refresh_token": "jwt...",
  "status": "insider" // начальный статус
}

# Вход (отправка SMS-кода)
POST /api/v1/auth/login/send-code
Request:
{
  "phone": "+79991234567"
}
Response:
{
  "message": "SMS sent",
  "expires_in": 300 // секунды
}

# Вход (проверка кода)
POST /api/v1/auth/login/verify-code
Request:
{
  "phone": "+79991234567",
  "code": "1234"
}
Response:
{
  "user_id": "uuid",
  "access_token": "jwt...",
  "refresh_token": "jwt..."
}

# Обновление токена
POST /api/v1/auth/refresh
Request:
{
  "refresh_token": "jwt..."
}
Response:
{
  "access_token": "new_jwt..."
}

# Получение профиля
GET /api/v1/users/me
Headers: Authorization: Bearer {access_token}
Response:
{
  "user_id": "uuid",
  "phone": "+79991234567",
  "first_name": "Анна",
  "last_name": "Смирнова",
  "email": "anna@example.com",
  "avatar_url": "https://...",
  "status": "vip",
  "total_purchases": 42,
  "categories_visited": 5,
  "total_bonuses": 12450,
  "events_attended": 8,
  "referral_code": "ANNA456",
  "referrals_count": 3
}

# Обновление профиля
PATCH /api/v1/users/me
Request:
{
  "first_name": "Анна",
  "avatar": "base64..." // или multipart/form-data
}

# Удаление аккаунта
DELETE /api/v1/users/me
```

**База данных (PostgreSQL):**

```sql
-- Таблица пользователей
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  phone VARCHAR(20) UNIQUE NOT NULL,
  email VARCHAR(255) UNIQUE,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  password_hash VARCHAR(255), -- для будущего
  avatar_url TEXT,
  birth_date DATE,
  city VARCHAR(100),
  status VARCHAR(20) DEFAULT 'insider', -- insider/vip/elite/inner_circle
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  last_login_at TIMESTAMP,
  is_active BOOLEAN DEFAULT TRUE,
  is_verified BOOLEAN DEFAULT FALSE
);

-- Таблица SMS-кодов для входа
CREATE TABLE sms_codes (
  id SERIAL PRIMARY KEY,
  phone VARCHAR(20) NOT NULL,
  code VARCHAR(6) NOT NULL,
  expires_at TIMESTAMP NOT NULL,
  is_used BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Таблица refresh токенов
CREATE TABLE refresh_tokens (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  token TEXT UNIQUE NOT NULL,
  expires_at TIMESTAMP NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Индексы
CREATE INDEX idx_users_phone ON users(phone);
CREATE INDEX idx_users_status ON users(status);
CREATE INDEX idx_sms_codes_phone ON sms_codes(phone, expires_at);
```

---

#### 2.2 Loyalty Service (Сервис лояльности)

**Ответственность:**
- Начисление и списание бонусов
- Расчет статусов
- Кросс-промо между бизнесами
- История транзакций

**API Endpoints:**

```python
# Получение баланса бонусов
GET /api/v1/loyalty/balance
Response:
{
  "total_bonuses": 12450,
  "available_bonuses": 10000, // доступны для списания
  "pending_bonuses": 2450, // в процессе обработки
  "expiring_soon": [
    {
      "amount": 500,
      "expires_at": "2025-12-31"
    }
  ]
}

# История начислений/списаний
GET /api/v1/loyalty/transactions?limit=50&offset=0
Response:
{
  "transactions": [
    {
      "id": "uuid",
      "type": "earned", // earned/spent/expired
      "amount": 500,
      "business_name": "Салон Миндаль",
      "description": "Кешбэк за маникюр",
      "created_at": "2025-11-15T14:30:00"
    },
    ...
  ],
  "total": 150
}

# Получение статуса и прогресса
GET /api/v1/loyalty/status-progress
Response:
{
  "current_status": "vip",
  "next_status": "elite",
  "progress": {
    "total_spent": 45000, // за 12 месяцев
    "total_spent_required": 100000,
    "categories_visited": 4,
    "categories_required": 5,
    "percentage": 68 // общий прогресс
  },
  "benefits": [
    "Приоритетная запись",
    "VIP-зона на мероприятиях",
    "Двойные баллы за новые категории"
  ]
}

# Получение активных купонов
GET /api/v1/loyalty/coupons
Response:
{
  "coupons": [
    {
      "id": "uuid",
      "business_id": "uuid",
      "business_name": "Стим Центр",
      "type": "discount", // discount/bonus/gift
      "value": 1000, // скидка 1000₽
      "description": "Скидка на профессиональную чистку зубов",
      "expires_at": "2025-12-01",
      "conditions": "Только для новых клиентов клиники"
    }
  ]
}

# Активация купона (использование)
POST /api/v1/loyalty/coupons/{coupon_id}/activate
Response:
{
  "activation_code": "ABC123", // код для предъявления в бизнесе
  "valid_until": "2025-11-20T23:59:59"
}
```

**Логика начисления бонусов:**

```python
def calculate_bonuses(purchase_amount: float, user_status: str, 
                     is_new_category: bool, business_id: str) -> float:
    """
    Расчет бонусов за покупку
    """
    base_cashback_rate = {
        'insider': 0.05,  # 5%
        'vip': 0.07,      # 7%
        'elite': 0.10     # 10%
    }
    
    bonuses = purchase_amount * base_cashback_rate[user_status]
    
    # Бонус за новую категорию
    if is_new_category:
        bonuses *= 1.5
    
    # Специальные акции бизнеса (если есть)
    business_multiplier = get_business_multiplier(business_id)
    bonuses *= business_multiplier
    
    return round(bonuses, 2)

def calculate_cross_bonus(from_business_id: str, to_business_id: str,
                         purchase_amount: float) -> float:
    """
    Расчет кросс-бонуса при переходе между бизнесами
    Пример: купила в Лисичкино → получила промо на Миндаль
    """
    if has_active_cross_promo(from_business_id, to_business_id):
        return purchase_amount * 0.10  # 10% кросс-бонус
    return 0

def update_user_status(user_id: str):
    """
    Пересчет статуса пользователя
    Вызывается после каждой транзакции
    """
    # Получаем статистику за последние 12 месяцев
    stats = get_user_stats_12m(user_id)
    
    total_spent = stats['total_spent']
    categories_count = stats['categories_visited']
    
    # Правила перехода
    if total_spent >= 100000 and categories_count >= 5:
        new_status = 'elite'
    elif total_spent >= 30000 and categories_count >= 3:
        new_status = 'vip'
    else:
        new_status = 'insider'
    
    update_user_status_in_db(user_id, new_status)
```

**База данных:**

```sql
-- Таблица транзакций покупок
CREATE TABLE transactions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  business_id UUID REFERENCES businesses(id),
  amount DECIMAL(10,2) NOT NULL,
  bonuses_earned DECIMAL(10,2) DEFAULT 0,
  category VARCHAR(50), -- красота/здоровье/еда и т.д.
  description TEXT,
  transaction_date TIMESTAMP DEFAULT NOW(),
  source VARCHAR(50) DEFAULT 'manual', -- manual/api/qr
  metadata JSONB -- доп. данные
);

-- Таблица бонусного счета
CREATE TABLE bonus_accounts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) UNIQUE,
  total_bonuses DECIMAL(10,2) DEFAULT 0,
  available_bonuses DECIMAL(10,2) DEFAULT 0,
  pending_bonuses DECIMAL(10,2) DEFAULT 0,
  updated_at TIMESTAMP DEFAULT NOW()
);

-- История движения бонусов
CREATE TABLE bonus_transactions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  type VARCHAR(20), -- earned/spent/expired/gift
  amount DECIMAL(10,2) NOT NULL,
  source_transaction_id UUID REFERENCES transactions(id),
  description TEXT,
  expires_at DATE, -- дата сгорания (если применимо)
  created_at TIMESTAMP DEFAULT NOW()
);

-- Купоны и промо
CREATE TABLE coupons (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  business_id UUID REFERENCES businesses(id),
  type VARCHAR(20), -- discount/bonus/gift
  value DECIMAL(10,2),
  description TEXT,
  conditions TEXT,
  code VARCHAR(50) UNIQUE,
  is_activated BOOLEAN DEFAULT FALSE,
  activated_at TIMESTAMP,
  expires_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Индексы
CREATE INDEX idx_transactions_user ON transactions(user_id, transaction_date DESC);
CREATE INDEX idx_transactions_business ON transactions(business_id);
CREATE INDEX idx_bonus_tx_user ON bonus_transactions(user_id, created_at DESC);
CREATE INDEX idx_coupons_user ON coupons(user_id, expires_at);
```

---

#### 2.3 Events Service (Сервис мероприятий)

**Ответственность:**
- Создание и управление мероприятиями
- Регистрация участников
- Голосование за предложения
- Бюджетирование мероприятий
- Конструктор событий

**API Endpoints:**

```python
# Получение списка мероприятий
GET /api/v1/events?status=upcoming&limit=20
Query params:
  - status: upcoming/past/all
  - format: free/paid/closed
  - business_id: фильтр по организатору
Response:
{
  "events": [
    {
      "id": "uuid",
      "title": "Винный вечер с дегустацией",
      "description": "...",
      "format": "paid",
      "price": 2500,
      "date": "2025-12-05T19:00:00",
      "location": {
        "business_id": "uuid",
        "business_name": "Лисичкино",
        "address": "ул. Примерная, 10"
      },
      "max_participants": 20,
      "registered_count": 15,
      "status_required": "vip", // минимальный статус для участия
      "cover_image_url": "https://...",
      "organizer": {
        "type": "business", // business/user
        "name": "Рестолавка Лисичкино"
      }
    }
  ]
}

# Детали мероприятия
GET /api/v1/events/{event_id}
Response:
{
  "id": "uuid",
  "title": "...",
  "full_description": "...",
  "program": [
    {
      "time": "19:00",
      "activity": "Приветственный коктейль"
    },
    {
      "time": "19:30",
      "activity": "Дегустация вин с сомелье"
    }
  ],
  "what_to_bring": ["Хорошее настроение"],
  "speakers": [
    {
      "name": "Мария Петрова",
      "title": "Сомелье",
      "photo_url": "https://..."
    }
  ],
  "gallery": ["url1", "url2"],
  "reviews": [
    {
      "user_name": "Анна С.",
      "rating": 5,
      "text": "Было потрясающе!",
      "date": "2025-10-15"
    }
  ],
  "is_registered": false,
  "can_register": true // на основе статуса пользователя
}

# Регистрация на мероприятие
POST /api/v1/events/{event_id}/register
Request:
{
  "plus_one": false, // +1 гость (если разрешено)
  "dietary_restrictions": "вегетарианство" // опционально
}
Response:
{
  "registration_id": "uuid",
  "status": "confirmed", // confirmed/waitlist
  "ticket_url": "https://..." // QR-билет
}

# Отмена регистрации
DELETE /api/v1/events/{event_id}/register

# Конструктор мероприятий (создание предложения)
POST /api/v1/events/proposals
Request:
{
  "title": "Йога на крыше",
  "description": "...",
  "type": "wellness",
  "preferred_date": "2025-12-10",
  "location_preference": "Лисичкино", // или business_id
  "budget_per_person": 1500,
  "max_participants": 15,
  "program": [...]
}
Response:
{
  "proposal_id": "uuid",
  "status": "voting", // voting/approved/rejected
  "voting_ends_at": "2025-11-30T23:59:59"
}

# Голосование за предложение
POST /api/v1/events/proposals/{proposal_id}/vote
Request:
{
  "vote": "yes" // yes/no
}
Response:
{
  "total_votes": 42,
  "weighted_score": 156.5, // с учетом веса голосов
  "user_vote_weight": 3.0 // вес голоса текущего пользователя
}

# Список предложений на голосовании
GET /api/v1/events/proposals?status=voting
```

**Логика голосования с весом:**

```python
def get_vote_weight(user_status: str) -> float:
    """
    Вес голоса в зависимости от статуса
    """
    weights = {
        'insider': 1.0,
        'vip': 2.0,
        'elite': 3.0,
        'inner_circle': 5.0
    }
    return weights.get(user_status, 1.0)

def calculate_proposal_score(proposal_id: str) -> dict:
    """
    Расчет взвешенного рейтинга предложения
    """
    votes = get_proposal_votes(proposal_id)
    
    total_yes = 0
    total_no = 0
    weighted_yes = 0
    weighted_no = 0
    
    for vote in votes:
        weight = get_vote_weight(vote.user_status)
        if vote.vote == 'yes':
            total_yes += 1
            weighted_yes += weight
        else:
            total_no += 1
            weighted_no += weight
    
    return {
        'total_votes': total_yes + total_no,
        'yes_votes': total_yes,
        'no_votes': total_no,
        'weighted_score': weighted_yes - weighted_no,
        'approval_rate': weighted_yes / (weighted_yes + weighted_no) if (weighted_yes + weighted_no) > 0 else 0
    }
```

**База данных:**

```sql
-- Таблица мероприятий
CREATE TABLE events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title VARCHAR(255) NOT NULL,
  description TEXT,
  full_description TEXT,
  type VARCHAR(50), -- gala/masterclass/wellness/networking
  format VARCHAR(20), -- free/paid/closed
  price DECIMAL(10,2) DEFAULT 0,
  date TIMESTAMP NOT NULL,
  location_business_id UUID REFERENCES businesses(id),
  location_address TEXT,
  max_participants INTEGER,
  min_status VARCHAR(20) DEFAULT 'insider',
  cover_image_url TEXT,
  program JSONB, -- массив объектов с программой
  speakers JSONB, -- массив спикеров
  organizer_type VARCHAR(20), -- business/platform/user
  organizer_id UUID,
  created_at TIMESTAMP DEFAULT NOW(),
  status VARCHAR(20) DEFAULT 'upcoming' -- upcoming/past/cancelled
);

-- Регистрации на мероприятия
CREATE TABLE event_registrations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  event_id UUID REFERENCES events(id),
  user_id UUID REFERENCES users(id),
  status VARCHAR(20) DEFAULT 'confirmed', -- confirmed/waitlist/cancelled
  plus_one BOOLEAN DEFAULT FALSE,
  dietary_restrictions TEXT,
  registered_at TIMESTAMP DEFAULT NOW(),
  ticket_code VARCHAR(50) UNIQUE,
  UNIQUE(event_id, user_id)
);

-- Предложения мероприятий от участниц
CREATE TABLE event_proposals (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  title VARCHAR(255) NOT NULL,
  description TEXT,
  type VARCHAR(50),
  preferred_date DATE,
  location_preference TEXT,
  budget_per_person DECIMAL(10,2),
  max_participants INTEGER,
  program JSONB,
  status VARCHAR(20) DEFAULT 'voting', -- voting/approved/rejected/realized
  voting_ends_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Голоса за предложения
CREATE TABLE proposal_votes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  proposal_id UUID REFERENCES event_proposals(id),
  user_id UUID REFERENCES users(id),
  vote VARCHAR(3) NOT NULL, -- yes/no
  vote_weight DECIMAL(3,1), -- вес голоса на момент голосования
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(proposal_id, user_id)
);

-- Бюджет мероприятий (формируется из покупок)
CREATE TABLE events_budget (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  total_budget DECIMAL(12,2) DEFAULT 0,
  allocated_budget DECIMAL(12,2) DEFAULT 0, -- распределенный
  available_budget DECIMAL(12,2) DEFAULT 0, -- доступный
  updated_at TIMESTAMP DEFAULT NOW()
);

-- История вкладов в бюджет
CREATE TABLE budget_contributions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  transaction_id UUID REFERENCES transactions(id),
  amount DECIMAL(10,2), -- % от покупки
  contributed_at TIMESTAMP DEFAULT NOW()
);

-- Индексы
CREATE INDEX idx_events_date ON events(date DESC);
CREATE INDEX idx_event_reg_event ON event_registrations(event_id);
CREATE INDEX idx_proposals_status ON event_proposals(status, voting_ends_at);
```

---

#### 2.4 Analytics Service (Сервис аналитики)

**Ответственность:**
- Сбор и обработка метрик
- Когортный анализ
- RFM-сегментация
- Дашборды для бизнесов
- Прогнозирование (churn prediction)

**API Endpoints для владельцев бизнеса:**

```python
# Общая статистика бизнеса
GET /api/v1/analytics/business/{business_id}/overview
Response:
{
  "period": {
    "from": "2025-10-01",
    "to": "2025-10-31"
  },
  "total_revenue": 450000,
  "total_transactions": 320,
  "new_customers": 45,
  "returning_customers": 275,
  "avg_check": 1406.25,
  "revenue_from_ecosystem": 85000, // доход от кросс-клиентов
  "ecosystem_share": 0.189 // 18.9% выручки от экосистемы
}

# Откуда приходят клиенты
GET /api/v1/analytics/business/{business_id}/customer-sources
Response:
{
  "sources": [
    {
      "source_business_id": "uuid",
      "source_business_name": "Лисичкино",
      "customers_count": 23,
      "revenue": 32500,
      "conversion_rate": 0.15 // 15% от клиентов Лисичкино пришли
    },
    {
      "source": "direct", // прямой визит
      "customers_count": 120,
      "revenue": 168000
    }
  ]
}

# Куда уходят клиенты
GET /api/v1/analytics/business/{business_id}/customer-destinations
Response:
{
  "destinations": [
    {
      "destination_business_id": "uuid",
      "destination_business_name": "Стим Центр",
      "customers_count": 18,
      "conversion_rate": 0.056 // 5.6% клиентов ушли в Стим
    }
  ]
}

# Win-Win цепочки (успешные связки)
GET /api/v1/analytics/business/{business_id}/win-win-chains
Response:
{
  "chains": [
    {
      "pattern": "Миндаль → Лисичкино → Стим Центр",
      "frequency": 12, // 12 клиентов прошли этот путь
      "avg_ltv": 25000, // средний LTV таких клиентов
      "recommendation": "Создать пакет: маникюр + ужин + чистка зубов"
    }
  ]
}

# RFM-сегментация клиентов
GET /api/v1/analytics/business/{business_id}/rfm-segments
Response:
{
  "segments": [
    {
      "segment": "Champions", // лучшие клиенты
      "count": 45,
      "avg_revenue": 12000,
      "characteristics": {
        "recency": "recent",
        "frequency": "high",
        "monetary": "high"
      }
    },
    {
      "segment": "At Risk",
      "count": 23,
      "characteristics": {
        "recency": "long_ago",
        "frequency": "high",
        "monetary": "high"
      },
      "action": "Отправить персональное возвратное предложение"
    }
  ]
}

# Прогноз оттока (churn prediction)
GET /api/v1/analytics/business/{business_id}/churn-risk
Response:
{
  "high_risk_customers": [
    {
      "user_id": "uuid",
      "user_name": "Анна С.",
      "last_visit": "2025-08-15",
      "days_since_last_visit": 90,
      "churn_probability": 0.78, // 78% вероятность оттока
      "recommended_action": "Отправить скидку 15% на любую услугу"
    }
  ],
  "total_at_risk": 12
}

# Экспорт данных
GET /api/v1/analytics/business/{business_id}/export?format=csv
Response: CSV файл со всеми транзакциями
```

**Аналитика на ClickHouse:**

```sql
-- Материализованное представление для быстрой аналитики
CREATE MATERIALIZED VIEW mv_business_daily_stats
ENGINE = SummingMergeTree()
ORDER BY (business_id, date)
AS SELECT
    business_id,
    toDate(transaction_date) as date,
    count() as transactions_count,
    sum(amount) as total_revenue,
    uniq(user_id) as unique_customers,
    avg(amount) as avg_check
FROM transactions
GROUP BY business_id, date;

-- RFM-сегментация
WITH rfm_scores AS (
    SELECT
        user_id,
        business_id,
        dateDiff('day', max(transaction_date), today()) as recency,
        count() as frequency,
        sum(amount) as monetary
    FROM transactions
    WHERE transaction_date >= today() - INTERVAL 365 DAY
    GROUP BY user_id, business_id
),
rfm_quantiles AS (
    SELECT
        business_id,
        quantile(0.25)(recency) as r_25,
        quantile(0.50)(recency) as r_50,
        quantile(0.75)(recency) as r_75,
        quantile(0.25)(frequency) as f_25,
        quantile(0.50)(frequency) as f_50,
        quantile(0.75)(frequency) as f_75,
        quantile(0.25)(monetary) as m_25,
        quantile(0.50)(monetary) as m_50,
        quantile(0.75)(monetary) as m_75
    FROM rfm_scores
    GROUP BY business_id
)
SELECT
    s.user_id,
    s.business_id,
    CASE
        WHEN s.recency <= q.r_25 THEN 4
        WHEN s.recency <= q.r_50 THEN 3
        WHEN s.recency <= q.r_75 THEN 2
        ELSE 1
    END as R,
    CASE
        WHEN s.frequency >= q.f_75 THEN 4
        WHEN s.frequency >= q.f_50 THEN 3
        WHEN s.frequency >= q.f_25 THEN 2
        ELSE 1
    END as F,
    CASE
        WHEN s.monetary >= q.m_75 THEN 4
        WHEN s.monetary >= q.m_50 THEN 3
        WHEN s.monetary >= q.m_25 THEN 2
        ELSE 1
    END as M
FROM rfm_scores s
JOIN rfm_quantiles q ON s.business_id = q.business_id;
```

---

### МОДУЛЬ 3: ИНТЕГРАЦИОННЫЙ СЛОЙ (Integration Service)

**Ответственность:**
- Подключение к CRM/ERP бизнесов
- Синхронизация транзакций
- Универсальные коннекторы
- Обработка webhook'ов

#### 3.1 Поддерживаемые системы

**1С (Skinerica, Лисичкино)**
```python
class Connector1C:
    """
    Коннектор для 1С через REST API
    """
    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url
        self.auth = (username, password)
    
    def fetch_transactions(self, date_from: datetime, date_to: datetime):
        """
        Получение транзакций из 1С
        """
        url = f"{self.base_url}/api/transactions"
        params = {
            'dateFrom': date_from.isoformat(),
            'dateTo': date_to.isoformat()
        }
        response = requests.get(url, params=params, auth=self.auth)
        return self.parse_transactions(response.json())
    
    def parse_transactions(self, raw_data):
        """
        Парсинг ответа 1С в стандартный формат
        """
        transactions = []
        for item in raw_data['Transactions']:
            transactions.append({
                'external_id': item['ID'],
                'amount': item['Total'],
                'date': item['Date'],
                'customer_phone': item.get('CustomerPhone'),
                'items': item.get('Items', [])
            })
        return transactions
```

**YCLIENTS (Миндаль)**
```python
class ConnectorYCLIENTS:
    """
    Интеграция с YCLIENTS через официальный API
    """
    API_URL = "https://api.yclients.com/api/v1"
    
    def __init__(self, token: str, company_id: str):
        self.token = token
        self.company_id = company_id
    
    def get_records(self, date_from: datetime, date_to: datetime):
        """
        Получение записей (appointments)
        """
        url = f"{self.API_URL}/records/{self.company_id}"
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        params = {
            'start_date': date_from.strftime('%Y-%m-%d'),
            'end_date': date_to.strftime('%Y-%m-%d')
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json()
    
    def sync_customer(self, phone: str, user_data: dict):
        """
        Синхронизация клиента из Свой Круг в YCLIENTS
        """
        url = f"{self.API_URL}/clients/{self.company_id}"
        # Реализация создания/обновления клиента
        pass
```

**AMO CRM (Стим Центр)**
```python
class ConnectorAMOCRM:
    """
    Интеграция с AMO CRM
    """
    def __init__(self, subdomain: str, access_token: str):
        self.base_url = f"https://{subdomain}.amocrm.ru/api/v4"
        self.access_token = access_token
    
    def get_deals(self, date_from: datetime):
        """
        Получение сделок (закрытых продаж)
        """
        url = f"{self.base_url}/leads"
        headers = {'Authorization': f'Bearer {self.access_token}'}
        params = {
            'filter[closed_at][from]': int(date_from.timestamp()),
            'filter[statuses][]': [142, 143]  # ID статусов "Успешно реализовано"
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json()
```

**МИС Renovatio (Миллениум)**
```python
class ConnectorRenovatio:
    """
    Специфичная интеграция с медицинской информационной системой
    
    Особенности:
    - Врачебная тайна: передаем только факт оказания услуги
    - Не передаем название услуги и диагнозы
    """
    def fetch_anonymized_transactions(self, date_from: datetime):
        """
        Получение обезличенных транзакций
        """
        # Возвращаем только: user_phone_hash, amount, category, date
        # БЕЗ: названия услуги, врача, диагноза
        pass
```

**Универсальный CSV-загрузчик**
```python
class ConnectorCSV:
    """
    Для бизнесов без API - ручная загрузка CSV
    """
    REQUIRED_COLUMNS = ['date', 'customer_phone', 'amount']
    
    def parse_csv(self, file_path: str):
        """
        Парсинг CSV файла
        Формат:
        date,customer_phone,amount,description
        2025-11-15,+79991234567,3000,Маникюр
        """
        df = pd.read_csv(file_path)
        self.validate_columns(df)
        return self.transform_to_transactions(df)
    
    def validate_columns(self, df):
        missing = set(self.REQUIRED_COLUMNS) - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns: {missing}")
```

#### 3.2 Процесс синхронизации

```python
# Периодическая задача (каждые 15 минут)
@celery.task
def sync_all_businesses():
    """
    Синхронизация транзакций со всех бизнесов
    """
    businesses = get_all_businesses_with_integrations()
    
    for business in businesses:
        try:
            connector = get_connector(business.integration_type)
            transactions = connector.fetch_transactions(
                date_from=datetime.now() - timedelta(hours=1),
                date_to=datetime.now()
            )
            
            for tx in transactions:
                process_transaction(business.id, tx)
            
        except Exception as e:
            logger.error(f"Sync failed for {business.name}: {e}")
            send_alert_to_admin(business, e)

def process_transaction(business_id: str, tx_data: dict):
    """
    Обработка одной транзакции
    """
    # 1. Найти пользователя по телефону
    user = find_user_by_phone(tx_data['customer_phone'])
    if not user:
        return  # Клиент не в экосистеме
    
    # 2. Сохранить транзакцию
    transaction = save_transaction(
        user_id=user.id,
        business_id=business_id,
        amount=tx_data['amount'],
        date=tx_data['date']
    )
    
    # 3. Начислить бонусы
    bonuses = calculate_bonuses(
        purchase_amount=tx_data['amount'],
        user_status=user.status,
        is_new_category=check_if_new_category(user.id, business_id),
        business_id=business_id
    )
    accrue_bonuses(user.id, bonuses, transaction.id)
    
    # 4. Проверить кросс-промо
    check_and_apply_cross_promos(user.id, business_id)
    
    # 5. Обновить статус пользователя
    update_user_status(user.id)
    
    # 6. Отправить уведомление
    send_transaction_notification(user.id, transaction)
```

---

## СИСТЕМА ГЕЙМИФИКАЦИИ И СТАТУСОВ

### Уровни статусов

```yaml
Insider (Базовый):
  Условия:
    - Регистрация в приложении
    - Минимум 1 покупка в экосистеме
  Привилегии:
    - Базовый кешбэк 5%
    - Доступ к открытым мероприятиям
    - QR-карта участницы
  Цвет: Жемчужно-белый
  Иконка: Круг

VIP:
  Условия:
    - ≥30,000₽ за последние 12 месяцев
    - ≥3 разные категории бизнесов
  Привилегии:
    - Кешбэк 7%
    - Приоритетная запись
    - VIP-зона на мероприятиях
    - Двойные баллы за новые категории
    - Доступ к конструктору мероприятий (без веса голоса)
  Цвет: Tiffany (#81D8D0)
  Иконка: Звезда

Elite:
  Условия:
    - ≥100,000₽ за последние 12 месяцев
    - ≥5 категорий бизнесов
    ИЛИ
    - Топ-1% по тратам
  Привилегии:
    - Кешбэк 10%
    - Закрытые встречи с собственницами
    - Private-ужины и выездные мероприятия
    - Возможность влиять на линейки товаров/услуг
    - Вес голоса в конструкторе: 3.0
    - Персональный консьерж
    - Спецподарки ко дню рождения
  Цвет: Золотой
  Иконка: Корона

Inner Circle (Пригласительный):
  Условия:
    - Только по приглашению собственниц
    - Или ≥200,000₽ + все категории
  Привилегии:
    - Все привилегии Elite
    - Статус "амбассадор"
    - Участие в стратегических сессиях
    - Личное представление в соцсетях клуба
    - Вес голоса: 5.0
    - Право вето на предложения мероприятий
  Цвет: Платиновый
  Иконка: Бриллиант
```

### Визуализация прогресса

```typescript
// Компонент кольца прогресса
<GamificationRing
  currentStatus="vip"
  nextStatus="elite"
  progress={{
    totalSpent: 45000,
    totalSpentRequired: 100000,
    categoriesVisited: 4,
    categoriesRequired: 5,
    overallPercentage: 68
  }}
/>

// Рендер
┌─────────────────────────────────┐
│     ╭───────────────────╮        │
│    ╱  68% до Elite     ╲       │
│   │                     │      │
│   │    [Tiffany Ring]   │      │
│   │         VIP         │      │
│   │                     │      │
│    ╲                   ╱       │
│     ╰───────────────────╯        │
│                                 │
│  💰 Потрачено: 45,000₽ / 100K   │
│  📊 Категории: 4 / 5            │
│  🎯 Осталось: 1 категория       │
└─────────────────────────────────┘
```

### Система бейджей

```yaml
Бейджи за категории:
  - 💄 Красота (салон красоты)
  - ✨ Косметология
  - 🦷 Стоматология
  - 🏥 Медицина
  - 🍽️ Гастрономия
  - 🌺 Флористика
  - 👓 Оптика
  - 🏠 Дом (текстиль)
  - ⚖️ Юридические услуги

Специальные бейджи:
  - 🌟 Первопроходец (первая регистрация)
  - 👥 Друг клуба (пригласила ≥3 подруг)
  - 🎉 Тусовщица (посетила ≥10 мероприятий)
  - 💎 Коллекционер (собрала все 9 категорий)
  - 📈 Инвестор (потратила ≥250,000₽)
```

---

## СИСТЕМА МЕРОПРИЯТИЙ

### Иерархия мероприятий

```
┌──────────────────────────────────────────────────────┐
│              ИЕРАРХИЯ МЕРОПРИЯТИЙ                    │
├──────────────────────────────────────────────────────┤
│ Уровень 1: Открытые (Insider+)                       │
│  - Гастровечера в Лисичкино                          │
│  - Мастер-классы по макияжу                          │
│  - Дегустации                                        │
│  Формат: Бесплатно / символическая оплата 500₽       │
│  Частота: 2 раза в месяц                             │
├──────────────────────────────────────────────────────┤
│ Уровень 2: VIP-события (VIP+)                        │
│  - Закрытые ужины с собственницами                   │
│  - Wellness-дни (йога + косметология)                │
│  - Винные вечера с сомелье                           │
│  Формат: 1,500-3,000₽ / частично из бюджета          │
│  Частота: 1 раз в месяц                              │
├──────────────────────────────────────────────────────┤
│ Уровень 3: Elite-клуб (Elite+)                       │
│  - Выездные спа-туры                                 │
│  - Встречи с экспертами (психологи, коучи)           │
│  - Закрытые показы / private shopping                │
│  Формат: 5,000-15,000₽ / софинансирование            │
│  Частота: 1 раз в квартал                            │
├──────────────────────────────────────────────────────┤
│ Уровень 4: Inner Circle (только по приглашению)      │
│  - Стратегические сессии с владельцами               │
│  - Бизнес-ретриты                                    │
│  - Поездки на производства партнеров                 │
│  Формат: Бесплатно для участниц                      │
│  Частота: 2-3 раза в год                             │
└──────────────────────────────────────────────────────┘
```

### Бюджетирование мероприятий

**Формирование бюджета:**
```python
def calculate_events_budget_contribution(transaction_amount: float) -> float:
    """
    От каждой покупки 2% идет в общий бюджет мероприятий
    """
    return transaction_amount * 0.02

# Пример:
# Клиентка купила в салоне на 5000₽
# → 5000₽ × 2% = 100₽ в бюджет мероприятий
# 
# Общий месячный бюджет при 500 клиентах:
# 500 клиентов × 2 покупки × 3500₽ средний чек × 2% = 70,000₽/мес
```

**Распределение бюджета:**
```yaml
Ежемесячный бюджет: 70,000₽

Распределение:
  - Открытые мероприятия: 30% (21,000₽)
    → Кейтеринг, зал, материалы для мастер-классов
  
  - VIP-события: 40% (28,000₽)
    → Сомелье, площадки, подарки участникам
  
  - Elite-клуб: 20% (14,000₽)
    → Софинансирование выездных мероприятий
  
  - Резерв / спецпроекты: 10% (7,000₽)
    → Благотворительность, эксперименты
```

**Прозрачность для участниц:**
```typescript
// Экран "Наш общий бюджет"
BudgetScreen:
  <Card>
    <Title>Бюджет мероприятий ноября</Title>
    <Amount>68,450₽</Amount>
    <Progress value={68450} max={70000} />
    
    <Contributions>
      Ваш вклад: 340₽ (от 17,000₽ покупок)
      Общий вклад участниц: 68,450₽
    </Contributions>
    
    <Allocation>
      Распределено:
      - Винный вечер 5 декабря: 15,000₽
      - Йога-утро 12 декабря: 8,000₽
      - Резерв: 45,450₽
    </Allocation>
  </Card>
```

### Конструктор мероприятий (UI)

```typescript
// Пошаговый конструктор
<EventBuilderWizard>
  <Step1_Type>
    <Options>
      {types.map(type => (
        <TypeCard
          icon={type.icon}
          title={type.title}
          description={type.description}
          examples={type.examples}
        />
      ))}
    </Options>
  </Step1_Type>
  
  <Step2_Details>
    <Input label="Название" />
    <TextArea label="Описание" maxLength={500} />
    <DatePicker label="Желаемая дата" />
    <Select
      label="Локация"
      options={partnerBusinesses}
    />
    <NumberInput label="Бюджет на человека" />
    <NumberInput label="Максимум участников" />
  </Step2_Details>
  
  <Step3_Program>
    <ProgramBuilder>
      {/* Drag-n-drop редактор программы */}
      <TimeSlot time="19:00">
        <Activity>Приветственный коктейль</Activity>
      </TimeSlot>
      <TimeSlot time="19:30">
        <Activity>Основная часть</Activity>
      </TimeSlot>
    </ProgramBuilder>
  </Step3_Program>
  
  <Step4_Preview>
    <EventPreview data={formData} />
    <Button onClick={submitProposal}>
      Отправить на голосование
    </Button>
  </Step4_Preview>
</EventBuilderWizard>
```

---

## АНАЛИТИКА И МЕТРИКИ

### KPI проекта

**Северная звезда:**
```
NSM (North Star Metric):
% клиентов, совершивших ≥2 покупки в разных категориях за 60 дней

Цель: 25% к концу 6-го месяца
```

**Операционные метрики:**

```yaml
Клиентские метрики:
  - CAC (Customer Acquisition Cost): стоимость привлечения
  - LTV (Lifetime Value): пожизненная ценность
  - Retention Rate: удержание по когортам
  - Churn Rate: отток клиентов
  - NPS (Net Promoter Score): готовность рекомендовать

Метрики вовлеченности:
  - DAU / MAU (Daily / Monthly Active Users)
  - Session Duration: время в приложении
  - Feature Adoption: использование функций
  - Event Attendance Rate: посещаемость мероприятий

Метрики экосистемы:
  - Cross-Purchase Rate: % кросс-покупок
  - Avg Categories per User: среднее число категорий
  - Time to Second Purchase: время до 2-й покупки в другой категории
  - Ecosystem Revenue Share: доля выручки от экосистемы

Метрики бизнесов:
  - Partner Satisfaction Score: удовлетворенность партнеров
  - Revenue from Ecosystem: доход бизнесов от экосистемы
  - New Customers via Ecosystem: новые клиенты через клуб
```

### Дашборды

**Дашборд для собственницы бизнеса:**

```
┌────────────────────────────────────────────────────┐
│  Салон Миндаль - Октябрь 2025                      │
├────────────────────────────────────────────────────┤
│  📊 Общая статистика                               │
│  ────────────────────────────────────────────────  │
│  Выручка: 450,000₽  ┃  +12% к сентябрю           │
│  Из них от клуба: 85,000₽ (18.9%)                 │
│  Новые клиенты: 45  ┃  Возвраты: 275              │
│  Средний чек: 1,406₽                               │
│                                                    │
│  🔄 Откуда приходят                                │
│  ────────────────────────────────────────────────  │
│  1. Лисичкино: 23 клиента → 32,500₽               │
│  2. Skinerica: 12 клиентов → 18,000₽              │
│  3. Прямые: 120 клиентов → 168,000₽               │
│                                                    │
│  🎯 Куда уходят                                    │
│  ────────────────────────────────────────────────  │
│  1. Стим Центр: 18 клиентов (конверсия 5.6%)      │
│  2. Skinerica: 15 клиентов (4.7%)                  │
│                                                    │
│  💡 Win-Win рекомендации                           │
│  ────────────────────────────────────────────────  │
│  🔥 Создать пакет:                                 │
│     Маникюр (Миндаль) + Ужин (Лисичкино)          │
│     → 12 клиентов прошли этот путь                │
│     → Средний LTV таких клиентов: 25,000₽          │
│                                                    │
│  ⚠️ Риск оттока                                    │
│  ────────────────────────────────────────────────  │
│  12 клиентов в зоне риска (не были 90+ дней)      │
│  [Отправить возвратное предложение]                │
└────────────────────────────────────────────────────┘
```

**Дашборд для администратора экосистемы:**

```
┌────────────────────────────────────────────────────┐
│  Свой Круг - Ноябрь 2025                           │
├────────────────────────────────────────────────────┤
│  Участницы: 487 активных                           │
│  ├─ Insider: 320 (65.7%)                           │
│  ├─ VIP: 142 (29.2%)                               │
│  └─ Elite: 25 (5.1%)                               │
│                                                    │
│  NSM: 28.3% (↑ от 23.1% в октябре)                │
│  Цель: 25% ✅                                      │
│                                                    │
│  Экосистемный доход: 1,245,000₽                    │
│  Комиссия (3%): 37,350₽                            │
│                                                    │
│  Топ-5 кросс-связок:                               │
│  1. Лисичкино → Миндаль: 45 переходов             │
│  2. Миндаль → Skinerica: 38 переходов             │
│  3. Стим → Миллениум: 28 переходов                │
│                                                    │
│  Мероприятия:                                      │
│  - Предстоящие: 3                                  │
│  - Зарегистрировано: 87 участниц                   │
│  - Бюджет месяца: 68,450₽ / 70,000₽               │
└────────────────────────────────────────────────────┘
```

---

## БЕЗОПАСНОСТЬ И COMPLIANCE

### Требования 152-ФЗ

```yaml
Персональные данные:
  Хранение:
    - Сервер: Yandex Cloud (РФ, ЦОД в Москве)
    - Резервные копии: 2 ЦОД в разных регионах РФ
  
  Шифрование:
    - Транспорт: TLS 1.3
    - Хранилище: AES-256-GCM
    - Ключи: Хранятся отдельно (Yandex KMS)
  
  Доступ:
    - Только авторизованный персонал
    - Двухфакторная аутентификация
    - Логирование всех операций с ПДн
  
  Согласия:
    - Явное согласие при регистрации
    - Возможность отзыва согласия
    - Право на удаление данных (GDPR-like)
```

### Врачебная тайна (для медицинских бизнесов)

```yaml
Специальные требования для Skinerica и Миллениум:

Что НЕ передается в экосистему:
  ❌ Названия процедур/услуг
  ❌ Диагнозы
  ❌ Медицинские записи
  ❌ Имена врачей
  ❌ Результаты анализов

Что передается:
  ✅ Факт визита (дата)
  ✅ Сумма оплаты
  ✅ Категория (обезличенная): "медицинская услуга"
  ✅ ID клиента (хешированный)

Реализация:
  # Псевдонимизация для медицинских данных
  class MedicalDataAnonymizer:
      def anonymize_transaction(self, transaction):
          return {
              'user_id': hash_user_id(transaction.user_id),
              'amount': transaction.amount,
              'category': 'medical_service',  # Общая категория
              'date': transaction.date
              # Без деталей услуги!
          }
```

### RBAC (Role-Based Access Control)

```python
# Роли и разрешения
ROLES = {
    'client_insider': {
        'permissions': [
            'view_own_profile',
            'view_own_transactions',
            'register_for_open_events',
            'use_qr_wallet'
        ]
    },
    'client_vip': {
        'inherits': 'client_insider',
        'permissions': [
            'create_event_proposals',
            'vote_on_proposals',
            'register_for_vip_events'
        ]
    },
    'client_elite': {
        'inherits': 'client_vip',
        'permissions': [
            'weighted_voting',
            'register_for_elite_events',
            'access_concierge'
        ]
    },
    'business_manager': {
        'permissions': [
            'view_own_business_analytics',
            'scan_qr_codes',
            'manual_transaction_entry',
            'view_customer_list'  # Только своих клиентов
        ]
    },
    'business_owner': {
        'inherits': 'business_manager',
        'permissions': [
            'configure_integrations',
            'create_promotions',
            'export_analytics',
            'view_cross_analytics'  # Кросс-аналитика
        ]
    },
    'platform_admin': {
        'permissions': [
            '*'  # Все разрешения
        ]
    }
}

# Middleware для проверки разрешений
@app.middleware("http")
async def check_permissions(request: Request, call_next):
    user = get_current_user(request)
    endpoint = request.url.path
    
    required_permission = ENDPOINT_PERMISSIONS.get(endpoint)
    if required_permission:
        if not user.has_permission(required_permission):
            raise PermissionDenied()
    
    response = await call_next(request)
    return response
```

---

## ДОРОЖНАЯ КАРТА РАЗРАБОТКИ

### Фаза 0: Подготовка (2 недели)

```yaml
Неделя 1-2:
  Задачи:
    - Финализация требований с партнерами
    - Сбор доступов к API партнеров
    - Настройка инфраструктуры (Yandex Cloud)
    - Создание репозиториев (GitHub)
    - Настройка CI/CD пайплайнов
  
  Deliverables:
    - Техническое задание (утверждено)
    - Настроенная инфраструктура
    - Dev/Staging окружения
```

### Фаза 1: MVP (10-12 недель)

```yaml
Спринт 1-2 (4 недели): Базовый функционал
  Backend:
    - User Service (регистрация, аутентификация)
    - Loyalty Service (бонусы, транзакции)
    - PostgreSQL схема
  
  Frontend:
    - Экраны onboarding
    - Регистрация/вход
    - QR-кошелек
    - Профиль пользователя
  
  Deliverable:
    - Можно зарегистрироваться и получить QR-карту

Спринт 3-4 (4 недели): Интеграции
  Backend:
    - Integration Service (коннекторы)
    - Интеграция с 1С (Лисичкино)
    - Интеграция с YCLIENTS (Миндаль)
    - Начисление бонусов за покупки
  
  Frontend:
    - История транзакций
    - Баланс бонусов
    - Каталог бизнесов
  
  Deliverable:
    - Покупка в Лисичкино → автоматически начисляются бонусы

Спринт 5-6 (4 недели): Геймификация + Мероприятия
  Backend:
    - Расчет статусов
    - Events Service (базовый)
    - Регистрация на мероприятия
  
  Frontend:
    - Кольцо прогресса
    - Экран мероприятий
    - Регистрация на события
  
  Deliverable:
    - Полноценный MVP готов к тестированию
```

### Фаза 2: Пилотный запуск (4 недели)

```yaml
Неделя 1-2: Закрытое бета-тестирование
  - Приглашение 50 участниц (по 10 от каждого бизнеса)
  - Сбор обратной связи
  - Исправление критических багов
  - Оптимизация UX

Неделя 3-4: Открытый пилот
  - Запуск для всех клиентов 5 бизнесов
  - Первое совместное мероприятие
  - Мониторинг метрик
  - Корректировка механик

Цель фазы:
  - Зарегистрировать 200 участниц
  - Достичь 15% NSM
  - Получить NPS 60+
```

### Фаза 3: Масштабирование (3-6 месяцев)

```yaml
Месяц 1-2: Расширение функционала
  - Конструктор мероприятий
  - Реферальная программа
  - AI-рекомендации (базовые)
  - Push-уведомления

Месяц 3-4: Подключение новых партнеров
  - Интеграции с оставшимися 4 бизнесами
  - Масштабирование до 10 партнеров
  - Запуск Premium-подписки

Месяц 5-6: Оптимизация и монетизация
  - Внедрение revenue share модели (2%)
  - Углубленная аналитика
  - Автоматизация маркетинга
  - Подготовка к расширению в другие города

Цель фазы:
  - 500 активных участниц
  - 25% NSM
  - 10 подключенных бизнесов
  - Break-even по экономике
```

---

## РИСКИ И МИТИГАЦИЯ

### Критические риски

```yaml
Риск 1: Низкая интеграция партнеров
  Вероятность: Средняя
  Влияние: Высокое
  Митигация:
    - Fallback: Ручной ввод транзакций через простой интерфейс
    - CSV-загрузчик для бизнесов без API
    - Поэтапное подключение (1-2 бизнеса в месяц)
  
Риск 2: Низкая вовлеченность клиентов
  Вероятность: Средняя
  Влияние: Критическое
  Митигация:
    - Активные мероприятия с первого месяца
    - Персональные онбординг-звонки первым 100 участницам
    - Геймификация с быстрыми наградами
    - Конкурсы и челленджи
  
Риск 3: Юридические проблемы (врачебная тайна, ПДн)
  Вероятность: Низкая
  Влияние: Критическое
  Митигация:
    - Консультация с юристом до запуска
    - Анонимизация медицинских данных
    - Согласия на обработку ПДн
    - Регулярные аудиты безопасности
  
Риск 4: Технические сбои
  Вероятность: Средняя
  Влияние: Среднее
  Митигация:
    - Мониторинг 24/7 (Sentry + Uptimerobot)
    - Auto-scaling для пиков нагрузки
    - Резервные копии БД (каждые 6 часов)
    - Offline-режим в приложении
  
Риск 5: Отток партнеров
  Вероятность: Низкая
  Влияние: Высокое
  Митигация:
    - Прозрачная аналитика ROI для партнеров
    - Регулярные встречи с собственницами
    - Гибкие условия выхода (без штрафов)
    - Фокус на win-win результатах
```

---

## ЭКОНОМИЧЕСКАЯ МОДЕЛЬ

### Unit-экономика (прогноз 6 месяцев)

```
Клиентская база через 6 месяцев: 500 участниц

Среднее поведение клиента:
- Покупок в месяц: 2
- Средний чек: 3,500₽
- Кросс-покупки: 40% клиентов

Выручка экосистемы:
500 клиентов × 2 покупки × 3,500₽ = 3,500,000₽/мес

Комиссия платформы (3%):
3,500,000₽ × 3% = 105,000₽/мес

Расходы:
- Инфраструктура (Yandex Cloud): 15,000₽/мес
- Разработка (аутсорс support): 0₽ (solo)
- Маркетинг: 20,000₽/мес
- Организация мероприятий: 30,000₽/мес (софинансируется из бюджета клуба)
- Прочие расходы: 10,000₽/мес
─────────────────────────────────
ИТОГО расходов: 75,000₽/мес

Прибыль:
105,000₽ - 75,000₽ = 30,000₽/мес

ROI к 12 месяцам: Положительный
```

---

## ЗАКЛЮЧЕНИЕ

Проект "Свой Круг" представляет собой комплексную цифровую экосистему, объединяющую независимые женские бизнесы через:

1. **Технологическую надстройку** - без разрушения существующей инфраструктуры
2. **Эмоциональное сообщество** - не просто бонусы, а статус и принадлежность
3. **Взаимовыгодную экономику** - win-win для всех участников
4. **Масштабируемую архитектуру** - готовность к росту

### Ключевые преимущества:

✅ **Для клиентов:**
- Единое пространство доверенных брендов
- Привилегии за лояльность
- Социальные связи через мероприятия

✅ **Для бизнесов:**
- Новые клиенты через кросс-продажи
- Аналитика поведения
- Совместный маркетинг

✅ **Для платформы:**
- Устойчивая монетизация
- Сетевые эффекты
- Барьеры для конкурентов

### Следующие шаги:

1. **Утверждение архитектуры** с партнерами
2. **Старт разработки MVP** (10-12 недель)
3. **Пилотный запуск** с 5 бизнесами
4. **Итерации на основе обратной связи**
5. **Масштабирование** до 500 участниц

---

**Готов к реализации** 🚀

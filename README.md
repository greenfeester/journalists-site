# Сайт набора журналистов-фрилансеров

Одностраничный лендинг на Flask для поиска людей на подработку (фото/видео строительных объектов).

## Локальный запуск

```bash
cd freelance_journalists
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Откройте http://127.0.0.1:5000

Заявки приходят в консоль + сохраняются в памяти. Посмотреть: http://127.0.0.1:5000/admin/applications

## Куда выставить (бесплатно / дёшево)

### 1. Render.com (рекомендую)
1. Зарегистрируйтесь на https://render.com
2. New → Web Service
3. Подключите GitHub-репозиторий с этим кодом (или загрузите через CLI)
4. Настройки:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Бесплатный тариф есть (засыпает после простоя, но для разового набора ок).

### 2. Railway.app
1. https://railway.app
2. New Project → Deploy from GitHub / локально
3. Добавьте переменную `PORT` (Railway сам подставляет)
4. Start: `gunicorn app:app`

### 3. PythonAnywhere
1. https://www.pythonanywhere.com (есть бесплатный тариф)
2. Загрузите файлы через Files
3. Web → Add a new web app → Flask
4. Укажите путь к `app.py`

### 4. Fly.io
```bash
fly launch
fly deploy
```

## Важно для продакшена

- Заявки сейчас только в памяти + print в консоль.  
  Для реального использования добавьте отправку в Telegram-бот или на email (через SMTP / Resend / etc.).
- Страницу `/admin/applications` лучше защитить паролем или убрать.
- Поставьте нормальный `SECRET_KEY` через переменную окружения.

## Структура

```
freelance_journalists/
├── app.py
├── requirements.txt
├── README.md
├── static/css/style.css
└── templates/
    ├── index.html
    └── admin.html
```

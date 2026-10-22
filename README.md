# AWWW

A lightweight Django web app for creating and managing SVG artwork in a simple gallery-style workspace.

This project lets users sign in, open an SVG canvas, add colored rectangles, and build small custom images that are stored and displayed in the app. It is designed as a simple collaborative art editor with a minimal interface and a focus on easy SVG composition.

## ✨ Features

- User authentication with Django login/logout
- SVG gallery view with image listings
- Artwork editor for custom canvas dimensions
- Add colored rectangles to an SVG canvas
- Remove objects from an image
- Per-user access control for owned artwork
- Built with Django and SQLite for quick local development

## 🧩 Project idea

The app is inspired by a simple drawing studio: each user can work with their own SVG images, place shapes on a canvas, and view the generated art in a gallery. It is intentionally compact and beginner-friendly, making it a good example of a practical Django app with file-based SVG output.

## 🛠️ Tech stack

- Python
- Django
- SQLite
- HTML / CSS / JavaScript
- SVG output

## 📁 Project structure

```bash
.
├── LICENSE
├── README.md
├── fastapi/
│   ├── obrazki.py
│   └── rozwiazywacz.py
├── mysite/
│   ├── manage.py
│   ├── mysite/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── polls/
│       ├── admin.py
│       ├── apps.py
│       ├── migrations/
│       ├── models.py
│       ├── static/
│       ├── templates/
│       ├── tests.py
│       ├── urls.py
│       └── views.py
└── .git/
```

## 🚀 Getting started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/zad3awww.git
cd zad3awww
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Django

```bash
pip install django
```

### 4. Run database migrations

```bash
cd mysite
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## 🎨 How it works

1. Sign in to the app.
2. Open or create an SVG image.
3. Add rectangles with a chosen position, size, and color.
4. View the updated artwork rendered as SVG.
5. Manage your image collection from the main gallery.

## 🧪 Useful Django commands

Create an admin user:

```bash
python manage.py createsuperuser
```

Run the app in debug mode:

```bash
python manage.py runserver 0.0.0.0:8000
```

## 📌 Notes

This project is a simple educational/demo application and is not a production-ready platform. It is intended to demonstrate Django fundamentals, image handling, and basic SVG generation in a web app.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

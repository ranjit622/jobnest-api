# JobNest API

A Job Application Tracker REST API built with Django and Django REST Framework.

## Features
- User Register & Login
- JWT Authentication
- Track Job Applications
- Filter by Status
- Search by Company & Role
- Admin Panel

## Tech Stack
- Django
- Django REST Framework
- JWT Auth
- SQLite

## API Endpoints

| Endpoint | Method | Kaam |
|---|---|---|
| /api/register/ | POST | Register |
| /api/token/ | POST | Login — Token lo |
| /api/token/refresh/ | POST | Token refresh karo |
| /api/applications/ | GET | Saari jobs dekho |
| /api/applications/ | POST | Nayi job add karo |
| /api/applications/?status=applied | GET | Filter karo |
| /api/applications/?search=Google | GET | Search karo |

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Author
Ranjit Kumar — Backend Developer
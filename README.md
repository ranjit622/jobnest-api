# JobNest API 💼

A Production-Ready Job Application Tracker REST API built with Django and Django REST Framework.

## About
JobNest helps job seekers track all their job applications in one place — 
interview details, HR contacts, meeting links, and application status!

## Features
- User Register & Login — JWT Authentication
- Track Job Applications with full details
- Interview Date, Time & Meeting Link
- HR Name, Email & Phone
- Filter by Status
- Search by Company & Role
- Dashboard — Application Statistics
- Admin Panel

## Tech Stack
- Django
- Django REST Framework
- JWT Authentication
- SQLite

## API Endpoints

| Endpoint | Method | Kaam |
|---|---|---|
| /api/register/ | POST | Register |
| /api/token/ | POST | Login — Token lo |
| /api/token/refresh/ | POST | Token refresh |
| /api/applications/ | GET | Saari jobs dekho |
| /api/applications/ | POST | Nayi job add karo |
| /api/applications/?status=applied | GET | Filter karo |
| /api/applications/?search=Google | GET | Search karo |
| /api/dashboard/ | GET | Stats dekho |

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Author
Ranjit Kumar — Backend Developer
GitHub: github.com/ranjit622

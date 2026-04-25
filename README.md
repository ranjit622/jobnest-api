# JobNest API 💼

A Production-Ready Job Application Tracker REST API built with Django and Django REST Framework.

## 🌍 Live API
Base URL: https://jobnest-api-production.up.railway.app/api/

## 🚀 Quick Test
- Register: POST https://jobnest-api-production.up.railway.app/api/register/
- Login: POST https://jobnest-api-production.up.railway.app/api/token/
- Applications: GET https://jobnest-api-production.up.railway.app/api/applications/
- Dashboard: GET https://jobnest-api-production.up.railway.app/api/dashboard/

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
- Deployed on Railway with PostgreSQL

## Tech Stack
- Django
- Django REST Framework
- JWT Authentication
- PostgreSQL
- Docker
- Railway (Deployment)

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

## Quick Test
- Register: `POST /api/register/`
- Login: `POST /api/token/`
- Add Job: `POST /api/applications/`
- Dashboard: `GET /api/dashboard/`

## Setup

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Author
Ranjit Kumar — Backend Developer
GitHub: github.com/ranjit622

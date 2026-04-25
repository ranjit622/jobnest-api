# Python version
FROM python:3.13-slim

# Working directory set karo
WORKDIR /app

# Requirements copy karo
COPY requirements.txt .

# Dependencies install karo
RUN pip install -r requirements.txt

# Poora code copy karo
COPY . .

# Port expose karo
EXPOSE 8000

# Server run karo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
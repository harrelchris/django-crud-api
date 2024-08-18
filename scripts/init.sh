#!/usr/bin/env bash

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

source .venv/bin/activate
python -m pip install --upgrade pip
pip install ruff
pip install -r requirements.txt

if [ ! -f ".env" ]; then
    cp example.env .env
fi

if [ -f "db.sqlite3" ]; then
    rm db.sqlite3
fi

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput --username user --email user@email.com

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Development Server:**
- `python manage.py runserver` - Start Django development server

**Database Management:**
- `python manage.py makemigrations` - Create database migrations
- `python manage.py migrate` - Apply database migrations
- `python manage.py createsuperuser` - Create admin superuser

**Testing:**
- `python manage.py test` - Run all tests
- `python manage.py test <app_name>` - Run tests for specific app

**Utilities:**
- `python manage.py shell` - Open Django shell
- `python manage.py collectstatic` - Collect static files

## Architecture

This is a Django 5.2.5 web application with the following structure:

- **Project Name:** proyecto2025
- **Database:** SQLite (db.sqlite3)
- **Settings Module:** proyecto2025.settings
- **Root URL Configuration:** proyecto2025.urls

The project follows Django's standard structure with:
- Main project configuration in `proyecto2025/` directory
- Standard Django apps can be added to extend functionality
- SQLite database for development (configured in settings.py)
- Standard Django middleware and authentication setup

Currently configured with only the Django admin interface at `/admin/`.
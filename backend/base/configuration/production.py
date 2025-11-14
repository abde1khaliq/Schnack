"""
📦 Environment Switching Guide

To run your project in different environments (development vs production),
you must set the DJANGO_SETTINGS_MODULE variable in both wsgi.py and asgi.py
to point to the correct settings file.

This tells Django which settings to load when starting the server.

✅ Example for production:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.production')

✅ Example for development:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.development')

⚠️ Note:
Cloud platforms (e.g. Heroku, Railway, Render) often set DJANGO_SETTINGS_MODULE
via environment variables or build config. Avoid hardcoding assumptions here—
just document clearly and let users configure it per platform.
"""
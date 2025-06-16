# api/index.py
from app import app

# Vercel expects 'handler' for ASGI apps
handler = app

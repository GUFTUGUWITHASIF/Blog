from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App'

# In __init__.py:
default_app_config = 'App.apps.MyAppConfig'

from django.apps import AppConfig


class IdgenieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'IDGenie'
    
    def ready(self):
        import IDGenie.signals  # Import the signals file to register the signals

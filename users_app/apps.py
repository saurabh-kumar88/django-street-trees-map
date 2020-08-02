from django.apps import AppConfig


class Users_AppConfig(AppConfig):
    name = 'users_app'

    def ready(self):
        import users_app.signals

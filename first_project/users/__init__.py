from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = 'first_project.users'
    label = 'users'
    verbose_name = 'users'

    # def ready(self):
    #     import first_project.users.signals

default_app_config = 'first_project.users.UsersAppConfig'
from django.apps import AppConfig


class PessoaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pessoa'

    def ready(self):
            import pessoa.signals
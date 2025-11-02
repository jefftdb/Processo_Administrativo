from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class UsernameOrEmailBackend(ModelBackend):
    """
    Permite autenticar usando username OU e-mail.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Tenta buscar por username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Se não achou, tenta pelo e-mail
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return None

        # Verifica a senha
        if user.check_password(password):
            return user
        return None

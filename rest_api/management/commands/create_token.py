from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Criar um novo token para ser usado'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']

        self.stdout.write(
            self.style.WARNING(f'Criando usuário com nome: {username}')
        )

        user = User(username=username)
        user.first_name = username
        user.set_password(password)
        user.save()

        self.stdout.write(
            self.style.SUCCESS(f'Usuário criado.')
        )

        self.stdout.write(
            self.style.WARNING('Criando token para o usuário')
        )

        token = Token.objects.create(user=user)
        self.stdout.write(
            self.style.SUCCESS(f'Token criado para o usuário: {token.key}')
        )

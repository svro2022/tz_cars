from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    '''Команда для создания пользователей с ролью - user'''

    def handle(self, *args, **options):
        # User_1
        user = User.objects.create(
            email='anna@mail.ru',
            first_name='Anna',
            last_name='Sorokina',
            phone=None,
            role='user',
            is_active=True

        )
        user.set_password('111test222')
        user.save()

        # User_2
        user = User.objects.create(
            email='pavel@mail.ru',
            first_name='Pavel',
            last_name='Levin',
            phone=None,
            role='user',
            is_active=True

        )
        user.set_password('222test333')
        user.save()

        # User_3
        user = User.objects.create(
            email='sergei@mail.ru',
            first_name='Sergei',
            last_name='Sobolev',
            phone=None,
            role='user',
            is_active=True

        )
        user.set_password('333test444')
        user.save()

        # User_4
        user = User.objects.create(
            email='olya@mail.ru',
            first_name='Olya',
            last_name='Tihonova',
            phone=None,
            role='user',
            is_active=True

        )
        user.set_password('444test555')
        user.save()

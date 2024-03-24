from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    '''Команда для создания пользователей с ролью - admin'''

    def handle(self, *args, **options):
        # Staff_1
        user = User.objects.create(
            email='sveta@mail.ru',
            first_name='Sveta',
            last_name='Romanova',
            phone=None,
            role='admin',
            is_active=True,

        )
        user.set_password('111test111')
        user.save()

        # Staff_2
        user = User.objects.create(
            email='dasha@mail.ru',
            first_name='Dasha',
            last_name='Petrova',
            phone=None,
            role='admin',
            is_active=True,

        )
        user.set_password('222test222')
        user.save()

from django.core.management.base import BaseCommand
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Удаление всех новостей из какой-либо категории'

    def add_arguments(self, parser):
        parser.add_argument('list', nargs='?', default='list')
        parser.add_argument('-c', '--category', type=str)

    def handle(self, *args, **options):
        categories = ", ".join(Category.objects.values_list('name', flat=True))
        if options['category']:
            answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no: ')

            if answer != 'yes':
                self.stdout.write(self.style.ERROR('Отменено'))
                return
            try:
                category = Category.objects.get(name=options['category'])
                Post.objects.filter(postCategory=category).delete()
                self.stdout.write(
                    self.style.SUCCESS(f'Успешно удалены все новости из категории {category.name}'))  # в случае неправильного подтверждения говорим, что в доступе отказано
            except Category.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'Не удалось найти категорию {options["category"]}'))  # в случае неправильного подтверждения, говорим что в доступе отказано
        elif options['list']:
            self.stdout.write(self.style.SUCCESS(f'Список доступных категорий {categories}'))
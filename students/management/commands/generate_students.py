from django.core.management.base import BaseCommand, CommandError
from students.models import Student

class Command(BaseCommand):
    help = 'Generate N students'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', default=10, type=int)

    def handle(self, *args, **options):
        count = options['count']
        Student.generate_students(count=count)

        self.stdout.write(self.style.SUCCESS('Successfully generated %d students' % count))
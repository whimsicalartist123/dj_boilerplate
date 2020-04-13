import os
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Rename a Django Project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help="The new Django Project name")

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']
        project_name = settings.ROOT_URLCONF.split('.')[0]

        files_to_rename = [
            f'{project_name}/settings/base.py', 
            f'{project_name}/wsgi.py', 
            f'{project_name}/asgi.py', 
            'manage.py']
        folder_to_rename = project_name

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()
            
            filedata = filedata.replace(project_name, new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)
        self.stdout.write(self.style.SUCCESS(f"Project has been renamed {new_project_name}"))

        

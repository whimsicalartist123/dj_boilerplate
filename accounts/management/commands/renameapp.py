import os
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Rename a Django App'

    def add_arguments(self, parser):
        parser.add_argument('old_app_name', type=str, help="The old Django app name")
        parser.add_argument('new_app_name', type=str, help="The new Django app name")

    def handle(self, *args, **kwargs):
        old_app_name = kwargs['old_app_name']
        new_app_name = kwargs['new_app_name']
        project_name = settings.ROOT_URLCONF.split('.')[0]

        files_to_rename = [
            f"{project_name}/settings/base.py",
            f"{old_app_name}/apps.py"
        ]
        folder_to_rename = old_app_name

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()
            
            filedata = filedata.replace(old_app_name, new_app_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_app_name)
        self.stdout.write(self.style.SUCCESS(f"{old_app_name} has been renamed {new_app_name}"))

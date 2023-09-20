from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings


script_dir = Path(__file__).resolve().parent

base_folder = script_dir / Path('./templates')

files_dict = {
    '__init__.py': base_folder / Path('__init__.py'),
    'admin.py': base_folder / Path('admin.py'),
    'apis.py': base_folder / Path('apis.py'),
    'models.py': base_folder / Path('models.py'),
    'serializers.py': base_folder / Path('serializers.py'),
    'apis.py': base_folder / Path('apis.py'),
    'urls.py': base_folder / Path('urls.py'),
}

class Command(BaseCommand):

    help = 'Creates a Django app structure'
    
    def add_arguments(self, parser):
        parser.add_argument('app_names', nargs='+', type=str, help='List of app names to create')
        
    def handle(self, *args, **options):
        app_names = options['app_names']
        
        if not app_names:
            self.stdout.write(self.style.ERROR('No app names provided. Please provide at least one app name.'))
            return
        
        for app_name in app_names:
            app_name_capital = app_name.capitalize()
            app_name_snake = app_name.lower()
            
            print(f"Creating app: {app_name}")
            
            # Use BASE_DIR from Django settings to construct the app folder path
            app_folder = Path(settings.BASE_DIR) / app_name
            app_folder.mkdir(parents=True, exist_ok=True)  # Create the app folder if it doesn't exist
            migration_folder = app_folder / 'migrations'
            # Dictionary to hold the file content with placeholders
            content_dict = {
                '__init__.py': '',
                'admin.py': '',
                'apis.py': '',
                'models.py': '',
                'serializers.py': '',
                'urls.py': '',
            }
            
            # Read content from files and replace placeholders with app_name
            for filename, rel_path in files_dict.items():
                full_path = Path(settings.BASE_DIR) / rel_path
                file_content = full_path.read_text()
                file_content = file_content.replace('Template', app_name_capital)
                file_content = file_content.replace('template', app_name_snake)
                content_dict[filename] = file_content
            
            # Loop over the dictionary keys and create files with content
            for filename, content in content_dict.items():
                file_path = app_folder / filename
                with open(file_path, 'w') as file:
                    file.write(content)
                    
            self.stdout.write(self.style.SUCCESS(
                f'App created successfully at "{app_folder}"'
            ))

            migration_folder.mkdir(parents=True, exist_ok=True)
            with open(migration_folder / '__init__.py', 'w') as file:
                file.write('')
            
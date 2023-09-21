from pathlib import Path
import shutil
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Creates Django apps by copying a base structure'

    def add_arguments(self, parser):
        parser.add_argument('app_names', nargs='+', type=str,
                            help='List of app names to create')
        parser.add_argument('-f', '--force', action='store_true', help='Overwrite existing app folder')


    def handle(self, *args, **options):
        app_names = options['app_names']
        if not app_names:
            self.print_error('No app names provided')
            return

        base_folder = self.get_base_folder()
        force = 'force' in options
        
        for app_name in app_names:
            self.create_app(app_name, base_folder, force)

    def get_base_folder(self) -> Path:
        """Get base folder path from settings"""
        base_folder = getattr(settings, 'SNIPPET_FOLDER', None)
        if not base_folder:
            print('SNIPPET_FOLDER not defined in settings. Using default location.')
            base_folder = Path(__file__).resolve().parent / Path('templates')
        return Path(base_folder)

    def create_app(self, app_name: Path, base_folder: Path, force:bool=False) -> None:
        """Create an app by copying base folder"""
        self.stdout.write(self.style.NOTICE(
            f"Creating app: {app_name}"
        ))
        app_folder = self.get_app_folder(app_name)

        # Check if app folder already exists
        if app_folder.exists():
            if force:
                shutil.rmtree(app_folder)
            else:
                self.stdout.write(self.style.ERROR(
                    f'App folder {app_folder} already exists. Use -f to overwrite.'
                ))
                return

        self.copy_files(base_folder, app_folder, app_name)
        
        # Add __init__.py folders
        init_file = app_folder / '__init__.py'
        init_file.touch()

        # Add migrations folder
        migrations_dir = app_folder / 'migrations'
        migrations_dir.mkdir(parents=True, exist_ok=True)

        # Add empty __init__.py file in migrations
        init_file = migrations_dir / '__init__.py'
        init_file.touch()

        self.stdout.write(self.style.SUCCESS(
            f'App created successfully at "{app_folder}"'
        ))

    def get_app_folder(self, app_name: Path):
        """Construct app folder path"""
        app_folder = settings.BASE_DIR / app_name
        app_folder.mkdir(parents=True, exist_ok=True)
        return app_folder

    def copy_files(self, base_folder: Path, app_folder: Path, app_name: str):
        """Copy files from base folder to app folder"""
        for path in base_folder.iterdir():
            dest_path = app_folder / path.name
            if path.is_file():
                content = self.process_file(path, app_name)
                dest_path.write_text(content)
            elif path.is_dir():
                dest_path.mkdir(parents=True, exist_ok=True)

    def process_file(self, path, app_name):
        """Process file content template replacements"""
        content = path.read_text()
        content = content.replace('Template', app_name.capitalize())
        content = content.replace('template', app_name.lower())
        return content

    def print_error(self, message):
        self.stdout.write(self.style.ERROR(message))

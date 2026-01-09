# import libraries
import os, sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTING_MODULE', 'settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                'Could not Import Django. Did you forget to activate Virtual Env?'
            )
        raise
    execute_from_command_line(sys.argv)
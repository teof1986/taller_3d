import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taller_3d.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Datos del superusuario
USERNAME = 'teof1986'
EMAIL = 'teof1986@gmail.com'
PASSWORD = '1986'  # Puedes cambiar esta contraseña por la que prefieras

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)
    print(f"Superusuario '{USERNAME}' creado con éxito.")
else:
    print(f"El superusuario '{USERNAME}' ya existe.")
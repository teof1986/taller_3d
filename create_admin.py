import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taller_3d.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Credenciales para tu superusuario
USERNAME = 'admin'
PASSWORD = 'goyo1986'  # <-- Escribe aquí la clave que prefieras

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(username=USERNAME, email='', password=PASSWORD)
    print(f"✅ Superusuario '{USERNAME}' creado exitosamente.")
else:
    user = User.objects.get(username=USERNAME)
    user.set_password(PASSWORD)
    user.save()
    print(f"✅ Contraseña del usuario '{USERNAME}' actualizada correctamente.")

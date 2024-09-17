DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',           # El nombre de tu base de datos
        'USER': 'usuario_db',    # Tu usuario de PostgreSQL
        'PASSWORD': 'contraseña_db',  # La contraseña de PostgreSQL
        'HOST': 'localhost',     # O la dirección de tu servidor de PostgreSQL (por ejemplo, si estás en Render, ellos te proporcionarán esto)
        'PORT': '5432',          # El puerto estándar de PostgreSQL (o el que uses)
    }
}

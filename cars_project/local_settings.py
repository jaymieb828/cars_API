# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6t0h828@xxj_=e_83c*q6o$*l)+_4&5d@=h-*43k8bw%06i_z1'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Addison2007!'
    }
}

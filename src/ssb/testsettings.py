DEBUG = TEMPLATE_DEBUG =True

DATABASES = {
    "default": {
        "ENGINE": "sqlite3",
        "NAME": "system-session-bookings.sqlite3"
    }
}

TIME_ZONE = "Etc/UTC"

LANGUAGE_CODE = "en-us"

SITE_ID = 1

USE_I18N = USE_L10N = False

SECRET_KEY = "f3es)idvfg+6pp+g5kviw3evrwci=t6^#8avq@ls#u2j_mn#&f"

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader"
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
)

ROOT_URLCONF = "ssb.testurls"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.admin",

    "ssb",
)

# How to use Google Oauth in Django Rest Framework


## Introduction

`dj_rest_auth` is a Django package that provides a set of REST API endpoints for authentication and registration. It is built on top of Django Rest Framework and integrates seamlessly with Django authentication and Allauth.

In this guide, we'll walk you through the steps to integrate `dj_rest_auth` into your Django project.

## Prerequisites

Before getting started, make sure you have the following installed:

- Python (>= 3.6)
- Django (>= 2.2)
- Django Rest Framework (>= 3.11)
- Allauth (>= 0.44)

## Google Developer console

Please make sure to register on https://console.cloud.google.com/ before starting. Click on the Api and Services, then click on the Credentials to create an Oauth client ID. After creating an Oauth client id, make sure to keep the clien id and client secret. It will be need in the project.

- Make sure to add http://127.0.0.1:8000 as the Authorized JavaScript origins

- Also make sure to add http://127.0.0.1:8000/accounts/google/login/callback/ as the Authorized redirect URIs

## Installation

You can install `dj_rest_auth` using pip. Run the following command in your terminal:

    ```bash
    pip install dj-rest-auth[with_social]


## Steps:
 Given that you have created a django app for auth:
1.  Add `'django.contrib.sites'` and `'allauth'` to your list of installed apps in settings.py
    ```bash
   INSTALLED_APPS = [
    ...
    'django.contrib.sites', #needed
    
    #Apps
    'accounts',
    
    #Third Party Apps
    'rest_framework',
    "rest_framework.authtoken",
    'dj_rest_auth.registration',
    'drf_spectacular',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    ]

2. add allauth middleware:
    ```bash
    MIDDLEWARE = [
        ...
    
        'allauth.account.middleware.AccountMiddleware',
    ]

3. Set up authentication backends by adding this code snippet:

    ```bash
    AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    ]

4.Add this to rest_framework setting in settings.py :

    ```bash
    REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        ]
        }

5. Specify the social account provider like this in your settings.py:

    ```bash
    SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'FETCH_USERINFO' : True,
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': config('GOOGLE_CLIENT_ID'),
            'secret': config('GOOGLE_CLIENT_SECRET'),
            'key': ''
        }
    }
    }

    SITE_ID = 2 #very important

6. Include the client credientials from your google developers console that you created at https://console.cloud.google.com/apis/credentials/

    ```bash
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_CLIENT_ID')
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_CLIENT_SECRET')
    SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', 'profile']
    SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = config('GOOGLE_OAUTH2_REDIRECT_URI')
### note that I used environment varialbes to security purposes.

7. Add  the following lines of code to project's urls.py file:

    ```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path("admin/", admin.site.urls),
    
    # App's API endpoints
    path('api/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    ]

8. Add the following to your app's urls.py file:

    ```bash
    from django.urls import path
    from dj_rest_auth.registration.views import RegisterView
    from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView

    urlpatterns = [
        path("register/", RegisterView.as_view(), name="rest_register"),
        path("login/", LoginView.as_view(), name="rest_login"),
    ]
This has a built-in views for /register endpoint and /login endpoint.

9. After you have ran migrations and created superuser. Run the server. 

    ```bash
    python manage.py runserver
Then login into the admin dashboard at http://127.0.0.1:8000/admin/

10. On the Admin Dashboard, navigate to "Sites" add add 127.0.0.1:8000 and then go to the "Social Applications" and add:

    ```bash
    Provider (Input Google)
    Name (Input Google)
    Secret  key (Use OAuth Secret Key)
    Client Key (Use Oauth client ID)
    Leave "key" empty
    Make sure 127.0.0.1:8000 is under "Chosen sites"

11. You can now proceed to register and verify users at http://127.0.0.1:8000/accounts/google/signup/ and login at http://127.0.0.1:8000/accounts/google/login/
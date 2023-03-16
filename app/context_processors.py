from django.conf import settings

def psychonauts(request):
    return {
        'GOOGLE_CLIENT_ID': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        'GOOGLE_AUTHORIZATION_URL': 'https://accounts.google.com/o/oauth2/auth',
        'GOOGLE_ACCESS_TOKEN_URL': 'https://accounts.google.com/o/oauth2/token',
        'GOOGLE_USERINFO_URL': 'https://www.googleapis.com/oauth2/v1/userinfo',
        'GOOGLE_REDIRECT_URI': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI,
    }

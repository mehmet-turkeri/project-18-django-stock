from django.urls import path, include

# after 'users/':
urlpatterns = [
    # redirect all auth process to dj_rest_auth:
    path('auth/', include('dj_rest_auth.urls')),    
]
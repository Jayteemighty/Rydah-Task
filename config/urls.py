from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import  SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # App's API endpoints
    path('api/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    
    # API documentation endpoints
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]

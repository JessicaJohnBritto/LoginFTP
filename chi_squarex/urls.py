# Django Imports
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import redirect

# Standard Package Imports

# Project Imports
from . import settings

# Third Party Imports


urlpatterns = [
    path('admin/', admin.site.urls), # Namespace name is admin and path/url name is index for home page
    path('', include('main_app.urls', namespace='main_app'), name='main_app'), # To use dynamic urls "{% url 'namespace:url_name' %}"
    # path('', lambda x: redirect('/get_quote/')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
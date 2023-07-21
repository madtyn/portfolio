"""
URL configuration for personal_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

PATH_LIST = [
    path('admin/', admin.site.urls),

    # i18n:  sets a user’s language preference and redirects to a given URL
    # or, by default, back to the previous page
    path("i18n/", include('django.conf.urls.i18n')),
]

I18N_PATH_LIST = [
    path('projects/', include('projects.urls')),
    path('blog/', include('blog.urls')),
]

urlpatterns = PATH_LIST + i18n_patterns(*I18N_PATH_LIST, prefix_default_language=True) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print('patata')

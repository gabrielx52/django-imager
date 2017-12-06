"""imagersite URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout

from imagersite.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',
        HomeView.as_view(template_name='imagersite/home.html'),
        name='home'),
    url(r'^login/$',
        login,
        {'template_name': 'imagersite/login.html'},
        name="login"),
    url(r'^logout/$',
        logout,
        {'next_page': '/'},
        name="logout"),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'profile/', include('imager_profile.urls')),
    url(r'images/', include('imager_images.urls')),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
